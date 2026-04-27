#!/usr/bin/env python3
"""Reference-free track analysis (numeric rubric only).

Input:
  - ref_free_track_structured_numeric.json

Outputs:
  - judge_scores.csv / human_scores.csv / all_scores.csv
  - human_deltas_by_language.csv
  - human_deltas_macro_over_languages.csv
  - judge_vs_human_agreement.csv
  - analysis_report.md

Run:
  python analyze_ref_free_track.py --data ref_free_track_structured_numeric.json --outdir .
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd

CRITERIA = ['meaning', 'tone', 'readability']

def bootstrap_ci(values, n_boot=10000, alpha=0.05, seed=0):
    rng = np.random.default_rng(seed)
    v = np.asarray(values, dtype=float)
    n = len(v)
    boots = [float(np.mean(rng.choice(v, size=n, replace=True))) for _ in range(n_boot)]
    return float(np.quantile(boots, alpha/2)), float(np.quantile(boots, 1-alpha/2))

def sign_flip_pvalue(deltas, n_perm=50000, seed=0):
    rng = np.random.default_rng(seed)
    d = np.asarray(deltas, dtype=float)
    obs = float(np.mean(d))
    count = 0
    for _ in range(n_perm):
        signs = rng.choice([-1,1], size=len(d))
        if abs(float(np.mean(d*signs))) >= abs(obs) - 1e-12:
            count += 1
    return float(count/n_perm), obs

def spearmanr(x, y):
    x = pd.Series(x).rank(method="average").to_numpy()
    y = pd.Series(y).rank(method="average").to_numpy()
    x = x - x.mean()
    y = y - y.mean()
    denom = float(np.sqrt((x*x).sum()*(y*y).sum()))
    return float((x*y).sum()/denom) if denom else float("nan")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=str, default="ref_free_track_structured_numeric.json")
    ap.add_argument("--outdir", type=str, default=".")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    payload = json.loads(Path(args.data).read_text(encoding="utf-8"))
    df_j = pd.DataFrame(payload["data"]["judge"])
    df_h = pd.DataFrame(payload["data"]["human"])

    df_j.to_csv(outdir / "judge_scores.csv", index=False)
    df_h.to_csv(outdir / "human_scores.csv", index=False)
    pd.concat([df_j, df_h], ignore_index=True).to_csv(outdir / "all_scores.csv", index=False)

    # Human: average across evaluators per (language, system, doc)
    human_doc = df_h.groupby(["language","system","doc_id"], as_index=False)[CRITERIA].mean()

    # Deltas by language (paired by doc)
    delta_rows = []
    for lang in sorted(human_doc["language"].unique()):
        g = human_doc[human_doc.language==lang]
        for crit in CRITERIA:
            gpt = g[g.system=="gpt4"].set_index("doc_id")[crit]
            az  = g[g.system=="azure"].set_index("doc_id")[crit]
            common = gpt.index.intersection(az.index)
            deltas = (gpt.loc[common] - az.loc[common]).to_numpy()
            if len(deltas)==0:
                continue
            lo, hi = bootstrap_ci(deltas, seed=0)
            p, obs = sign_flip_pvalue(deltas, seed=0)
            sd = float(np.std(deltas, ddof=1))
            dz = float(obs/sd) if sd>0 else float("nan")
            delta_rows.append({
                "language":lang,
                "criterion":crit,
                "mean_delta":float(obs),
                "ci95_low":lo,
                "ci95_high":hi,
                "signflip_p":p,
                "cohen_dz":dz,
                "n_docs":int(len(deltas))
            })
    delta_df = pd.DataFrame(delta_rows)
    delta_df.to_csv(outdir / "human_deltas_by_language.csv", index=False)

    # Macro (equal weight over languages)
    macro_rows = []
    for crit in CRITERIA:
        vals = delta_df[delta_df.criterion==crit]["mean_delta"].to_numpy()
        if len(vals)>1:
            lo, hi = bootstrap_ci(vals, seed=1)
            p, obs = sign_flip_pvalue(vals, seed=1)
            sd = float(np.std(vals, ddof=1))
            dz = float(obs/sd) if sd>0 else float("nan")
            macro_rows.append({
                "criterion":crit,
                "mean_delta":float(obs),
                "ci95_low":lo,
                "ci95_high":hi,
                "signflip_p":p,
                "cohen_dz":dz,
                "n_lang":int(len(vals))
            })
    macro_df = pd.DataFrame(macro_rows)
    macro_df.to_csv(outdir / "human_deltas_macro_over_languages.csv", index=False)

    # Judge vs human agreement (excerpt-level means)
    human_points = human_doc.set_index(["language","system","doc_id"])
    judge_points = df_j.set_index(["language","system","doc_id"])
    common = human_points.index.intersection(judge_points.index)

    agree_rows = []
    for crit in CRITERIA:
        h = human_points.loc[common][crit].to_numpy()
        j = judge_points.loc[common][crit].to_numpy()
        rho = spearmanr(h, j)
        mae = float(np.mean(np.abs(h-j)))
        rmse = float(np.sqrt(np.mean((h-j)**2)))
        X = np.vstack([np.ones_like(h), h]).T
        a, b = np.linalg.lstsq(X, j, rcond=None)[0]
        agree_rows.append({
            "criterion":crit,
            "n_points":int(len(h)),
            "spearman_rho":float(rho),
            "mae":mae,
            "rmse":rmse,
            "judge_vs_human_slope":float(b),
            "judge_vs_human_intercept":float(a),
        })
    agree_df = pd.DataFrame(agree_rows)
    agree_df.to_csv(outdir / "judge_vs_human_agreement.csv", index=False)

    # report
    lines = []
    lines.append("# Reference-free track analysis (numeric rubric only)\n")
    lines.append("## Macro deltas (GPT-4 − Azure)\n")
    lines.append(macro_df.to_markdown(index=False))
    lines.append("\n## Deltas by language\n")
    lines.append(delta_df.sort_values(['criterion','language']).to_markdown(index=False))
    lines.append("\n## Judge vs human agreement\n")
    lines.append(agree_df.to_markdown(index=False))
    (outdir / "analysis_report.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
