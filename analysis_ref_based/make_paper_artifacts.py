#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_paper_artifacts.py

Creates research-paper-ready tables and figures from the outputs of
evaluate_translations.py (reference-based MT evaluation).

Expected inputs inside --in_dir (default: out_translation_eval):
  - metrics_paragraph_level.csv
  - metrics_summary.csv

Outputs written to --out_dir (default: paper_artifacts):
  - tables/  : CSV + Markdown + LaTeX tables
  - figures/ : publication-style figures (PNG and/or PDF)
  - appendix/: larger tables, pairwise matrices, and outlier lists
  - README.md: index of all generated artifacts

Dependencies:
  pip install -U numpy pandas matplotlib scipy

Key update (per your request):
  - Scatter plots now plot ONE point per (language, model), i.e., CORPUS/DOCUMENT-level,
    using metrics_summary.csv — matching your script’s granularity.
  - Points remain colored (configurable via --scatter_color_by).
  - No per-point text labels (avoids clutter); outliers are circled and exported as tables.
  - Where possible, outlier tables include a “worst” example segment with excerpts
    (pulled from metrics_paragraph_level.csv) for interpretability.

Run:
  python make_paper_artifacts.py --in_dir out_translation_eval --out_dir paper_artifacts \
      --primary_metric comet --formats png pdf --seed 42 --scatter_color_by language

"""

from __future__ import annotations

import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Sequence, Tuple, Dict

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scipy.stats import kendalltau


# -----------------------------
# Utilities
# -----------------------------


def setup_logger(out_dir: Path, verbose: bool = False) -> logging.Logger:
    out_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("paper_artifacts")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(ch)

    fh = logging.FileHandler(out_dir / "make_paper_artifacts.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(fh)
    return logger


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def safe_read_csv(path: Path, logger: logging.Logger) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(str(path))
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        logger.warning(f"UTF-8 decode failed for {path}; trying latin-1.")
        return pd.read_csv(path, encoding="latin-1")


def available_columns(df: pd.DataFrame) -> set:
    return set(df.columns.tolist())


def metric_direction(metric: str) -> int:
    """+1 = higher better, -1 = lower better."""
    m = metric.lower()
    if m in ("ter",):
        return -1
    return +1


def normalize_metric_name(m: str) -> str:
    m = m.strip().lower()
    # common alias normalization
    if m == "bertscore":
        return "bertscore_f1"
    return m


def col_ci_low(col: str) -> str:
    return f"{col}_ci_low"


def col_ci_high(col: str) -> str:
    return f"{col}_ci_high"


def bootstrap_mean_ci(
    values: np.ndarray,
    rng: np.random.Generator,
    ci: float = 0.95,
    n_boot: int = 10000,
) -> Tuple[float, float]:
    """Bootstrap CI for the mean of `values`.

    Intended for macro uncertainty by resampling across languages (one value per language).
    """
    v = np.asarray(values, dtype=float)
    v = v[~np.isnan(v)]
    n = int(v.shape[0])
    if n == 0:
        return (np.nan, np.nan)
    if n == 1:
        m = float(v[0])
        return (m, m)

    alpha = 1.0 - float(ci)
    # (n_boot, n) resamples with replacement
    samples = rng.choice(v, size=(int(n_boot), n), replace=True)
    stats = samples.mean(axis=1)
    lo = float(np.percentile(stats, 100.0 * (alpha / 2.0)))
    hi = float(np.percentile(stats, 100.0 * (1.0 - alpha / 2.0)))
    return (lo, hi)


def macro_from_per_language_rows(
    summary_df: pd.DataFrame,
    languages: Sequence[str],
    metric_col: str,
    models: Optional[Sequence[str]] = None,
    ci: float = 0.95,
    n_boot: int = 10000,
    seed: int = 0,
) -> pd.DataFrame:
    """Compute macro means + bootstrap CIs across languages from per-language rows.

    This is used for forest plots where `metrics_summary.csv` may contain per-language CIs
    but the `__overall__` rows do not include CIs.
    """
    per_lang = summary_df[summary_df["language"].isin([str(l).lower() for l in languages])].copy()
    if per_lang.empty:
        return pd.DataFrame(columns=["model", metric_col, col_ci_low(metric_col), col_ci_high(metric_col)])

    if models is None:
        model_list = sorted(per_lang["model"].unique().tolist())
    else:
        # Keep a stable order and include only models present.
        present = set(per_lang["model"].unique().tolist())
        model_list = [m for m in models if m in present]

    rows: List[Dict[str, object]] = []
    for i, m in enumerate(model_list):
        g = per_lang[per_lang["model"] == m]
        vals = pd.to_numeric(g[metric_col], errors="coerce").to_numpy()
        vals = vals[~np.isnan(vals)]
        if vals.size == 0:
            continue
        mean = float(np.mean(vals))
        rng_i = np.random.default_rng(int(seed) + i)
        lo, hi = bootstrap_mean_ci(vals, rng=rng_i, ci=ci, n_boot=n_boot)
        rows.append(
            {
                "model": m,
                metric_col: mean,
                col_ci_low(metric_col): lo,
                col_ci_high(metric_col): hi,
                "n_langs": int(vals.size),
            }
        )

    return pd.DataFrame(rows)


def to_markdown_table(df: pd.DataFrame, float_digits: int = 2, index: bool = False) -> str:
    if df.empty:
        return "_(empty)_\n"
    d = df.copy()
    for c in d.columns:
        if pd.api.types.is_float_dtype(d[c]):
            d[c] = d[c].map(lambda x: "" if pd.isna(x) else f"{float(x):.{float_digits}f}")
        elif pd.api.types.is_integer_dtype(d[c]):
            d[c] = d[c].map(lambda x: "" if pd.isna(x) else str(int(x)))
        else:
            d[c] = d[c].astype(str)
    if index:
        d.insert(0, "index", d.index.astype(str))
    headers = d.columns.tolist()
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in d.values.tolist():
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def save_table_bundle(
    df: pd.DataFrame,
    out_base: Path,
    name: str,
    logger: logging.Logger,
    *,
    float_digits: int = 2,
    index: bool = False,
    latex: bool = True,
) -> List[Path]:
    written: List[Path] = []
    out_base.mkdir(parents=True, exist_ok=True)

    csv_path = out_base / f"{name}.csv"
    df.to_csv(csv_path, index=index, encoding="utf-8")
    written.append(csv_path)

    md_path = out_base / f"{name}.md"
    md_path.write_text(to_markdown_table(df, float_digits=float_digits, index=index), encoding="utf-8")
    written.append(md_path)

    if latex:
        tex_path = out_base / f"{name}.tex"
        try:
            tex = df.to_latex(index=index, float_format=lambda x: f"{x:.{float_digits}f}", escape=True)
            tex_path.write_text(tex, encoding="utf-8")
            written.append(tex_path)
        except Exception as e:
            logger.warning(f"Failed to write LaTeX for {name}: {e}")

    logger.info(f"Wrote table bundle: {name} ({len(written)} files)")
    return written


def save_figure(fig: plt.Figure, out_dir: Path, stem: str, formats: Sequence[str], logger: logging.Logger) -> List[Path]:
    ensure_dir(out_dir)
    out_paths: List[Path] = []
    for fmt in formats:
        fmt = fmt.lower().strip(".")
        path = out_dir / f"{stem}.{fmt}"
        fig.savefig(path, bbox_inches="tight", dpi=300 if fmt in ("png", "jpg", "jpeg") else None)
        out_paths.append(path)
    plt.close(fig)
    logger.info(f"Saved figure: {stem} ({', '.join([p.suffix for p in out_paths])})")
    return out_paths


def order_languages(langs: Sequence[str]) -> List[str]:
    preferred = ["turkish", "spanish", "english", "polish", "ukrainian", "arabic", "german"]
    langs = list(dict.fromkeys([str(x) for x in langs]))
    ordered = [l for l in preferred if l in langs]
    ordered += sorted([l for l in langs if l not in ordered])
    return ordered


def order_models(models: Sequence[str]) -> List[str]:
    return sorted(list(dict.fromkeys([str(x) for x in models])))


def _build_color_map(categories: List[str], cmap_name: str = "tab10") -> Dict[str, Tuple[float, float, float, float]]:
    """Stable mapping category -> RGBA color."""
    cmap = plt.get_cmap(cmap_name)
    colors = {}
    for i, cat in enumerate(categories):
        colors[cat] = cmap(i % cmap.N)
    return colors


def resolve_metric_col(df: pd.DataFrame, base: str) -> Optional[str]:
    """
    Try to resolve a metric column name in a df. Common patterns:
      - base
      - base_mean
    """
    base = normalize_metric_name(base)
    candidates = [base, f"{base}_mean"]
    for c in candidates:
        if c in df.columns:
            return c
    return None


def metric_pretty_name(metric_col: str) -> str:
    """Human-friendly metric name for axes/titles."""
    base = str(metric_col).lower().replace("_mean", "")
    mapping = {
        "bertscore_f1": "BERTScore-F1",
        "chrf": "chrF++",
        "bleu": "BLEU",
        "ter": "TER",
        "comet": "COMET",

        # error-probe / diagnostics metrics
        "len_ratio": "Length ratio",
        "len_ratio_abs_dev": "|Length ratio − 1|",
        "num_f1": "Numbers F1",
        "acr_f1": "Acronym F1",
        "punct_pres": "Punctuation preservation",
        # common aliases
        "bertscore": "BERTScore-F1",
    }
    return mapping.get(base, metric_col)


def metric_axis_label(metric_col: str) -> str:
    """Axis label with units when known."""
    base = str(metric_col).lower().replace("_mean", "")
    name = metric_pretty_name(metric_col)

    # In this project:
    # - COMET/BLEU/chrF++/BERTScore-F1 are reported on a 0–100-ish scale
    #   (BERTScore-F1 is scaled by 100).
    if base in {"comet", "bleu", "chrf", "bertscore_f1"}:
        return f"{name} (0–100)"

    # - Simple probe F1 / preservation scores are in [0, 1].
    if base in {"num_f1", "acr_f1", "punct_pres"}:
        return f"{name} (0–1)"

    # - Length ratios are unitless.
    return name



# -----------------------------
# Data prep
# -----------------------------


@dataclass
class EvalData:
    paragraph_df: pd.DataFrame
    summary_df: pd.DataFrame
    languages: List[str]
    models: List[str]


def load_eval_data(in_dir: Path, logger: logging.Logger) -> EvalData:
    paragraph_df = safe_read_csv(in_dir / "metrics_paragraph_level.csv", logger)
    summary_df = safe_read_csv(in_dir / "metrics_summary.csv", logger)

    if "language" not in paragraph_df.columns or "model" not in paragraph_df.columns:
        raise ValueError("metrics_paragraph_level.csv must contain columns: language, model")
    if "language" not in summary_df.columns or "model" not in summary_df.columns:
        raise ValueError("metrics_summary.csv must contain columns: language, model")

    paragraph_df["language"] = paragraph_df["language"].astype(str).str.lower()
    paragraph_df["model"] = paragraph_df["model"].astype(str)

    summary_df["language"] = summary_df["language"].astype(str).str.lower()
    summary_df["model"] = summary_df["model"].astype(str)

    languages = order_languages([l for l in summary_df["language"].unique().tolist() if l != "__overall__"])
    models = order_models([m for m in summary_df["model"].unique().tolist() if m != "__overall__"])

    paragraph_df = paragraph_df[paragraph_df["language"].isin(languages) & paragraph_df["model"].isin(models)].copy()
    summary_df = summary_df[summary_df["language"].isin(languages + ["__overall__"]) & summary_df["model"].isin(models + ["__overall__"])].copy()

    if "unit_id" not in paragraph_df.columns:
        raise ValueError("metrics_paragraph_level.csv must contain unit_id (aligned segment id).")
    paragraph_df["unit_id"] = paragraph_df["unit_id"].astype(int)

    return EvalData(paragraph_df=paragraph_df, summary_df=summary_df, languages=languages, models=models)


def infer_overall_rows(summary_df: pd.DataFrame, languages: Sequence[str], logger: logging.Logger) -> pd.DataFrame:
    df_over = summary_df[summary_df["language"] == "__overall__"].copy()
    if not df_over.empty:
        return df_over

    logger.warning("No __overall__ rows found; computing macro-averages across languages.")
    df = summary_df[summary_df["language"].isin(languages)].copy()
    out_rows = []
    metric_cols = [c for c in df.columns if c not in ("model", "language")]
    num_cols = [c for c in metric_cols if pd.api.types.is_numeric_dtype(df[c])]
    for model, g in df.groupby("model", sort=False):
        row = {"model": model, "language": "__overall__", "n_langs": int(g["language"].nunique())}
        for c in num_cols:
            vals = g[c].dropna().astype(float)
            row[c] = float(vals.mean()) if len(vals) else np.nan
            row[f"{c}_std"] = float(vals.std(ddof=0)) if len(vals) else np.nan
        out_rows.append(row)
    return pd.DataFrame(out_rows)


# -----------------------------
# Tables (unchanged from prior version)
# -----------------------------


def table_dataset_summary(data: EvalData, out_tables: Path, logger: logging.Logger) -> List[Path]:
    p = data.paragraph_df
    cols = available_columns(p)

    seg_counts = p.groupby("language")["unit_id"].nunique().rename("n_segments")

    ref_len_col = "ref_char_len" if "ref_char_len" in cols else ("ref_text_raw" if "ref_text_raw" in cols else None)

    ref_chars = []
    for lang in data.languages:
        df_lang = p[p["language"] == lang]
        if df_lang.empty:
            continue
        first_model = df_lang["model"].iloc[0]
        df_one = df_lang[df_lang["model"] == first_model]
        if ref_len_col == "ref_char_len":
            total = float(df_one["ref_char_len"].fillna(0).astype(float).sum())
        elif ref_len_col == "ref_text_raw":
            total = float(df_one["ref_text_raw"].fillna("").astype(str).map(len).sum())
        else:
            total = np.nan
        ref_chars.append((lang, total))

    ref_chars_s = pd.Series({k: v for k, v in ref_chars}, name="ref_chars_total")

    models_per_lang = (
        data.summary_df[data.summary_df["language"] != "__overall__"].groupby("language")["model"].nunique().rename("n_models")
    )

    df = pd.concat([seg_counts, ref_chars_s, models_per_lang], axis=1).reset_index().rename(columns={"index": "language"})
    df = df.set_index("language").loc[data.languages].reset_index()

    totals = {
        "language": "ALL",
        "n_segments": int(seg_counts.sum()) if len(seg_counts) else np.nan,
        "ref_chars_total": float(ref_chars_s.sum()) if len(ref_chars_s) else np.nan,
        "n_models": int(data.summary_df[data.summary_df["language"] != "__overall__"]["model"].nunique()),
    }
    df = pd.concat([df, pd.DataFrame([totals])], ignore_index=True)

    return save_table_bundle(df, out_tables, "T1_dataset_summary", logger, float_digits=0, index=False, latex=True)


def table_overall_results(
    data: EvalData,
    out_tables: Path,
    logger: logging.Logger,
    primary_metric: str,
    metrics: Sequence[str],
) -> List[Path]:
    summary = data.summary_df.copy()
    overall = infer_overall_rows(summary, data.languages, logger)

    primary_col = normalize_metric_name(primary_metric)
    cols = available_columns(overall)

    metric_cols = []
    for m in metrics:
        c = normalize_metric_name(m)
        # allow *_mean if present
        if c not in cols and f"{c}_mean" in cols:
            c = f"{c}_mean"
        if c in cols:
            metric_cols.append(c)

    consistency_cols = [f"{c}_std" for c in metric_cols if f"{c}_std" in cols]
    keep_cols = ["model", "n_langs"] if "n_langs" in cols else ["model"]
    keep_cols += metric_cols + consistency_cols

    df = overall[keep_cols].copy()

    # Sort by primary if present
    pri = primary_col if primary_col in df.columns else (f"{primary_col}_mean" if f"{primary_col}_mean" in df.columns else None)
    if pri and pri in df.columns and df[pri].notna().any():
        ascending = metric_direction(primary_col) < 0
        df = df.sort_values(pri, ascending=ascending).reset_index(drop=True)

    # Ranks (per metric column)
    for c in metric_cols:
        base = c.replace("_mean", "")
        ascending = metric_direction(base) < 0
        df[f"rank_{c}"] = df[c].rank(ascending=ascending, method="average")
    rank_cols = [f"rank_{c}" for c in metric_cols]
    if rank_cols:
        df["rank_mean"] = df[rank_cols].mean(axis=1)
        df = df.sort_values("rank_mean", ascending=True).reset_index(drop=True)

    rename = {
        "bertscore_f1": "BERTScore-F1",
        "bertscore_f1_mean": "BERTScore-F1",
        "chrf": "chrF",
        "chrf_mean": "chrF",
        "bleu": "BLEU",
        "bleu_mean": "BLEU",
        "ter": "TER",
        "ter_mean": "TER",
        "comet": "COMET",
        "comet_mean": "COMET",
    }
    for c in consistency_cols:
        base = c.replace("_std", "").replace("_mean", "")
        if base in rename:
            rename[c] = f"σ(lang) {rename[base]}"
    if "n_langs" in df.columns:
        rename["n_langs"] = "Langs"

    df = df.rename(columns=rename)

    keep = ["model"]
    if "Langs" in df.columns:
        keep.append("Langs")
    keep += [rename.get(c, c) for c in metric_cols]
    keep += [rename.get(c, c) for c in consistency_cols]

    # Optional CI for primary
    if pri:
        ci_low = col_ci_low(pri)
        ci_high = col_ci_high(pri)
        if ci_low in overall.columns and ci_high in overall.columns:
            df_ci = overall[["model", ci_low, ci_high]].copy()
            df_ci = df_ci.rename(columns={ci_low: "Primary CI low", ci_high: "Primary CI high"})
            df = df.merge(df_ci, on="model", how="left")
            keep += ["Primary CI low", "Primary CI high"]

    return save_table_bundle(df[keep], out_tables, "T2_overall_results", logger, float_digits=2, index=False, latex=True)


def table_per_language_winners(
    data: EvalData,
    out_tables: Path,
    logger: logging.Logger,
    metrics: Sequence[str],
    tie_mode: str = "ci_overlap",
) -> List[Path]:
    s = data.summary_df[data.summary_df["language"].isin(data.languages)].copy()
    rows = []
    for lang in data.languages:
        df = s[s["language"] == lang].copy()
        if df.empty:
            continue
        for m in metrics:
            base = normalize_metric_name(m)
            col = base if base in df.columns else (f"{base}_mean" if f"{base}_mean" in df.columns else None)
            if col is None or df[col].isna().all():
                continue
            ascending = metric_direction(base) < 0
            d2 = df[["model", col]].dropna().sort_values(col, ascending=ascending).reset_index(drop=True)
            if d2.empty:
                continue
            best_model = str(d2.loc[0, "model"])
            best_val = float(d2.loc[0, col])
            tie = False
            if tie_mode == "ci_overlap":
                lo, hi = col_ci_low(col), col_ci_high(col)
                if lo in df.columns and hi in df.columns and len(d2) >= 2:
                    top = df[df["model"] == d2.loc[0, "model"]].iloc[0]
                    second = df[df["model"] == d2.loc[1, "model"]].iloc[0]
                    if pd.notna(top.get(lo)) and pd.notna(top.get(hi)) and pd.notna(second.get(lo)) and pd.notna(second.get(hi)):
                        tlo, thi = float(top[lo]), float(top[hi])
                        slo, shi = float(second[lo]), float(second[hi])
                        tie = not (tlo > shi or slo > thi)
            rows.append({"language": lang, "metric": col, "winner": best_model, "winner_score": best_val, "tie_top2": tie})

    out = pd.DataFrame(rows)
    if out.empty:
        logger.warning("Could not build T3_per_language_winners (no metric columns present).")
        return []

    pretty = {
        "bertscore_f1": "BERTScore-F1",
        "bertscore_f1_mean": "BERTScore-F1",
        "chrf": "chrF",
        "chrf_mean": "chrF",
        "bleu": "BLEU",
        "bleu_mean": "BLEU",
        "ter": "TER",
        "ter_mean": "TER",
        "comet": "COMET",
        "comet_mean": "COMET",
    }
    out["metric"] = out["metric"].map(lambda x: pretty.get(x, x))
    out = out.sort_values(["language", "metric"]).reset_index(drop=True)
    return save_table_bundle(out, out_tables, "T3_per_language_winners", logger, float_digits=2, index=False, latex=True)


def table_metric_agreement(
    data: EvalData,
    out_tables: Path,
    logger: logging.Logger,
    metrics: Sequence[str],
    lexical_cols: Sequence[str],
    semantic_cols: Sequence[str],
) -> List[Path]:
    p = data.paragraph_df.copy()
    cols = available_columns(p)

    chosen = []
    for m in metrics:
        c = normalize_metric_name(m)
        if c in cols and p[c].notna().any():
            chosen.append(c)
    if len(chosen) < 2:
        logger.warning("Not enough metrics for correlation tables.")
        return []

    df = p[chosen].copy()
    if "ter" in df.columns:
        df["neg_ter"] = -df["ter"]
        df = df.drop(columns=["ter"])

    pearson = df.corr(method="pearson")
    spearman = df.corr(method="spearman")

    written = []
    written += save_table_bundle(pearson, out_tables, "T4_metric_corr_pearson", logger, float_digits=3, index=True, latex=True)
    written += save_table_bundle(spearman, out_tables, "T4_metric_corr_spearman", logger, float_digits=3, index=True, latex=True)

    def z(x: pd.Series) -> pd.Series:
        return (x - x.mean()) / (x.std(ddof=0) + 1e-9)

    lex = []
    sem = []

    for c in lexical_cols:
        c2 = normalize_metric_name(c)
        if c2 in p.columns and p[c2].notna().any():
            lex.append(z(-p[c2].astype(float)) if c2 == "ter" else z(p[c2].astype(float)))

    for c in semantic_cols:
        c2 = normalize_metric_name(c)
        if c2 in p.columns and p[c2].notna().any():
            sem.append(z(p[c2].astype(float)))

    if lex and sem:
        p2 = p.copy()
        p2["lex_score_z"] = sum(lex) / len(lex)
        p2["sem_score_z"] = sum(sem) / len(sem)
        p2["disagree_z"] = p2["lex_score_z"] - p2["sem_score_z"]

        thr = 1.0
        summary = (
            p2.groupby(["language", "model"])["disagree_z"]
            .apply(lambda s: float((s.abs() >= thr).mean()))
            .rename("rate_|lex-sem|>=1")
            .reset_index()
        )
        overall = (
            p2.groupby("model")["disagree_z"]
            .apply(lambda s: float((s.abs() >= thr).mean()))
            .rename("rate_|lex-sem|>=1")
            .reset_index()
        )
        overall.insert(0, "language", "ALL")

        out = pd.concat([summary, overall], ignore_index=True)
        out = out.sort_values(["language", "rate_|lex-sem|>=1"], ascending=[True, False]).reset_index(drop=True)
        written += save_table_bundle(out, out_tables, "T4_metric_disagreement_rate", logger, float_digits=3, index=False, latex=True)
    else:
        logger.warning("Could not compute disagreement rate (missing lexical or semantic columns).")

    return written


# -----------------------------
# Pairwise comparisons (appendix-friendly)
# -----------------------------


def paired_bootstrap_diff(
    df: pd.DataFrame,
    metric_col: str,
    model_a: str,
    model_b: str,
    rng: np.random.Generator,
    n_samples: int = 5000,
) -> Tuple[float, float, float, float]:
    da = df[df["model"] == model_a][["unit_id", metric_col]].dropna()
    db = df[df["model"] == model_b][["unit_id", metric_col]].dropna()

    merged = da.merge(db, on="unit_id", suffixes=("_a", "_b"))
    if merged.empty or merged["unit_id"].nunique() < 2:
        return np.nan, np.nan, np.nan, np.nan

    diffs = (merged[f"{metric_col}_a"].astype(float) - merged[f"{metric_col}_b"].astype(float)).values
    n = len(diffs)
    idx = np.arange(n)
    samples = np.empty(n_samples, dtype=np.float64)
    for i in range(n_samples):
        sidx = rng.choice(idx, size=n, replace=True)
        samples[i] = diffs[sidx].mean()

    mean_diff = float(diffs.mean())
    ci_low = float(np.percentile(samples, 2.5))
    ci_high = float(np.percentile(samples, 97.5))

    p_le = float((samples <= 0).mean())
    p_ge = float((samples >= 0).mean())
    p = 2 * min(p_le, p_ge)
    p = min(1.0, max(0.0, p))
    return mean_diff, ci_low, ci_high, p


def holm_bonferroni(pvals: List[float], alpha: float = 0.05) -> List[bool]:
    m = len(pvals)
    order = np.argsort(pvals)
    reject_sorted = [False] * m
    for k, idx in enumerate(order):
        threshold = alpha / (m - k)
        if pvals[idx] <= threshold:
            reject_sorted[k] = True
        else:
            break
    rejects = [False] * m
    for k, idx in enumerate(order):
        rejects[idx] = reject_sorted[k]
    return rejects


def appendix_pairwise_matrices(
    data: EvalData,
    out_appendix: Path,
    logger: logging.Logger,
    primary_metric: str,
    bootstrap_samples: int,
    seed: int,
    alpha: float,
) -> List[Path]:
    p = data.paragraph_df.copy()
    metric_col = normalize_metric_name(primary_metric)
    if metric_col not in p.columns or p[metric_col].isna().all():
        logger.warning(f"Primary metric '{metric_col}' not available; skipping pairwise matrices.")
        return []

    dirn = metric_direction(metric_col)
    models = data.models
    languages = data.languages
    rng = np.random.default_rng(seed)

    win = pd.DataFrame(index=models, columns=models, dtype=float)
    win[:] = np.nan

    sig = pd.DataFrame(index=models, columns=models, dtype=object)
    sig[:] = ""

    pair_records = []
    pvals = []

    for i, a in enumerate(models):
        for j, b in enumerate(models):
            if i == j:
                sig.loc[a, b] = "—"
                continue

            wr_langs = []
            diffs_lang = []
            p_lang = []

            for lang in languages:
                df_lang = p[p["language"] == lang]
                da = df_lang[df_lang["model"] == a][["unit_id", metric_col]].dropna()
                db = df_lang[df_lang["model"] == b][["unit_id", metric_col]].dropna()
                merged = da.merge(db, on="unit_id", suffixes=("_a", "_b"))
                if merged.empty:
                    continue
                xa = merged[f"{metric_col}_a"].astype(float).values
                xb = merged[f"{metric_col}_b"].astype(float).values
                wr = float((xa > xb).mean()) if dirn > 0 else float((xa < xb).mean())
                wr_langs.append(wr)

                md, _, _, pv = paired_bootstrap_diff(
                    df_lang, metric_col, a, b, rng=rng, n_samples=max(500, bootstrap_samples // 2)
                )
                diffs_lang.append(md)
                p_lang.append(pv)

            win.loc[a, b] = float(np.mean(wr_langs)) if wr_langs else np.nan
            md = float(np.mean(diffs_lang)) if diffs_lang else np.nan
            pv = float(np.max(p_lang)) if p_lang else np.nan  # conservative across langs
            pair_records.append((a, b, md, pv))
            pvals.append(pv if np.isfinite(pv) else 1.0)

    unordered = {}
    for (a, b, md, pv) in pair_records:
        key = tuple(sorted([a, b]))
        if key not in unordered:
            unordered[key] = pv
        else:
            unordered[key] = min(unordered[key], pv)

    unordered_keys = list(unordered.keys())
    unordered_pvals = [unordered[k] if np.isfinite(unordered[k]) else 1.0 for k in unordered_keys]
    unordered_rej = holm_bonferroni(unordered_pvals, alpha=alpha)
    unordered_sig = {k: unordered_rej[i] for i, k in enumerate(unordered_keys)}

    for (a, b, md, pv) in pair_records:
        if not np.isfinite(md):
            sig.loc[a, b] = ""
            continue
        key = tuple(sorted([a, b]))
        is_sig = unordered_sig.get(key, False)
        better = (md > 0) if dirn > 0 else (md < 0)
        sig.loc[a, b] = ("↑" if better else "↓") if is_sig else "·"

    written = []
    written += save_table_bundle(win, out_appendix, "A2_winrate_matrix_primary_metric", logger, float_digits=3, index=True, latex=True)
    written += save_table_bundle(sig, out_appendix, "A3_significance_matrix_primary_metric_holm", logger, float_digits=0, index=True, latex=True)

    long = []
    for (a, b, md, pv) in pair_records:
        key = tuple(sorted([a, b]))
        long.append(
            {
                "model_a": a,
                "model_b": b,
                "mean_diff_A_minus_B": md,
                "p_value_conservative": pv,
                "holm_sig_unordered_pair": bool(unordered_sig.get(key, False)),
            }
        )
    df_long = pd.DataFrame(long)
    written += save_table_bundle(df_long, out_appendix, "A3_pairwise_diffs_pvals_long", logger, float_digits=5, index=False, latex=True)
    return written


# -----------------------------
# Figures
# -----------------------------


def fig_heatmap_model_language(
    data: EvalData,
    out_figs: Path,
    logger: logging.Logger,
    primary_metric: str,
    formats: Sequence[str],
) -> List[Path]:
    s = data.summary_df[data.summary_df["language"].isin(data.languages)].copy()
    metric_col = resolve_metric_col(s, primary_metric)
    if metric_col is None or s[metric_col].isna().all():
        logger.warning(f"Cannot create heatmap: metric '{primary_metric}' not available.")
        return []

    pivot = s.pivot_table(index="model", columns="language", values=metric_col, aggfunc="mean")
    pivot = pivot.reindex(index=data.models, columns=data.languages)

    # sort models by macro
    base = normalize_metric_name(primary_metric)
    dirn = metric_direction(base)
    macro = pivot.mean(axis=1, skipna=True)
    pivot = pivot.loc[macro.sort_values(ascending=(dirn < 0)).index]

    fig = plt.figure(figsize=(1.3 * len(data.languages) + 4, 0.35 * len(pivot.index) + 3))
    ax = fig.add_subplot(111)
    im = ax.imshow(pivot.values, aspect="auto")
    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_title(f"Model × Language heatmap ({metric_pretty_name(metric_col)})")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(metric_axis_label(metric_col))

    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            v = pivot.values[i, j]
            if np.isfinite(v):
                ax.text(j, i, f"{v:.1f}", ha="center", va="center", fontsize=7)

    fig.tight_layout()
    return save_figure(fig, out_figs, f"F1_heatmap_{metric_col}", formats, logger)


def fig_forest_overall_with_ci(
    data: EvalData,
    out_figs: Path,
    logger: logging.Logger,
    primary_metric: str,
    formats: Sequence[str],
    top_k: int = 10,
    seed: int = 42,
    n_boot: int = 5000,
    ci: float = 0.95,
) -> List[Path]:
    """Forest plot of macro (across-language) scores with bootstrap CIs.

    Unlike the per-language CIs stored in `metrics_summary.csv`, this macro CI is computed
    by bootstrapping *across languages* (one value per language), directly from the
    per-language rows. This ensures CI bars are available even when `__overall__` rows
    do not have CI columns populated.
    """
    base = normalize_metric_name(primary_metric)

    # Prefer computing macro uncertainty from per-language rows (Option B).
    per_lang = data.summary_df[data.summary_df["language"].isin(data.languages)].copy()
    metric_col = resolve_metric_col(per_lang, base) or base
    if metric_col not in per_lang.columns or per_lang[metric_col].isna().all():
        logger.warning(f"Cannot create forest plot: metric '{primary_metric}' not available.")
        return []

    df = macro_from_per_language_rows(
        data.summary_df,
        data.languages,
        metric_col,
        models=data.models,
        ci=ci,
        n_boot=n_boot,
        seed=seed,
    )

    if df.empty or metric_col not in df.columns or df[metric_col].isna().all():
        logger.warning(f"Cannot create forest plot: could not compute macro values for '{primary_metric}'.")
        return []

    dirn = metric_direction(base)
    df = df.dropna(subset=[metric_col]).copy()
    df = df.sort_values(metric_col, ascending=(dirn < 0)).reset_index(drop=True)
    df = df.head(top_k)

    y = np.arange(len(df))
    fig = plt.figure(figsize=(7.5, 0.45 * len(df) + 2.2))
    ax = fig.add_subplot(111)

    ax.scatter(df[metric_col].values, y)

    lo_col, hi_col = col_ci_low(metric_col), col_ci_high(metric_col)
    if lo_col in df.columns and hi_col in df.columns and df[lo_col].notna().any() and df[hi_col].notna().any():
        xerr_left = df[metric_col].values - df[lo_col].values
        xerr_right = df[hi_col].values - df[metric_col].values
        ax.errorbar(df[metric_col].values, y, xerr=[xerr_left, xerr_right], fmt="none", capsize=3)

    ax.set_yticks(y)
    ax.set_yticklabels(df["model"].tolist())
    ax.invert_yaxis()
    ax.set_xlabel(metric_axis_label(metric_col))
    # Keep the in-plot title minimal for paper use; the LaTeX caption carries the methodology.
    ax.set_title("")
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return save_figure(fig, out_figs, f"F2_forest_overall_{metric_col}", formats, logger)

def fig_violin_segment_distributions(
    data: EvalData,
    out_figs: Path,
    logger: logging.Logger,
    primary_metric: str,
    formats: Sequence[str],
    by_language: bool = False,
) -> List[Path]:
    p = data.paragraph_df.copy()
    metric_col = normalize_metric_name(primary_metric)
    if metric_col not in p.columns or p[metric_col].isna().all():
        logger.warning(f"Cannot create violin plots: metric '{primary_metric}' not in paragraph data.")
        return []

    written = []
    models = data.models

    def make_one(df: pd.DataFrame, tag: str) -> List[Path]:
        vals = []
        labels = []
        for m in models:
            v = df[df["model"] == m][metric_col].dropna().astype(float).values
            if len(v) == 0:
                continue
            vals.append(v)
            labels.append(m)
        if len(vals) < 2:
            return []
        fig = plt.figure(figsize=(max(8, 0.6 * len(labels)), 4.5))
        ax = fig.add_subplot(111)
        ax.violinplot(vals, showmeans=True, showmedians=False, showextrema=False)
        ax.set_xticks(np.arange(1, len(labels) + 1))
        ax.set_xticklabels(labels, rotation=45, ha="right")
        ax.set_ylabel(metric_axis_label(metric_col))
        ax.set_title(f"Segment-level distribution by model ({metric_pretty_name(metric_col)}){tag}")
        ax.grid(True, axis="y", alpha=0.3)
        fig.tight_layout()
        return save_figure(fig, out_figs, f"F3_violin_{metric_col}{tag.replace(' ', '_')}".strip("_"), formats, logger)

    if not by_language:
        written += make_one(p, tag="")
    else:
        for lang in data.languages:
            df_lang = p[p["language"] == lang]
            if not df_lang.empty:
                written += make_one(df_lang, tag=f" ({lang})")
    return written


# ---- UPDATED: corpus-level scatter (one point per language, model) ----


def fig_scatter_corpus_lexical_semantic_with_outliers(
    data: EvalData,
    out_figs: Path,
    logger: logging.Logger,
    x_metric: str,
    y_metric: str,
    formats: Sequence[str],
    *,
    color_by: str = "language",
    annotate_n: int = 0,  # default off to avoid clutter
    legend_max_items: int = 12,
    highlight_outliers: bool = True,
) -> List[Path]:
    """
    CORPUS-level scatter: ONE point per (language, model), using metrics_summary.csv.

    - color_by: 'language' or 'model' or 'none'
    - No per-point text labels by default; optional numeric labels ONLY for outliers.
    - Outliers circled and exported to appendix; if paragraph-level raw text exists,
      also include a representative “worst” segment excerpt for that (language, model).
    """
    s = data.summary_df[data.summary_df["language"].isin(data.languages)].copy()
    x_col = resolve_metric_col(s, x_metric)
    y_col = resolve_metric_col(s, y_metric)
    if x_col is None or y_col is None:
        logger.warning(f"Cannot create corpus scatter: missing columns for {x_metric} or {y_metric}.")
        return []
    if s[x_col].isna().all() or s[y_col].isna().all():
        logger.warning(f"Cannot create corpus scatter: {x_col} or {y_col} is entirely NaN.")
        return []

    # Ensure unique (language, model)
    df = (
        s[["language", "model", x_col, y_col]]
        .dropna(subset=[x_col, y_col])
        .groupby(["language", "model"], as_index=False)
        .mean()
    )
    if df.empty:
        return []

    def z_within_lang(series: pd.Series) -> pd.Series:
        return (series - series.mean()) / (series.std(ddof=0) + 1e-9)

    df["x_z"] = df.groupby("language")[x_col].transform(z_within_lang)
    df["y_z"] = df.groupby("language")[y_col].transform(z_within_lang)
    df["disagree"] = df["x_z"] - df["y_z"]
    df["abs_disagree"] = df["disagree"].abs()

    # Outliers: extremes across all (language, model) points
    k = 10
    top_pos = df.sort_values("disagree", ascending=False).head(k // 2)
    top_neg = df.sort_values("disagree", ascending=True).head(k - len(top_pos))
    extreme = pd.concat([top_pos, top_neg], ignore_index=True)

    # Plot
    fig = plt.figure(figsize=(6.4, 5.4))
    ax = fig.add_subplot(111)

    if color_by not in ("language", "model", "none"):
        logger.warning(f"Unknown --scatter_color_by='{color_by}', defaulting to 'language'.")
        color_by = "language"

    categories: List[str] = []
    cmap: Dict[str, Tuple[float, float, float, float]] = {}

    if color_by == "none":
        ax.scatter(df[x_col].astype(float).values, df[y_col].astype(float).values, alpha=0.8, s=45)
    else:
        categories = sorted(df[color_by].astype(str).unique().tolist())
        cmap_name = "tab10" if len(categories) <= 10 else ("tab20" if len(categories) <= 20 else "hsv")
        cmap = _build_color_map(categories, cmap_name=cmap_name)
        for cat in categories:
            sub = df[df[color_by].astype(str) == cat]
            ax.scatter(
                sub[x_col].astype(float).values,
                sub[y_col].astype(float).values,
                alpha=0.85,
                s=45,
                label=cat,
                color=cmap[cat],
            )

    # Outlier rings
    if highlight_outliers and not extreme.empty:
        ax.scatter(
            extreme[x_col].astype(float).values,
            extreme[y_col].astype(float).values,
            s=90,
            alpha=0.95,
            facecolors="none",
            edgecolors="black",
            linewidths=1.0,
            label="Outliers" if (color_by != "none" and len(categories) <= legend_max_items) else None,
        )

    # Optional: tiny numeric labels for outliers only
    n = max(0, int(annotate_n))
    if n > 0 and not extreme.empty:
        extreme2 = extreme.sort_values("abs_disagree", ascending=False).head(n).reset_index(drop=True)
        for i, r in extreme2.iterrows():
            ax.annotate(
                str(i + 1),
                (float(r[x_col]), float(r[y_col])),
                textcoords="offset points",
                xytext=(3, 3),
                fontsize=8,
                color="black",
            )

    ax.set_xlabel(metric_axis_label(x_col))
    ax.set_ylabel(metric_axis_label(y_col))

    # Paper-ready title: keep it short; move methodological details into caption or a small in-plot note.
    ax.set_title(f"{metric_pretty_name(x_col)} vs {metric_pretty_name(y_col)}")
    ax.grid(True, alpha=0.25)

    if color_by != "none" and len(categories) <= legend_max_items:
        ax.legend(
            loc="upper left",
            bbox_to_anchor=(1.02, 1.0),
            borderaxespad=0,
            frameon=False,
            title=("Language" if color_by == "language" else ("System" if color_by == "model" else str(color_by))),
        )

    fig.tight_layout()

    # Appendix outlier table
    out_appendix = out_figs.parent / "appendix"
    ensure_dir(out_appendix)

    out_tbl = extreme[["language", "model", x_col, y_col, "disagree", "abs_disagree"]].copy()
    out_tbl["outlier_rank_abs"] = out_tbl["abs_disagree"].rank(ascending=False, method="min").astype(int)

    # If we can, add a representative “worst segment” excerpt for that (language, model)
    p = data.paragraph_df.copy()
    seg_x = normalize_metric_name(x_metric)
    seg_y = normalize_metric_name(y_metric)
    have_seg_y = seg_y in p.columns and p[seg_y].notna().any()
    have_text = ("sys_text_raw" in p.columns) and ("ref_text_raw" in p.columns)
    if have_seg_y and have_text:
        y_dir = metric_direction(seg_y)

        def excerpt(s: object, n_chars: int = 240) -> str:
            s = "" if pd.isna(s) else str(s).replace("\n", " ").strip()
            return (s[:n_chars] + "…") if len(s) > n_chars else s

        worst_unit_ids = []
        worst_sys = []
        worst_ref = []
        for _, r in out_tbl.iterrows():
            lang = r["language"]
            model = r["model"]
            sub = p[(p["language"] == lang) & (p["model"] == model)].dropna(subset=[seg_y])
            if sub.empty:
                worst_unit_ids.append(np.nan)
                worst_sys.append("")
                worst_ref.append("")
                continue
            # “worst” by semantic metric y: min if higher-better, max if lower-better
            sub = sub.sort_values(seg_y, ascending=(y_dir > 0))
            worst = sub.iloc[0]
            worst_unit_ids.append(int(worst["unit_id"]))
            worst_sys.append(excerpt(worst.get("sys_text_raw", "")))
            worst_ref.append(excerpt(worst.get("ref_text_raw", "")))
        out_tbl["worst_unit_id_by_y"] = worst_unit_ids
        out_tbl["worst_sys_excerpt"] = worst_sys
        out_tbl["worst_ref_excerpt"] = worst_ref
    else:
        # keep columns absent rather than empty, to avoid implying availability
        pass

    save_table_bundle(out_tbl, out_appendix, f"A4_corpus_scatter_outliers_{x_col}_vs_{y_col}", logger, float_digits=3, index=False, latex=True)

    return save_figure(fig, out_figs, f"F4_scatter_corpus_{x_col}_vs_{y_col}_colored_{color_by}", formats, logger)


def fig_error_probe_bars(
    data: EvalData,
    out_figs: Path,
    logger: logging.Logger,
    formats: Sequence[str],
) -> List[Path]:
    s = data.summary_df[data.summary_df["language"].isin(data.languages)].copy()
    needed = ["len_ratio_mean", "num_f1_mean", "punct_pres_mean", "acr_f1_mean"]
    cols = available_columns(s)
    avail = [c for c in needed if c in cols and s[c].notna().any()]
    if not avail:
        logger.warning("No probe columns available for error-probe figure.")
        return []

    out = []
    for model, g in s.groupby("model"):
        row = {"model": model}
        for c in avail:
            row[c] = float(g[c].dropna().astype(float).mean()) if g[c].notna().any() else np.nan
        out.append(row)
    df = pd.DataFrame(out).set_index("model").reindex(data.models)

    if "len_ratio_mean" in df.columns:
        df["len_ratio_abs_dev"] = (df["len_ratio_mean"].astype(float) - 1.0).abs()

    written = []
    for c in df.columns:
        vals = df[c].astype(float).values
        if not np.isfinite(vals).any():
            continue
        fig = plt.figure(figsize=(max(8, 0.55 * len(df.index)), 4.2))
        ax = fig.add_subplot(111)
        ax.bar(df.index.tolist(), vals.tolist())
        ax.set_xticklabels(df.index.tolist(), rotation=45, ha="right")
        ax.set_title("")
        ax.set_ylabel(metric_axis_label(c))
        ax.grid(True, axis="y", alpha=0.3)
        fig.tight_layout()
        written += save_figure(fig, out_figs, f"F5_probe_{c}", formats, logger)

    out_appendix = out_figs.parent / "appendix"
    ensure_dir(out_appendix)
    save_table_bundle(df.reset_index(), out_appendix, "A5_probe_summary_by_model", logger, float_digits=3, index=False, latex=True)
    return written


def fig_rank_stability(
    data: EvalData,
    out_figs: Path,
    logger: logging.Logger,
    metrics: Sequence[str],
    formats: Sequence[str],
) -> List[Path]:
    s = data.summary_df.copy()
    langs = data.languages
    cols = available_columns(s)

    candidates = ["comet", "bertscore_f1", "chrf", "bleu"]
    primary = next((c for c in candidates if c in cols and s[c].notna().any()), None)
    if primary is None:
        primary = next((f"{c}_mean" for c in candidates if f"{c}_mean" in cols and s[f"{c}_mean"].notna().any()), None)
    if primary is None:
        logger.warning("Cannot compute rank stability: no usable metric columns.")
        return []

    metrics_cols = []
    for m in metrics:
        c = normalize_metric_name(m)
        if c not in cols and f"{c}_mean" in cols:
            c = f"{c}_mean"
        if c in cols and s[c].notna().any():
            metrics_cols.append(c)
    metrics_cols = list(dict.fromkeys(metrics_cols))
    if len(metrics_cols) < 2:
        return []

    over = infer_overall_rows(s, langs, logger)

    def ranks(df: pd.DataFrame, col: str) -> pd.Series:
        base = col.replace("_mean", "")
        ascending = metric_direction(base) < 0
        return df.set_index("model")[col].rank(ascending=ascending, method="average")

    over = over.dropna(subset=[primary]).copy()
    if over.empty:
        return []

    base_r = ranks(over, primary)

    taus = []
    for c in metrics_cols:
        if c == primary:
            continue
        d = over.dropna(subset=[c]).copy()
        common = base_r.index.intersection(d["model"])
        if len(common) < 3:
            continue
        r1 = base_r.loc[common].values
        r2 = ranks(d, c).loc[common].values
        tau = float(kendalltau(r1, r2).correlation)
        taus.append({"metric": c, "kendall_tau_vs_primary": tau})

    df_tau = pd.DataFrame(taus)
    if df_tau.empty:
        return []

    fig = plt.figure(figsize=(7.0, 3.8))
    ax = fig.add_subplot(111)
    ax.bar(df_tau["metric"].apply(metric_pretty_name).tolist(), df_tau["kendall_tau_vs_primary"].astype(float).tolist())
    ax.set_ylim(-1.0, 1.0)
    ax.set_title(f"Rank stability vs primary metric ({metric_pretty_name(primary)}) — Kendall τ (overall macro)")
    ax.set_ylabel("Kendall τ")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()

    out_appendix = out_figs.parent / "appendix"
    ensure_dir(out_appendix)
    save_table_bundle(df_tau, out_appendix, "A6_rank_stability_kendall_tau", logger, float_digits=3, index=False, latex=True)

    return save_figure(fig, out_figs, "A6_rank_stability_kendall_tau", formats, logger)


# -----------------------------
# README index
# -----------------------------


def write_readme(out_dir: Path, tables: List[Path], figures: List[Path], appendix: List[Path]) -> None:
    lines = []
    lines.append("# Paper artifacts index\n")
    lines.append("This folder was generated by `make_paper_artifacts.py`.\n")

    def section(title: str, paths: List[Path]) -> None:
        lines.append(f"## {title}\n")
        if not paths:
            lines.append("_(none)_\n")
            return
        for p in sorted(paths):
            rel = p.relative_to(out_dir)
            lines.append(f"- `{rel.as_posix()}`")
        lines.append("")

    section("Tables", tables)
    section("Figures", figures)
    section("Appendix", appendix)
    (out_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


# -----------------------------
# Main
# -----------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description="Create research-paper tables and figures from MT eval outputs.")
    ap.add_argument("--in_dir", type=str, default="out_translation_eval", help="Folder containing eval CSVs.")
    ap.add_argument("--out_dir", type=str, default="paper_artifacts", help="Output folder for paper artifacts.")
    ap.add_argument("--primary_metric", type=str, default="comet", help="Primary metric for headline figures.")
    ap.add_argument(
        "--metrics",
        nargs="*",
        default=["comet", "bertscore", "chrf", "bleu", "ter"],
        help="Metrics to consider (aliases allowed; bertscore -> bertscore_f1).",
    )
    ap.add_argument("--lexical_metrics", nargs="*", default=["chrf", "bleu", "ter"], help="Lexical metrics set.")
    ap.add_argument("--semantic_metrics", nargs="*", default=["bertscore", "comet"], help="Semantic metrics set.")
    ap.add_argument("--formats", nargs="*", default=["png"], help="Figure formats: png pdf (can include both).")
    ap.add_argument("--seed", type=int, default=42, help="Random seed.")
    ap.add_argument("--bootstrap_samples", type=int, default=5000, help="Bootstrap samples for pairwise tests.")
    ap.add_argument("--alpha", type=float, default=0.05, help="Alpha for Holm correction.")
    ap.add_argument(
        "--scatter_color_by",
        type=str,
        default="language",
        choices=["language", "model", "none"],
        help="How to color scatterplot dots.",
    )
    ap.add_argument(
        "--scatter_annotate_n",
        type=int,
        default=0,
        help="Annotate ONLY outliers with tiny numbers (0 disables). Avoids clutter.",
    )
    ap.add_argument("--top_k_forest", type=int, default=10, help="Top-k models in forest plot.")
    ap.add_argument("--violin_by_language", action="store_true", help="Also generate one violin plot per language.")
    ap.add_argument("--verbose", action="store_true", help="Verbose logging.")
    args = ap.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    ensure_dir(out_dir)

    logger = setup_logger(out_dir, verbose=args.verbose)
    logger.info(f"Input dir: {in_dir.resolve()}")
    logger.info(f"Output dir: {out_dir.resolve()}")

    data = load_eval_data(in_dir, logger)
    logger.info(f"Loaded: {len(data.paragraph_df):,} paragraph-level rows")
    logger.info(f"Loaded: {len(data.summary_df):,} summary rows")
    logger.info(f"Models: {len(data.models)}  Languages: {len(data.languages)}")

    out_tables = out_dir / "tables"
    out_figs = out_dir / "figures"
    out_appendix = out_dir / "appendix"
    ensure_dir(out_tables)
    ensure_dir(out_figs)
    ensure_dir(out_appendix)

    metrics = args.metrics
    formats = [f.lower().strip(".") for f in args.formats if f.strip()]

    written_tables: List[Path] = []
    written_figs: List[Path] = []
    written_appendix: List[Path] = []

    # --------- Main tables ----------
    written_tables += table_dataset_summary(data, out_tables, logger)
    written_tables += table_overall_results(data, out_tables, logger, args.primary_metric, metrics)
    written_tables += table_per_language_winners(data, out_tables, logger, metrics, tie_mode="ci_overlap")
    written_tables += table_metric_agreement(
        data, out_tables, logger, metrics=metrics, lexical_cols=args.lexical_metrics, semantic_cols=args.semantic_metrics
    )

    # --------- Main figures ----------
    written_figs += fig_heatmap_model_language(data, out_figs, logger, args.primary_metric, formats)
    written_figs += fig_forest_overall_with_ci(data, out_figs, logger, args.primary_metric, formats, top_k=args.top_k_forest, seed=args.seed, n_boot=args.bootstrap_samples)
    written_figs += fig_violin_segment_distributions(data, out_figs, logger, args.primary_metric, formats, by_language=False)
    if args.violin_by_language:
        written_figs += fig_violin_segment_distributions(data, out_figs, logger, args.primary_metric, formats, by_language=True)

    # CORPUS-level scatter panels (one point per language×model), like your plot
    written_figs += fig_scatter_corpus_lexical_semantic_with_outliers(
        data,
        out_figs,
        logger,
        x_metric="chrf",
        y_metric="bertscore",
        formats=formats,
        color_by=args.scatter_color_by,
        annotate_n=args.scatter_annotate_n,
    )
    written_figs += fig_scatter_corpus_lexical_semantic_with_outliers(
        data,
        out_figs,
        logger,
        x_metric="chrf",
        y_metric="comet",
        formats=formats,
        color_by=args.scatter_color_by,
        annotate_n=args.scatter_annotate_n,
    )

    written_figs += fig_error_probe_bars(data, out_figs, logger, formats)

    # --------- Appendix artifacts ----------
    written_appendix += appendix_pairwise_matrices(
        data,
        out_appendix,
        logger,
        primary_metric=args.primary_metric,
        bootstrap_samples=args.bootstrap_samples,
        seed=args.seed,
        alpha=args.alpha,
    )
    written_figs += fig_rank_stability(data, out_figs, logger, metrics=metrics, formats=formats)

    # Full per-language summary table (appendix)
    s = data.summary_df[data.summary_df["language"].isin(data.languages)].copy()
    numeric_cols = [c for c in s.columns if c not in ("model", "language") and pd.api.types.is_numeric_dtype(s[c])]
    full = s[["language", "model"] + numeric_cols].copy().sort_values(["language", "model"])
    written_appendix += save_table_bundle(full, out_appendix, "A1_full_summary_all_metrics", logger, float_digits=3, index=False, latex=True)

    write_readme(out_dir, written_tables, written_figs, written_appendix)

    print("\n=== Paper artifacts created ===")
    print(f"Tables:   {len(written_tables)} files (bundled formats)")
    print(f"Figures:  {len(written_figs)} files")
    print(f"Appendix: {len(written_appendix)} files (bundled formats)")
    print(f"Index:    {(out_dir / 'README.md').resolve()}")


if __name__ == "__main__":
    main()
