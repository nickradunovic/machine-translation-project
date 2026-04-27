#!/usr/bin/env python3
"""
Generate LaTeX tables + figures for the reference-free track from:
  ref_free_track_structured_numeric.json

Outputs (by default under ./tables and ./figures):
  tables/ref-free-avg-scores.tex
  tables/ref-free-deltas-macro.tex
  tables/ref-free-deltas-human-by-language.tex
  tables/ref-free-judge-human-agreement.tex
  figures/png/reference-free-results-average-with-overall.png
  figures/png/judge-vs-human-overall-scatter.png
  figures/reference-free-results-average-with-overall.tex
  figures/ref-free-judge-vs-human.tex

Usage:
  python generate_ref_free_artifacts.py \
      --json /path/to/ref_free_track_structured_numeric.json \
      --outdir . \
      --color_scatter_by language

Notes:
- Human scores are aggregated as: average over evaluators per (language, system, doc_id) first.
- "Overall" is computed per doc as mean(meaning, tone, readability), then aggregated like other metrics.
- Macro deltas are computed over language-level paired deltas (GPT-4 minus Azure).
- CIs:
  - Macro: bootstrap over languages.
  - Per-language: bootstrap over docs.
- p-values: exact sign-flip permutation test (two-sided), over languages or docs.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CRITERIA = ["meaning", "tone", "readability"]
METRICS = CRITERIA + ["overall"]

METRIC_LABELS = {
    "meaning": "Correctheid",
    "tone": "Toon en stijl",
    "readability": "Leesbaarheid",
    "overall": "Overall",
}

SYSTEM_LABELS = {
    "azure": "Azure Translator",
    "gpt4": "GPT-4 (translator)",
}

EVAL_LABELS = {
    "human": "Native speaker",
    "judge": "GPT-4 (judge)",
}

LANG_ORDER = ["German", "Turkish", "English", "Polish", "Spanish", "Arabic", "Ukrainian"]  # for plotting order


# -------------------------
# Plot helpers
# -------------------------
def _build_color_map(categories: List[str], cmap_name: str = "tab10") -> Dict[str, Tuple[float, float, float, float]]:
    """Stable mapping category -> RGBA color."""
    cmap = plt.get_cmap(cmap_name)
    return {cat: cmap(i % cmap.N) for i, cat in enumerate(categories)}


def _ordered_categories(values: List[str], preferred: List[str]) -> List[str]:
    """Return `values` ordered by `preferred`, then alphabetically for remaining."""
    vals = [str(v) for v in values]
    seen: List[str] = []
    for v in preferred:
        if v in vals and v not in seen:
            seen.append(v)
    for v in sorted(vals):
        if v not in seen:
            seen.append(v)
    return seen


# -------------------------
# Stats helpers
# -------------------------
def bootstrap_ci_mean(values: np.ndarray, n_boot: int = 10000, alpha: float = 0.05, seed: int = 0) -> Tuple[float, float]:
    """Bootstrap CI for the mean."""
    rng = np.random.default_rng(seed)
    values = np.asarray(values, dtype=float)
    n = values.shape[0]
    boots = rng.choice(values, size=(n_boot, n), replace=True).mean(axis=1)
    lo = float(np.quantile(boots, alpha / 2))
    hi = float(np.quantile(boots, 1 - alpha / 2))
    return lo, hi


def signflip_p_value(values: np.ndarray) -> float:
    """
    Exact two-sided sign-flip test for mean(values).
    Null: symmetric around 0.
    """
    values = np.asarray(values, dtype=float)
    obs = float(values.mean())
    n = values.shape[0]
    means = []
    for signs in itertools.product([1, -1], repeat=n):
        means.append(float((values * np.array(signs)).mean()))
    means = np.array(means, dtype=float)
    p = float((np.abs(means) >= abs(obs) - 1e-12).mean())
    return p


def spearman_rho(x: np.ndarray, y: np.ndarray) -> float:
    """Spearman rho without scipy (rank then Pearson)."""
    x = pd.Series(x).rank(method="average").to_numpy(dtype=float)
    y = pd.Series(y).rank(method="average").to_numpy(dtype=float)
    # Pearson correlation of ranks
    x = x - x.mean()
    y = y - y.mean()
    denom = (np.sqrt((x * x).sum()) * np.sqrt((y * y).sum()))
    if denom == 0:
        return float("nan")
    return float((x * y).sum() / denom)


def linear_fit(y: np.ndarray, x: np.ndarray) -> Tuple[float, float]:
    """Least-squares fit y = a + b x. Returns (b, a)."""
    b, a = np.polyfit(x.astype(float), y.astype(float), deg=1)
    return float(b), float(a)


def stars(p: float) -> str:
    if p < 0.01:
        return r"$^{***}$"
    if p < 0.05:
        return r"$^{**}$"
    if p < 0.10:
        return r"$^{*}$"
    return ""


# -------------------------
# Data loading + aggregation
# -------------------------
@dataclass
class RefFreeData:
    judge_doc: pd.DataFrame   # language, system, doc_id, meaning, tone, readability, overall
    human_doc: pd.DataFrame   # same
    docs_expected: int


def load_ref_free_json(json_path: Path) -> RefFreeData:
    with open(json_path, "r", encoding="utf-8") as f:
        obj = json.load(f)

    docs_expected = int(obj.get("docs_per_language_expected", 6))

    df_j = pd.DataFrame(obj["data"]["judge"])
    df_h = pd.DataFrame(obj["data"]["human"])

    # Aggregate human over evaluators first
    df_j_doc = df_j.groupby(["language", "system", "doc_id"], as_index=False)[CRITERIA].mean()
    df_h_doc = df_h.groupby(["language", "system", "doc_id"], as_index=False)[CRITERIA].mean()

    for df in (df_j_doc, df_h_doc):
        df["overall"] = df[CRITERIA].mean(axis=1)

    return RefFreeData(judge_doc=df_j_doc, human_doc=df_h_doc, docs_expected=docs_expected)


def sanity_check(df_doc: pd.DataFrame, docs_expected: int, label: str) -> None:
    # Ensure each language-system has expected doc count
    counts = df_doc.groupby(["language", "system"])["doc_id"].nunique().reset_index(name="n_docs")
    bad = counts[counts["n_docs"] != docs_expected]
    if not bad.empty:
        print(f"[WARN] {label}: doc count mismatches (expected {docs_expected} per language-system):")
        print(bad.to_string(index=False))


# -------------------------
# Table generation
# -------------------------
def write_tex(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.rstrip() + "\n")


def fmt(x: float, nd: int = 1) -> str:
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "NA"
    return f"{x:.{nd}f}"


def make_table_avg_scores(human_doc: pd.DataFrame, judge_doc: pd.DataFrame) -> str:
    # micro-aggregate over all language-doc items
    rows = []
    for system in ["azure", "gpt4"]:
        h_mean = human_doc[human_doc["system"] == system][METRICS].mean()
        j_mean = judge_doc[judge_doc["system"] == system][METRICS].mean()
        rows.append((SYSTEM_LABELS[system], EVAL_LABELS["human"], h_mean))
        rows.append((SYSTEM_LABELS[system], EVAL_LABELS["judge"], j_mean))

    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")
    lines.append(r"\scriptsize")
    lines.append(r"\renewcommand{\arraystretch}{1.15}")
    lines.append(r"\setlength{\tabcolsep}{6pt}")
    lines.append(
        r"\caption{Average rubric scores aggregated across languages and excerpts (reference-free track). "
        r"``Native speaker'' denotes the native-speaker evaluators; ``GPT-4 (judge)'' denotes the rubric-based LLM-as-a-judge. "
        r"We additionally report an Overall score (mean of Correctheid, Toon en stijl, and Leesbaarheid).}"
    )
    lines.append(r"\label{tab:ref-free-avg-scores}")
    lines.append(r"\begin{tabular}{@{}l l c c c c@{}}")
    lines.append(r"\toprule")
    lines.append(r"System & Evaluator & Correctheid & Toon en stijl & Leesbaarheid & Overall \\")
    lines.append(r"\midrule")
    for sys_label, eval_label, s in rows:
        lines.append(
            f"{sys_label} & {eval_label} & "
            f"{fmt(s['meaning'])} & {fmt(s['tone'])} & {fmt(s['readability'])} & {fmt(s['overall'])} \\\\"
        )
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def make_table_deltas_macro(human_doc: pd.DataFrame, seed: int = 0) -> str:
    # Language-level deltas (paired): mean over docs per language-system, then diff
    langs = sorted(human_doc["language"].unique().tolist())
    deltas = []
    for lang in langs:
        sub = human_doc[human_doc["language"] == lang]
        means = sub.groupby("system")[METRICS].mean()
        d = means.loc["gpt4"] - means.loc["azure"]
        d["language"] = lang
        deltas.append(d)
    deltas_df = pd.DataFrame(deltas).set_index("language")

    # Bootstrap CI over languages
    rng = np.random.default_rng(seed)
    n_lang = len(langs)

    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")
    lines.append(r"\scriptsize")
    lines.append(r"\renewcommand{\arraystretch}{1.15}")
    lines.append(r"\setlength{\tabcolsep}{6pt}")
    lines.append(
        r"\caption{Macro-averaged paired deltas (GPT-4 minus Azure) over languages for the reference-free track, "
        r"using native-speaker excerpt-level means (6 excerpts per language). Confidence intervals are bootstrap 95\% CIs over languages; "
        r"$p$ values are from an exact sign-flip permutation test over language-level deltas.}"
    )
    lines.append(r"\label{tab:ref-free-deltas-macro}")
    lines.append(r"\begin{tabular}{@{}l c c c c c@{}}")
    lines.append(r"\toprule")
    lines.append(r"Metric & Mean $\Delta$ & 95\% CI & $p$ (sign-flip) & Cohen's $d_z$ & $N_{\text{lang}}$ \\")
    lines.append(r"\midrule")

    for m in METRICS:
        vals = deltas_df[m].to_numpy(dtype=float)
        mean_delta = float(vals.mean())

        # bootstrap: resample languages (indices)
        boots = []
        for _ in range(10000):
            idx = rng.integers(0, n_lang, size=n_lang)
            boots.append(float(vals[idx].mean()))
        lo = float(np.quantile(boots, 0.025))
        hi = float(np.quantile(boots, 0.975))

        p = signflip_p_value(vals)

        # Cohen's dz (paired): mean / sd
        sd = float(vals.std(ddof=1)) if len(vals) > 1 else float("nan")
        dz = (mean_delta / sd) if sd and sd > 0 else float("nan")

        lines.append(
            f"{METRIC_LABELS[m]} & {fmt(mean_delta, 2)} & [{fmt(lo, 2)}, {fmt(hi, 2)}] & "
            f"{fmt(p, 3)}{stars(p)} & {fmt(dz, 2)} & {n_lang} \\\\"
        )

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def make_table_deltas_by_language(doc_df: pd.DataFrame, seed: int = 0) -> str:
    # For each language, diff (gpt4 - azure) over docs; CI + signflip over docs
    langs = LANG_ORDER[:]  # keep order
    langs = [l for l in langs if l in doc_df["language"].unique().tolist()] + \
            [l for l in sorted(doc_df["language"].unique().tolist()) if l not in langs]

    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")
    lines.append(r"\scriptsize")
    lines.append(r"\renewcommand{\arraystretch}{1.15}")
    lines.append(r"\setlength{\tabcolsep}{6pt}")
    lines.append(
        r"\caption{Per-language paired deltas (GPT-4 minus Azure) for the reference-free track, using excerpt-level means (6 excerpts per language). "
        r"Confidence intervals are bootstrap 95\% CIs over excerpts; $p$ values are from an exact sign-flip permutation test over excerpt-level deltas.}"
    )
    lines.append(r"\label{tab:ref-free-deltas-by-language}")
    lines.append(r"\begin{tabular}{@{}l c c c c c@{}}")
    lines.append(r"\toprule")
    lines.append(r"Language & Metric & Mean $\Delta$ & 95\% CI & $p$ (sign-flip) & $N_{\text{doc}}$ \\")
    lines.append(r"\midrule")

    rng = np.random.default_rng(seed)

    for lang in langs:
        sub = doc_df[doc_df["language"] == lang]
        piv = sub.pivot_table(index="doc_id", columns="system", values=METRICS)
        diffs = piv.xs("gpt4", axis=1, level=1) - piv.xs("azure", axis=1, level=1)
        n_docs = diffs.shape[0]
        for m in METRICS:
            vals = diffs[m].to_numpy(dtype=float)
            mean_delta = float(np.nanmean(vals))

            # bootstrap over docs
            vals_nonan = vals[~np.isnan(vals)]
            if len(vals_nonan) >= 2:
                boots = []
                for _ in range(10000):
                    idx = rng.integers(0, len(vals_nonan), size=len(vals_nonan))
                    boots.append(float(vals_nonan[idx].mean()))
                lo = float(np.quantile(boots, 0.025))
                hi = float(np.quantile(boots, 0.975))
            else:
                lo = float("nan")
                hi = float("nan")

            p = signflip_p_value(vals_nonan) if len(vals_nonan) > 0 else float("nan")

            lines.append(
                f"{lang} & {METRIC_LABELS[m]} & {fmt(mean_delta, 2)} & [{fmt(lo, 2)}, {fmt(hi, 2)}] & "
                f"{fmt(p, 3)}{stars(p)} & {n_docs} \\\\"
            )

        lines.append(r"\addlinespace[2pt]")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def make_table_judge_human_agreement(human_doc: pd.DataFrame, judge_doc: pd.DataFrame) -> str:
    # agreement metrics on overall, pooling all docs+langs+systems
    merged = human_doc.merge(judge_doc, on=["language", "system", "doc_id"], suffixes=("_human", "_judge"))
    rows = []
    for m in METRICS:
        x = merged[f"{m}_human"].to_numpy(dtype=float)
        y = merged[f"{m}_judge"].to_numpy(dtype=float)
        # Spearman + linear fit
        rho = spearman_rho(x, y)
        b, a = linear_fit(y, x)  # y = a + b x
        rows.append((METRIC_LABELS[m], rho, b, a, len(x)))

    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")
    lines.append(r"\scriptsize")
    lines.append(r"\renewcommand{\arraystretch}{1.15}")
    lines.append(r"\setlength{\tabcolsep}{6pt}")
    lines.append(
        r"\caption{Agreement between GPT-4 (judge) and native-speaker evaluators on reference-free rubric scores, pooling all language--excerpt--system items ($n=84$). "
        r"We report Spearman's $\rho$ and a least-squares fit $y = a + b x$ (where $x$ is native-speaker score and $y$ is judge score).}"
    )
    lines.append(r"\label{tab:ref-free-judge-human-agreement}")
    lines.append(r"\begin{tabular}{@{}l c c c c@{}}")
    lines.append(r"\toprule")
    lines.append(r"Metric & Spearman $\rho$ & Slope $b$ & Intercept $a$ & $N$ \\")
    lines.append(r"\midrule")
    for name, rho, b, a, n in rows:
        lines.append(f"{name} & {fmt(rho, 2)} & {fmt(b, 2)} & {fmt(a, 2)} & {n} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


# -------------------------
# Figure generation
# -------------------------
def plot_reference_free_panels(
    human_doc: pd.DataFrame,
    judge_doc: pd.DataFrame,
    out_png: Path,
    aggregation: str = "micro",
) -> None:
    """
    Creates a 4x2 panel plot: 7 languages + average.
    Each panel: bar chart of mean scores for each system, scored by human and judge.
    Error bars: SD over docs.
    """
    plt.rcParams.update({
        # "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 10,
        "axes.labelsize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 9,
        "figure.dpi": 300,
    })

    def panel_stats(human_doc: pd.DataFrame, judge_doc: pd.DataFrame, language: str | None, aggregation: str):
        if language is None:
            if aggregation == "micro":
                h = human_doc.copy()
                j = judge_doc.copy()
            else:
                h = human_doc.groupby(["language", "system"], as_index=False)[METRICS].mean()
                j = judge_doc.groupby(["language", "system"], as_index=False)[METRICS].mean()
        else:
            h = human_doc[human_doc["language"] == language].copy()
            j = judge_doc[judge_doc["language"] == language].copy()

        def sys_eval_means(df_doc: pd.DataFrame) -> Dict[str, np.ndarray]:
            out = {}
            for sys in ["azure", "gpt4"]:
                sub = df_doc[df_doc["system"] == sys]
                if aggregation == "micro" or language is not None:
                    out[sys] = sub[METRICS].mean().to_numpy(dtype=float)
                    out[sys + "_std"] = sub[METRICS].std(ddof=1).to_numpy(dtype=float)
                else:
                    out[sys] = sub.groupby("language")[METRICS].mean().mean().to_numpy(dtype=float)
                    out[sys + "_std"] = sub.groupby("language")[METRICS].mean().std(ddof=1).to_numpy(dtype=float)
            return out

        h_stats = sys_eval_means(h)
        j_stats = sys_eval_means(j)

        return {
            "expert_azure": h_stats["azure"],
            "expert_azure_std": h_stats["azure_std"],
            "expert_gpt": h_stats["gpt4"],
            "expert_gpt_std": h_stats["gpt4_std"],
            "gptjudge_azure": j_stats["azure"],
            "gptjudge_azure_std": j_stats["azure_std"],
            "gptjudge_gpt": j_stats["gpt4"],
            "gptjudge_gpt_std": j_stats["gpt4_std"],
        }

    languages = LANG_ORDER[:]  # stable
    languages = [l for l in languages if l in human_doc["language"].unique().tolist()] + \
                [l for l in sorted(human_doc["language"].unique().tolist()) if l not in languages]

    items = languages + ["Average (All Languages)"]

    fig, axs = plt.subplots(4, 2, figsize=(10.5, 10.5), sharey=True, sharex=False)
    axs = axs.flatten()

    x = np.arange(len(METRICS))
    width = 0.18

    for i, title in enumerate(items):
        ax = axs[i]
        language = None if title.startswith("Average") else title
        stats = panel_stats(human_doc, judge_doc, language=language, aggregation=aggregation)

        # Bars: 4 groups
        ax.bar(x - 1.5 * width, stats["expert_azure"], width, yerr=stats["expert_azure_std"], capsize=3,
               label="AT (Native-speaker Scored)")
        ax.bar(x - 0.5 * width, stats["gptjudge_azure"], width, yerr=stats["gptjudge_azure_std"], capsize=3,
               label="AT (LLM-as-judge Scored)")
        ax.bar(x + 0.5 * width, stats["expert_gpt"], width, yerr=stats["expert_gpt_std"], capsize=3,
               label="GPT-4 (Native-speaker Scored)")
        ax.bar(x + 1.5 * width, stats["gptjudge_gpt"], width, yerr=stats["gptjudge_gpt_std"], capsize=3,
               label="GPT-4 (LLM-as-judge Scored)")

        ax.set_title(title, fontweight="bold", pad=3)
        ax.set_ylim(0, 10.5)
        ax.grid(axis="y", linestyle="--", alpha=0.3)

        ax.set_xticks(x)
        if i >= 6:
            ax.set_xticklabels([METRIC_LABELS[m] for m in METRICS], rotation=0)
        else:
            ax.set_xticklabels([])

        if i % 2 == 0:
            ax.set_ylabel("Score (0–10)")

    # Legend
    handles = [axs[0].containers[0], axs[0].containers[1], axs[0].containers[2], axs[0].containers[3]]
    labels = ["AT (Native-speaker Scored)", "AT (LLM-as-judge Scored)", "GPT-4 (Native-speaker Scored)", "GPT-4 (LLM-as-judge Scored)"]
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.98), ncol=2, frameon=False)

    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, bbox_inches="tight")
    plt.close(fig)


def plot_judge_vs_human_overall(
    human_doc: pd.DataFrame,
    judge_doc: pd.DataFrame,
    out_png: Path,
    *,
    color_by: str = "language",
    legend_max_items: int = 12,
) -> None:
    """Scatter: native-speaker Overall (x) vs GPT-4 (judge) Overall (y).

    One point per (language, system, doc_id). Styling/layout matches the publication-style
    scatter used in `make_paper_artifacts_optionB_paperlabels_v2.py`.
    """
    merged = human_doc.merge(judge_doc, on=["language", "system", "doc_id"], suffixes=("_human", "_judge"))
    if merged.empty:
        raise ValueError("No overlapping rows between human_doc and judge_doc (after merge on language/system/doc_id).")

    df = merged[["language", "system", "overall_human", "overall_judge"]].copy()
    df = df.dropna(subset=["overall_human", "overall_judge"])
    if df.empty:
        raise ValueError("All judge-vs-human Overall pairs are NaN after merging.")

    plt.rcParams.update({
        # "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "figure.dpi": 300,
    })

    fig = plt.figure(figsize=(6.4, 5.4))
    ax = fig.add_subplot(111)

    if color_by not in ("language", "system", "none"):
        print(f"[WARN] Unknown --color_scatter_by='{color_by}', defaulting to 'language'.")
        color_by = "language"

    if color_by == "none":
        ax.scatter(
            df["overall_human"].astype(float).values,
            df["overall_judge"].astype(float).values,
            alpha=0.85,
            s=45,
        )
        categories: List[str] = []
    else:
        raw_cats = df[color_by].astype(str).unique().tolist()
        if color_by == "language":
            categories = _ordered_categories(raw_cats, preferred=LANG_ORDER)
            legend_title = "Language"
            legend_label = lambda c: c
        else:
            categories = _ordered_categories(raw_cats, preferred=["azure", "gpt4"])
            legend_title = "System"
            legend_label = lambda c: SYSTEM_LABELS.get(c, c)

        cmap_name = "tab10" if len(categories) <= 10 else ("tab20" if len(categories) <= 20 else "hsv")
        cmap = _build_color_map(categories, cmap_name=cmap_name)

        for cat in categories:
            sub = df[df[color_by].astype(str) == cat]
            ax.scatter(
                sub["overall_human"].astype(float).values,
                sub["overall_judge"].astype(float).values,
                alpha=0.85,
                s=45,
                label=legend_label(cat),
                color=cmap[cat],
            )

        if len(categories) <= legend_max_items:
            ax.legend(
                loc="upper left",
                bbox_to_anchor=(1.02, 1.0),
                borderaxespad=0,
                frameon=False,
                title=legend_title,
            )

    # Perfect-agreement line (y=x)
    lo = float(min(df["overall_human"].min(), df["overall_judge"].min()))
    hi = float(max(df["overall_human"].max(), df["overall_judge"].max()))
    lo = max(0.0, lo - 0.2)
    hi = min(10.5, hi + 0.2)

    ax.plot([lo, hi], [lo, hi], linestyle="--", linewidth=1.0, alpha=0.7)

    ax.set_xlabel("Native-speaker Overall (0–10)")
    ax.set_ylabel("GPT-4 (judge) Overall (0–10)")
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.25)

    fig.tight_layout()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, bbox_inches="tight")
    plt.close(fig)


def make_figure_tex_average(png_rel_path: str) -> str:
    return "\n".join([
        r"\begin{figure}[t]",
        r"    \centering",
        rf"    \includegraphics[width=0.92\textwidth]{{{png_rel_path}}}",
        r"    \caption{Reference-free track results across seven languages. Each panel shows mean rubric scores (0--10) for Correctheid, Toon en stijl, Leesbaarheid, and Overall, comparing Azure Translator and GPT-4 (translator), evaluated by native speakers (Human) and GPT-4 (judge). Error bars are $\pm 1$ SD over the six excerpts per language.}",
        r"    \label{fig:reference-free-results-average-overall}",
        r"\end{figure}",
    ])


def make_figure_tex_scatter(png_rel_path: str) -> str:
    return "\n".join([
        r"\begin{figure}[t]",
        r"    \centering",
        rf"    \includegraphics[width=0.55\textwidth]{{{png_rel_path}}}",
        r"    \caption{Agreement between GPT-4 (judge) and native-speaker ratings on the \emph{Overall} rubric score across all language--excerpt--system items ($n=84$). The dashed line indicates perfect agreement ($y=x$).}",
        r"    \label{fig:ref-free-judge-vs-human}",
        r"\end{figure}",
    ])


def make_table_deltas_by_language_human_vs_judge(human_doc: pd.DataFrame, judge_doc: pd.DataFrame, seed: int = 0) -> str:
    langs = sorted(set(human_doc["language"].unique().tolist()) & set(judge_doc["language"].unique().tolist()))

    def per_lang_row(df_doc: pd.DataFrame, lang: str) -> Dict[str, Tuple[float, float, float, float]]:
        """
        Returns dict metric -> (mean_delta, lo, hi, p)
        Delta computed paired by doc_id: gpt4 - azure
        """
        sub = df_doc[df_doc["language"] == lang]
        piv = sub.pivot_table(index="doc_id", columns="system", values=METRICS)
        diffs = piv.xs("gpt4", axis=1, level=1) - piv.xs("azure", axis=1, level=1)

        out = {}
        rng = np.random.default_rng(seed)
        for m in METRICS:
            vals = diffs[m].to_numpy(dtype=float)
            vals_nonan = vals[~np.isnan(vals)]
            mean_delta = float(np.nanmean(vals))

            if len(vals_nonan) >= 2:
                boots = []
                for _ in range(10000):
                    idx = rng.integers(0, len(vals_nonan), size=len(vals_nonan))
                    boots.append(float(vals_nonan[idx].mean()))
                lo = float(np.quantile(boots, 0.025))
                hi = float(np.quantile(boots, 0.975))
            else:
                lo, hi = float("nan"), float("nan")

            p = signflip_p_value(vals_nonan) if len(vals_nonan) > 0 else float("nan")
            out[m] = (mean_delta, lo, hi, p, len(vals_nonan))
        return out

    rows = []
    for lang in langs:
        h = per_lang_row(human_doc, lang)
        j = per_lang_row(judge_doc, lang)
        for m in METRICS:
            dh, loh, hih, ph, nh = h[m]
            dj, loj, hij, pj, nj = j[m]
            rows.append((lang, m, dh, loh, hih, ph, dj, loj, hij, pj, int(min(nh, nj))))

    df = pd.DataFrame(rows, columns=[
        "language", "metric",
        "delta_human", "lo_human", "hi_human", "p_human",
        "delta_judge", "lo_judge", "hi_judge", "p_judge",
        "n_docs",
    ])

    lines = []
    lines.append(r"\begin{table}[htbp]")
    lines.append(r"\centering")
    lines.append(r"\scriptsize")
    lines.append(r"\renewcommand{\arraystretch}{1.15}")
    lines.append(r"\setlength{\tabcolsep}{5pt}")
    lines.append(
        r"\caption{Per-language paired deltas (GPT-4 minus Azure) computed from native-speaker scores vs GPT-4 (judge) scores (reference-free track). "
        r"Each delta is paired by excerpt; confidence intervals are bootstrap 95\% CIs over excerpts; $p$ values are exact sign-flip tests over excerpt-level deltas.}"
    )
    lines.append(r"\label{tab:ref-free-deltas-by-language-human-vs-judge}")
    lines.append(r"\begin{tabular}{@{}l l c c c c c c@{}}")
    lines.append(r"\toprule")
    lines.append(r"Language & Metric & $\Delta$ Human & 95\% CI & $p$ & $\Delta$ Judge & 95\% CI & $p$ \\")
    lines.append(r"\midrule")

    for _, r in df.iterrows():
        lines.append(
            f"{r['language']} & {METRIC_LABELS[r['metric']]} & "
            f"{fmt(r['delta_human'], 2)} & [{fmt(r['lo_human'], 2)}, {fmt(r['hi_human'], 2)}] & {fmt(r['p_human'], 3)}{stars(float(r['p_human']))} & "
            f"{fmt(r['delta_judge'], 2)} & [{fmt(r['lo_judge'], 2)}, {fmt(r['hi_judge'], 2)}] & {fmt(r['p_judge'], 3)}{stars(float(r['p_judge']))} \\\\"
        )

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


# -------------------------
# Main
# -------------------------
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=str, required=True, help="Path to ref_free_track_structured_numeric.json")
    ap.add_argument("--outdir", type=str, default=".", help="Output root directory (default: .)")
    ap.add_argument("--aggregation", choices=["micro", "macro"], default="micro",
                    help="How to build the Average panel: micro (all docs) or macro (avg over languages).")
    ap.add_argument("--seed", type=int, default=0, help="Random seed for bootstraps.")
    ap.add_argument(
        "--color_scatter_by",
        choices=["language", "system", "none"],
        default="language",
        help="How to color points in the judge-vs-human Overall scatter plot.",
    )
    args = ap.parse_args()

    out_root = Path(args.outdir)

    tables_dir = out_root / "tables"
    figures_dir = out_root / "figures"
    figures_png_dir = figures_dir / "png"

    data = load_ref_free_json(Path(args.json))
    sanity_check(data.human_doc, data.docs_expected, "human")
    sanity_check(data.judge_doc, data.docs_expected, "judge")

    # --- Tables ---
    write_tex(tables_dir / "ref-free-avg-scores.tex", make_table_avg_scores(data.human_doc, data.judge_doc))
    write_tex(tables_dir / "ref-free-deltas-macro.tex", make_table_deltas_macro(data.human_doc, seed=args.seed))
    write_tex(tables_dir / "ref-free-deltas-human-by-language.tex", make_table_deltas_by_language(data.human_doc, seed=args.seed))
    write_tex(tables_dir / "ref-free-deltas-judge-by-language.tex", make_table_deltas_by_language(data.judge_doc, seed=args.seed))
    write_tex(tables_dir / "ref-free-judge-human-agreement.tex", make_table_judge_human_agreement(data.human_doc, data.judge_doc))
    write_tex(tables_dir / "ref-free-deltas-by-language-human-vs-judge.tex", make_table_deltas_by_language_human_vs_judge(data.human_doc, data.judge_doc, seed=args.seed))

    # --- Figures (PNGs) ---
    avg_png = figures_png_dir / "reference-free-results-average-with-overall.png"
    scatter_png = figures_png_dir / "judge-vs-human-overall-scatter.png"
    plot_reference_free_panels(data.human_doc, data.judge_doc, avg_png, aggregation=args.aggregation)
    plot_judge_vs_human_overall(data.human_doc, data.judge_doc, scatter_png, color_by=args.color_scatter_by)

    # --- Figure include .tex ---
    # Use paths relative to paper root, adjust if your project differs
    write_tex(
        figures_dir / "reference-free-results-average-with-overall.tex",
        make_figure_tex_average("figures/png/reference-free-results-average-with-overall.png"),
    )
    write_tex(
        figures_dir / "ref-free-judge-vs-human.tex",
        make_figure_tex_scatter("figures/png/judge-vs-human-overall-scatter.png"),
    )

    print("Done. Wrote:")
    print(f"  {tables_dir / 'ref-free-avg-scores.tex'}")
    print(f"  {tables_dir / 'ref-free-deltas-macro.tex'}")
    print(f"  {tables_dir / 'ref-free-deltas-human-by-language.tex'}")
    print(f"  {tables_dir / 'ref-free-judge-human-agreement.tex'}")
    print(f"  {avg_png}")
    print(f"  {scatter_png}")
    print(f"  {figures_dir / 'reference-free-results-average-with-overall.tex'}")
    print(f"  {figures_dir / 'ref-free-judge-vs-human.tex'}")


if __name__ == "__main__":
    main()