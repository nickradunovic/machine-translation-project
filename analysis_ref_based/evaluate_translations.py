#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
evaluate_translations.py

Reference-based MT evaluation for a small multi-paragraph document translated into multiple languages
by multiple systems.

Data layout (default --root translations_ref_based):
  - Source (Dutch): translations_ref_based/dutch_original_text.txt
  - Reference translations: translations_ref_based/reference-translation/<language>.txt
  - System translations: translations_ref_based/<model_name>/<language>.txt

Outputs (default --out out_translation_eval):
  - metrics_paragraph_level.csv
  - metrics_summary.csv
  - leaderboards.md
  - diagnostics.md
  - plots/*.png

Install (minimal):
  pip install -U sacrebleu numpy pandas matplotlib

Optional semantic metric (BERTScore):
  pip install -U bert-score torch transformers

Optional metric (COMET, heavier):
  pip install -U unbabel-comet torch transformers

Notes / limitations:
  - The provided reference translation is used as the evaluation anchor; it may not be perfect.
  - For small documents, bootstrap confidence intervals can be wide; treat them as *uncertainty hints*.
  - Some metrics (especially neural ones) require model downloads; they are optional and will be skipped if unavailable.

Example:
  python evaluate_translations.py --root translations_ref_based --out out_translation_eval \
      --metrics bleu chrf ter bertscore --seed 42

Dutch source format example used when designing paragraph splitting (blank-line separated paragraphs):
  :contentReference[oaicite:0]{index=0}
"""

from __future__ import annotations

import argparse
import logging
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

# Matplotlib is used only for saving PNGs (no GUI required).
import matplotlib

matplotlib.use("Agg")  # headless backend
import matplotlib.pyplot as plt

try:
    import sacrebleu
    from sacrebleu.metrics import BLEU, CHRF, TER
except Exception as e:  # pragma: no cover
    print("ERROR: This script requires sacrebleu. Install with: pip install -U sacrebleu")
    raise

# Optional metrics
_BERTSCORE_AVAILABLE = False
_BERTSCORE_IMPORT_ERROR: Optional[str] = None
try:
    from bert_score import score as bert_score_score  # type: ignore

    _BERTSCORE_AVAILABLE = True
except Exception as e:  # pragma: no cover
    _BERTSCORE_IMPORT_ERROR = str(e)

_COMET_AVAILABLE = False
_COMET_IMPORT_ERROR: Optional[str] = None
try:
    # Unbabel COMET (optional). Note: module name may conflict with comet_ml in some envs.
    from comet import download_model as comet_download_model  # type: ignore
    from comet import load_from_checkpoint as comet_load_from_checkpoint  # type: ignore

    _COMET_AVAILABLE = True
except Exception as e:  # pragma: no cover
    _COMET_IMPORT_ERROR = str(e)


# Preferred display order for known languages (others will be appended alphabetically).
EXPECTED_LANG_ORDER = ["turkish", "spanish", "english", "polish", "ukrainian", "arabic", "german"]

# Used only for BERTScore's `lang` hint (when available).
LANG_CODE_MAP = {
    "turkish": "tr",
    "spanish": "es",
    "english": "en",
    "polish": "pl",
    "ukrainian": "uk",
    "arabic": "ar",
    "german": "de",
}

# Metric directions: +1 means higher is better; -1 means lower is better.
METRIC_DIRECTIONS = {
    "bleu": +1,
    "chrf": +1,
    "ter": -1,
    "bertscore": +1,  # stored as F1*100
    "comet": +1,  # stored as score*100 (if used)
}

DEFAULT_METRICS = ["bleu", "chrf", "ter", "bertscore"]

# Probes / heuristics
PUNCT_CHARS = [
    '"',
    "'",
    "‘",
    "’",
    "“",
    "”",
    "«",
    "»",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "%",
    "/",
    "\\",
    ":",
    ";",
    ",",
    ".",
    "!",
    "?",
    "…",
    "-",
    "–",
    "—",
]
NUM_REGEX = re.compile(r"\b\d+(?:[.,]\d+)*\b")
ACRONYM_REGEX = re.compile(r"\b[A-Z]{2,}(?:/[A-Z]{2,})*\b")


@dataclass
class LoadedText:
    path: Path
    encoding: str
    text: str
    paragraphs_raw: List[str]
    paragraphs_norm: List[str]


@dataclass
class AlignmentUnit:
    unit_id: int
    sys_start: int
    sys_end: int  # exclusive
    ref_start: int
    ref_end: int  # exclusive
    sys_text_raw: str
    ref_text_raw: str
    sys_text_norm: str
    ref_text_norm: str


def setup_logging(out_dir: Path, verbose: bool = False) -> logging.Logger:
    out_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("translation_eval")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    # Console handler
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    ch.setFormatter(ch_formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler(out_dir / "run.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)

    return logger


def read_text_file(path: Path, logger: Optional[logging.Logger] = None) -> Tuple[str, str]:
    """
    Read a text file robustly with encoding fallbacks.
    Returns (text, encoding_used).
    """
    encodings_to_try = ["utf-8", "utf-8-sig", "cp1252", "latin-1"]
    last_err: Optional[Exception] = None
    for enc in encodings_to_try:
        try:
            text = path.read_text(encoding=enc)
            return text, enc
        except Exception as e:
            last_err = e
            continue

    # Final fallback: bytes + replace errors
    try:
        data = path.read_bytes()
        text = data.decode("utf-8", errors="replace")
        if logger:
            logger.warning(f"Decoding {path} with utf-8 errors=replace (original decode failed).")
        return text, "utf-8-replace"
    except Exception as e:
        if logger:
            logger.error(f"Failed to read {path}: {e}")
        raise last_err or e


def normalize_for_metrics(text: str) -> str:
    """
    Normalize whitespace for metric computation:
      - Normalize newlines
      - Collapse all whitespace to a single space
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_paragraphs(text: str) -> Tuple[List[str], List[str]]:
    """
    Split on blank lines into paragraph units.
    Returns (raw_paragraphs, normalized_paragraphs).
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return [], []
    chunks = re.split(r"\n\s*\n+", text)
    paras_raw = [c.strip() for c in chunks if c.strip()]
    paras_norm = [normalize_for_metrics(p) for p in paras_raw]
    return paras_raw, paras_norm


def load_text(path: Path, logger: logging.Logger) -> LoadedText:
    text, enc = read_text_file(path, logger)
    paras_raw, paras_norm = split_paragraphs(text)
    return LoadedText(path=path, encoding=enc, text=text, paragraphs_raw=paras_raw, paragraphs_norm=paras_norm)


def discover_models(root: Path, exclude_dirs: Optional[Sequence[str]] = None) -> List[str]:
    exclude = set(exclude_dirs or [])
    models: List[str] = []
    for p in root.iterdir():
        if not p.is_dir():
            continue
        if p.name.startswith("."):
            continue
        if p.name in exclude:
            continue
        models.append(p.name)
    models.sort()
    return models


def discover_languages(reference_dir: Path, restrict_to: Optional[Sequence[str]] = None) -> List[str]:
    restrict = set([x.lower() for x in restrict_to]) if restrict_to else None
    langs: List[str] = []
    if not reference_dir.exists() or not reference_dir.is_dir():
        return langs
    for p in reference_dir.glob("*.txt"):
        lang = p.stem.lower()
        if restrict is not None and lang not in restrict:
            continue
        langs.append(lang)

    # Prefer expected order first
    ordered: List[str] = []
    for l in EXPECTED_LANG_ORDER:
        if l in langs and l not in ordered:
            ordered.append(l)
    for l in sorted(set(langs)):
        if l not in ordered:
            ordered.append(l)
    return ordered


def extract_numbers(text: str) -> List[str]:
    nums = NUM_REGEX.findall(text)
    # Normalize decimal commas to dots for comparison.
    return [n.replace(",", ".") for n in nums]


def extract_acronyms(text: str) -> List[str]:
    return ACRONYM_REGEX.findall(text)


def f1_set(sys_items: Sequence[str], ref_items: Sequence[str]) -> Tuple[float, float, float]:
    """
    Set-based precision/recall/F1 over extracted items (numbers, acronyms, etc.).
    Heuristic but useful for catching obvious losses/insertions.
    """
    sys_set = set(sys_items)
    ref_set = set(ref_items)
    if not sys_set and not ref_set:
        return 1.0, 1.0, 1.0
    if not sys_set and ref_set:
        return 1.0, 0.0, 0.0
    if sys_set and not ref_set:
        return 0.0, 1.0, 0.0
    inter = sys_set & ref_set
    prec = len(inter) / len(sys_set) if sys_set else 0.0
    rec = len(inter) / len(ref_set) if ref_set else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    return prec, rec, f1


def count_chars(text: str, chars: Sequence[str]) -> Dict[str, int]:
    counts = {c: 0 for c in chars}
    for c in text:
        if c in counts:
            counts[c] += 1
    return counts


def punctuation_preservation(sys_text: str, ref_text: str) -> Tuple[float, int, int, int]:
    """
    Returns (preservation_score, abs_diff_total, ref_total, sys_total).

    Score is a simple heuristic in [0,1] where 1 means identical punctuation counts
    for a curated list of punctuation/format characters.
    """
    sys_counts = count_chars(sys_text, PUNCT_CHARS)
    ref_counts = count_chars(ref_text, PUNCT_CHARS)
    abs_diff = sum(abs(sys_counts[c] - ref_counts[c]) for c in PUNCT_CHARS)
    ref_total = sum(ref_counts.values())
    sys_total = sum(sys_counts.values())
    denom = ref_total + 1  # reference is the anchor
    score = 1.0 - (abs_diff / denom)
    return max(0.0, min(1.0, score)), abs_diff, ref_total, sys_total


def alignment_cost(sys_group: Sequence[str], ref_group: Sequence[str], a: int, b: int) -> float:
    """
    Cost for aligning sys_group paragraphs to ref_group paragraphs. Lower is better.
    This is intentionally simple and language-agnostic:
      - length mismatch (log ratio)
      - penalty for merging/splitting
      - light penalties for numeral / punctuation mismatch
    """
    sys_text = " ".join(sys_group)
    ref_text = " ".join(ref_group)

    ls = max(1, len(sys_text))
    lr = max(1, len(ref_text))
    len_term = abs(math.log(ls / lr))  # symmetric

    merge_term = 0.20 * ((a - 1) + (b - 1))

    sys_nums = set(extract_numbers(sys_text))
    ref_nums = set(extract_numbers(ref_text))
    num_term = 0.05 * len(sys_nums.symmetric_difference(ref_nums))

    sys_p = sum(count_chars(sys_text, PUNCT_CHARS).values())
    ref_p = sum(count_chars(ref_text, PUNCT_CHARS).values())
    punct_term = 0.01 * abs(sys_p - ref_p) / max(1, ref_p)

    return len_term + merge_term + num_term + punct_term


def align_paragraphs_dp(
    sys_paras_norm: Sequence[str],
    ref_paras_norm: Sequence[str],
    sys_paras_raw: Sequence[str],
    ref_paras_raw: Sequence[str],
    max_group: int = 3,
    logger: Optional[logging.Logger] = None,
) -> List[AlignmentUnit]:
    """
    Align system and reference paragraphs using a DP that allows grouping up to max_group
    paragraphs on either side. If alignment fails, fall back to a single segment.

    This yields *aligned units* used for paragraph-level scoring and bootstrap resampling.
    """
    n, m = len(sys_paras_norm), len(ref_paras_norm)

    if n == 0 and m == 0:
        return []
    if n == 0 or m == 0:
        sys_text_raw = "\n\n".join(sys_paras_raw)
        ref_text_raw = "\n\n".join(ref_paras_raw)
        return [
            AlignmentUnit(
                unit_id=0,
                sys_start=0,
                sys_end=n,
                ref_start=0,
                ref_end=m,
                sys_text_raw=sys_text_raw,
                ref_text_raw=ref_text_raw,
                sys_text_norm=normalize_for_metrics(sys_text_raw),
                ref_text_norm=normalize_for_metrics(ref_text_raw),
            )
        ]

    max_group = max(1, int(max_group))
    # Note: if mismatch is extreme, DP may fail and we fall back to full-doc scoring.
    max_group = min(max_group, max(n, m))

    INF = 1e18
    dp = np.full((n + 1, m + 1), INF, dtype=np.float64)
    bp: Dict[Tuple[int, int], Tuple[int, int, int, int]] = {}  # (i,j)->(pi,pj,a,b)
    dp[0, 0] = 0.0

    for i in range(n + 1):
        for j in range(m + 1):
            if not np.isfinite(dp[i, j]):
                continue
            if i == n and j == m:
                continue
            for a in range(1, max_group + 1):
                if i + a > n:
                    break
                for b in range(1, max_group + 1):
                    if j + b > m:
                        break
                    cost = alignment_cost(sys_paras_norm[i : i + a], ref_paras_norm[j : j + b], a, b)
                    cand = dp[i, j] + cost
                    if cand < dp[i + a, j + b]:
                        dp[i + a, j + b] = cand
                        bp[(i + a, j + b)] = (i, j, a, b)

    if not np.isfinite(dp[n, m]):
        if logger:
            logger.warning("Alignment DP failed; falling back to single-segment (full-document) alignment.")
        sys_text_raw = "\n\n".join(sys_paras_raw)
        ref_text_raw = "\n\n".join(ref_paras_raw)
        return [
            AlignmentUnit(
                unit_id=0,
                sys_start=0,
                sys_end=n,
                ref_start=0,
                ref_end=m,
                sys_text_raw=sys_text_raw,
                ref_text_raw=ref_text_raw,
                sys_text_norm=normalize_for_metrics(sys_text_raw),
                ref_text_norm=normalize_for_metrics(ref_text_raw),
            )
        ]

    # Backtrack
    spans: List[Tuple[int, int, int, int]] = []
    i, j = n, m
    while (i, j) != (0, 0):
        if (i, j) not in bp:
            if logger:
                logger.warning("Alignment backtrack failed; falling back to single-segment alignment.")
            sys_text_raw = "\n\n".join(sys_paras_raw)
            ref_text_raw = "\n\n".join(ref_paras_raw)
            return [
                AlignmentUnit(
                    unit_id=0,
                    sys_start=0,
                    sys_end=n,
                    ref_start=0,
                    ref_end=m,
                    sys_text_raw=sys_text_raw,
                    ref_text_raw=ref_text_raw,
                    sys_text_norm=normalize_for_metrics(sys_text_raw),
                    ref_text_norm=normalize_for_metrics(ref_text_raw),
                )
            ]
        pi, pj, a, b = bp[(i, j)]
        spans.append((pi, i, pj, j))
        i, j = pi, pj
    spans.reverse()

    units: List[AlignmentUnit] = []
    for uid, (si0, si1, rj0, rj1) in enumerate(spans):
        sys_text_raw = "\n\n".join(sys_paras_raw[si0:si1])
        ref_text_raw = "\n\n".join(ref_paras_raw[rj0:rj1])
        units.append(
            AlignmentUnit(
                unit_id=uid,
                sys_start=si0,
                sys_end=si1,
                ref_start=rj0,
                ref_end=rj1,
                sys_text_raw=sys_text_raw,
                ref_text_raw=ref_text_raw,
                sys_text_norm=" ".join(sys_paras_norm[si0:si1]).strip(),
                ref_text_norm=" ".join(ref_paras_norm[rj0:rj1]).strip(),
            )
        )
    return units


def safe_metric_list(metrics: Sequence[str]) -> List[str]:
    m = []
    for x in metrics:
        x = x.strip().lower()
        if x:
            m.append(x)
    # de-dup preserving order
    out: List[str] = []
    seen = set()
    for x in m:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out


def compute_corpus_metrics(
    bleu_metric: BLEU,
    chrf_metric: CHRF,
    ter_metric: TER,
    hyps: List[str],
    refs: List[str],
    metrics: Sequence[str],
) -> Dict[str, float]:
    res: Dict[str, float] = {}
    if "bleu" in metrics:
        res["bleu"] = float(bleu_metric.corpus_score(hyps, [refs]).score)
    if "chrf" in metrics:
        res["chrf"] = float(chrf_metric.corpus_score(hyps, [refs]).score)
    if "ter" in metrics:
        res["ter"] = float(ter_metric.corpus_score(hyps, [refs]).score)
    return res


def compute_sentence_metrics(
    bleu_metric: BLEU,
    chrf_metric: CHRF,
    ter_metric: TER,
    hyp: str,
    ref: str,
    metrics: Sequence[str],
) -> Dict[str, float]:
    res: Dict[str, float] = {}
    if "bleu" in metrics:
        res["bleu"] = float(bleu_metric.sentence_score(hyp, [ref]).score)
    if "chrf" in metrics:
        res["chrf"] = float(chrf_metric.sentence_score(hyp, [ref]).score)
    if "ter" in metrics:
        res["ter"] = float(ter_metric.sentence_score(hyp, [ref]).score)
    return res


def bootstrap_ci(
    metric_name: str,
    hyps: List[str],
    refs: List[str],
    segment_scores: Optional[np.ndarray],
    bleu_metric: BLEU,
    chrf_metric: CHRF,
    ter_metric: TER,
    rng: np.random.Generator,
    n_samples: int = 1000,
    ci: float = 0.95,
) -> Tuple[Optional[float], Optional[float]]:
    """
    Bootstrap CI over aligned units.

    For BLEU/chrF/TER we recompute corpus metric on resampled units.
    For metrics where only per-segment values exist (e.g., BERTScore), bootstrap the mean.
    """
    if not hyps or not refs:
        return None, None
    n = min(len(hyps), len(refs))
    if n <= 1:
        return None, None

    alpha = 1.0 - ci
    lo_q = 100 * (alpha / 2)
    hi_q = 100 * (1 - alpha / 2)

    idx = np.arange(n)
    samples = np.empty(n_samples, dtype=np.float64)

    if metric_name in ("bleu", "chrf", "ter"):
        for k in range(n_samples):
            sidx = rng.choice(idx, size=n, replace=True)
            hyps_s = [hyps[i] for i in sidx]
            refs_s = [refs[i] for i in sidx]
            val = compute_corpus_metrics(bleu_metric, chrf_metric, ter_metric, hyps_s, refs_s, [metric_name])[
                metric_name
            ]
            samples[k] = val
    else:
        if segment_scores is None or len(segment_scores) < n:
            return None, None
        seg = np.asarray(segment_scores[:n], dtype=np.float64)
        for k in range(n_samples):
            sidx = rng.choice(idx, size=n, replace=True)
            samples[k] = seg[sidx].mean()

    return float(np.percentile(samples, lo_q)), float(np.percentile(samples, hi_q))


def compute_bertscore(
    cands: List[str],
    refs: List[str],
    lang: str,
    model_type: str,
    rescale_with_baseline: bool,
    device: Optional[str],
    logger: logging.Logger,
) -> Optional[np.ndarray]:
    if not _BERTSCORE_AVAILABLE:
        logger.warning(f"Skipping BERTScore (bert_score not available): {_BERTSCORE_IMPORT_ERROR}")
        return None
    if not cands or not refs:
        return None
    try:
        kwargs: Dict[str, Any] = {
            "model_type": model_type,
            "lang": lang,
            "rescale_with_baseline": rescale_with_baseline,
            "verbose": False,
        }
        if device:
            kwargs["device"] = device
        _, _, F1 = bert_score_score(cands, refs, **kwargs)
        return F1.detach().cpu().numpy().astype(np.float64) * 100.0
    except Exception as e:
        logger.warning(f"Skipping BERTScore due to runtime error: {e}")
        return None


def compute_comet(
    srcs: List[str],
    cands: List[str],
    refs: List[str],
    comet_model: str,
    device: Optional[str],
    logger: logging.Logger,
) -> Optional[np.ndarray]:
    """
    Optional: compute COMET scores per segment (scaled 0-100).
    Requires internet on first run to download the model.
    """
    if not _COMET_AVAILABLE:
        logger.warning(f"Skipping COMET (unbabel-comet not available): {_COMET_IMPORT_ERROR}")
        return None
    if not (srcs and cands and refs):
        return None
    try:
        model_path = comet_download_model(comet_model)
        model = comet_load_from_checkpoint(model_path)
        if device:
            model.to(device)
        data = [{"src": s, "mt": m, "ref": r} for s, m, r in zip(srcs, cands, refs)]
        out = model.predict(data, batch_size=8, gpus=1 if (device and "cuda" in device) else 0, num_workers=1)
        return np.asarray(out.scores, dtype=np.float64) * 100.0
    except Exception as e:
        logger.warning(f"Skipping COMET due to runtime error: {e}")
        return None


def df_to_markdown_table(df: pd.DataFrame, float_digits: int = 3, index: bool = True) -> str:
    """
    Minimal DataFrame -> markdown table without external deps (avoids requiring `tabulate`).
    """
    if df.empty:
        return "_(empty)_"
    df2 = df.copy()

    for col in df2.columns:
        if pd.api.types.is_integer_dtype(df2[col]):
            df2[col] = df2[col].apply(lambda x: "" if pd.isna(x) else str(int(x)))
        elif pd.api.types.is_float_dtype(df2[col]):
            df2[col] = df2[col].apply(lambda x: "" if pd.isna(x) else f"{float(x):.{float_digits}f}")
        else:
            df2[col] = df2[col].astype(str)

    if index:
        df2.insert(0, "index", [str(i) for i in df2.index.tolist()])

    headers = df2.columns.tolist()
    rows = df2.values.tolist()

    lines: List[str] = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def available_metrics_in_df(summary_df: pd.DataFrame, requested: List[str]) -> List[str]:
    """
    Keep only metrics that have at least one non-NaN value in summary_df.
    """
    out: List[str] = []
    for m in requested:
        col = "bertscore_f1" if m == "bertscore" else m
        if col in summary_df.columns and summary_df[col].notna().any():
            out.append(m)
    return out


def build_leaderboards_md(
    summary_df: pd.DataFrame,
    paragraph_df: pd.DataFrame,
    diagnostics: Dict[str, Any],
    requested_metrics: List[str],
    logger: logging.Logger,
) -> str:
    """
    Human-readable report. Designed to still be useful if some metrics are missing.
    """
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines: List[str] = []
    lines.append("# Translation Evaluation Report\n")
    lines.append(f"- Generated: {now}")
    lines.append(f"- Root: `{diagnostics.get('root')}`")
    lines.append(f"- Output: `{diagnostics.get('out')}`")
    lines.append(f"- Models discovered: {len(diagnostics.get('models', []))}")
    lines.append(f"- Languages (with references): {len(diagnostics.get('languages', []))}")
    lines.append(f"- Metrics requested: {', '.join(requested_metrics)}")

    # Mention metric availability
    notes: List[str] = []
    if "bertscore" in requested_metrics and not _BERTSCORE_AVAILABLE:
        notes.append(f"BERTScore requested but not available (import error: {_BERTSCORE_IMPORT_ERROR}).")
    if "comet" in requested_metrics and not _COMET_AVAILABLE:
        notes.append(f"COMET requested but not available (import error: {_COMET_IMPORT_ERROR}).")
    if notes:
        lines.append(f"- Notes: {' '.join(notes)}")

    lines.append("\n## Reference caveat\n")
    lines.append(
        "All scores are **reference-based**: they quantify similarity to the provided reference translation(s). "
        "A correct translation can score lower if it uses different wording than the reference.\n"
    )

    languages: List[str] = diagnostics.get("languages", [])
    models: List[str] = diagnostics.get("models", [])

    # Decide which metrics are actually available for reporting
    metrics = available_metrics_in_df(summary_df, requested_metrics)
    if not metrics:
        lines.append("\n_No metrics were successfully computed._\n")
        return "\n".join(lines)

    # ---------------------------------------------------------------------
    # Language difficulty snapshot
    # ---------------------------------------------------------------------
    lines.append("\n## Language difficulty snapshot\n")
    lines.append(
        'Mean document-level score across models (macro view). Lower means "harder" *with respect to the reference*.\n'
    )
    lang_rows: List[Dict[str, Any]] = []
    for lang in languages:
        df_lang = summary_df[(summary_df["language"] == lang) & (summary_df["model"] != "__overall__")].copy()
        if df_lang.empty:
            continue
        row: Dict[str, Any] = {"language": lang, "n_models": int(df_lang["model"].nunique())}
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            vals = df_lang[col].dropna().astype(float)
            if len(vals) == 0:
                row[m] = np.nan
            else:
                # For TER, invert to keep "higher is better" for this snapshot.
                if METRIC_DIRECTIONS[m] < 0:
                    row[m] = float((-vals).mean())
                else:
                    row[m] = float(vals.mean())
        lang_rows.append(row)

    if lang_rows:
        df_langsnap = pd.DataFrame(lang_rows).set_index("language")
        # Sort by primary metric if available
        primary = "bertscore" if "bertscore" in metrics else ("chrf" if "chrf" in metrics else "bleu")
        df_langsnap = df_langsnap.sort_values(primary, ascending=True)
        lines.append(df_to_markdown_table(df_langsnap, float_digits=2, index=True))
        lines.append("\n*(For TER we report -TER so that higher is better in this snapshot.)*\n")
    else:
        lines.append("No per-language summary available.\n")

    # ---------------------------------------------------------------------
    # Per-language leaderboards
    # ---------------------------------------------------------------------
    lines.append("\n## Per-language leaderboards\n")

    for lang in languages:
        df_lang = summary_df[(summary_df["language"] == lang) & (summary_df["model"] != "__overall__")].copy()
        if df_lang.empty:
            continue

        # Only rank on metrics that have non-NaN values for this language
        rank_metrics: List[str] = []
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            if col in df_lang.columns and df_lang[col].notna().any():
                rank_metrics.append(m)

        # Composite rank across available metrics
        rank_cols = []
        for m in rank_metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            ascending = METRIC_DIRECTIONS[m] < 0  # TER lower is better
            df_lang[f"rank_{m}"] = df_lang[col].rank(ascending=ascending, method="average")
            rank_cols.append(f"rank_{m}")
        if rank_cols:
            df_lang["rank_mean"] = df_lang[rank_cols].mean(axis=1)
            df_lang = df_lang.sort_values(["rank_mean", "model"])
        else:
            df_lang = df_lang.sort_values(["model"])

        lines.append(f"\n### {lang}\n")

        # Tie detection on a primary metric (BERTScore > chrF > BLEU)
        primary_metric = None
        for cand in ["bertscore", "chrf", "bleu"]:
            if cand in rank_metrics:
                primary_metric = cand
                break
        if primary_metric:
            col = "bertscore_f1" if primary_metric == "bertscore" else primary_metric
            lo_col = f"{col}_ci_low"
            hi_col = f"{col}_ci_high"
            if lo_col in df_lang.columns and hi_col in df_lang.columns and len(df_lang) >= 2:
                top = df_lang.iloc[0]
                second = df_lang.iloc[1]
                if (
                    pd.notnull(top[lo_col])
                    and pd.notnull(top[hi_col])
                    and pd.notnull(second[lo_col])
                    and pd.notnull(second[hi_col])
                ):
                    overlap = not (top[lo_col] > second[hi_col] or second[lo_col] > top[hi_col])
                    if overlap:
                        lines.append(
                            f"**Tie watch:** top-2 {primary_metric.upper()} 95% CIs overlap; treat as a statistical tie for this document.\n"
                        )

        # Build markdown table
        header = ["Model", "N"]
        for m in rank_metrics:
            header.append("BERTScore-F1" if m == "bertscore" else m.upper())
        header += ["Len ratio", "Nums F1", "Acr F1", "Punct pres."]

        lines.append("| " + " | ".join(header) + " |")
        lines.append("|" + "|".join(["---"] * len(header)) + "|")

        for _, row in df_lang.iterrows():
            vals = [str(row["model"]), str(int(row.get("n_units", 0)))]
            for m in rank_metrics:
                col = "bertscore_f1" if m == "bertscore" else m
                lo_col = f"{col}_ci_low"
                hi_col = f"{col}_ci_high"
                s = row.get(col, np.nan)
                lo = row.get(lo_col, np.nan)
                hi = row.get(hi_col, np.nan)
                if pd.isna(s):
                    vals.append("—")
                elif lo_col in df_lang.columns and hi_col in df_lang.columns and not pd.isna(lo) and not pd.isna(hi):
                    vals.append(f"{float(s):.2f} [{float(lo):.2f}, {float(hi):.2f}]")
                else:
                    vals.append(f"{float(s):.2f}")

            def fmt(x: Any, digits: int) -> str:
                return "—" if pd.isna(x) else f"{float(x):.{digits}f}"

            vals.append(fmt(row.get("len_ratio_mean", np.nan), 3))
            vals.append(fmt(row.get("num_f1_mean", np.nan), 2))
            vals.append(fmt(row.get("acr_f1_mean", np.nan), 2))
            vals.append(fmt(row.get("punct_pres_mean", np.nan), 2))
            lines.append("| " + " | ".join(vals) + " |")

        mismatch_rows = diagnostics.get("mismatches", {}).get(lang, [])
        if mismatch_rows:
            lines.append("\n<details>\n<summary>Alignment / paragraph-count warnings</summary>\n\n")
            lines.extend([f"- {msg}" for msg in mismatch_rows])
            lines.append("\n</details>\n")

    # ---------------------------------------------------------------------
    # Overall leaderboard (macro-average across languages) + variance
    # ---------------------------------------------------------------------
    lines.append("\n## Overall leaderboard\n")
    overall_df = summary_df[summary_df["language"] == "__overall__"].copy()
    if overall_df.empty:
        lines.append("No overall results available (not enough evaluated languages/models).\n")
    else:
        # Rank across metrics (using doc columns)
        rank_cols = []
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            if col not in overall_df.columns or overall_df[col].isna().all():
                continue
            ascending = METRIC_DIRECTIONS[m] < 0
            overall_df[f"rank_{m}"] = overall_df[col].rank(ascending=ascending, method="average")
            rank_cols.append(f"rank_{m}")
        if rank_cols:
            overall_df["rank_mean"] = overall_df[rank_cols].mean(axis=1)
            overall_df = overall_df.sort_values(["rank_mean", "model"])
        else:
            overall_df = overall_df.sort_values(["model"])

        header = ["Model", "Langs"]
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            if col not in overall_df.columns or overall_df[col].isna().all():
                continue
            header += [("BERTScore-F1" if m == "bertscore" else m.upper()), "σ(lang)"]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("|" + "|".join(["---"] * len(header)) + "|")
        for _, row in overall_df.iterrows():
            vals = [str(row["model"]), str(int(row.get("n_langs", 0)))]
            for m in metrics:
                col = "bertscore_f1" if m == "bertscore" else m
                sd_col = f"{col}_std"
                if col not in overall_df.columns or overall_df[col].isna().all():
                    continue
                vals.append("—" if pd.isna(row.get(col)) else f"{float(row[col]):.2f}")
                vals.append("—" if pd.isna(row.get(sd_col)) else f"{float(row[sd_col]):.2f}")
            lines.append("| " + " | ".join(vals) + " |")
        lines.append(
            "\n*Overall scores are macro-averages across languages (each language weighted equally). "
            "σ(lang) is the per-language standard deviation: smaller means more consistent across languages.*\n"
        )

    # ---------------------------------------------------------------------
    # Metric agreement/disagreement
    # ---------------------------------------------------------------------
    lines.append("\n## Metric agreement and disagreement\n")
    plots = diagnostics.get("plots", {})
    if plots.get("corr_heatmap"):
        lines.append(f"- Correlation heatmap: `{plots['corr_heatmap']}`")
    if plots.get("scatter"):
        lines.append(f"- Metric scatter plot: `{plots['scatter']}`")
    lines.append("")

    # Correlation on paragraph-level metrics (higher-is-better view)
    col_map = {
        "bleu": "bleu",
        "chrf": "chrf",
        "ter": "ter",
        "bertscore": "bertscore_f1",
        "comet": "comet",
    }
    corr_cols = []
    for m in metrics:
        c = col_map.get(m)
        if c and c in paragraph_df.columns and paragraph_df[c].notna().any():
            corr_cols.append(c)

    if len(corr_cols) >= 2:
        dfc = paragraph_df[corr_cols].copy()
        if "ter" in dfc.columns:
            dfc["-ter"] = -dfc["ter"]
            dfc = dfc.drop(columns=["ter"])

        pearson = dfc.corr(method="pearson")
        spearman = dfc.corr(method="spearman")
        lines.append("### Correlations (paragraph-level)\n")
        lines.append("Pearson (TER shown as -TER):\n")
        lines.append(df_to_markdown_table(pearson.round(3), float_digits=3, index=True))
        lines.append("\nSpearman (rank correlation):\n")
        lines.append(df_to_markdown_table(spearman.round(3), float_digits=3, index=True))
        lines.append("")
    else:
        lines.append("_Not enough metric columns to compute correlations._\n")

    # Lexical vs semantic disagreement examples
    if (
        "bertscore_f1" in paragraph_df.columns
        and paragraph_df["bertscore_f1"].notna().any()
        and (
            ("bleu" in paragraph_df.columns and paragraph_df["bleu"].notna().any())
            or ("chrf" in paragraph_df.columns and paragraph_df["chrf"].notna().any())
        )
    ):
        lines.append("### Lexical vs semantic disagreement examples\n")
        df = paragraph_df.copy()

        # Lexical score = average of available lexical metrics on 0-100 scale.
        parts = []
        if "bleu" in df.columns and df["bleu"].notna().any():
            parts.append(df["bleu"])
        if "chrf" in df.columns and df["chrf"].notna().any():
            parts.append(df["chrf"])
        df["lex_score"] = sum(parts) / max(1, len(parts))

        # z-score within language (so "hard" languages don't dominate)
        df["lex_z"] = df.groupby("language")["lex_score"].transform(
            lambda x: (x - x.mean()) / (x.std(ddof=0) + 1e-9)
        )
        df["sem_z"] = df.groupby("language")["bertscore_f1"].transform(
            lambda x: (x - x.mean()) / (x.std(ddof=0) + 1e-9)
        )
        df["disagree"] = df["lex_z"] - df["sem_z"]

        top_pos = df.sort_values("disagree", ascending=False).head(8)
        top_neg = df.sort_values("disagree", ascending=True).head(8)

        def add_examples(ex_df: pd.DataFrame, title: str) -> None:
            lines.append(f"**{title}**\n")
            for _, r in ex_df.iterrows():
                lines.append(
                    f"- **{r['language']} / {r['model']} / unit {int(r['unit_id'])}** "
                    f"(LEX={float(r['lex_score']):.1f}, BERTScore={float(r['bertscore_f1']):.1f}; "
                    f"BLEU={float(r.get('bleu', np.nan)):.1f}, chrF={float(r.get('chrf', np.nan)):.1f}, "
                    f"TER={float(r.get('ter', np.nan)):.1f})"
                )
                sys_snip = str(r["sys_text_raw"]).strip().replace("\n", " ")
                ref_snip = str(r["ref_text_raw"]).strip().replace("\n", " ")
                sys_snip = (sys_snip[:280] + "…") if len(sys_snip) > 280 else sys_snip
                ref_snip = (ref_snip[:280] + "…") if len(ref_snip) > 280 else ref_snip
                lines.append(f"  - MT: `{sys_snip}`")
                lines.append(f"  - REF: `{ref_snip}`")
            lines.append("")

        add_examples(top_pos, "Lexical metrics high, semantic metric low (possible meaning drift / shallow matching)")
        add_examples(top_neg, "Semantic metric high, lexical metrics low (possible good paraphrase vs reference)")

    # ---------------------------------------------------------------------
    # Outlier paragraphs (worst segments) per model & language
    # ---------------------------------------------------------------------
    lines.append("## Outlier paragraphs per model and language\n")
    lines.append(
        "For each (model, language), we list the **worst segments** by a primary metric "
        "(BERTScore if available, else chrF, else BLEU). These are good starting points for manual inspection.\n"
    )

    primary_col = None
    if "bertscore_f1" in paragraph_df.columns and paragraph_df["bertscore_f1"].notna().any():
        primary_col = "bertscore_f1"
    elif "chrf" in paragraph_df.columns and paragraph_df["chrf"].notna().any():
        primary_col = "chrf"
    elif "bleu" in paragraph_df.columns and paragraph_df["bleu"].notna().any():
        primary_col = "bleu"

    if primary_col is None:
        lines.append("_No paragraph-level metric available for outlier selection._\n")
    else:
        for lang in languages:
            df_lang = paragraph_df[paragraph_df["language"] == lang].copy()
            if df_lang.empty:
                continue
            lines.append(f"### {lang}\n")
            for model in models:
                df_ml = df_lang[df_lang["model"] == model].copy()
                if df_ml.empty:
                    continue
                df_ml = df_ml.sort_values(primary_col, ascending=True).head(5)
                lines.append(f"<details>\n<summary>{model} (worst 5 by {primary_col})</summary>\n")
                for _, r in df_ml.iterrows():
                    lines.append(
                        f"- **Unit {int(r['unit_id'])}** "
                        f"({primary_col}={float(r[primary_col]):.2f}; "
                        f"BLEU={float(r.get('bleu', np.nan)):.2f}, chrF={float(r.get('chrf', np.nan)):.2f}, "
                        f"TER={float(r.get('ter', np.nan)):.2f}; "
                        f"len_ratio={float(r.get('len_ratio', np.nan)):.3f}, "
                        f"num_f1={float(r.get('num_f1', np.nan)):.2f}, "
                        f"acr_f1={float(r.get('acr_f1', np.nan)):.2f}, "
                        f"punct_pres={float(r.get('punct_pres', np.nan)):.2f})"
                    )
                    lines.append("  - REF:")
                    lines.append("```")
                    lines.append(str(r["ref_text_raw"]).strip())
                    lines.append("```")
                    lines.append("  - MT:")
                    lines.append("```")
                    lines.append(str(r["sys_text_raw"]).strip())
                    lines.append("```")
                lines.append("</details>\n")

    return "\n".join(lines)


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def plot_language_bars(
    summary_df: pd.DataFrame,
    metric: str,
    out_dir: Path,
    languages: Sequence[str],
    logger: logging.Logger,
) -> List[str]:
    """
    Create per-language bar charts of model scores for a given metric.
    Returns list of saved file paths (relative to out_dir).
    """
    saved: List[str] = []
    metric_col = "bertscore_f1" if metric == "bertscore" else metric
    if metric_col not in summary_df.columns or summary_df[metric_col].isna().all():
        return saved

    plots_dir = out_dir / "plots"
    ensure_dir(plots_dir)

    for lang in languages:
        df = summary_df[(summary_df["language"] == lang) & (summary_df["model"] != "__overall__")].copy()
        if df.empty or metric_col not in df.columns or df[metric_col].isna().all():
            continue
        direction = METRIC_DIRECTIONS.get(metric, +1)
        df = df.sort_values(metric_col, ascending=(direction < 0))
        plt.figure(figsize=(max(8, 0.55 * len(df)), 4))
        plt.bar(df["model"].tolist(), df[metric_col].tolist())
        plt.xticks(rotation=45, ha="right")
        title_metric = "BERTScore-F1" if metric == "bertscore" else metric.upper()
        plt.title(f"{lang}: {title_metric} by model")
        plt.ylabel(title_metric)
        plt.tight_layout()
        fname = f"bar_{metric}_{lang}.png"
        fpath = plots_dir / fname
        plt.savefig(fpath, dpi=150)
        plt.close()
        saved.append(str(Path("plots") / fname))
    if saved:
        logger.info(f"Saved {len(saved)} bar plot(s) for metric '{metric}'.")
    return saved


def plot_metric_correlation_heatmap(
    paragraph_df: pd.DataFrame,
    requested_metrics: List[str],
    out_dir: Path,
    logger: logging.Logger,
) -> Optional[str]:
    """
    Pearson correlation heatmap over paragraph-level metrics (TER is shown as -TER).
    """
    plots_dir = out_dir / "plots"
    ensure_dir(plots_dir)

    col_map = {
        "bleu": "bleu",
        "chrf": "chrf",
        "ter": "ter",
        "bertscore": "bertscore_f1",
        "comet": "comet",
    }
    cols: List[str] = []
    for m in requested_metrics:
        c = col_map.get(m)
        if c and c in paragraph_df.columns and paragraph_df[c].notna().any():
            cols.append(c)

    if len(cols) < 2:
        return None

    df = paragraph_df[cols].copy()
    if "ter" in df.columns:
        df["-ter"] = -df["ter"]
        df = df.drop(columns=["ter"])

    corr = df.corr(method="pearson").values

    plt.figure(figsize=(6, 5))
    plt.imshow(corr, interpolation="nearest", vmin=-1, vmax=1)
    plt.xticks(range(len(df.columns)), df.columns, rotation=45, ha="right")
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title("Metric Pearson correlation (paragraph-level)")
    plt.colorbar()
    plt.tight_layout()
    fname = "metric_correlation_heatmap.png"
    fpath = plots_dir / fname
    plt.savefig(fpath, dpi=150)
    plt.close()
    logger.info(f"Saved correlation heatmap to {fpath}")
    return str(Path("plots") / fname)


def plot_metric_scatter(
    paragraph_df: pd.DataFrame,
    out_dir: Path,
    logger: logging.Logger,
) -> Optional[str]:
    """
    Simple scatter plot to visualize metric agreement (chrF vs BERTScore if available, else BLEU vs chrF).
    """
    plots_dir = out_dir / "plots"
    ensure_dir(plots_dir)

    x_col: Optional[str] = None
    y_col: Optional[str] = None
    title = ""

    if (
        "chrf" in paragraph_df.columns
        and paragraph_df["chrf"].notna().any()
        and "bertscore_f1" in paragraph_df.columns
        and paragraph_df["bertscore_f1"].notna().any()
    ):
        x_col, y_col = "chrf", "bertscore_f1"
        title = "chrF vs BERTScore-F1 (paragraph-level)"
    elif (
        "bleu" in paragraph_df.columns
        and paragraph_df["bleu"].notna().any()
        and "chrf" in paragraph_df.columns
        and paragraph_df["chrf"].notna().any()
    ):
        x_col, y_col = "bleu", "chrf"
        title = "BLEU vs chrF (paragraph-level)"

    if not x_col or not y_col:
        return None

    df = paragraph_df[[x_col, y_col]].dropna()
    if df.empty:
        return None

    r = float(np.corrcoef(df[x_col].values, df[y_col].values)[0, 1]) if len(df) >= 2 else float("nan")

    plt.figure(figsize=(5.5, 4.5))
    plt.scatter(df[x_col].values, df[y_col].values, alpha=0.7)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{title}\nPearson r={r:.3f}")
    plt.tight_layout()
    fname = "metric_scatter.png"
    fpath = plots_dir / fname
    plt.savefig(fpath, dpi=150)
    plt.close()
    logger.info(f"Saved scatter plot to {fpath}")
    return str(Path("plots") / fname)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reference-based translation evaluation (multi-model, multi-language).")
    parser.add_argument("--root", type=str, default="translations_ref_based", help="Root folder containing translations.")
    parser.add_argument("--out", type=str, default="out_translation_eval", help="Output folder.")
    parser.add_argument(
        "--metrics",
        nargs="+",
        default=DEFAULT_METRICS,
        help="Metrics to compute: bleu chrf ter bertscore comet (or 'all').",
    )
    parser.add_argument(
        "--languages",
        nargs="*",
        default=None,
        help="Optional list of languages to evaluate (lowercase file stems).",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed (bootstrap).")
    parser.add_argument("--bootstrap-samples", type=int, default=1000, help="Bootstrap samples for 95% CIs.")
    parser.add_argument(
        "--max-align-group",
        type=int,
        default=3,
        help="Max paragraphs to group on each side during alignment.",
    )
    parser.add_argument("--verbose", action="store_true", help="Verbose logging.")
    parser.add_argument(
        "--bertscore-model",
        type=str,
        default="xlm-roberta-base",
        help="Transformers model for BERTScore.",
    )
    parser.add_argument(
        "--bertscore-rescale",
        action="store_true",
        help="Use BERTScore baseline rescaling (may not exist for all langs).",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Torch device for neural metrics (e.g., cuda, cuda:0, cpu).",
    )
    parser.add_argument(
        "--comet-model",
        type=str,
        default="Unbabel/wmt22-comet-da",
        help="COMET model name to download (if used).",
    )
    parser.add_argument(
        "--bleu-tokenize",
        type=str,
        default="intl",
        help="SacreBLEU tokenization for BLEU (e.g., 13a, intl).",
    )

    args = parser.parse_args()

    out_dir = Path(args.out)
    logger = setup_logging(out_dir, verbose=args.verbose)

    root = Path(args.root)
    if not root.exists():
        logger.error(f"Root folder not found: {root}")
        sys.exit(1)

    metrics = safe_metric_list(args.metrics)
    if metrics == ["all"]:
        metrics = ["bleu", "chrf", "ter", "bertscore", "comet"]

    known = set(METRIC_DIRECTIONS.keys())
    unknown = [m for m in metrics if m not in known]
    if unknown:
        logger.warning(f"Unknown metrics requested (will be ignored): {unknown}")
        metrics = [m for m in metrics if m in known]
    if not metrics:
        logger.error("No valid metrics selected.")
        sys.exit(1)

    ref_dir = root / "reference-translation"
    languages = discover_languages(ref_dir, restrict_to=args.languages)
    if not languages:
        logger.error(f"No reference translations found in: {ref_dir}")
        sys.exit(1)

    models = discover_models(root, exclude_dirs=["reference-translation"])
    if not models:
        logger.error(f"No model directories found under: {root}")
        sys.exit(1)

    # Load Dutch source (optional; used only for COMET src segments if available)
    source_path = root / "dutch_original_text.txt"
    source_loaded: Optional[LoadedText] = None
    if source_path.exists():
        source_loaded = load_text(source_path, logger)
        logger.info(f"Loaded source: {source_path} (paragraphs={len(source_loaded.paragraphs_norm)})")
    else:
        logger.warning(f"Source file not found (optional): {source_path}")

    logger.info(f"Discovered {len(models)} model(s): {models}")
    logger.info(f"Discovered {len(languages)} language(s) with references: {languages}")

    # SacreBLEU metrics (explicit config for reproducibility)
    bleu_metric = BLEU(tokenize=args.bleu_tokenize, effective_order=True)
    chrf_metric = CHRF(word_order=2)
    ter_metric = TER()

    rng = np.random.default_rng(args.seed)

    diagnostics: Dict[str, Any] = {
        "root": str(root),
        "out": str(out_dir),
        "models": models,
        "languages": languages,
        "missing": [],
        "mismatches": {lang: [] for lang in languages},
        "files": [],
        "plots": {},
    }

    paragraph_rows: List[Dict[str, Any]] = []
    summary_rows: List[Dict[str, Any]] = []

    for lang in languages:
        ref_path = ref_dir / f"{lang}.txt"
        if not ref_path.exists():
            msg = f"Missing reference for language '{lang}': {ref_path}"
            logger.warning(msg)
            diagnostics["missing"].append(msg)
            continue

        ref_loaded = load_text(ref_path, logger)
        ref_n = len(ref_loaded.paragraphs_norm)

        for model in models:
            sys_path = root / model / f"{lang}.txt"
            if not sys_path.exists():
                msg = f"Missing system output: model='{model}', lang='{lang}' -> {sys_path}"
                logger.warning(msg)
                diagnostics["missing"].append(msg)
                continue

            sys_loaded = load_text(sys_path, logger)
            sys_n = len(sys_loaded.paragraphs_norm)

            if sys_n != ref_n:
                msg = f"Paragraph count mismatch: model='{model}', lang='{lang}' sys={sys_n} ref={ref_n} (DP alignment)."
                logger.warning(msg)
                diagnostics["mismatches"][lang].append(msg)

            units = align_paragraphs_dp(
                sys_loaded.paragraphs_norm,
                ref_loaded.paragraphs_norm,
                sys_loaded.paragraphs_raw,
                ref_loaded.paragraphs_raw,
                max_group=args.max_align_group,
                logger=logger,
            )

            # Alignment operation counts
            merge_sys = sum(1 for u in units if (u.sys_end - u.sys_start) > 1)
            merge_ref = sum(1 for u in units if (u.ref_end - u.ref_start) > 1)

            file_info = {
                "model": model,
                "language": lang,
                "sys_path": str(sys_path),
                "ref_path": str(ref_path),
                "sys_paragraphs": sys_n,
                "ref_paragraphs": ref_n,
                "aligned_units": len(units),
                "merge_sys_units": merge_sys,
                "merge_ref_units": merge_ref,
                "sys_encoding": sys_loaded.encoding,
                "ref_encoding": ref_loaded.encoding,
                # Filled in later (after scoring):
                "doc_sys_chars": None,
                "doc_ref_chars": None,
                "doc_char_ratio": np.nan,
                "len_ratio_mean": np.nan,
            }
            diagnostics["files"].append(file_info)

            sys_segs = [u.sys_text_norm for u in units]
            ref_segs = [u.ref_text_norm for u in units]

            # Document-length diagnostics (in chars over normalized units)
            doc_sys_chars = sum(len(s) for s in sys_segs)
            doc_ref_chars = sum(len(r) for r in ref_segs)
            file_info["doc_sys_chars"] = doc_sys_chars
            file_info["doc_ref_chars"] = doc_ref_chars
            file_info["doc_char_ratio"] = (doc_sys_chars / doc_ref_chars) if doc_ref_chars > 0 else np.nan

            # Paragraph-level lexical metrics
            seg_scores_list: List[Dict[str, float]] = []
            for u in units:
                seg_scores_list.append(
                    compute_sentence_metrics(
                        bleu_metric,
                        chrf_metric,
                        ter_metric,
                        u.sys_text_norm,
                        u.ref_text_norm,
                        metrics,
                    )
                )

            # Optional BERTScore
            bert_f1: Optional[np.ndarray] = None
            if "bertscore" in metrics:
                lang_code = LANG_CODE_MAP.get(lang, "en")
                bert_f1 = compute_bertscore(
                    cands=sys_segs,
                    refs=ref_segs,
                    lang=lang_code,
                    model_type=args.bertscore_model,
                    rescale_with_baseline=bool(args.bertscore_rescale),
                    device=args.device,
                    logger=logger,
                )

            # Optional COMET (best-effort segmentation)
            comet_scores: Optional[np.ndarray] = None
            if "comet" in metrics:
                if source_loaded and source_loaded.paragraphs_norm:
                    # Align source to reference; then use those source segments.
                    src_units = align_paragraphs_dp(
                        source_loaded.paragraphs_norm,
                        ref_loaded.paragraphs_norm,
                        source_loaded.paragraphs_raw,
                        ref_loaded.paragraphs_raw,
                        max_group=args.max_align_group,
                        logger=logger,
                    )
                    src_segs = [u.sys_text_norm for u in src_units]
                    if len(src_segs) != len(sys_segs):
                        # Fall back to whole source repeated (rare).
                        src_join = normalize_for_metrics("\n\n".join(source_loaded.paragraphs_raw))
                        src_segs = [src_join] * len(sys_segs)
                    comet_scores = compute_comet(
                        srcs=src_segs,
                        cands=sys_segs,
                        refs=ref_segs,
                        comet_model=args.comet_model,
                        device=args.device,
                        logger=logger,
                    )
                else:
                    logger.warning("Skipping COMET: no source text available.")

            # Write paragraph-level rows
            for idx, u in enumerate(units):
                seg_scores = seg_scores_list[idx]
                sys_len = len(u.sys_text_norm)
                ref_len = len(u.ref_text_norm)
                len_ratio = (sys_len / ref_len) if ref_len > 0 else np.nan

                num_prec, num_rec, num_f1 = f1_set(extract_numbers(u.sys_text_norm), extract_numbers(u.ref_text_norm))
                acr_prec, acr_rec, acr_f1 = f1_set(
                    extract_acronyms(u.sys_text_norm), extract_acronyms(u.ref_text_norm)
                )
                punct_pres, punct_absdiff, punct_ref_total, punct_sys_total = punctuation_preservation(
                    u.sys_text_norm, u.ref_text_norm
                )

                row: Dict[str, Any] = {
                    "model": model,
                    "language": lang,
                    "unit_id": u.unit_id,
                    "sys_para_span": f"{u.sys_start}:{u.sys_end}",
                    "ref_para_span": f"{u.ref_start}:{u.ref_end}",
                    "sys_char_len": sys_len,
                    "ref_char_len": ref_len,
                    "len_ratio": len_ratio,
                    "num_prec": num_prec,
                    "num_rec": num_rec,
                    "num_f1": num_f1,
                    "acr_prec": acr_prec,
                    "acr_rec": acr_rec,
                    "acr_f1": acr_f1,
                    "punct_pres": punct_pres,
                    "punct_absdiff": punct_absdiff,
                    "punct_ref_total": punct_ref_total,
                    "punct_sys_total": punct_sys_total,
                    "sys_text_raw": u.sys_text_raw,
                    "ref_text_raw": u.ref_text_raw,
                }
                for k, v in seg_scores.items():
                    row[k] = v
                if bert_f1 is not None and idx < len(bert_f1):
                    row["bertscore_f1"] = float(bert_f1[idx])
                if comet_scores is not None and idx < len(comet_scores):
                    row["comet"] = float(comet_scores[idx])
                paragraph_rows.append(row)

            # Document-level metrics
            doc_metrics = compute_corpus_metrics(bleu_metric, chrf_metric, ter_metric, sys_segs, ref_segs, metrics)

            # Document-level semantic metrics = mean over units
            doc_bert = float(np.mean(bert_f1)) if (bert_f1 is not None and len(bert_f1) > 0) else np.nan
            doc_comet = float(np.mean(comet_scores)) if (comet_scores is not None and len(comet_scores) > 0) else np.nan

            # Bootstrap CIs
            ci_map: Dict[str, Tuple[Optional[float], Optional[float]]] = {}
            for mname in metrics:
                if mname in ("bleu", "chrf", "ter"):
                    ci_map[mname] = bootstrap_ci(
                        mname,
                        sys_segs,
                        ref_segs,
                        None,
                        bleu_metric,
                        chrf_metric,
                        ter_metric,
                        rng=rng,
                        n_samples=args.bootstrap_samples,
                    )
                elif mname == "bertscore" and bert_f1 is not None:
                    ci_map[mname] = bootstrap_ci(
                        "bertscore",
                        sys_segs,
                        ref_segs,
                        bert_f1,
                        bleu_metric,
                        chrf_metric,
                        ter_metric,
                        rng=rng,
                        n_samples=args.bootstrap_samples,
                    )
                elif mname == "comet" and comet_scores is not None:
                    ci_map[mname] = bootstrap_ci(
                        "comet",
                        sys_segs,
                        ref_segs,
                        comet_scores,
                        bleu_metric,
                        chrf_metric,
                        ter_metric,
                        rng=rng,
                        n_samples=args.bootstrap_samples,
                    )

            # Aggregate probes from paragraph-level rows for this pair
            df_pair = pd.DataFrame([r for r in paragraph_rows if r["model"] == model and r["language"] == lang])
            len_ratio_mean = float(df_pair["len_ratio"].mean()) if not df_pair.empty else np.nan
            len_ratio_median = float(df_pair["len_ratio"].median()) if not df_pair.empty else np.nan
            num_f1_mean = float(df_pair["num_f1"].mean()) if not df_pair.empty else np.nan
            acr_f1_mean = float(df_pair["acr_f1"].mean()) if not df_pair.empty else np.nan
            punct_pres_mean = float(df_pair["punct_pres"].mean()) if not df_pair.empty else np.nan

            # Update file-level diagnostics with a quick length-ratio statistic.
            file_info["len_ratio_mean"] = len_ratio_mean

            sum_row: Dict[str, Any] = {
                "model": model,
                "language": lang,
                "n_units": len(units),
                "sys_paragraphs": sys_n,
                "ref_paragraphs": ref_n,
                "merge_sys_units": merge_sys,
                "merge_ref_units": merge_ref,
                "len_ratio_mean": len_ratio_mean,
                "len_ratio_median": len_ratio_median,
                "num_f1_mean": num_f1_mean,
                "acr_f1_mean": acr_f1_mean,
                "punct_pres_mean": punct_pres_mean,
            }

            # Add doc metrics + CI + within-doc std over units
            df_pair_metrics = df_pair.copy()
            for k, v in doc_metrics.items():
                sum_row[k] = v
                lo, hi = ci_map.get(k, (None, None))
                sum_row[f"{k}_ci_low"] = lo
                sum_row[f"{k}_ci_high"] = hi
                # within-doc variability (std over aligned units)
                if k in df_pair_metrics.columns and df_pair_metrics[k].notna().any():
                    sum_row[f"{k}_std_units"] = float(df_pair_metrics[k].astype(float).std(ddof=0))
                else:
                    sum_row[f"{k}_std_units"] = np.nan

            if "bertscore" in metrics:
                sum_row["bertscore_f1"] = doc_bert
                lo, hi = ci_map.get("bertscore", (None, None))
                sum_row["bertscore_f1_ci_low"] = lo
                sum_row["bertscore_f1_ci_high"] = hi
                if "bertscore_f1" in df_pair_metrics.columns and df_pair_metrics["bertscore_f1"].notna().any():
                    sum_row["bertscore_f1_std_units"] = float(df_pair_metrics["bertscore_f1"].astype(float).std(ddof=0))
                else:
                    sum_row["bertscore_f1_std_units"] = np.nan

            if "comet" in metrics:
                sum_row["comet"] = doc_comet
                lo, hi = ci_map.get("comet", (None, None))
                sum_row["comet_ci_low"] = lo
                sum_row["comet_ci_high"] = hi
                if "comet" in df_pair_metrics.columns and df_pair_metrics["comet"].notna().any():
                    sum_row["comet_std_units"] = float(df_pair_metrics["comet"].astype(float).std(ddof=0))
                else:
                    sum_row["comet_std_units"] = np.nan

            summary_rows.append(sum_row)

    if not paragraph_rows:
        logger.error("No paragraph-level results produced (check missing files / references).")
        sys.exit(1)

    paragraph_df = pd.DataFrame(paragraph_rows).sort_values(["language", "model", "unit_id"])
    summary_df = pd.DataFrame(summary_rows).sort_values(["language", "model"])

    # Write CSVs
    paragraph_df.to_csv(out_dir / "metrics_paragraph_level.csv", index=False, encoding="utf-8")
    logger.info(f"Wrote: {out_dir / 'metrics_paragraph_level.csv'}")

    summary_df.to_csv(out_dir / "metrics_summary.csv", index=False, encoding="utf-8")
    logger.info(f"Wrote: {out_dir / 'metrics_summary.csv'}")

    # Add overall macro-average rows
    overall_rows: List[Dict[str, Any]] = []
    for model in models:
        df_m = summary_df[summary_df["model"] == model]
        if df_m.empty:
            continue
        row: Dict[str, Any] = {
            "model": model,
            "language": "__overall__",
            "n_langs": int(df_m["language"].nunique()),
        }
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            if col not in df_m.columns:
                continue
            vals = df_m[col].dropna().astype(float)
            if len(vals) == 0:
                row[col] = np.nan
                row[f"{col}_std"] = np.nan
            else:
                row[col] = float(vals.mean())
                row[f"{col}_std"] = float(vals.std(ddof=0))
        overall_rows.append(row)

    if overall_rows:
        overall_df = pd.DataFrame(overall_rows)
        summary_df2 = pd.concat([summary_df, overall_df], ignore_index=True).sort_values(["language", "model"])
        summary_df2.to_csv(out_dir / "metrics_summary.csv", index=False, encoding="utf-8")
        summary_df = summary_df2
        logger.info("Added __overall__ macro-average rows to metrics_summary.csv")

    # Plots
    plots: Dict[str, Any] = {}
    bar_metrics: List[str] = []
    if "chrf" in metrics:
        bar_metrics.append("chrf")
    elif "bleu" in metrics:
        bar_metrics.append("bleu")
    if "bertscore" in metrics and "bertscore_f1" in paragraph_df.columns and paragraph_df["bertscore_f1"].notna().any():
        bar_metrics.append("bertscore")

    bar_paths: List[str] = []
    for m in bar_metrics:
        bar_paths.extend(plot_language_bars(summary_df, m, out_dir, languages, logger))
    if bar_paths:
        plots["bars"] = bar_paths

    corr_path = plot_metric_correlation_heatmap(paragraph_df, metrics, out_dir, logger)
    if corr_path:
        plots["corr_heatmap"] = corr_path

    scatter_path = plot_metric_scatter(paragraph_df, out_dir, logger)
    if scatter_path:
        plots["scatter"] = scatter_path

    diagnostics["plots"] = plots

    # Diagnostics markdown
    diag_lines: List[str] = []
    diag_lines.append("# Diagnostics\n")
    diag_lines.append(f"- Root: `{root}`")
    diag_lines.append(f"- Output: `{out_dir}`")
    diag_lines.append(f"- Models discovered: {len(models)}")
    diag_lines.append(f"- Languages (with references): {len(languages)}")
    diag_lines.append(f"- Metrics requested: {', '.join(metrics)}")
    diag_lines.append("")

    diag_lines.append("## Missing files\n")
    if diagnostics["missing"]:
        diag_lines.extend([f"- {msg}" for msg in diagnostics["missing"]])
    else:
        diag_lines.append("- None")
    diag_lines.append("")

    diag_lines.append("## Paragraph counts and alignment\n")
    diag_lines.append(
        "| Model | Language | Sys paras | Ref paras | Units | Sys merges | Ref merges | Len ratio (mean) | Doc char ratio | Sys enc | Ref enc |"
    )
    diag_lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|")
    for info in diagnostics["files"]:
        diag_lines.append(
            f"| {info['model']} | {info['language']} | {info['sys_paragraphs']} | {info['ref_paragraphs']} | "
            f"{info['aligned_units']} | {info['merge_sys_units']} | {info['merge_ref_units']} | "
            f"{float(info.get('len_ratio_mean', np.nan)):.3f} | {float(info.get('doc_char_ratio', np.nan)):.3f} | "
            f"{info['sys_encoding']} | {info['ref_encoding']} |"
        )
    diag_lines.append("")

    diag_lines.append("## Mismatch summaries\n")
    any_mismatch = False
    for lang in languages:
        msgs = diagnostics["mismatches"].get(lang, [])
        if not msgs:
            continue
        any_mismatch = True
        diag_lines.append(f"### {lang}")
        diag_lines.extend([f"- {msg}" for msg in msgs])
        diag_lines.append("")
    if not any_mismatch:
        diag_lines.append("- None\n")

    (out_dir / "diagnostics.md").write_text("\n".join(diag_lines), encoding="utf-8")
    logger.info(f"Wrote: {out_dir / 'diagnostics.md'}")

    # Leaderboards markdown
    leader_md = build_leaderboards_md(summary_df, paragraph_df, diagnostics, metrics, logger)
    (out_dir / "leaderboards.md").write_text(leader_md, encoding="utf-8")
    logger.info(f"Wrote: {out_dir / 'leaderboards.md'}")

    # Console summary (concise)
    print("\n=== Console summary ===")
    print(f"Models discovered: {len(models)}")
    print(f"Languages with references: {len(languages)}")
    print(f"Metrics requested: {', '.join(metrics)}")
    if diagnostics["missing"]:
        print(f"Missing files: {len(diagnostics['missing'])} (see diagnostics.md)")

    overall_df = summary_df[summary_df["language"] == "__overall__"].copy()
    if not overall_df.empty:
        # Composite rank across available metrics
        rank_cols = []
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            if col not in overall_df.columns or overall_df[col].isna().all():
                continue
            ascending = METRIC_DIRECTIONS[m] < 0
            overall_df[f"rank_{m}"] = overall_df[col].rank(ascending=ascending, method="average")
            rank_cols.append(f"rank_{m}")
        if rank_cols:
            overall_df["rank_mean"] = overall_df[rank_cols].mean(axis=1)
            overall_df = overall_df.sort_values(["rank_mean", "model"])
        print("\nTop overall models (macro-average across languages):")
        for _, r in overall_df.head(5).iterrows():
            parts = []
            for m in metrics:
                col = "bertscore_f1" if m == "bertscore" else m
                if col in overall_df.columns and not pd.isna(r.get(col)) and not overall_df[col].isna().all():
                    parts.append(f"{m}={float(r[col]):.2f}")
            print(f"  - {r['model']}: " + ", ".join(parts))

        # Biggest gaps (best - worst) for each metric
        print("\nBiggest gaps (best - worst) across models (overall):")
        for m in metrics:
            col = "bertscore_f1" if m == "bertscore" else m
            if col not in overall_df.columns or overall_df[col].isna().all():
                continue
            vals = overall_df[col].astype(float)
            if METRIC_DIRECTIONS[m] > 0:
                gap = float(vals.max() - vals.min())
            else:
                # lower-better metric: gap in "better direction"
                gap = float(vals.min() - vals.max())
            print(f"  - {m}: {gap:.2f}")
    else:
        print("\nNo overall rows (insufficient data).")

    print("\nOutputs written to:", out_dir.resolve())


if __name__ == "__main__":
    main()
