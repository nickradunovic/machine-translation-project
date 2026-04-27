# Machine Translation Project

Machine-translation evaluation project with two tracks:

- **Reference-based track:** Dutch source text is translated into Turkish, Spanish, English, Polish, Ukrainian, Arabic, and German, then scored against reference translations.
- **Reference-free track:** Azure Translator and GPT-4 translations are scored with a numeric human/GPT judge rubric for meaning, register, and readability.

## Scripts

| Script | What it does | When to use it |
|---|---|---|
| `translate_script.py` | Generates reference-based translations from `translations_ref_based/dutch_original_text.txt` for Azure Translator, GPT-4, GPT-5.2, and Llama models. Outputs `translations_ref_based/<model>/<language>.txt`. | Use only when regenerating API-produced translations. It does not generate the web-interface systems: DeepL, Google Translate, or Gemini 3 Pro. |
| `analysis_ref_based/evaluate_translations.py` | Computes BLEU, chrF++, TER, BERTScore, and optionally COMET from `translations_ref_based/`. Outputs paragraph metrics, summaries, leaderboards, diagnostics, and plots. | Use to reproduce the reference-based metric results. |
| `analysis_ref_based/make_paper_artifacts.py` | Converts reference-based evaluation CSVs into paper-ready tables, appendix files, and figures. | Use after `evaluate_translations.py`. |
| `analysis_ref_free/analyze_ref_free_track.py` | Loads `analysis_ref_free/ref_free_track_structured_numeric.json`, exports judge/human score CSVs, paired GPT-4-minus-Azure deltas, agreement metrics, and a Markdown report. | Use to reproduce the numeric reference-free analysis. |
| `analysis_ref_free/generate_ref_free_artifacts.py` | Generates LaTeX tables and PNG figures for the reference-free track. | Use after or alongside `analyze_ref_free_track.py` when preparing paper artifacts. |

## Reproduce the Paper Artifacts

From the repository root:

```bash
python -m pip install -U openai requests numpy pandas matplotlib scipy sacrebleu==2.6.0 bert-score unbabel-comet torch transformers

python analysis_ref_based/evaluate_translations.py \
  --root translations_ref_based \
  --out analysis_ref_based/out_translation_eval \
  --metrics bleu chrf ter bertscore comet \
  --bertscore-model xlm-roberta-large \
  --comet-model Unbabel/wmt22-comet-da \
  --bleu-tokenize intl \
  --seed 42

python analysis_ref_based/make_paper_artifacts.py \
  --in_dir analysis_ref_based/out_translation_eval \
  --out_dir analysis_ref_based/paper_artifacts \
  --primary_metric comet \
  --formats png pdf \
  --seed 42 \
  --scatter_color_by language \
  --violin_by_language

python analysis_ref_free/analyze_ref_free_track.py \
  --data analysis_ref_free/ref_free_track_structured_numeric.json \
  --outdir analysis_ref_free

python analysis_ref_free/generate_ref_free_artifacts.py \
  --json analysis_ref_free/ref_free_track_structured_numeric.json \
  --outdir analysis_ref_free \
  --aggregation micro \
  --seed 0 \
  --color_scatter_by language
```

To regenerate the API translations before scoring, create `.env` from `.env.example`, fill in the Azure/OpenAI keys, then run:

```bash
python translate_script.py --env-file .env
```

## Paper Settings

Evaluated systems:

- **NMT:** Azure Translator via Microsoft Translator Text API v3.0; DeepL Translator via web interface; Google Translate via web interface.
- **LLM:** Gemini 3 Pro via Google web interface; GPT-4 via Microsoft Foundry API as `gpt-4` (`turbo-2024-04-09`); GPT-5.2 via Microsoft Foundry API as `gpt-5.2` (`2025-12-11`); Llama models via Microsoft Foundry API as `Meta-Llama-3.1-8B-Instruct` v6, `Meta-Llama-3.1-405B-Instruct` v1, and `Llama-3.3-70B-Instruct` v9.

API generation settings:

- Chat Completions models: `temperature=0`, `top_p=1`, `seed=0`, token limit `2048`.
- GPT-5.2: `reasoning_effort=none` and `max_completion_tokens=2048`.
- Azure Translator: Microsoft Translator Text API; temperature, top-p, seed, reasoning effort, and token limit do not apply.

Reference-based metric settings:

- BLEU: `sacreBLEU v2.6.0`, `nrefs:1|case:mixed|eff:yes|tok:intl|smooth:exp|version:2.6.0`.
- chrF++: `sacreBLEU v2.6.0`, `nrefs:1|case:mixed|eff:yes|nc:6|nw:2|space:no|version:2.6.0`.
- TER: `sacreBLEU v2.6.0`, `nrefs:1|case:lc|tok:tercom|norm:no|punct:yes|asian:no|version:2.6.0`.
- BERTScore: F1 with `xlm-roberta-large`, no baseline rescaling.
- COMET: `Unbabel/wmt22-comet-da`, checkpoint `2760a223ac957f30acfb18c8aa649b01cf1d75f2`.

## Citation

If you use these reproducibility materials, please cite the archived Zenodo release. Citation metadata is available in [CITATION.cff](CITATION.cff).

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE).
