# Translation Evaluation Report

- Generated: 2026-01-24 17:20 UTC
- Root: `translations_ref_based`
- Output: `out_translation_eval_v2`
- Models discovered: 9
- Languages (with references): 7
- Metrics requested: bleu, chrf, ter, bertscore, comet

## Reference caveat

All scores are **reference-based**: they quantify similarity to the provided reference translation(s). A correct translation can score lower if it uses different wording than the reference.


## Language difficulty snapshot

Mean document-level score across models (macro view). Lower means "harder" *with respect to the reference*.

| index | n_models | bleu | chrf | ter | bertscore | comet |
|---|---|---|---|---|---|---|
| arabic | 9 | 14.59 | 36.72 | -75.21 | 91.91 | 76.90 |
| ukrainian | 9 | 14.61 | 38.35 | -71.76 | 92.66 | 80.18 |
| polish | 9 | 28.58 | 51.30 | -60.90 | 93.50 | 85.61 |
| turkish | 9 | 23.71 | 44.12 | -71.58 | 94.01 | 81.78 |
| english | 9 | 40.10 | 57.88 | -47.20 | 95.18 | 81.20 |
| german | 9 | 36.82 | 61.71 | -46.24 | 95.81 | 86.63 |
| spanish | 9 | 48.23 | 65.39 | -35.48 | 96.60 | 82.76 |

*(For TER we report -TER so that higher is better in this snapshot.)*


## Per-language leaderboards


### turkish

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| deepl | 5 | 35.60 [20.59, 47.33] | 50.56 [39.38, 59.81] | 59.62 [45.83, 72.73] | 94.89 [92.77, 96.27] | 82.20 [74.61, 87.73] | 0.869 | 1.00 | 1.00 | 0.70 |
| gemini-3-pro | 5 | 30.20 [21.06, 41.27] | 50.05 [45.48, 55.79] | 62.18 [50.82, 71.35] | 94.73 [94.13, 95.31] | 85.01 [82.13, 88.18] | 0.912 | 1.00 | 1.00 | 0.60 |
| google-translate | 5 | 33.49 [18.48, 46.86] | 49.21 [37.02, 58.71] | 63.46 [46.56, 78.81] | 94.45 [92.88, 95.87] | 85.76 [83.75, 87.43] | 0.892 | 1.00 | 1.00 | 0.74 |
| gpt-5-2 | 5 | 21.92 [11.76, 33.05] | 44.49 [37.03, 52.08] | 68.59 [56.92, 76.44] | 94.74 [93.82, 95.61] | 83.39 [78.20, 87.76] | 0.882 | 1.00 | 1.00 | 0.47 |
| gpt-4 | 5 | 25.03 [19.08, 30.98] | 43.69 [40.37, 47.24] | 66.03 [54.40, 73.16] | 94.31 [93.65, 95.09] | 83.23 [81.58, 85.02] | 0.894 | 1.00 | 1.00 | 0.64 |
| azure-translator | 5 | 27.18 [15.32, 44.99] | 45.92 [37.73, 56.42] | 67.31 [48.48, 78.45] | 94.13 [92.81, 95.67] | 79.17 [73.44, 85.19] | 0.857 | 1.00 | 1.00 | 0.58 |
| meta-llama-3-1-405b-instruct | 5 | 17.62 [11.99, 23.96] | 40.37 [34.45, 45.08] | 73.08 [64.34, 80.33] | 94.21 [93.20, 95.00] | 81.81 [76.64, 85.79] | 0.853 | 1.00 | 1.00 | 0.59 |
| llama-3-3-70b-instruct | 5 | 16.62 [9.56, 22.61] | 42.27 [39.85, 44.92] | 80.13 [73.13, 85.54] | 93.44 [92.37, 94.41] | 82.86 [80.99, 84.96] | 0.959 | 1.00 | 1.00 | 0.63 |
| meta-llama-3-1-8b-instruct | 5 | 5.71 [3.64, 7.52] | 30.50 [25.02, 36.02] | 103.85 [83.69, 131.01] | 91.18 [90.07, 92.58] | 72.60 [67.29, 77.18] | 0.976 | 1.00 | 1.00 | 0.33 |

### spanish

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| deepl | 5 | 59.04 [53.80, 68.09] | 72.17 [68.65, 78.27] | 25.32 [22.31, 30.22] | 97.39 [97.10, 97.79] | 84.90 [82.03, 88.28] | 0.958 | 1.00 | 1.00 | 0.56 |
| gpt-5-2 | 5 | 55.18 [49.13, 65.35] | 70.80 [68.06, 74.76] | 27.90 [22.62, 34.32] | 97.13 [96.38, 98.02] | 85.11 [82.64, 87.91] | 0.974 | 1.00 | 1.00 | 0.54 |
| gemini-3-pro | 5 | 50.95 [41.05, 65.57] | 67.30 [61.70, 76.79] | 33.48 [27.69, 39.73] | 96.67 [95.56, 98.07] | 84.24 [80.45, 88.21] | 0.994 | 1.00 | 1.00 | 0.59 |
| llama-3-3-70b-instruct | 5 | 51.34 [42.73, 67.60] | 66.58 [60.51, 76.76] | 33.48 [21.89, 41.03] | 96.94 [96.09, 98.31] | 83.13 [79.12, 88.19] | 0.943 | 1.00 | 1.00 | 0.60 |
| gpt-4 | 5 | 51.22 [45.81, 62.45] | 67.79 [63.70, 74.73] | 34.33 [25.49, 41.92] | 96.72 [95.42, 98.16] | 83.85 [81.47, 87.50] | 1.001 | 1.00 | 1.00 | 0.61 |
| meta-llama-3-1-405b-instruct | 5 | 49.52 [45.91, 54.60] | 65.43 [62.72, 68.34] | 33.91 [29.56, 38.12] | 97.01 [96.37, 98.03] | 83.65 [78.83, 87.93] | 0.950 | 1.00 | 1.00 | 0.53 |
| azure-translator | 5 | 42.92 [36.93, 51.46] | 62.02 [57.99, 68.16] | 40.34 [35.29, 43.65] | 96.45 [95.48, 97.41] | 79.24 [76.40, 82.55] | 0.952 | 1.00 | 1.00 | 0.55 |
| meta-llama-3-1-8b-instruct | 5 | 41.03 [37.28, 45.56] | 59.42 [56.72, 62.96] | 42.06 [40.10, 43.27] | 95.95 [95.19, 96.84] | 79.43 [76.34, 82.44] | 0.933 | 1.00 | 1.00 | 0.66 |
| google-translate | 5 | 32.88 [25.32, 39.51] | 57.01 [52.33, 60.60] | 48.50 [41.99, 54.91] | 95.17 [94.17, 96.52] | 81.30 [76.60, 86.48] | 0.933 | 1.00 | 1.00 | 0.57 |

### english

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| gpt-5-2 | 5 | 46.88 [38.15, 52.56] | 61.21 [52.17, 67.04] | 41.87 [36.08, 47.96] | 95.59 [94.43, 96.37] | 81.47 [76.56, 85.30] | 0.854 | 1.00 | 0.92 | 0.95 |
| gemini-3-pro | 5 | 47.76 [37.08, 53.71] | 61.73 [51.43, 69.99] | 44.31 [37.56, 52.02] | 95.27 [94.09, 95.92] | 81.96 [76.01, 85.41] | 0.874 | 1.00 | 0.92 | 0.87 |
| deepl | 5 | 45.69 [34.66, 52.53] | 60.26 [48.81, 68.27] | 43.90 [37.10, 52.94] | 95.04 [94.01, 95.75] | 81.10 [75.81, 85.11] | 0.855 | 1.00 | 0.92 | 0.92 |
| meta-llama-3-1-405b-instruct | 5 | 37.58 [31.19, 43.30] | 57.05 [49.33, 64.99] | 48.78 [38.14, 54.64] | 95.49 [94.15, 96.65] | 81.65 [76.47, 86.08] | 0.874 | 1.00 | 0.92 | 0.59 |
| azure-translator | 5 | 37.20 [26.43, 46.65] | 56.94 [49.16, 65.58] | 47.97 [38.81, 55.36] | 95.34 [94.23, 96.29] | 81.66 [76.66, 86.03] | 0.878 | 1.00 | 0.92 | 0.58 |
| llama-3-3-70b-instruct | 5 | 37.33 [31.27, 44.31] | 56.86 [48.34, 65.02] | 48.37 [38.38, 54.30] | 95.48 [94.14, 96.59] | 81.43 [76.03, 86.13] | 0.869 | 1.00 | 0.92 | 0.60 |
| gpt-4 | 5 | 39.51 [31.07, 48.54] | 57.07 [50.23, 65.82] | 46.75 [38.31, 53.21] | 94.85 [93.62, 96.08] | 80.39 [74.27, 85.74] | 0.889 | 1.00 | 0.92 | 0.84 |
| meta-llama-3-1-8b-instruct | 5 | 35.82 [26.16, 42.83] | 55.32 [43.82, 63.29] | 49.19 [41.83, 56.36] | 95.36 [93.81, 96.50] | 80.63 [74.69, 85.62] | 0.847 | 1.00 | 0.92 | 0.60 |
| google-translate | 5 | 33.18 [25.10, 41.07] | 54.47 [45.95, 63.19] | 53.66 [45.27, 59.45] | 94.18 [93.16, 95.62] | 80.50 [75.40, 85.61] | 0.860 | 1.00 | 0.92 | 0.61 |

### polish

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| google-translate | 5 | 40.99 [37.44, 45.50] | 63.62 [60.27, 66.74] | 41.18 [38.46, 42.92] | 94.77 [94.01, 95.54] | 89.75 [86.80, 92.60] | 0.874 | 1.00 | 1.00 | 0.69 |
| gpt-5-2 | 5 | 48.90 [42.75, 56.41] | 63.23 [59.02, 69.85] | 48.13 [38.60, 52.29] | 95.50 [94.93, 96.21] | 88.97 [86.74, 91.42] | 0.929 | 1.00 | 1.00 | 0.65 |
| deepl | 5 | 34.65 [28.22, 41.14] | 58.26 [53.70, 63.70] | 55.08 [49.11, 60.41] | 94.36 [93.58, 95.46] | 88.37 [86.07, 91.18] | 0.913 | 1.00 | 1.00 | 0.55 |
| gemini-3-pro | 5 | 32.70 [25.15, 41.30] | 55.95 [49.83, 65.13] | 55.08 [43.41, 62.35] | 93.82 [92.69, 95.51] | 87.57 [82.65, 91.64] | 0.911 | 1.00 | 1.00 | 0.52 |
| gpt-4 | 5 | 27.08 [17.88, 35.65] | 50.67 [44.21, 57.67] | 68.45 [56.28, 80.10] | 93.19 [91.85, 94.33] | 86.19 [83.00, 89.25] | 0.971 | 1.00 | 1.00 | 0.51 |
| meta-llama-3-1-405b-instruct | 5 | 21.78 [16.15, 27.51] | 46.31 [42.77, 50.00] | 64.17 [58.47, 69.95] | 92.93 [92.24, 93.66] | 84.94 [81.10, 88.77] | 0.838 | 1.00 | 1.00 | 0.44 |
| llama-3-3-70b-instruct | 5 | 20.69 [14.34, 28.43] | 46.39 [42.09, 52.29] | 69.52 [57.84, 80.95] | 92.67 [91.77, 93.83] | 86.29 [83.35, 89.29] | 0.910 | 1.00 | 1.00 | 0.47 |
| azure-translator | 5 | 18.90 [11.05, 26.59] | 44.02 [37.23, 50.97] | 67.91 [58.92, 77.06] | 92.84 [91.82, 94.07] | 82.65 [74.20, 88.93] | 0.865 | 1.00 | 1.00 | 0.42 |
| meta-llama-3-1-8b-instruct | 5 | 11.54 [6.67, 16.21] | 33.28 [29.61, 38.17] | 78.61 [73.23, 82.94] | 91.38 [90.57, 92.19] | 75.71 [70.05, 80.81] | 0.822 | 1.00 | 1.00 | 0.46 |

### ukrainian

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| gemini-3-pro | 5 | 19.66 [6.95, 28.87] | 42.51 [30.20, 52.91] | 65.10 [55.98, 76.47] | 93.34 [91.53, 95.07] | 81.89 [73.63, 87.61] | 0.736 | 1.00 | 0.40 | 0.72 |
| gpt-5-2 | 5 | 22.46 [11.33, 30.93] | 44.47 [32.08, 55.56] | 65.49 [53.28, 77.73] | 93.54 [91.34, 95.52] | 79.76 [67.85, 88.10] | 0.716 | 1.00 | 0.40 | 0.72 |
| deepl | 5 | 18.29 [7.35, 24.83] | 40.16 [29.05, 49.58] | 69.02 [61.78, 78.87] | 92.84 [91.19, 94.24] | 81.04 [74.41, 86.32] | 0.698 | 1.00 | 0.40 | 0.75 |
| llama-3-3-70b-instruct | 5 | 12.29 [6.65, 16.85] | 37.97 [29.10, 47.25] | 70.59 [64.47, 77.00] | 92.82 [91.24, 94.33] | 79.70 [72.67, 85.66] | 0.721 | 1.00 | 0.40 | 0.75 |
| azure-translator | 5 | 15.63 [7.80, 22.54] | 37.09 [27.16, 46.19] | 70.98 [64.09, 78.60] | 92.44 [90.34, 94.24] | 77.41 [68.24, 84.89] | 0.719 | 1.00 | 0.40 | 0.69 |
| google-translate | 5 | 15.09 [7.76, 23.34] | 36.32 [27.61, 44.93] | 75.69 [69.58, 82.55] | 91.80 [90.61, 93.36] | 80.12 [69.39, 87.46] | 0.752 | 1.00 | 0.40 | 0.61 |
| meta-llama-3-1-405b-instruct | 5 | 8.77 [3.18, 14.02] | 35.94 [30.56, 43.21] | 76.08 [68.86, 82.03] | 92.61 [91.21, 93.91] | 80.21 [75.92, 84.51] | 0.738 | 1.00 | 0.40 | 0.46 |
| gpt-4 | 5 | 11.13 [3.03, 19.29] | 36.02 [26.49, 46.91] | 74.12 [63.88, 82.35] | 92.50 [90.88, 94.10] | 79.60 [71.61, 86.91] | 0.704 | 1.00 | 0.40 | 0.53 |
| meta-llama-3-1-8b-instruct | 5 | 8.11 [2.70, 13.34] | 34.65 [30.06, 40.53] | 78.82 [73.57, 83.17] | 92.01 [90.80, 93.18] | 81.91 [77.42, 85.68] | 0.799 | 1.00 | 0.47 | 0.55 |

### arabic

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| gemini-3-pro | 5 | 27.83 [22.09, 33.56] | 48.66 [45.16, 51.91] | 66.12 [59.32, 73.23] | 93.75 [93.17, 94.24] | 84.51 [80.75, 87.41] | 0.881 | 1.00 | 1.00 | 0.67 |
| google-translate | 5 | 21.61 [16.75, 29.55] | 41.05 [37.32, 47.61] | 69.83 [61.14, 74.76] | 92.59 [91.42, 93.76] | 83.04 [80.32, 85.35] | 0.801 | 1.00 | 1.00 | 0.58 |
| deepl | 5 | 13.68 [10.69, 18.73] | 39.12 [34.34, 45.40] | 72.31 [62.15, 79.52] | 92.24 [90.92, 93.66] | 78.44 [71.48, 84.88] | 0.815 | 1.00 | 1.00 | 0.30 |
| gpt-5-2 | 5 | 14.05 [8.07, 20.59] | 37.45 [30.41, 44.27] | 73.97 [64.32, 82.10] | 92.20 [90.65, 93.80] | 77.87 [70.09, 84.52] | 0.756 | 1.00 | 1.00 | 0.28 |
| gpt-4 | 5 | 12.15 [9.21, 15.28] | 37.65 [32.10, 43.25] | 75.21 [68.08, 82.97] | 92.09 [90.93, 93.26] | 78.89 [73.73, 84.04] | 0.795 | 1.00 | 1.00 | 0.35 |
| meta-llama-3-1-405b-instruct | 5 | 13.14 [7.37, 16.97] | 36.32 [27.80, 41.69] | 74.79 [67.06, 83.41] | 91.83 [90.37, 92.85] | 74.79 [67.80, 81.78] | 0.711 | 1.00 | 1.00 | 0.37 |
| azure-translator | 5 | 11.62 [5.53, 21.05] | 35.70 [30.20, 44.67] | 77.69 [66.67, 85.24] | 91.45 [89.59, 93.40] | 75.08 [66.69, 83.45] | 0.790 | 1.00 | 0.83 | 0.34 |
| meta-llama-3-1-8b-instruct | 5 | 8.94 [6.31, 11.17] | 27.71 [23.93, 33.04] | 82.64 [77.30, 87.34] | 90.51 [89.58, 91.51] | 67.27 [58.28, 76.67] | 0.752 | 1.00 | 0.96 | 0.33 |
| llama-3-3-70b-instruct | 5 | 8.34 [3.80, 12.16] | 26.84 [21.87, 34.18] | 84.30 [76.19, 90.39] | 90.53 [88.93, 92.14] | 72.20 [65.95, 78.46] | 0.706 | 1.00 | 0.83 | 0.35 |

### german

**Tie watch:** top-2 BERTSCORE 95% CIs overlap; treat as a statistical tie for this document.

| Model | N | BLEU | CHRF | TER | BERTScore-F1 | COMET | Len ratio | Nums F1 | Acr F1 | Punct pres. |
|---|---|---|---|---|---|---|---|---|---|---|
| gpt-5-2 | 5 | 45.90 [37.56, 55.05] | 70.24 [65.84, 77.63] | 35.86 [25.87, 43.06] | 96.87 [96.25, 97.65] | 88.78 [87.21, 90.64] | 0.958 | 1.00 | 0.93 | 0.65 |
| gemini-3-pro | 5 | 44.64 [33.75, 58.98] | 67.71 [60.75, 78.90] | 39.90 [26.57, 50.51] | 96.75 [95.84, 97.81] | 88.39 [86.74, 90.67] | 0.963 | 1.00 | 0.93 | 0.66 |
| gpt-4 | 5 | 39.60 [33.29, 49.40] | 65.36 [58.71, 75.74] | 39.90 [30.57, 45.08] | 96.53 [95.69, 97.50] | 88.37 [86.36, 90.71] | 0.955 | 1.00 | 0.60 | 0.59 |
| meta-llama-3-1-405b-instruct | 5 | 41.72 [36.97, 44.06] | 65.49 [61.63, 68.71] | 39.90 [36.75, 42.03] | 96.33 [96.14, 96.62] | 87.18 [85.30, 88.50] | 0.955 | 1.00 | 0.93 | 0.58 |
| deepl | 5 | 36.58 [30.07, 44.31] | 62.18 [58.19, 66.82] | 46.97 [41.14, 51.72] | 95.87 [95.41, 96.27] | 87.23 [86.23, 88.14] | 0.994 | 1.00 | 0.93 | 0.66 |
| llama-3-3-70b-instruct | 5 | 39.21 [35.79, 43.69] | 61.09 [57.72, 66.34] | 42.93 [39.90, 46.11] | 95.84 [95.35, 96.40] | 86.65 [85.35, 88.11] | 0.947 | 1.00 | 0.93 | 0.58 |
| azure-translator | 5 | 34.55 [25.05, 41.77] | 60.11 [55.85, 64.04] | 50.00 [43.43, 57.22] | 95.35 [94.96, 95.73] | 85.64 [84.02, 87.36] | 1.001 | 1.00 | 0.93 | 0.58 |
| meta-llama-3-1-8b-instruct | 5 | 32.23 [25.77, 39.17] | 57.35 [52.03, 65.61] | 50.00 [48.99, 51.43] | 95.67 [94.66, 96.67] | 85.66 [82.67, 88.66] | 0.947 | 1.00 | 0.93 | 0.58 |
| google-translate | 5 | 16.99 [10.04, 23.38] | 45.90 [43.07, 48.58] | 70.71 [64.12, 77.78] | 93.08 [92.20, 94.31] | 81.79 [77.40, 85.02] | 1.059 | 1.00 | 0.93 | 0.53 |

## Overall leaderboard

| Model | Langs | BLEU | σ(lang) | CHRF | σ(lang) | TER | σ(lang) | BERTScore-F1 | σ(lang) | COMET | σ(lang) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gpt-5-2 | 7 | 36.47 | 15.18 | 55.98 | 12.60 | 51.69 | 16.47 | 95.08 | 1.63 | 83.62 | 3.97 |
| gemini-3-pro | 7 | 36.25 | 10.78 | 56.27 | 9.01 | 52.31 | 12.14 | 94.90 | 1.29 | 84.80 | 2.32 |
| deepl | 7 | 34.79 | 14.29 | 54.67 | 11.19 | 53.17 | 14.94 | 94.66 | 1.62 | 83.33 | 3.35 |
| gpt-4 | 7 | 29.39 | 13.83 | 51.18 | 11.84 | 57.83 | 15.78 | 94.31 | 1.71 | 82.93 | 3.27 |
| meta-llama-3-1-405b-instruct | 7 | 27.16 | 14.52 | 49.56 | 12.06 | 58.67 | 16.32 | 94.35 | 1.84 | 82.03 | 3.66 |
| google-translate | 7 | 27.75 | 9.09 | 49.65 | 8.77 | 60.43 | 11.92 | 93.72 | 1.15 | 83.18 | 3.20 |
| azure-translator | 7 | 26.86 | 10.99 | 48.83 | 10.06 | 60.31 | 12.98 | 94.00 | 1.69 | 80.12 | 3.24 |
| llama-3-3-70b-instruct | 7 | 26.54 | 14.92 | 48.28 | 12.97 | 61.33 | 18.19 | 93.96 | 2.06 | 81.75 | 4.52 |
| meta-llama-3-1-8b-instruct | 7 | 20.48 | 14.04 | 42.60 | 12.99 | 69.31 | 20.93 | 93.15 | 2.21 | 77.60 | 5.75 |

*Overall scores are macro-averages across languages (each language weighted equally). σ(lang) is the per-language standard deviation: smaller means more consistent across languages.*


## Metric agreement and disagreement

- Correlation heatmap: `plots/metric_correlation_heatmap.png`
- Metric scatter plot: `plots/metric_scatter.png`

### Correlations (paragraph-level)

Pearson (TER shown as -TER):

| index | bleu | chrf | bertscore_f1 | comet | -ter |
|---|---|---|---|---|---|
| bleu | 1.000 | 0.938 | 0.862 | 0.519 | 0.921 |
| chrf | 0.938 | 1.000 | 0.920 | 0.656 | 0.910 |
| bertscore_f1 | 0.862 | 0.920 | 1.000 | 0.644 | 0.876 |
| comet | 0.519 | 0.656 | 0.644 | 1.000 | 0.492 |
| -ter | 0.921 | 0.910 | 0.876 | 0.492 | 1.000 |

Spearman (rank correlation):

| index | bleu | chrf | bertscore_f1 | comet | -ter |
|---|---|---|---|---|---|
| bleu | 1.000 | 0.945 | 0.872 | 0.480 | 0.939 |
| chrf | 0.945 | 1.000 | 0.912 | 0.574 | 0.935 |
| bertscore_f1 | 0.872 | 0.912 | 1.000 | 0.552 | 0.894 |
| comet | 0.480 | 0.574 | 0.552 | 1.000 | 0.455 |
| -ter | 0.939 | 0.935 | 0.894 | 0.455 | 1.000 |

### Lexical vs semantic disagreement examples

**Lexical metrics high, semantic metric low (possible meaning drift / shallow matching)**

- **spanish / gemini-3-pro / unit 0** (LEX=62.8, BERTScore=94.9; BLEU=57.2, chrF=68.4, TER=32.4)
  - MT: `Hemos recibido información del *Uitvoeringsinstituut Werknemersverzekeringen* (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta leerá lo que esto significa para usted.`
  - REF: `Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.`
- **spanish / gpt-4 / unit 0** (LEX=59.2, BERTScore=94.6; BLEU=49.7, chrF=68.8, TER=44.1)
  - MT: `Hemos recibido información del Instituto de Seguros para Empleados (UWV, por sus siglas en neerlandés). La información del UWV se refiere a su incapacidad laboral. En esta carta, usted leerá lo que esto significa para usted.`
  - REF: `Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.`
- **turkish / meta-llama-3-1-8b-instruct / unit 1** (LEX=22.4, BERTScore=90.0; BLEU=6.8, chrF=38.1, TER=151.4)
  - MT: `Sizin için ne anlama geliyor? Sizin için 'premievrije pensioen' (prensip olarak prim ödemesi olmayan emeklilik) inşa ediyoruz. Bu, sizin iş göremezlik durumunuzdan ve UWV tarafından size verilecek WAO/WIA (Aile ve Sosyal Hizmetler Bakanlığına bağlı işsizlik yardımı) ödeneğinden d…`
  - REF: `Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız. Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak adlandırılmaktadır. Ödediğimiz katkı p…`
- **english / google-translate / unit 4** (LEX=51.3, BERTScore=93.7; BLEU=39.1, chrF=63.5, TER=43.6)
  - MT: `You must report any changes to your disability yourself. If you receive a new letter from the Employee Insurance Agency (UWV), you must send us a copy of that letter. The portion of the premium we pay will then change.`
  - REF: `You must personally report any changes in your disability Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.`
- **english / deepl / unit 3** (LEX=62.4, BERTScore=95.4; BLEU=53.2, chrF=71.7, TER=35.6)
  - MT: `What does this mean for your PVD? In the column ‘Premium-free pension accrual’, you will see a percentage (%). This is the portion for which you receive PVD. We pay this portion of the pension premium. If your ‘benefit percentage’ changes, the percentage of ‘premium-free pension …`
  - REF: `What does this mean for your PVD? The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage…`
- **german / google-translate / unit 0** (LEX=30.4, BERTScore=91.8; BLEU=16.9, chrF=43.9, TER=68.0)
  - MT: `Wir haben Informationen von der britischen Arbeitsagentur (UWV) erhalten. Diese Informationen betreffen Ihre Behinderung. Dieses Schreiben erläutert Ihnen die Bedeutung dieser Informationen.`
  - REF: `Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das für Sie bedeutet.`
- **spanish / google-translate / unit 3** (LEX=51.2, BERTScore=94.2; BLEU=41.2, chrF=61.2, TER=39.4)
  - MT: `¿Qué significa esto para su PVD? En la columna "Acumulación de pensión no contributiva", verá un porcentaje (%). Esta es la parte de la prima de pensión que recibirá. Nosotros pagamos esta parte de la prima de pensión. ¿Cambiará su porcentaje de beneficio? El porcentaje de acumul…`
  - REF: `¿Qué significa esto para su PVD? En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también ca…`
- **polish / gpt-4 / unit 1** (LEX=34.3, BERTScore=90.8; BLEU=22.3, chrF=46.2, TER=84.0)
  - MT: `Naliczane jest Państwu 'premiovrij pensioen' (emerytura bez składek) Dzieje się tak, ponieważ są Państwo niezdolni do pracy. Oraz dlatego, że otrzymują Państwo świadczenie WAO/WIA od UWV. Dlatego my opłacamy (część) Państwa składki emerytalnej. Nazywamy to 'premievrije deelname (…`
  - REF: `Gromadzi Pan/Pani u nas emeryturę bezskładkową. Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się t…`

**Semantic metric high, lexical metrics low (possible good paraphrase vs reference)**

- **spanish / google-translate / unit 2** (LEX=43.9, BERTScore=97.9; BLEU=29.3, chrF=58.6, TER=45.5)
  - MT: `Su PVD ha cambiado. Recibe una prestación de WAO/WIA. La UWV nos ha proporcionado nueva información sobre su prestación de WAO/WIA. El resumen a continuación explica qué significa esto para usted.`
  - REF: `Su PVD ha cambiado Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.`
- **spanish / meta-llama-3-1-8b-instruct / unit 2** (LEX=50.3, BERTScore=97.7; BLEU=38.3, chrF=62.3, TER=42.4)
  - MT: `Su PVD ha cambiado U tiene una prestación de la WAO/WIA. El UWV nos ha proporcionado nueva información sobre su prestación de la WAO/WIA. A continuación, puede leer qué significa esto para usted.`
  - REF: `Su PVD ha cambiado Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.`
- **german / gemini-3-pro / unit 4** (LEX=41.0, BERTScore=96.6; BLEU=23.7, chrF=58.4, TER=55.9)
  - MT: `Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst mitteilen Erhalten Sie ein neues Schreiben vom UWV? Dann müssen Sie uns eine Kopie dieses Schreibens senden. Der Teil des Beitrags, den wir zahlen, ändert sich dann.`
  - REF: `Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken. Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.`
- **arabic / meta-llama-3-1-405b-instruct / unit 0** (LEX=20.6, BERTScore=93.0; BLEU=8.4, chrF=32.9, TER=74.2)
  - MT: `لقد تلقينا معلومات من معهد تنفيذ تأمين العمال (UWV). تتعلق المعلومات من UWV بإعاقة عملك. في هذه الرسالة، ستقرأ ما يعني ذلك لك.`
  - REF: `تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.`
- **german / deepl / unit 4** (LEX=40.0, BERTScore=96.3; BLEU=24.6, chrF=55.4, TER=52.9)
  - MT: `Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden Erhalten Sie ein neues Schreiben vom UWV? Dann müssen Sie uns eine Kopie dieses Schreibens zusenden. Der Teil der Prämie, den wir bezahlen, ändert sich dann.`
  - REF: `Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken. Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.`
- **arabic / gpt-4 / unit 0** (LEX=26.4, BERTScore=94.0; BLEU=10.6, chrF=42.2, TER=71.0)
  - MT: `لقد تلقينا معلومات من معهد تنفيذ تأمينات العمال (UWV). تتعلق المعلومات التي وردت من UWV بعجزكم عن العمل. في هذه الرسالة، ستقرأون ما يعنيه ذلك بالنسبة لكم.`
  - REF: `تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.`
- **german / gpt-5-2 / unit 4** (LEX=45.5, BERTScore=96.9; BLEU=27.9, chrF=63.2, TER=50.0)
  - MT: `Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden Erhalten Sie ein neues Schreiben vom UWV? Dann müssen Sie uns eine Kopie dieses Schreibens schicken. Der Teil des Beitrags, den wir zahlen, ändert sich dann.`
  - REF: `Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken. Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.`
- **polish / gpt-4 / unit 4** (LEX=25.1, BERTScore=93.4; BLEU=10.3, chrF=39.9, TER=77.4)
  - MT: `Muszą Państwo sami zgłaszać zmiany w swojej niezdolności do pracy Jeśli otrzymają Państwo nowy list od UWV, muszą Państwo przesłać nam kopię tego pisma. Wtedy zmieni się część składki, którą opłacamy.`
  - REF: `Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy. Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.`

## Outlier paragraphs per model and language

For each (model, language), we list the **worst segments** by a primary metric (BERTScore if available, else chrF, else BLEU). These are good starting points for manual inspection.

### turkish

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=91.90; BLEU=6.58, chrF=31.15, TER=78.57; len_ratio=0.751, num_f1=1.00, acr_f1=1.00, punct_pres=0.43)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
İş göremezliğinizdeki değişiklikleri kendiniz bildirmelisiniz
UWV'den yeni bir mektup aldınız mı? O zaman bize bu mektubun bir kopyasını göndermelisiniz. Primin ödediğimiz kısmı daha sonra değişecektir.
```
- **Unit 3** (bertscore_f1=93.34; BLEU=18.36, chrF=44.06, TER=79.55; len_ratio=0.901, num_f1=1.00, acr_f1=1.00, punct_pres=0.31)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu, PVD'niz için ne anlama geliyor?
'Primsiz emeklilik tahakkuku' sütununda bir yüzde (%) göreceksiniz. Bu, PVD'yi aldığınız kısımdır. Emeklilik katkı payının bu kısmını ödüyoruz. 'Ödeme alma yüzdeniz' değişiyor mu? O zaman 'primsiz emekli maaşı tahakkuku' yüzdesi de değişecek. Ve bu nedenle emeklilik priminin ödediğimiz kısmı.
```
- **Unit 1** (bertscore_f1=93.57; BLEU=16.96, chrF=43.42, TER=75.68; len_ratio=0.907, num_f1=1.00, acr_f1=1.00, punct_pres=0.37)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizde 'primsiz emeklilik' tahakkuk ettirirsiniz
Bunun nedeni, iş için yetersiz olmanızdır. Ve UWV'den bir WAO/WIA ödeneği aldığınız için. Bu nedenle emeklilik katkı payınızın (bir kısmını) ödüyoruz. Biz buna 'katkısız katılım (PVD)' diyoruz. Ödediğimiz prim miktarı 'ödeme yüzdenize' bağlıdır.
```
- **Unit 2** (bertscore_f1=95.20; BLEU=34.96, chrF=53.34, TER=52.17; len_ratio=0.891, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD'niz değişti
WAO/WIA avantajınız var. UWV bize WAO/WIA avantajınız hakkında yeni bilgiler sağladı. Aşağıdaki genel bakışta bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
- **Unit 0** (bertscore_f1=96.61; BLEU=61.05, chrF=65.32, TER=33.33; len_ratio=0.835, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi aldık. UWV'den gelen bilgiler, iş göremezliğinizle ilgilidir. Bu mektupta bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=90.80; BLEU=6.41, chrF=28.56, TER=82.14; len_ratio=0.740, num_f1=1.00, acr_f1=1.00, punct_pres=0.43)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
Çalışma yeteneğinizdeki değişiklikleri kendiniz bildirmelisiniz
UWV'den yeni bir mektup mu aldınız? O zaman bu mektubun bir kopyasını bize göndermelisiniz. Ödediklerimiz primin kısmı da değişecektir.
```
- **Unit 3** (bertscore_f1=94.94; BLEU=23.44, chrF=48.89, TER=70.45; len_ratio=0.973, num_f1=1.00, acr_f1=1.00, punct_pres=0.69)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu, PVD'niz için ne anlama geliyor?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) görürsünüz. Bu, PVD aldığınız kısımdır. Emeklilik priminin bu kısmını biz öderiz. “Ödeme yüzdesinde” değişiklik mi oldu? O zaman “primsiz emeklilik birikimi” yüzdesinde de değişiklik olur. Dolayısıyla, emeklilik priminin bizim ödediğimiz kısmında da değişiklik olur.
```
- **Unit 0** (bertscore_f1=96.06; BLEU=49.49, chrF=62.61, TER=45.83; len_ratio=0.915, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Çalışan Sigortaları Uygulama Kurumu'ndan (UWV) bilgi aldık. UWV'den gelen bilgi, iş göremezlik durumunuzla ilgilidir. Bu mektupta bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
- **Unit 1** (bertscore_f1=96.13; BLEU=46.33, chrF=56.76, TER=54.05; len_ratio=0.867, num_f1=1.00, acr_f1=1.00, punct_pres=0.47)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizde ‘primsiz emeklilik’ biriktiriyorsunuz.
Bunun nedeni, iş göremez durumda olmanız ve UWV'den WAO/WIA ödeneği almanızdır. Bu nedenle, emeklilik priminizin (bir kısmını) biz ödüyoruz. Buna ‘primsiz katılım (PVD)’ diyoruz. Ödediğimiz prim tutarı, ‘ödemenizin yüzdesine’ bağlıdır.
```
- **Unit 2** (bertscore_f1=96.52; BLEU=45.91, chrF=59.53, TER=34.78; len_ratio=0.851, num_f1=1.00, acr_f1=1.00, punct_pres=0.89)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD'niz değişti
WAO/WIA ödeneği alıyorsunuz. UWV, WAO/WIA ödeneğinizle ilgili yeni bilgiler verdi. Aşağıdaki özetinde bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=93.84; BLEU=18.17, chrF=46.75, TER=77.27; len_ratio=0.992, num_f1=1.00, acr_f1=1.00, punct_pres=0.31)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu, PVD'niz için ne anlama geliyor?
‘Primsiz emeklilik birikimi’ sütununda bir yüzde (%) göreceksiniz. Bu, üzerinden PVD (primsiz katılım) aldığınız kısımdır. Emeklilik priminin bu kısmını biz ödüyoruz. ‘Ödenek yüzdeniz’ değişti mi? O halde ‘primsiz emeklilik birikimi’ yüzdesi de değişir. Dolayısıyla, emeklilik priminin bizim ödediğimiz kısmı da değişmiş olur.
```
- **Unit 4** (bertscore_f1=93.93; BLEU=13.30, chrF=41.93, TER=57.14; len_ratio=0.777, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
İş göremezlik durumunuzdaki değişiklikleri kendiniz bildirmelisiniz
UWV'den yeni bir mektup alırsanız, bu mektubun bir kopyasını bize göndermeniz gerekmektedir. Bu durumda ödediğimiz prim miktarı değişecektir.
```
- **Unit 1** (bertscore_f1=95.11; BLEU=31.36, chrF=50.65, TER=64.86; len_ratio=0.938, num_f1=1.00, acr_f1=1.00, punct_pres=0.32)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizde ‘primsiz emeklilik’ hakkı kazanıyorsunuz
Bunun nedeni iş göremez durumda olmanız ve UWV'den bir WAO/WIA ödeneği almanızdır. Bu sebeple emeklilik priminizin (bir kısmını) biz ödüyoruz. Buna ‘primsiz katılım (PVD)’ adını veriyoruz. Bizim ödediğimiz primin miktarı, sizin ‘ödenek yüzdenize’ bağlıdır.
```
- **Unit 2** (bertscore_f1=95.26; BLEU=44.18, chrF=56.96, TER=47.83; len_ratio=0.940, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD durumunuz değişti
Bir WAO/WIA ödeneğiniz bulunmaktadır. UWV, WAO/WIA ödeneğiniz hakkında bize yeni bilgiler iletti. Aşağıdaki özette bunun sizin için ne anlama geldiğini görebilirsiniz.
```
- **Unit 0** (bertscore_f1=95.51; BLEU=44.85, chrF=58.91, TER=50.00; len_ratio=0.915, num_f1=1.00, acr_f1=1.00, punct_pres=0.89)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Çalışan Sigortaları Kurumu'ndan (UWV) bilgi aldık. UWV'den gelen bu bilgi, iş göremezlik durumunuzla ilgilidir. Bu mektupta, bu durumun sizin için ne anlama geldiğini okuyabilirsiniz.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=91.39; BLEU=4.13, chrF=26.98, TER=89.29; len_ratio=0.866, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
Engelliliğinizdeki herhangi bir değişikliği kendiniz bildirmelisiniz.
Çalışan Sigorta Kurumu'ndan (UWV) yeni bir mektup alırsanız, bu mektubun bir kopyasını bize göndermelisiniz. Ödediğimiz primin bir kısmı da buna göre değişecektir.
```
- **Unit 3** (bertscore_f1=93.86; BLEU=19.09, chrF=47.63, TER=77.27; len_ratio=0.992, num_f1=1.00, acr_f1=1.00, punct_pres=0.62)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu, PVD'niz için ne anlama geliyor?
"Katkı payı ödemeden emeklilik birikimi" sütununda bir yüzde (%) göreceksiniz. Bu, alacağınız emeklilik priminin oranıdır. Emeklilik priminin bu kısmını biz ödüyoruz. Yardım yüzdesi değişecek mi? Prim ödemeden emeklilik birikimi yüzdesi de değişecektir. Bu aynı zamanda ödediğimiz emeklilik priminin bir kısmını da ifade eder.
```
- **Unit 0** (bertscore_f1=94.61; BLEU=46.28, chrF=52.71, TER=45.83; len_ratio=0.810, num_f1=1.00, acr_f1=1.00, punct_pres=0.89)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
İşveren Sigorta Kurumu'ndan (UWV) bilgi aldık. UWV'den gelen bu bilgi, engelliliğinizle ilgilidir. Bu mektup, bunun sizin için ne anlama geldiğini açıklamaktadır.
```
- **Unit 1** (bertscore_f1=95.98; BLEU=47.70, chrF=61.12, TER=51.35; len_ratio=0.895, num_f1=1.00, acr_f1=1.00, punct_pres=0.74)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizimle katkı payı ödemeden emeklilik hakkı biriktiriyorsunuz.
Bunun nedeni engelli olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu nedenle, emeklilik priminizin (bir kısmını) biz ödüyoruz. Buna katkı payı ödemeden katılım (PVD) denir. Ödediğimiz prim miktarı, yardım yüzdesine bağlıdır.
```
- **Unit 2** (bertscore_f1=96.39; BLEU=43.06, chrF=58.35, TER=43.48; len_ratio=0.896, num_f1=1.00, acr_f1=1.00, punct_pres=0.89)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD'niz değişti.
WAO/WIA yardımı alıyorsunuz. UWV, WAO/WIA yardımınız hakkında bize yeni bilgiler verdi. Aşağıdaki genel bakış, bunun sizin için ne anlama geldiğini açıklamaktadır.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 0** (bertscore_f1=93.15; BLEU=27.53, chrF=44.20, TER=58.33; len_ratio=1.005, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Uitvoeringsinstituut Werknemersverzekeringen (UWV) tarafından bilgi aldık. UWV'den alınan bilgiler, sizin iş göremezliğinizle ilgilidir. Bu mektupta, bunun sizin için ne anlama geldiğini okuyacaksınız.
```
- **Unit 4** (bertscore_f1=93.85; BLEU=12.52, chrF=37.11, TER=67.86; len_ratio=0.755, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
İş göremezlik durumunuzdaki değişiklikleri bize kendiniz bildirmelisiniz
UWV'den yeni bir mektup aldığınızda, o mektubun bir kopyasını bize göndermelisiniz. Bizim ödediğimiz prim miktarı o zaman değişir.
```
- **Unit 1** (bertscore_f1=94.38; BLEU=25.32, chrF=42.87, TER=72.97; len_ratio=0.950, num_f1=1.00, acr_f1=1.00, punct_pres=0.47)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizde ‘prim ödemesiz emeklilik’ biriktiriyorsunuz
Bu, iş göremez olmanızdan kaynaklanıyor. Ve UWV'den WAO/WIA ödeneği alıyorsunuz. Bu yüzden biz, emeklilik priminizin (bir kısmını) ödüyoruz. Buna ‘prim ödemesiz katılım (PVD)’ diyoruz. Bizim ödediğimiz prim miktarı, ‘ödenek yüzdenizin’ büyüklüğüne bağlıdır.
```
- **Unit 3** (bertscore_f1=94.43; BLEU=19.69, chrF=44.97, TER=75.00; len_ratio=0.904, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
PVD'niz için bu ne anlama geliyor?
‘Prim ödemesiz emeklilik birikimi’ sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısmı ifade eder. Bu kısım için emeklilik primini biz ödüyoruz. ‘Ödenek yüzdeniz’ değişirse, ‘prim ödemesiz emeklilik birikimi’ yüzdesi de değişir. Ve dolayısıyla bizim ödediğimiz prim miktarı da değişir.
```
- **Unit 2** (bertscore_f1=95.73; BLEU=37.93, chrF=50.77, TER=43.48; len_ratio=0.856, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD'niz değişti
Bir WAO/WIA ödeneği alıyorsunuz. UWV, WAO/WIA ödeneğinizle ilgili bize yeni bilgiler verdi. Aşağıdaki özet, bunun sizin için ne anlama geldiğini gösteriyor.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=93.03; BLEU=3.83, chrF=29.57, TER=78.57; len_ratio=0.747, num_f1=1.00, acr_f1=1.00, punct_pres=0.43)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
Çalışma göremezliğinizdeki değişiklikleri kendiniz bildirmeniz gerekir  
UWV’den yeni bir mektup alırsanız, o mektubun bir kopyasını bize göndermeniz gerekir. Bizim ödediğimiz prim kısmı o zaman değişir.
```
- **Unit 1** (bertscore_f1=94.39; BLEU=21.28, chrF=47.65, TER=75.68; len_ratio=0.975, num_f1=1.00, acr_f1=1.00, punct_pres=0.32)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizde ‘prim ödemesiz emeklilik’ biriktiriyorsunuz  
Bunun nedeni, çalışma göremez durumda olmanızdır. Ayrıca UWV’den bir WAO/WIA ödeneği aldığınız için. Bu nedenle emeklilik priminizin (bir kısmını) biz ödüyoruz. Buna ‘prim ödemesiz katılım (PVD)’ diyoruz. Bizim ödediğimiz primin tutarı, ‘ödenek oranınıza’ bağlıdır.
```
- **Unit 3** (bertscore_f1=94.55; BLEU=10.49, chrF=41.74, TER=75.00; len_ratio=0.901, num_f1=1.00, acr_f1=1.00, punct_pres=0.38)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu, PVD’niz için ne anlama geliyor?  
‘Prim ödemesiz emeklilik birikimi’ sütununda bir yüzde (%) görürsünüz. Bu, PVD aldığınız kısmı gösterir. Emeklilik priminin bu kısmını biz öderiz. ‘Ödenek oranınız’ değişirse, ‘prim ödemesiz emeklilik birikimi’ yüzdesi de değişir. Dolayısıyla bizim ödediğimiz emeklilik primi kısmı da değişir.
```
- **Unit 2** (bertscore_f1=95.65; BLEU=40.23, chrF=51.03, TER=47.83; len_ratio=0.876, num_f1=1.00, acr_f1=1.00, punct_pres=0.67)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD’niz değişti  
Bir WAO/WIA ödeneği alıyorsunuz. UWV, WAO/WIA ödeneğiniz hakkında bize yeni bilgi verdi. Aşağıdaki tabloda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
- **Unit 0** (bertscore_f1=96.09; BLEU=36.38, chrF=56.89, TER=54.17; len_ratio=0.910, num_f1=1.00, acr_f1=1.00, punct_pres=0.56)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Çalışan Sigortaları Uygulama Kurumu’ndan (UWV) bilgi aldık. UWV’den gelen bilgi, çalışma göremezliğinizle ilgilidir. Bu mektupta bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 0** (bertscore_f1=91.54; BLEU=16.31, chrF=41.89, TER=87.50; len_ratio=1.060, num_f1=1.00, acr_f1=1.00, punct_pres=0.67)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Uygun Uygulama Enstitüsü Çalışan Sigortaları (UWV) tarafında alınan bilgilerimize göre, sizin iş göremezlik durumunuz hakkında bilgi aldık. Bu mektup size bu durumun sizin için ne anlama geldiğini açıklamaktadır.
```
- **Unit 1** (bertscore_f1=93.36; BLEU=23.27, chrF=43.00, TER=86.49; len_ratio=0.988, num_f1=1.00, acr_f1=1.00, punct_pres=0.42)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Siz bizimle 'prim ödenmeyen emeklilik' biriktiriyorsunuz
Bu, sizin iş göremez olmanız ve UWV'den WAO/WIA ödenneği almanız nedeniyle oluşmaktadır. Bu nedenle, biz (primin bir kısmını) sizin adınıza ödüyoruz. Buna 'prim ödenmeyen katılım (PVD)' diyoruz. Ödediğimiz prim tutarının yüksekliği, 'ödenek yüzdesi' ne bağlıdır.
```
- **Unit 4** (bertscore_f1=93.62; BLEU=8.83, chrF=37.81, TER=75.00; len_ratio=0.766, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
Sizin iş göremezlik durumunuzdaki değişiklikleri kendiniz bildirmelisiniz
UWV'den yeni bir mektup alırsanız, bize o mektubun bir kopyasını göndermelisiniz. Biz tarafından ödenen prim tutarı da değişecektir.
```
- **Unit 3** (bertscore_f1=93.67; BLEU=8.20, chrF=41.79, TER=81.82; len_ratio=1.003, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu, sizin PVD'niz için ne anlama geliyor?
'Prim ödenmeyen emeklilik biriktirme' sütununda bir yüzde (%) görüyorsunuz. Bu, sizin PVD alacağınız tutarın oranıdır. Bu emeklilik priminin bir kısmı biz tarafından ödenmektedir. 'Ödenek yüzdesi' değişirse, 'prim ödenmeyen emeklilik biriktirme' yüzdesi de değişir ve biz tarafından ödenen emeklilik primi tutarı da değişir.
```
- **Unit 2** (bertscore_f1=95.02; BLEU=22.84, chrF=47.98, TER=65.22; len_ratio=0.980, num_f1=1.00, acr_f1=1.00, punct_pres=0.89)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Sizin PVD'niz değişti
Siz WAO/WIA ödenneği alıyorsunuz. UWV, sizin WAO/WIA ödenneğin hakkında bize yeni bilgiler verdi. Aşağıdaki özet size bu durumun sizin için ne anlama geldiğini açıklamaktadır.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=92.32; BLEU=6.41, chrF=28.65, TER=78.57; len_ratio=0.717, num_f1=1.00, acr_f1=1.00, punct_pres=0.43)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
İş göremezliğinizdeki değişiklikleri kendiniz bildirmelisiniz
UWV'den yeni bir mektup alıyor musunuz? O zaman bize o mektubun bir kopyasını göndermelisiniz. Bizim ödediğimiz prim kısmı değişir.
```
- **Unit 1** (bertscore_f1=93.99; BLEU=15.77, chrF=40.02, TER=83.78; len_ratio=0.926, num_f1=1.00, acr_f1=1.00, punct_pres=0.32)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Bizimle 'prim ödemesiz emeklilik' biriktiriyorsunuz
Bu, iş göremez olduğunuz için ve UWV'den bir WAO/WIA ödeneği aldığınız için oluyor. Bu nedenle biz (emeklilik priminizin bir kısmını) ödüyoruz. Buna 'prim ödemesiz katılım (PVD)' diyoruz. Ödediğimiz primin yüksekliği 'ödenek yüzdesi'nize bağlıdır.
```
- **Unit 0** (bertscore_f1=94.52; BLEU=26.95, chrF=45.70, TER=66.67; len_ratio=0.920, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Biz, Çalışan Sigortaları Uygulama Enstitüsü'nden (UWV) bilgi aldık. UWV'nin bilgisi sizin iş göremezliğiniz hakkındadır. Bu mektupta bunun sizin için ne anlama geldiğini okuyacaksınız.
```
- **Unit 3** (bertscore_f1=94.89; BLEU=13.80, chrF=42.24, TER=72.73; len_ratio=0.871, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
PVD'niz için ne anlama geliyor?
'Prim ödemesiz emeklilik birikimi' sütununda bir yüzde (%) görüyorsunuz. Bu, PVD aldığınız kısım. Bu emeklilik primi kısmını biz ödüyoruz. 'Ödenek yüzdesi'niz değişirse, 'prim ödemesiz emeklilik birikimi' yüzdesi de değişir. Ve böylece bizim ödediğimiz emeklilik primi kısmı da değişir.
```
- **Unit 2** (bertscore_f1=95.34; BLEU=26.82, chrF=47.20, TER=56.52; len_ratio=0.831, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
PVD'niz değişti
Bir WAO/WIA ödeneğiniz var. UWV bize WAO/WIA ödeneğiniz hakkında yeni bilgi verdi. Aşağıdaki özetde bunun sizin için ne anlama geldiğini okuyacaksınız.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 0** (bertscore_f1=89.89; BLEU=4.77, chrF=23.81, TER=91.67; len_ratio=0.875, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
Çalışan Sigorta Kurumu'ndan (UWV) bilgi almış bulunmaktayız. UWV'den gelen bilgiler, çalışamayacak
durumda olduğunuza işaret etmektedir. Bu yazıda bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Biz, Uitvoeringsinstituut Werknemersverzekeringen (UWV) tarafından aldığımız bilgiye dayanarak, bu mektubun içinde sizin iş göremezlik durumunuz hakkında bilgi yer almaktadır.
```
- **Unit 1** (bertscore_f1=90.05; BLEU=6.81, chrF=38.05, TER=151.35; len_ratio=1.582, num_f1=1.00, acr_f1=1.00, punct_pres=0.26)
  - REF:
```
Bizimle birlikte “primsiz emeklilik” birikimi yapmaktasınız.
Bunun nedeni, çalışamayacak durumda olmanız ve UWV'den WAO/WIA yardımı almanızdır. Bu
nedenle, emeklilik priminizin (bir kısmını) biz ödemekteyiz. Bu “primsiz katılım (PVD)” olarak
adlandırılmaktadır.
Ödediğimiz katkı payının miktarı, yardım yüzdesine bağlıdır.
```
  - MT:
```
Sizin için ne anlama geliyor?
Sizin için 'premievrije pensioen' (prensip olarak prim ödemesi olmayan emeklilik) inşa ediyoruz. Bu, sizin iş göremezlik durumunuzdan ve UWV tarafından size verilecek WAO/WIA (Aile ve Sosyal Hizmetler Bakanlığına bağlı işsizlik yardımı) ödeneğinden dolayıdır. Bu nedenle, biz sizin emeklilik priminizin bir kısmını ödüyoruz. Bu durum 'premievrije deelname (PVD)' olarak adlandırılır. Biz ödediğimiz primin tutarı, sizin 'uitkeringspercentage' (ödenen primin yüzdesi) ile ilgilidir.
```
- **Unit 3** (bertscore_f1=90.49; BLEU=5.28, chrF=24.45, TER=93.18; len_ratio=0.833, num_f1=1.00, acr_f1=1.00, punct_pres=0.12)
  - REF:
```
Bunun PVD'niz için anlamı nedir?
“Primsiz emeklilik birikimi” sütununda bir yüzde (%) göreceksiniz. Bu, PVD aldığınız kısımdır. Biz
emeklilik katkısının bu kadarlık bir kısmını ödemekteyiz.
Yardım yüzdesinde değişiklik olursa, primsiz emeklilik birikiminin yüzdesi de değişecektir. Sonuç
olarak, tarafımızdan ödenen emeklilik katkısının miktarı da değişecektir.
```
  - MT:
```
Bu ne anlama geliyor sizin için PVD?
'Premievrije pensioenopbouw' sütununda bir yüzde (%) yer alır. Bu, sizin PVD alacağınız bölümü gösterir. Biz bu bölümü ödüyoruz. 'Uitkeringspercentage' değişti mi? O zaman 'premievrije pensioenopbouw' yüzde değişti mi? Ve biz ödediğimiz emeklilik priminin değişti mi?
```
- **Unit 4** (bertscore_f1=91.50; BLEU=6.32, chrF=28.33, TER=92.86; len_ratio=0.788, num_f1=1.00, acr_f1=1.00, punct_pres=0.29)
  - REF:
```
İş göremezlik durumunuzdaki değişiklikleri bildirmekle yükümlüsünüz.
UWV'den tarafınıza yeni bir yazı gönderilmesi durumunda, bu yazının bir kopyasını tarafımıza
göndermeniz gerekecektir. Sonrasında, tarafımızca ödenecek katkı miktarı uygun şekilde
ayarlanacaktır.
```
  - MT:
```
Sizin iş göremezlik durumunuz değişti mi? O zaman bunu bizlere bildirmelisiniz
UWV'den yeni bir mektup aldığınız zaman, bize o mektubun bir kopyasını göndermelisiniz. Biz ödediğimiz emeklilik priminin değişti mi?
```
- **Unit 2** (bertscore_f1=93.97; BLEU=13.08, chrF=36.88, TER=73.91; len_ratio=0.801, num_f1=1.00, acr_f1=1.00, punct_pres=0.56)
  - REF:
```
PVD'niz değişmiş bulunmaktadır.
WAO/WIA yardımı almaktasınız. UWV, WAO/WIA tarafımıza yardımınızla ilgili yeni bilgiler sunmuştur.
Aşağıdaki özette bunun sizin için ne anlama geldiğini okuyabilirsiniz.
```
  - MT:
```
Sizin PVD değişti
Sizin WAO/WIA-ödeneği var. UWV, sizin WAO/WIA-ödeneği hakkında yeni bilgi verdi. Aşağıdaki tabloyu okuyarak ne anlama geldiğini görebilirsiniz.
```
</details>

### spanish

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=94.59; BLEU=33.64, chrF=55.78, TER=45.07; len_ratio=0.933, num_f1=1.00, acr_f1=1.00, punct_pres=0.20)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna 'Devengo de pensiones no contributivas' verás un porcentaje (%). Esta es la parte en la que se obtiene PVD. Pagamos esta parte de la cotización a la pensión. ¿Va a cambiar tu "porcentaje de pago"? A continuación, también cambiará el porcentaje de "devengo de pensiones no contributivas". Y, por tanto, también la parte de la cotización previsional que pagamos.
```
- **Unit 1** (bertscore_f1=95.93; BLEU=40.92, chrF=59.74, TER=43.33; len_ratio=0.938, num_f1=1.00, acr_f1=1.00, punct_pres=0.18)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Acumulas una "pensión no contributiva" con nosotros
Esto se debe a que está incapacitado para trabajar. Y porque recibes un beneficio de WAO/WIA de la UWV. Es por eso que pagamos (parte de) su contribución a la pensión. A esto lo llamamos 'participación no contributiva (PVD)'. El monto de la prima que pagamos depende de su "porcentaje de pago".
```
- **Unit 4** (bertscore_f1=96.80; BLEU=48.05, chrF=69.01, TER=37.14; len_ratio=0.972, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Debe informar usted mismo de cualquier cambio en su incapacidad para trabajar
¿Ha recibido una nueva carta de la UWV? Entonces debe enviarnos una copia de esa carta. La parte de la prima que pagamos cambiará.
```
- **Unit 0** (bertscore_f1=96.82; BLEU=48.35, chrF=68.29, TER=35.29; len_ratio=0.927, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información de la Agencia de Seguros de Empleados (UWV). La información de la UWV se refiere a su incapacidad laboral. En esta carta puedes leer lo que esto significa para ti.
```
- **Unit 2** (bertscore_f1=98.10; BLEU=54.78, chrF=66.12, TER=33.33; len_ratio=0.990, num_f1=1.00, acr_f1=1.00, punct_pres=0.86)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
Usted tiene un beneficio de WAO/WIA. El UWV nos ha proporcionado nueva información sobre su beneficio de WAO/WIA. En el siguiente resumen puedes leer lo que esto significa para ti.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=97.04; BLEU=49.25, chrF=71.37, TER=34.29; len_ratio=0.930, num_f1=1.00, acr_f1=1.00, punct_pres=0.75)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Debe comunicar usted mismo los cambios en su incapacidad laboral
¿Ha recibido una nueva carta del UWV? En ese caso, debe enviarnos una copia de dicha carta. La parte de la prima que pagamos cambiará.
```
- **Unit 0** (bertscore_f1=97.13; BLEU=68.00, chrF=76.09, TER=23.53; len_ratio=0.961, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del Instituto Ejecutivo de Seguros Laborales (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
- **Unit 3** (bertscore_f1=97.16; BLEU=54.19, chrF=69.68, TER=21.13; len_ratio=0.911, num_f1=1.00, acr_f1=1.00, punct_pres=0.15)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna «Acumulación de pensión libre de primas» verá un porcentaje (%). Esta es la parte sobre la que recibe PVD. Nosotros pagamos esta parte de la prima de pensión. ¿Cambia su «porcentaje de prestación»? Entonces también cambia el porcentaje de «acumulación de pensión libre de primas». Y, por lo tanto, también la parte de la prima de pensión que pagamos.
```
- **Unit 1** (bertscore_f1=97.51; BLEU=54.43, chrF=66.83, TER=26.67; len_ratio=0.927, num_f1=1.00, acr_f1=1.00, punct_pres=0.18)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Usted acumula una «pensión libre de primas» con nosotros
Esto se debe a que está incapacitado para trabajar. Y a que recibe una prestación WAO/WIA del UWV. Por eso pagamos (una parte de) su prima de pensión. A esto lo llamamos «participación libre de primas (PVD)». El importe de la prima que pagamos depende de su «porcentaje de prestación».
```
- **Unit 2** (bertscore_f1=98.13; BLEU=71.99, chrF=84.02, TER=24.24; len_ratio=1.060, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado.
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información sobre su prestación WAO/WIA. En el resumen que figura a continuación puede leer lo que esto significa para usted.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 0** (bertscore_f1=94.89; BLEU=57.23, chrF=68.42, TER=32.35; len_ratio=0.966, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del *Uitvoeringsinstituut Werknemersverzekeringen* (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta leerá lo que esto significa para usted.
```
- **Unit 4** (bertscore_f1=96.17; BLEU=32.14, chrF=62.48, TER=45.71; len_ratio=0.986, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Usted mismo debe comunicar los cambios en su incapacidad laboral
¿Ha recibido una nueva carta del UWV? Entonces debe enviarnos una copia de dicha carta, ya que la parte de la prima que nosotros pagamos cambiará.
```
- **Unit 1** (bertscore_f1=96.43; BLEU=42.60, chrF=59.42, TER=38.33; len_ratio=0.986, num_f1=1.00, acr_f1=1.00, punct_pres=0.24)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Usted acumula una ‘pensión libre de primas’ con nosotros
Esto se debe a que usted tiene una incapacidad laboral. Y a que percibe una prestación WAO/WIA del UWV. Por esta razón, nosotros pagamos (una parte de) su prima de pensión. A esto lo llamamos ‘participación libre de primas (PVD)’. El importe de la prima que pagamos depende de su ‘porcentaje de prestación’.
```
- **Unit 3** (bertscore_f1=96.71; BLEU=46.92, chrF=66.71, TER=29.58; len_ratio=0.968, num_f1=1.00, acr_f1=1.00, punct_pres=0.20)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna ‘Acumulación de pensión libre de primas’ verá un porcentaje (%). Esta es la parte sobre la cual usted recibe la PVD. Nosotros pagamos esta parte de la prima de pensión. ¿Cambia su ‘porcentaje de prestación’? En ese caso, también cambiará el porcentaje de ‘acumulación de pensión libre de primas’. Y, por lo tanto, también la parte de la prima de pensión que nosotros pagamos.
```
- **Unit 2** (bertscore_f1=99.16; BLEU=78.44, chrF=86.83, TER=21.21; len_ratio=1.065, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información sobre su prestación WAO/WIA. En el resumen que aparece a continuación, puede leer lo que esto significa para usted.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=93.81; BLEU=22.52, chrF=50.01, TER=56.67; len_ratio=0.870, num_f1=1.00, acr_f1=1.00, punct_pres=0.59)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Está acumulando una pensión no contributiva con nosotros.
Esto se debe a su discapacidad y a que recibe una prestación de WAO/WIA de la UWV. Por lo tanto, pagamos (parte de) su prima de pensión. Esto se denomina participación no contributiva (PVD). El monto de la prima que pagamos depende del porcentaje de su beneficio.
```
- **Unit 3** (bertscore_f1=94.20; BLEU=41.23, chrF=61.20, TER=39.44; len_ratio=0.906, num_f1=1.00, acr_f1=1.00, punct_pres=0.30)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna "Acumulación de pensión no contributiva", verá un porcentaje (%). Esta es la parte de la prima de pensión que recibirá. Nosotros pagamos esta parte de la prima de pensión. ¿Cambiará su porcentaje de beneficio? El porcentaje de acumulación de pensión sin prima también cambiará. Esto también se refiere a la parte de la prima de pensión que pagamos.
```
- **Unit 4** (bertscore_f1=94.84; BLEU=31.34, chrF=60.44, TER=54.29; len_ratio=1.037, num_f1=1.00, acr_f1=1.00, punct_pres=0.25)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Debe informar usted mismo sobre cualquier cambio en su discapacidad.
Si recibe una nueva carta de la Agencia de Seguros para Empleados (UWV), debe enviarnos una copia. La parte de la prima que pagamos cambiará en ese caso.
```
- **Unit 0** (bertscore_f1=95.16; BLEU=28.62, chrF=55.30, TER=50.00; len_ratio=0.878, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información de la Agencia de Seguros para Empleados (UWV). Esta información de la UWV se refiere a su discapacidad. Esta carta explica qué significa esto para usted.
```
- **Unit 2** (bertscore_f1=97.85; BLEU=29.25, chrF=58.64, TER=45.45; len_ratio=0.975, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado.
Recibe una prestación de WAO/WIA. La UWV nos ha proporcionado nueva información sobre su prestación de WAO/WIA. El resumen a continuación explica qué significa esto para usted.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 0** (bertscore_f1=94.58; BLEU=49.66, chrF=68.79, TER=44.12; len_ratio=1.093, num_f1=1.00, acr_f1=1.00, punct_pres=0.67)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del Instituto de Seguros para Empleados (UWV, por sus siglas en neerlandés). La información del UWV se refiere a su incapacidad laboral. En esta carta, usted leerá lo que esto significa para usted.
```
- **Unit 4** (bertscore_f1=96.31; BLEU=49.71, chrF=62.24, TER=42.86; len_ratio=0.935, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Usted debe informarnos por su cuenta los cambios en su incapacidad laboral
Si recibe una nueva carta del UWV, debe enviarnos una copia de esa carta. Entonces cambiará la parte de la prima que pagamos.
```
- **Unit 1** (bertscore_f1=96.68; BLEU=45.67, chrF=63.10, TER=38.33; len_ratio=1.014, num_f1=1.00, acr_f1=1.00, punct_pres=0.24)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Usted acumula 'pensión sin aportación de primas' con nosotros
Esto se debe a que usted está incapacitado para trabajar. Y porque recibe una prestación WAO/WIA del UWV. Por eso, nosotros pagamos (una parte de) su prima de pensión. A esto lo llamamos 'participación sin aportación de primas (PVD)'. La cantidad de la prima que pagamos depende de su 'porcentaje de prestación'.
```
- **Unit 3** (bertscore_f1=96.77; BLEU=45.16, chrF=66.82, TER=30.99; len_ratio=0.963, num_f1=1.00, acr_f1=1.00, punct_pres=0.15)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna 'Acumulación de pensión sin aportación de primas', verá un porcentaje (%). Esa es la parte sobre la cual usted recibe PVD. Nosotros pagamos esa parte de la prima de pensión. ¿Cambia su 'porcentaje de prestación'? Entonces también cambia el porcentaje de 'acumulación de pensión sin aportación de primas'. Y por lo tanto, también la parte de la prima de pensión que pagamos.
```
- **Unit 2** (bertscore_f1=99.24; BLEU=75.95, chrF=83.44, TER=15.15; len_ratio=1.000, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha proporcionado nueva información sobre su prestación WAO/WIA. En el siguiente resumen, usted leerá lo que esto significa para usted.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=95.96; BLEU=47.42, chrF=65.39, TER=40.00; len_ratio=0.958, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Usted debe comunicar por su cuenta los cambios en su incapacidad laboral
¿Recibe una nueva carta del UWV? Entonces debe enviarnos una copia de esa carta. La parte de la prima que pagamos cambiará entonces.
```
- **Unit 1** (bertscore_f1=96.85; BLEU=51.35, chrF=68.97, TER=30.00; len_ratio=0.954, num_f1=1.00, acr_f1=1.00, punct_pres=0.18)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Usted acumula con nosotros una ‘pensión exenta de prima’
Esto se debe a que está incapacitado para trabajar. Y porque recibe una prestación WAO/WIA del UWV. Por eso nosotros pagamos (una parte de) su prima de pensión. A esto lo llamamos ‘participación exenta de prima (PVD)’. El importe de la prima que pagamos depende de su ‘porcentaje de prestación’.
```
- **Unit 3** (bertscore_f1=96.99; BLEU=48.30, chrF=69.11, TER=23.94; len_ratio=0.927, num_f1=1.00, acr_f1=1.00, punct_pres=0.15)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna ‘Acumulación de pensión exenta de prima’ verá un porcentaje (%). Este es la parte por la que usted recibe PVD. Nosotros pagamos esa parte de la prima de pensión. ¿Cambia su ‘porcentaje de prestación’? Entonces también cambia el porcentaje de ‘acumulación de pensión exenta de prima’. Y, por tanto, también cambia la parte de la prima de pensión que pagamos.
```
- **Unit 0** (bertscore_f1=97.18; BLEU=69.75, chrF=77.68, TER=17.65; len_ratio=0.961, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del Instituto de Seguros de los Trabajadores (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
- **Unit 2** (bertscore_f1=98.69; BLEU=67.03, chrF=76.53, TER=30.30; len_ratio=1.070, num_f1=1.00, acr_f1=1.00, punct_pres=0.86)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha proporcionado nueva información sobre su prestación WAO/WIA. En el resumen que aparece a continuación podrá ver lo que esto significa para usted.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=95.91; BLEU=42.01, chrF=57.98, TER=45.00; len_ratio=0.913, num_f1=1.00, acr_f1=1.00, punct_pres=0.24)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Usted acumula 'pensión sin prima' con nosotros
Esto se debe a que usted es incapaz de trabajar. Y porque recibe una prestación WAO/WIA del UWV. Por lo tanto, nosotros pagamos (una parte de) su prima de pensión. A esto lo llamamos 'participación sin prima (PVD)'. El monto de la prima que pagamos depende de su 'porcentaje de prestación'.
```
- **Unit 4** (bertscore_f1=96.20; BLEU=51.13, chrF=63.14, TER=37.14; len_ratio=0.911, num_f1=1.00, acr_f1=1.00, punct_pres=0.75)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Usted debe notificarnos los cambios en su incapacidad laboral
¿Recibe una nueva carta del UWV? Entonces, debe enviarnos una copia de esa carta. La parte de la prima que pagamos cambiará entonces.
```
- **Unit 3** (bertscore_f1=96.21; BLEU=40.78, chrF=62.29, TER=36.62; len_ratio=0.901, num_f1=1.00, acr_f1=1.00, punct_pres=0.20)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna 'Acumulación de pensión sin prima' verá un porcentaje (%) indicado. Esto es la parte por la que recibe PVD. Esta parte de la prima de pensión la pagamos nosotros. ¿Cambia su 'porcentaje de prestación'? Entonces, también cambia el porcentaje 'acumulación de pensión sin prima'. Y, por lo tanto, también la parte de la prima de pensión que pagamos.
```
- **Unit 0** (bertscore_f1=96.90; BLEU=63.92, chrF=76.30, TER=23.53; len_ratio=0.995, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del Instituto de Ejecución de Seguros de Empleados (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta, podrá leer lo que esto significa para usted.
```
- **Unit 2** (bertscore_f1=99.48; BLEU=78.50, chrF=85.34, TER=12.12; len_ratio=0.995, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha proporcionado nueva información sobre su prestación WAO/WIA. En el siguiente resumen, podrá leer lo que esto significa para usted.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 4** (bertscore_f1=96.18; BLEU=48.29, chrF=62.19, TER=37.14; len_ratio=0.893, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Usted debe notificar los cambios en su incapacidad laboral
¿Recibe una nueva carta del UWV? Entonces debe enviarnos una copia de esa carta. La parte de la prima que pagamos cambiará entonces.
```
- **Unit 0** (bertscore_f1=96.49; BLEU=48.35, chrF=66.29, TER=38.24; len_ratio=0.956, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del Instituto de Ejecución de Seguros de Empleados (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta, leerá qué significa esto para usted.
```
- **Unit 3** (bertscore_f1=96.53; BLEU=50.03, chrF=67.01, TER=28.17; len_ratio=0.940, num_f1=1.00, acr_f1=1.00, punct_pres=0.10)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna "Acumulación de pensión libre de prima" verá un porcentaje (%). Esta es la parte sobre la que usted recibe PVD. Esta parte de la prima de pensión la pagamos nosotros. ¿Cambia su "porcentaje de prestación"? Entonces también cambia el porcentaje de "acumulación de pensión libre de prima". Y por lo tanto, también cambia la parte de la prima de pensión que pagamos.
```
- **Unit 1** (bertscore_f1=96.85; BLEU=43.34, chrF=61.69, TER=38.33; len_ratio=0.981, num_f1=1.00, acr_f1=1.00, punct_pres=0.24)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
Usted acumula una "pensión libre de prima" con nosotros
Esto se debe a que usted está incapacitado para trabajar. Y porque recibe una prestación WAO/WIA del UWV. Por lo tanto, nosotros pagamos (una parte de) su prima de pensión. A esto lo llamamos "participación libre de prima (PVD)". La cuantía de la prima que pagamos depende de su "porcentaje de prestación".
```
- **Unit 2** (bertscore_f1=99.02; BLEU=59.89, chrF=71.46, TER=30.30; len_ratio=0.980, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha proporcionado nueva información sobre su prestación WAO/WIA. En el resumen a continuación, leerá qué significa esto para usted.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=94.78; BLEU=36.49, chrF=56.86, TER=43.66; len_ratio=0.929, num_f1=1.00, acr_f1=1.00, punct_pres=0.25)
  - REF:
```
¿Qué significa esto para su PVD?
En la columna “Acumulación de pensión exenta de contribuciones”, verá un porcentaje (%). Esta es la parte sobre la que recibe su PVD. Nosotros pagamos esta parte de la contribución de su pensión. Si su “porcentaje de prestación” cambia, también cambia el porcentaje de “acumulación de pensión exenta de contribuciones”, y, por lo tanto, también cambia la parte de la contribución de pensión que pagamos.
```
  - MT:
```
¿Qué significa esto para su PVD?
En la columna 'Construcción de pensión sin prima' ve un porcentaje (%) que aparece. Esto es el porcentaje sobre el que recibe PVD. Este porcentaje de la prima de pensión la pagamos nosotros. Si su 'porcentaje de prestación' cambia, también cambia el porcentaje de 'construcción de pensión sin prima'. Y, por lo tanto, también el porcentaje de prima de pensión que pagamos.
```
- **Unit 4** (bertscore_f1=95.43; BLEU=38.28, chrF=54.75, TER=42.86; len_ratio=0.879, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Debe comunicar usted mismo cualquier cambio en su incapacidad laboral
Si ha recibido una nueva carta del UWV, debe enviarnos una copia de esa carta. La parte de la contribución que pagamos cambiará en consecuencia.
```
  - MT:
```
Usted debe informar sobre los cambios en su incapacidad laboral
Si recibe una nueva carta del UWV, debe enviarle una copia de esa carta. El porcentaje de prima que pagamos cambia entonces.
```
- **Unit 1** (bertscore_f1=95.54; BLEU=44.89, chrF=59.94, TER=41.67; len_ratio=0.902, num_f1=1.00, acr_f1=1.00, punct_pres=0.24)
  - REF:
```
Usted recibe una “pensión exenta de contribuciones” con nosotros
Esto se debe a que está incapacitado para trabajar y a que recibe una prestación WAO/WIA del UWV. Por eso, pagamos (una parte de) su contribución a la pensión. A esto lo llamamos “pensión exenta de contribuciones (PVD)”. El importe de la contribución que pagamos depende de su “porcentaje de prestación”.
```
  - MT:
```
U está construyendo 'pensión sin prima' con nosotros
Esto se debe a que está incapacitado para trabajar. Y porque recibe una prestación de la WAO/WIA del UWV. Por eso, pagamos (una parte de) su prima de pensión. Esto se llama 'participación sin prima (PVD)'. El monto de la prima que pagamos depende de su 'porcentaje de prestación'.
```
- **Unit 0** (bertscore_f1=96.31; BLEU=48.35, chrF=65.98, TER=38.24; len_ratio=0.985, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
Hemos recibido información del Servicio Público de Empleo de los Países Bajos (UWV). Esta información del UWV se refiere a su incapacidad laboral. En esta carta podrá leer lo que esto significa para usted.
```
  - MT:
```
Hemos recibido información del Instituto de Ejecución de Seguros de Empleados (UWV). La información del UWV se refiere a su incapacidad laboral. En esta carta, usted leerá qué significa esto para usted.
```
- **Unit 2** (bertscore_f1=97.71; BLEU=38.26, chrF=62.28, TER=42.42; len_ratio=0.970, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Su PVD ha cambiado
Usted recibe una prestación WAO/WIA. El UWV nos ha facilitado nueva información acerca de su prestación WAO/WIA. En el siguiente resumen, puede leer lo que esto significa para usted.
```
  - MT:
```
Su PVD ha cambiado
U tiene una prestación de la WAO/WIA. El UWV nos ha proporcionado nueva información sobre su prestación de la WAO/WIA. A continuación, puede leer qué significa esto para usted.
```
</details>

### english

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=93.19; BLEU=27.04, chrF=42.94, TER=54.00; len_ratio=0.599, num_f1=1.00, acr_f1=0.80, punct_pres=0.83)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You receive a WAO/WIA benefit. The UWV has provided us with new information about your WAO/WIA benefit. In the overview below, you can read what this means for you.
```
- **Unit 1** (bertscore_f1=94.91; BLEU=22.22, chrF=50.29, TER=59.09; len_ratio=0.817, num_f1=1.00, acr_f1=0.80, punct_pres=0.26)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are accruing 'premium-free pension' with us
This is because you are incapacitated for work and because you receive a WAO/WIA benefit from the UWV. Therefore, we pay (a part of) your pension contribution. This is called 'premium-free participation (PVD)'. The amount of the contribution we pay depends on your 'benefit percentage'.
```
- **Unit 3** (bertscore_f1=95.74; BLEU=44.49, chrF=65.81, TER=44.07; len_ratio=1.063, num_f1=1.00, acr_f1=1.00, punct_pres=0.17)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?  
In the column 'Premium-free pension accrual' you will see a percentage (%). This is the portion for which you receive PVD. We pay this part of the pension contribution. If your 'benefit percentage' changes, the percentage of 'premium-free pension accrual' also changes. And therefore the portion of the pension contribution that we pay will change as well.
```
- **Unit 4** (bertscore_f1=96.21; BLEU=45.88, chrF=64.11, TER=38.46; len_ratio=0.985, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report changes in your disability yourself  
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The portion of the contribution that we pay will then change.
```
- **Unit 0** (bertscore_f1=96.66; BLEU=47.68, chrF=65.85, TER=34.38; len_ratio=0.926, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your incapacity for work. In this letter, you can read what this means for you.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=93.07; BLEU=24.79, chrF=40.19, TER=60.00; len_ratio=0.573, num_f1=1.00, acr_f1=0.80, punct_pres=1.00)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You receive a WAO/WIA benefit. The UWV has provided us with new information about your WAO/WIA benefit. The overview below explains what this means for you.
```
- **Unit 1** (bertscore_f1=95.27; BLEU=46.02, chrF=60.50, TER=43.94; len_ratio=0.817, num_f1=1.00, acr_f1=0.80, punct_pres=1.00)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are accruing a ‘premium-free pension’ with us.
This is because you are incapacitated for work and because you receive a WAO/WIA benefit from the UWV. That is why we pay (part of) your pension contribution. We call this ‘premium-free participation (PVD)’. The amount of the contribution we pay depends on your ‘benefit percentage’.
```
- **Unit 3** (bertscore_f1=95.42; BLEU=53.17, chrF=71.68, TER=35.59; len_ratio=0.997, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the column ‘Premium-free pension accrual’, you will see a percentage (%). This is the portion for which you receive PVD. We pay this portion of the pension premium. If your ‘benefit percentage’ changes, the percentage of ‘premium-free pension accrual’ will also change. And so will the portion of the pension premium that we pay.
```
- **Unit 4** (bertscore_f1=95.42; BLEU=48.41, chrF=64.73, TER=41.03; len_ratio=1.000, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report any changes in your incapacity for work yourself
If you receive a new letter from the UWV, you must send us a copy of that letter. The portion of the premium that we pay will then change.
```
- **Unit 0** (bertscore_f1=96.01; BLEU=45.45, chrF=62.16, TER=37.50; len_ratio=0.887, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your incapacity for work. This letter explains what this means for you.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=92.93; BLEU=27.96, chrF=44.05, TER=58.00; len_ratio=0.586, num_f1=1.00, acr_f1=0.80, punct_pres=1.00)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You receive a WAO/WIA benefit. The UWV has provided us with new information regarding your WAO/WIA benefit. The overview below explains what this means for you.
```
- **Unit 3** (bertscore_f1=95.73; BLEU=49.97, chrF=74.16, TER=35.59; len_ratio=1.101, num_f1=1.00, acr_f1=1.00, punct_pres=0.61)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the column ‘Premium-free pension accrual’ (*Premievrije pensioenopbouw*), you will see a percentage (%). This is the portion for which you receive PVD. We pay this part of the pension premium. If your ‘benefit percentage’ changes, the ‘premium-free pension accrual’ percentage changes as well. And consequently, so does the portion of the pension premium that we pay.
```
- **Unit 1** (bertscore_f1=95.80; BLEU=50.65, chrF=61.87, TER=45.45; len_ratio=0.790, num_f1=1.00, acr_f1=0.80, punct_pres=0.95)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are accruing a ‘premium-free pension’ with us
This is because you are incapacitated for work. And because you receive a WAO/WIA benefit from the UWV. Therefore, we pay (part of) your pension premium. We call this ‘premium-free participation (PVD)’. The amount of the premium we pay depends on your ‘benefit percentage’.
```
- **Unit 4** (bertscore_f1=95.86; BLEU=45.85, chrF=62.30, TER=43.59; len_ratio=1.005, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report changes in your incapacity for work yourself
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The portion of the premium that we pay will then change.
```
- **Unit 0** (bertscore_f1=96.01; BLEU=45.45, chrF=62.16, TER=37.50; len_ratio=0.887, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your incapacity for work. This letter explains what this means for you.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=92.65; BLEU=22.77, chrF=39.48, TER=62.00; len_ratio=0.576, num_f1=1.00, acr_f1=0.80, punct_pres=0.83)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed.
You receive a WAO/WIA benefit. The UWV has provided us with new information about your WAO/WIA benefit. The overview below explains what this means for you.
```
- **Unit 1** (bertscore_f1=93.50; BLEU=23.33, chrF=49.05, TER=59.09; len_ratio=0.768, num_f1=1.00, acr_f1=0.80, punct_pres=0.58)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are accruing a non-contributory pension with us.
This is because you are disabled. And because you receive a WAO/WIA benefit from the UWV. Therefore, we pay (part of) your pension premium. This is called non-contributory participation (PVD). The amount of the premium we pay depends on your benefit percentage.
```
- **Unit 4** (bertscore_f1=93.72; BLEU=39.06, chrF=63.51, TER=43.59; len_ratio=1.074, num_f1=1.00, acr_f1=1.00, punct_pres=0.20)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report any changes to your disability yourself.
If you receive a new letter from the Employee Insurance Agency (UWV), you must send us a copy of that letter. The portion of the premium we pay will then change.
```
- **Unit 3** (bertscore_f1=94.14; BLEU=40.45, chrF=61.03, TER=55.93; len_ratio=1.035, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the "Non-contributory pension accrual" column, you will see a percentage (%). This is the portion of the pension premium you will receive. We pay this portion of the pension premium. Will your benefit percentage change? The percentage of premium-free pension accrual will also change. This also means the portion of the pension premium we pay.
```
- **Unit 0** (bertscore_f1=96.89; BLEU=38.80, chrF=64.81, TER=37.50; len_ratio=0.847, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). This information from the UWV concerns your disability. This letter explains what this means for you.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=92.98; BLEU=25.97, chrF=45.94, TER=54.00; len_ratio=0.589, num_f1=1.00, acr_f1=0.80, punct_pres=0.67)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You are receiving a WAO/WIA benefit. The UWV has provided us with new information about your benefit. In the summary below, you can read what this means for you.
```
- **Unit 1** (bertscore_f1=93.76; BLEU=31.43, chrF=49.30, TER=56.06; len_ratio=0.834, num_f1=1.00, acr_f1=0.80, punct_pres=0.95)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are building up a ‘non-contributory pension’ with us
This is because you are occupationally disabled and are receiving a WAO/WIA benefit from the UWV. That is why we pay (part of) your pension contribution. This is called ‘non-contributory participation’ (PVD). The amount of the contribution we pay depends on your ‘benefit percentage’.
```
- **Unit 3** (bertscore_f1=94.63; BLEU=43.39, chrF=62.72, TER=42.37; len_ratio=1.049, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the column ‘Non-contributory pension accrual’, you will see a percentage (%). This is the portion over which you receive PVD. We pay this part of the pension contribution. If your ‘benefit percentage’ changes, then the percentage of ‘non-contributory pension accrual’ also changes. And therefore also the portion of the pension contribution we pay.
```
- **Unit 4** (bertscore_f1=96.18; BLEU=48.41, chrF=65.49, TER=38.46; len_ratio=1.069, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report any changes in your occupational disability yourself
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The portion of the contribution that we pay will then change.
```
- **Unit 0** (bertscore_f1=96.71; BLEU=51.37, chrF=68.95, TER=34.38; len_ratio=0.906, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your occupational disability. This letter explains what that means for you.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=93.39; BLEU=30.15, chrF=45.05, TER=52.00; len_ratio=0.595, num_f1=1.00, acr_f1=0.80, punct_pres=1.00)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You receive a WAO/WIA benefit. The UWV has provided us with new information about your WAO/WIA benefit. In the overview below you can read what that means for you.
```
- **Unit 4** (bertscore_f1=95.66; BLEU=43.28, chrF=58.70, TER=46.15; len_ratio=0.990, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report changes in your incapacity for work yourself
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The part of the premium that we pay will then change.
```
- **Unit 1** (bertscore_f1=95.98; BLEU=54.19, chrF=64.45, TER=40.91; len_ratio=0.792, num_f1=1.00, acr_f1=0.80, punct_pres=1.00)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are accruing a ‘premium-free pension’ with us
This is because you are incapacitated for work. And because you receive a WAO/WIA benefit from the UWV. That is why we pay (part of) your pension premium. We call this ‘premium-free participation (PVD)’. The amount of the premium we pay depends on your ‘benefit percentage’.
```
- **Unit 3** (bertscore_f1=96.33; BLEU=48.80, chrF=68.89, TER=37.29; len_ratio=0.973, num_f1=1.00, acr_f1=1.00, punct_pres=0.94)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the column ‘Premium-free pension accrual’ you will see a percentage (%). This is the part for which you receive PVD. We pay this part of the pension premium. Does your ‘benefit percentage’ change? Then the ‘premium-free pension accrual’ percentage also changes. And therefore the part of the pension premium that we pay.
```
- **Unit 0** (bertscore_f1=96.61; BLEU=47.72, chrF=66.00, TER=31.25; len_ratio=0.921, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your incapacity for work. In this letter you can read what this means for you.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=92.93; BLEU=25.20, chrF=40.60, TER=56.00; len_ratio=0.589, num_f1=1.00, acr_f1=0.80, punct_pres=0.83)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You have a WAO/WIA benefit. The UWV has provided us with new information about your WAO/WIA benefit. In the overview below, you can read what this means for you.
```
- **Unit 1** (bertscore_f1=95.17; BLEU=32.02, chrF=53.87, TER=54.55; len_ratio=0.795, num_f1=1.00, acr_f1=0.80, punct_pres=0.32)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are building up 'premium-free pension' with us
This is because you are occupationally disabled. And because you receive a WAO/WIA benefit from the UWV. That's why we pay (part of) your pension premium. We call this 'premium-free participation (PVD)'. The amount of the premium we pay depends on your 'benefit percentage'.
```
- **Unit 3** (bertscore_f1=95.62; BLEU=38.89, chrF=62.00, TER=50.85; len_ratio=1.005, num_f1=1.00, acr_f1=1.00, punct_pres=0.22)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the 'Premium-free pension accrual' column, you will see a percentage (%) listed. This is the part for which you receive PVD. We pay this part of the pension premium. If your 'benefit percentage' changes? Then the percentage 'premium-free pension accrual' also changes. And therefore also the part of the pension premium that we pay.
```
- **Unit 4** (bertscore_f1=96.31; BLEU=43.67, chrF=62.55, TER=41.03; len_ratio=1.010, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report changes in your occupational disability yourself
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The part of the premium that we pay will then change.
```
- **Unit 0** (bertscore_f1=97.36; BLEU=48.76, chrF=70.24, TER=28.12; len_ratio=0.946, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your occupational disability. In this letter, you can read what this means for you.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=93.19; BLEU=27.04, chrF=42.94, TER=54.00; len_ratio=0.599, num_f1=1.00, acr_f1=0.80, punct_pres=0.83)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You receive a WAO/WIA benefit. The UWV has provided us with new information about your WAO/WIA benefit. In the overview below, you can read what this means for you.
```
- **Unit 1** (bertscore_f1=94.86; BLEU=31.13, chrF=52.99, TER=56.06; len_ratio=0.795, num_f1=1.00, acr_f1=0.80, punct_pres=0.32)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are building up 'premium-free pension' with us
This is because you are occupationally disabled. And because you receive a WAO/WIA benefit from the UWV. Therefore, we pay (part of) your pension premium. We call this 'premium-free participation (PVD)'. The amount of the premium we pay depends on your 'benefit percentage'.
```
- **Unit 3** (bertscore_f1=95.74; BLEU=38.35, chrF=61.92, TER=52.54; len_ratio=1.022, num_f1=1.00, acr_f1=1.00, punct_pres=0.17)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the 'Premium-free pension accrual' column, you will see a percentage (%). This is the part for which you receive PVD. We pay this part of the pension premium. Does your 'benefit percentage' change? Then the percentage of 'premium-free pension accrual' also changes. And therefore, the part of the pension premium that we pay also changes.
```
- **Unit 4** (bertscore_f1=96.31; BLEU=43.67, chrF=62.55, TER=41.03; len_ratio=1.010, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report changes in your occupational disability yourself
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The part of the premium that we pay will then change.
```
- **Unit 0** (bertscore_f1=97.36; BLEU=48.76, chrF=70.24, TER=28.12; len_ratio=0.946, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employee Insurance Agency (UWV). The information from the UWV concerns your occupational disability. In this letter, you can read what this means for you.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=92.47; BLEU=15.75, chrF=33.03, TER=62.00; len_ratio=0.566, num_f1=1.00, acr_f1=0.80, punct_pres=0.83)
  - REF:
```
Your PVD has changed
You receive benefits under the Disability Insurance/Work and Income Capacity for Work Act. The UWV has provided us with new information regarding your benefits under the Disability Insurance/Work and Income Capacity for Work Act. You can read in the summary below what that means for you.
```
  - MT:
```
Your PVD has changed
You have a WAO/WIA benefit. The UWV has given us new information about your WAO/WIA benefit. In the overview below, you will read what this means for you.
```
- **Unit 1** (bertscore_f1=95.28; BLEU=37.25, chrF=57.54, TER=46.97; len_ratio=0.785, num_f1=1.00, acr_f1=0.80, punct_pres=0.37)
  - REF:
```
You are accruing a ‘premium-free pension’ with us
This is because of your disability. And because you are receiving benefits from the UWV under the Disability Insurance/Work and Income Capacity for Work Act. That is why we are paying (a portion of) your pension premium. We call this ‘pension-free participation scheme (PVD)’. The amount of the premium that we are paying depends on your ‘benefit percentage’.
```
  - MT:
```
You are building 'premium-free pension' with us
This is because you are work disabled. And because you are receiving a WAO/WIA benefit from the UWV. That is why we pay (a part of) your pension premium. We call this 'premium-free participation (PVD)'. The amount of the premium we pay depends on your 'benefit percentage'.
```
- **Unit 3** (bertscore_f1=95.68; BLEU=34.03, chrF=59.67, TER=52.54; len_ratio=0.997, num_f1=1.00, acr_f1=1.00, punct_pres=0.17)
  - REF:
```
What does this mean for your PVD?
The column ‘Premievrije pensioenopbouw’ shows a percentage (%). This is the portion for which you receive PVD. We are paying this portion of the pension premium. Has your ‘benefit percentage’ changed? The ‘premium-free pension accrual’ percentage will change as well. And therefore also the portion of the pension premium paid by us.
```
  - MT:
```
What does this mean for your PVD?
In the column 'Premium-free pension build-up' you see a percentage (%) listed. This is the part for which you receive PVD. This part of the pension premium we pay. Does your 'benefit percentage' change? Then the percentage 'premium-free pension build-up' also changes. And therefore also the part of the pension premium that we pay.
```
- **Unit 4** (bertscore_f1=96.38; BLEU=43.67, chrF=61.71, TER=41.03; len_ratio=0.970, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
You must personally report any changes in your disability
Did you receive a new letter from the UWV? Please send us a copy of that letter. In that case, the portion of the premium paid by us will change.
```
  - MT:
```
You must report changes in your work disability yourself
Do you receive a new letter from the UWV? Then you must send us a copy of that letter. The part of the premium that we pay will then change.
```
- **Unit 0** (bertscore_f1=96.98; BLEU=47.72, chrF=67.58, TER=37.50; len_ratio=0.916, num_f1=1.00, acr_f1=1.00, punct_pres=0.83)
  - REF:
```
We have received information from the Employed Persons Insurance Administration Agency (UWV). The information from the UWV relates to your disability. You can read in this letter what that means for you.
```
  - MT:
```
We have received information from the Employees Insurance Agency (UWV). The information from the UWV concerns your work disability. In this letter, you will read what this means for you.
```
</details>

### polish

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=91.43; BLEU=12.69, chrF=39.27, TER=74.00; len_ratio=0.801, num_f1=1.00, acr_f1=1.00, punct_pres=0.30)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
U nas nabywasz "emeryturę nieskładkową"
Dzieje się tak, ponieważ jesteś niezdolny do pracy. A także dlatego, że otrzymujesz zasiłek WAO/WIA od UWV. Dlatego płacimy (część) składki emerytalnej. Nazywamy to "partycypacją nieskładkową (PVD)". Wysokość składki, którą płacimy, zależy od Twojego "procentu wypłaty".
```
- **Unit 2** (bertscore_f1=91.92; BLEU=13.64, chrF=31.92, TER=82.76; len_ratio=0.831, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Twoja powłoka PVD uległa zmianie
Masz prawo do zasiłku WAO/WIA. UWV dostarczyło nam nowych informacji na temat korzyści WAO/WIA. W poniższym przeglądzie możesz przeczytać, co to oznacza dla Ciebie.
```
- **Unit 4** (bertscore_f1=92.77; BLEU=7.46, chrF=41.07, TER=74.19; len_ratio=0.835, num_f1=1.00, acr_f1=1.00, punct_pres=0.27)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Wszelkie zmiany dotyczące niezdolności do pracy musisz zgłaszać samodzielnie
Czy otrzymałeś nowy list z UWV? Następnie musisz przesłać nam kopię tego listu. Zmieni się wtedy część składki, którą płacimy.
```
- **Unit 3** (bertscore_f1=92.86; BLEU=26.25, chrF=50.66, TER=57.41; len_ratio=0.873, num_f1=1.00, acr_f1=1.00, punct_pres=0.26)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Twojej powłoki PVD?
W kolumnie "Nieskładkowe naliczanie emerytury" zobaczysz wartość procentową (%). Jest to część, na której otrzymujesz PVD. Płacimy tę część składki emerytalnej. Czy zmienia się Twój "procent wypłaty"? Wtedy zmieni się również procent "nieskładkowego naliczania emerytury". A więc także część składki emerytalnej, którą płacimy.
```
- **Unit 0** (bertscore_f1=95.19; BLEU=34.35, chrF=58.14, TER=52.17; len_ratio=0.984, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informację z Agencji Ubezpieczeń Pracowniczych (UWV). Informacje z UWV dotyczą Twojej niezdolności do pracy. W tym liście możesz przeczytać, co to oznacza dla Ciebie.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=93.23; BLEU=30.37, chrF=55.35, TER=56.00; len_ratio=0.796, num_f1=1.00, acr_f1=1.00, punct_pres=0.52)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Gromadzisz u nas „emeryturę bezskładkową”.
Wynika to z faktu, że jesteś niezdolny do pracy. Otrzymujesz również zasiłek WAO/WIA od UWV. Dlatego opłacamy (część) Twojej składki emerytalnej. Nazywamy to „udziałem bezskładkowym (PVD)”. Wysokość składki, którą opłacamy, zależy od Państwa „procentu świadczenia”.
```
- **Unit 3** (bertscore_f1=93.86; BLEU=42.85, chrF=60.60, TER=55.56; len_ratio=0.955, num_f1=1.00, acr_f1=1.00, punct_pres=0.53)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Państwa PVD?
W kolumnie „Bezskładkowe gromadzenie emerytury” widnieje wartość procentowa (%). Jest to część, od której otrzymujesz PVD. Tę część składki emerytalnej opłacamy my. Czy zmienia się Twój „procent świadczenia”? W takim przypadku zmienia się również wartość procentowa „bezskładkowego gromadzenia emerytury”. A tym samym również część składki emerytalnej, którą opłacamy.
```
- **Unit 2** (bertscore_f1=93.93; BLEU=23.37, chrF=49.71, TER=65.52; len_ratio=0.911, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Państwa PVD uległo zmianie.
Otrzymują Państwo świadczenie WAO/WIA. UWV przekazało nam nowe informacje dotyczące Państwa świadczenia WAO/WIA. W poniższym zestawieniu mogą Państwo przeczytać, co to dla Państwa oznacza.
```
- **Unit 4** (bertscore_f1=94.30; BLEU=33.18, chrF=56.80, TER=54.84; len_ratio=0.885, num_f1=1.00, acr_f1=1.00, punct_pres=0.36)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Musisz samodzielnie zgłaszać zmiany dotyczące Twojej niezdolności do pracy
Otrzymałeś nowy list od UWV? W takim przypadku musisz przesłać nam kopię tego listu. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
- **Unit 0** (bertscore_f1=96.50; BLEU=41.94, chrF=71.83, TER=39.13; len_ratio=1.016, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje od Instytutu Ubezpieczeń Pracowniczych (UWV). Informacje od UWV dotyczą Państwa niezdolności do pracy. W niniejszym piśmie wyjaśniono, co to oznacza dla Państwa.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=92.31; BLEU=28.92, chrF=53.32, TER=60.00; len_ratio=0.897, num_f1=1.00, acr_f1=1.00, punct_pres=0.52)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Gromadzą Państwo u nas „emeryturę bezskładkową”
Wynika to z faktu, że są Państwo niezdolni do pracy i otrzymują świadczenie WAO/WIA z UWV. Dlatego to my opłacamy (część) Państwa składki emerytalnej. Nazywamy to „uczestnictwem bezskładkowym (PVD)”. Wysokość składki, którą opłacamy, zależy od Państwa „wskaźnika świadczenia” (uitkeringspercentage).
```
- **Unit 2** (bertscore_f1=92.77; BLEU=17.86, chrF=44.16, TER=65.52; len_ratio=0.852, num_f1=1.00, acr_f1=1.00, punct_pres=0.43)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Państwa PVD uległo zmianie
Pobierają Państwo świadczenie WAO/WIA. UWV przekazał nam nowe informacje dotyczące tego świadczenia. W poniższym zestawieniu mogą Państwo sprawdzić, co to dla Państwa oznacza.
```
- **Unit 3** (bertscore_f1=93.28; BLEU=37.14, chrF=56.08, TER=53.70; len_ratio=0.933, num_f1=1.00, acr_f1=1.00, punct_pres=0.53)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Państwa PVD?
W kolumnie „Bezskładkowe budowanie emerytury” znajduje się wartość procentowa (%). Jest to część, w ramach której przysługuje Państwu PVD. Tę część składki emerytalnej opłacamy my. Czy Państwa „wskaźnik świadczenia” ulega zmianie? Wówczas zmienia się również procent „bezskładkowego budowania emerytury”. A tym samym część składki emerytalnej, którą opłacamy.
```
- **Unit 4** (bertscore_f1=93.74; BLEU=29.57, chrF=53.90, TER=61.29; len_ratio=0.864, num_f1=1.00, acr_f1=1.00, punct_pres=0.36)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Zmiany w niezdolności do pracy należy zgłaszać samodzielnie
Czy otrzymali Państwo nowe pismo z UWV? W takim przypadku muszą nam Państwo przesłać jego kopię. Część składki, którą opłacamy, ulegnie wtedy zmianie.
```
- **Unit 0** (bertscore_f1=97.02; BLEU=55.43, chrF=78.88, TER=26.09; len_ratio=1.011, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje od Instytutu Ubezpieczeń Pracowniczych (UWV). Informacje z UWV dotyczą Państwa niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Państwa oznacza.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=93.83; BLEU=35.15, chrF=59.44, TER=37.93; len_ratio=0.768, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Twój PVD uległ zmianie.
Otrzymujesz świadczenie WAO/WIA. UWV przekazał nam nowe informacje na temat Twojego świadczenia WAO/WIA. Poniższy przegląd wyjaśnia, co to dla Ciebie oznacza.
```
- **Unit 1** (bertscore_f1=93.90; BLEU=37.42, chrF=59.39, TER=44.00; len_ratio=0.811, num_f1=1.00, acr_f1=1.00, punct_pres=0.65)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Otrzymujesz u nas emeryturę nieskładkową.
Wynika to z Twojej niepełnosprawności. Oraz z faktu, że otrzymujesz świadczenie WAO/WIA z UWV. W związku z tym opłacamy (część) Twojej składki emerytalnej. Nazywa się to udziałem nieskładkowym (PVD). Wysokość składki, którą płacimy, zależy od procentu Twojego świadczenia.
```
- **Unit 3** (bertscore_f1=94.51; BLEU=41.18, chrF=67.14, TER=42.59; len_ratio=0.943, num_f1=1.00, acr_f1=1.00, punct_pres=0.63)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Twojego PVD?
W kolumnie „Naliczanie składek emerytalnych nieskładkowych” zobaczysz wartość procentową (%). Jest to część składki emerytalnej, którą otrzymasz. Tę część składki emerytalnej opłacamy my. Czy procent Twojego świadczenia ulegnie zmianie? Zmieni się również procent składki emerytalnej wolnej od składek. Oznacza to również część składki emerytalnej, którą płacimy.
```
- **Unit 0** (bertscore_f1=95.71; BLEU=45.65, chrF=66.10, TER=39.13; len_ratio=0.912, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Twojej niepełnosprawności. Niniejszy list wyjaśnia, co to dla Ciebie oznacza.
```
- **Unit 4** (bertscore_f1=95.90; BLEU=48.94, chrF=66.28, TER=38.71; len_ratio=0.938, num_f1=1.00, acr_f1=1.00, punct_pres=0.82)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Musisz sam zgłosić wszelkie zmiany dotyczące Twojej niepełnosprawności.
Jeśli otrzymasz nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), musisz przesłać nam jego kopię. Część składki, którą płacimy, ulegnie wówczas zmianie.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=90.82; BLEU=22.31, chrF=46.24, TER=84.00; len_ratio=1.044, num_f1=1.00, acr_f1=1.00, punct_pres=0.35)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Naliczane jest Państwu 'premiovrij pensioen' (emerytura bez składek)
Dzieje się tak, ponieważ są Państwo niezdolni do pracy. Oraz dlatego, że otrzymują Państwo świadczenie WAO/WIA od UWV. Dlatego my opłacamy (część) Państwa składki emerytalnej. Nazywamy to 'premievrije deelname (PVD)', czyli uczestnictwo bez opłacania składek. Wysokość składki, którą opłacamy, zależy od Państwa 'procentu świadczenia'.
```
- **Unit 3** (bertscore_f1=93.21; BLEU=37.81, chrF=56.34, TER=55.56; len_ratio=0.911, num_f1=1.00, acr_f1=1.00, punct_pres=0.47)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Państwa PVD?
W kolumnie 'Premievrije pensioenopbouw' (Naliczanie emerytury bez składek) widnieje procent (%). Jest to część, na którą przysługuje Państwu PVD. Tę część składki emerytalnej opłacamy my. Jeśli zmieni się Państwa 'procent świadczenia', zmieni się również procent 'naliczania emerytury bez składek'. A więc i część składki emerytalnej, którą opłacamy.
```
- **Unit 4** (bertscore_f1=93.40; BLEU=10.33, chrF=39.87, TER=77.42; len_ratio=0.823, num_f1=1.00, acr_f1=1.00, punct_pres=0.45)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Muszą Państwo sami zgłaszać zmiany w swojej niezdolności do pracy
Jeśli otrzymają Państwo nowy list od UWV, muszą Państwo przesłać nam kopię tego pisma. Wtedy zmieni się część składki, którą opłacamy.
```
- **Unit 2** (bertscore_f1=93.54; BLEU=19.75, chrF=46.13, TER=72.41; len_ratio=0.890, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Państwa PVD uległo zmianie
Otrzymują Państwo świadczenie WAO/WIA. UWV przekazało nam nowe informacje dotyczące Państwa świadczenia WAO/WIA. W poniższym zestawieniu przeczytają Państwo, co to oznacza dla Państwa.
```
- **Unit 0** (bertscore_f1=95.01; BLEU=41.93, chrF=66.80, TER=47.83; len_ratio=1.187, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje od Instytutu Wykonawczego Ubezpieczeń Pracowniczych (UWV). Informacje od UWV dotyczą Państwa niezdolności do pracy. W niniejszym piśmie przeczytają Państwo, co to oznacza dla Państwa sytuacji.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=94.58; BLEU=42.80, chrF=58.53, TER=53.70; len_ratio=0.945, num_f1=1.00, acr_f1=1.00, punct_pres=0.63)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Bezskładkowe gromadzenie emerytury” widzi Pan/Pani procent (%). Jest to część, w odniesieniu do której przysługuje Panu/Pani PVD. Tę część składki emerytalnej opłacamy my. Czy zmienia się Pana/Pani „procent świadczenia”? Wtedy zmienia się również procent „bezskładkowego gromadzenia emerytury”. A więc także część składki emerytalnej, którą opłacamy.
```
- **Unit 1** (bertscore_f1=95.23; BLEU=48.50, chrF=64.61, TER=50.00; len_ratio=0.894, num_f1=1.00, acr_f1=1.00, punct_pres=0.74)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Gromadzi Pan/Pani u nas „emeryturę bez składek”
Dzieje się tak, ponieważ jest Pan/Pani niezdolny/a do pracy. Oraz ponieważ otrzymuje Pan/Pani z UWV świadczenie WAO/WIA. Dlatego opłacamy (część) Pana/Pani składki emerytalnej. Nazywamy to „udziałem bezskładkowym (PVD)”. Wysokość składki, którą opłacamy, zależy od Pana/Pani „procentu świadczenia”.
```
- **Unit 2** (bertscore_f1=95.42; BLEU=54.29, chrF=64.04, TER=48.28; len_ratio=0.882, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Pana/Pani PVD uległo zmianie
Ma Pan/Pani świadczenie WAO/WIA. UWV przekazał nam nowe informacje dotyczące Pana/Pani świadczenia WAO/WIA. W poniższym zestawieniu przeczyta Pan/Pani, co to dla Pana/Pani oznacza.
```
- **Unit 4** (bertscore_f1=95.48; BLEU=37.69, chrF=57.46, TER=51.61; len_ratio=0.889, num_f1=1.00, acr_f1=1.00, punct_pres=0.27)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Musi Pan/Pani sam/a zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy
Otrzyma Pan/Pani nowy list z UWV? Wtedy musi Pan/Pani przesłać nam kopię tego pisma. Część składki, którą opłacamy, ulegnie wtedy zmianie.
```
- **Unit 0** (bertscore_f1=96.79; BLEU=61.22, chrF=77.72, TER=26.09; len_ratio=1.033, num_f1=1.00, acr_f1=1.00, punct_pres=0.89)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje z Instytutu Ubezpieczeń Pracowniczych (UWV). Informacje z UWV dotyczą Pana/Pani niezdolności do pracy. W tym piśmie przeczyta Pan/Pani, co to dla Pana/Pani oznacza.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=91.28; BLEU=14.04, chrF=43.80, TER=82.00; len_ratio=0.943, num_f1=1.00, acr_f1=1.00, punct_pres=0.39)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Ty gromadzisz u nas "emeryturę bez składek"
Dzieje się tak, ponieważ jesteś niezdolny do pracy. I dlatego, że otrzymujesz świadczenie z tytułu niezdolności do pracy (WAO/WIA) od UWV. Dlatego my (w części) opłacamy Twoją składkę emerytalną. Nazywamy to "uczestnictwem bez składek (PVD)". Wysokość składki, którą my opłacamy, zależy od Twojego "procentu świadczenia".
```
- **Unit 2** (bertscore_f1=92.03; BLEU=14.12, chrF=40.15, TER=86.21; len_ratio=1.013, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Twoje PVD uległo zmianie
Otrzymujesz świadczenie z tytułu niezdolności do pracy (WAO/WIA). UWV przekazał nam nowe informacje o Twoim świadczeniu z tytułu niezdolności do pracy. W poniższym podsumowaniu przeczytasz, co to dla Ciebie oznacza.
```
- **Unit 3** (bertscore_f1=92.24; BLEU=25.24, chrF=48.41, TER=61.11; len_ratio=0.789, num_f1=1.00, acr_f1=1.00, punct_pres=0.26)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Twojego PVD?
W kolumnie "Emerytura bez składek" widzisz procent (%). Jest to część, za którą otrzymujesz PVD. My opłacamy tę część składki emerytalnej. Czy zmienia się Twój "procent świadczenia"? Wtedy zmienia się również procent "emerytury bez składek". I tym samym część składki emerytalnej, którą my opłacamy.
```
- **Unit 4** (bertscore_f1=93.14; BLEU=15.60, chrF=42.67, TER=67.74; len_ratio=0.761, num_f1=1.00, acr_f1=1.00, punct_pres=0.36)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Musisz sam zgłaszać zmiany w swojej niezdolności do pracy
Czy otrzymałeś nowy list od UWV? Wtedy musisz nam przesłać kopię tego listu. Część składki, którą my opłacamy, ulegnie zmianie.
```
- **Unit 0** (bertscore_f1=94.66; BLEU=38.75, chrF=60.50, TER=43.48; len_ratio=1.044, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje od Instytutu Wykonawczego Ubezpieczeń Pracowniczych (UWV). Informacje od UWV dotyczą Twojej niezdolności do pracy. W tym liście przeczytasz, co to dla Ciebie oznacza.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=92.11; BLEU=15.30, chrF=44.38, TER=72.00; len_ratio=0.858, num_f1=1.00, acr_f1=1.00, punct_pres=0.30)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Budujesz u nas "składkę emerytalną bez składki"
Dzieje się tak, ponieważ jesteś niezdolny do pracy. I dlatego, że otrzymujesz świadczenie WAO/WIA od UWV. Dlatego my płacimy (część) Twojej składki emerytalnej. Nazywamy to "bezskładkowym uczestnictwem (PVD)". Wysokość składki, którą płacimy, zależy od Twojego "procentu świadczenia".
```
- **Unit 2** (bertscore_f1=92.15; BLEU=20.92, chrF=43.79, TER=65.52; len_ratio=0.734, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Twój PVD uległ zmianie
Masz świadczenie WAO/WIA. UWV przekazał nam nowe informacje o Twoim świadczeniu WAO/WIA. W poniższym przeglądzie przeczytasz, co to oznacza dla Ciebie.
```
- **Unit 3** (bertscore_f1=92.67; BLEU=28.84, chrF=49.95, TER=57.41; len_ratio=0.809, num_f1=1.00, acr_f1=1.00, punct_pres=0.26)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Twojego PVD?
W kolumnie "Budowa emerytury bez składki" widzisz procent (%). Jest to część, za którą otrzymujesz PVD. Tę część składki emerytalnej płacimy my. Zmienia się Twój "procent świadczenia"? Wtedy zmienia się również procent "budowy emerytury bez składki". A więc również część składki emerytalnej, którą płacimy.
```
- **Unit 4** (bertscore_f1=93.49; BLEU=14.08, chrF=39.68, TER=67.74; len_ratio=0.757, num_f1=1.00, acr_f1=1.00, punct_pres=0.36)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Musisz sam zgłaszać zmiany w swojej niezdolności do pracy
Otrzymujesz nowy list od UWV? Wtedy musisz nam przesłać kopię tego listu. Część składki, którą płacimy, ulegnie wtedy zmianie.
```
- **Unit 0** (bertscore_f1=94.22; BLEU=28.18, chrF=53.98, TER=56.52; len_ratio=1.033, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informacje od Instytutu Wykonawczego Ubezpieczeń Pracowników (UWV). Informacje od UWV dotyczą Twojej niezdolności do pracy. W tym liście przeczytasz, co to oznacza dla Ciebie.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=90.03; BLEU=6.99, chrF=29.85, TER=82.00; len_ratio=0.806, num_f1=1.00, acr_f1=1.00, punct_pres=0.35)
  - REF:
```
Gromadzi Pan/Pani u nas emeryturę bezskładkową.
Wynika to z faktu, że jest Pan/Pani niezdolny/niezdolna do pracy. Z Zakładu Ubezpieczeń Pracowniczych (UWV) otrzymuje Pan/Pani również świadczenie WAO/WIA. W związku z tym opłacamy (część) Pana/Pani składki emerytalnej. Nazywa się to udziałem bezskładkowym (PVD). Wysokość składki, którą opłacamy, zależy od procentu Pana/Pani świadczenia.
```
  - MT:
```
Budujesz 'pensjonat bez opłat'
To się dzieje dlatego, że jesteś niezdolny do pracy. I dlatego otrzymujesz zasiłek WAO/WIA od UWV. Dlatego my (część) Twojej pensjonatowej opłaty za emeryturę płacimy. Nazywamy to 'bezpłatna uczestnictwo (PVD)'. Wysokość opłaty, którą płacimy, zależy od Twojego 'procenta zasiłku'.
```
- **Unit 3** (bertscore_f1=90.67; BLEU=13.30, chrF=35.24, TER=75.93; len_ratio=0.885, num_f1=1.00, acr_f1=1.00, punct_pres=0.32)
  - REF:
```
Co to oznacza dla Pana/Pani PVD?
W kolumnie „Naliczanie bezskładkowych składek emerytalnych” widnieje wartość procentowa (%). Jest to część, od której otrzymuje Pan/Pani udział bezskładkowy (PVD). Tę część składki emerytalnej opłacamy my. Jeśli procent Pana/Pani świadczenia ulegnie zmianie, zmieni się również procent bezskładkowej składki emerytalnej. Oznacza to również część składki emerytalnej, którą opłacamy my.
```
  - MT:
```
Co to oznacza dla Twojego PVD?
W kolumnie 'budowanie pensjonatu bez opłat' widzisz procent (%). To jest część, o którą otrzymujesz PVD. To część pensjonatowej opłaty za emeryturę, którą my płacimy. Zmienia się Twój 'procent zasiłku'? Zmienia się również procent 'budowania pensjonatu bez opłat'. I zatem również część pensjonatowej opłaty za emeryturę, którą my płacimy.
```
- **Unit 4** (bertscore_f1=91.43; BLEU=5.30, chrF=28.31, TER=83.87; len_ratio=0.687, num_f1=1.00, acr_f1=1.00, punct_pres=0.36)
  - REF:
```
Należy samodzielnie zgłaszać zmiany dotyczące Pana/Pani niezdolności do pracy.
Jeśli otrzyma Pan/Pani nowe pismo z Zakładu Ubezpieczeń Pracowniczych (UWV), należy przesłać nam jego kopię. Część składki, którą opłacamy, ulegnie wówczas zmianie.
```
  - MT:
```
Musisz przekazywać zmiany w Twojej niezdolności do pracy
Otrzymasz nową listę od UWV? Należy nam wysłać kopię tej listy. Część opłaty, którą płacimy, zmieni się wtedy.
```
- **Unit 2** (bertscore_f1=92.23; BLEU=12.42, chrF=31.45, TER=82.76; len_ratio=0.717, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Pana/Pani PVD uległ zmianie.
Otrzymuje Pan/Pani świadczenie WAO/WIA. Zakład Ubezpieczeń Pracowniczych (UWV) przekazał nam nowe informacje na temat Pana/Pani świadczenia WAO/WIA. Poniższe zestawienie wyjaśnia, co to dla Pana/Pani oznacza.
```
  - MT:
```
Twoje PVD zmieniło się
Otrzymałeś zasiłek WAO/WIA. UWV przekazało nam nową informację o Twoim zasiłku WAO/WIA. Poniżej znajduje się zestawienie, co to oznacza dla Ciebie.
```
- **Unit 0** (bertscore_f1=92.53; BLEU=22.97, chrF=44.57, TER=65.22; len_ratio=1.016, num_f1=1.00, acr_f1=1.00, punct_pres=0.78)
  - REF:
```
Otrzymaliśmy informacje z Zakładu Ubezpieczeń Pracowniczych (UWV). Informacje te dotyczą Pana/Pani niezdolności do pracy. W niniejszym piśmie wyjaśniamy, co to dla Pana/Pani oznacza.
```
  - MT:
```
Otrzymaliśmy informację od Uitvoeringsinstituut Werknemersverzekeringen (UWV). Informacja z UWV dotyczy Twojej niezdolności do pracy. W tej liście przeczytasz, co to oznacza dla Ciebie.
```
</details>

### ukrainian

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.08; BLEU=2.98, chrF=18.26, TER=83.67; len_ratio=0.464, num_f1=1.00, acr_f1=0.50, punct_pres=0.25)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваш PVD змінився
У вас є пільга WAO/WIA. UWV надав нам нову інформацію про вашу допомогу WAO/WIA. В огляді нижче ви можете прочитати, що це означає для вас.
```
- **Unit 1** (bertscore_f1=90.94; BLEU=13.83, chrF=33.48, TER=73.68; len_ratio=0.619, num_f1=1.00, acr_f1=0.50, punct_pres=0.80)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви нараховуєте «пенсію без внесків» у нас
Це пов'язано з тим, що ви непрацездатні. А тому, що ви отримуєте допомогу WAO/WIA від UWV. Саме тому ми сплачуємо (частину) вашого пенсійного внеску. Ми називаємо це «неконтрибуційною участю (PVD)». Розмір премії, яку ми сплачуємо, залежить від вашого «відсотка виплат».
```
- **Unit 0** (bertscore_f1=93.20; BLEU=8.13, chrF=40.63, TER=71.88; len_ratio=0.781, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Агентства зі страхування працівників (UWV). Інформація від UWV стосується вашої непрацездатності. У цьому листі ви можете прочитати, що це означає для вас.
```
- **Unit 3** (bertscore_f1=93.68; BLEU=24.63, chrF=45.66, TER=61.54; len_ratio=0.779, num_f1=1.00, acr_f1=1.00, punct_pres=0.76)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашої ПСЗ?
У графі «Ненакопичувальне нарахування пенсії» ви побачите відсоток (%). Це та частина, на якій ви отримуєте PVD. Цю частину пенсійного внеску ми сплачуємо. Чи змінюється ваш "відсоток виплат"? Тоді зміниться і відсоток «ненакопичувального нарахування пенсії». А отже, і ту частину пенсійного внеску, яку ми сплачуємо.
```
- **Unit 4** (bertscore_f1=95.32; BLEU=24.83, chrF=49.86, TER=63.64; len_ratio=0.951, num_f1=1.00, acr_f1=0.00, punct_pres=0.62)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Про будь-які зміни у зв'язку з непрацездатністю ви повинні повідомляти самостійно
Ви отримали нового листа від UWV? Тоді ви повинні надіслати нам копію цього листа. Тоді зміниться та частина премії, яку ми платимо.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.66; BLEU=2.88, chrF=18.32, TER=85.71; len_ratio=0.497, num_f1=1.00, acr_f1=0.50, punct_pres=0.25)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваш PVD змінився
Ви отримуєте виплату WAO/WIA. UWV надало нам нову інформацію про вашу виплату WAO/WIA. У наведеному нижче огляді ви дізнаєтеся, що це означає для вас.
```
- **Unit 1** (bertscore_f1=92.29; BLEU=21.28, chrF=38.39, TER=68.42; len_ratio=0.625, num_f1=1.00, acr_f1=0.50, punct_pres=0.80)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте у нас «пенсію без сплати внесків»
Це пов'язано з тим, що ви непрацездатні. І з тим, що ви отримуєте виплати WAO/WIA від UWV. Тому ми сплачуємо (частину) ваших пенсійних внесків. Це називається «участь без сплати внесків (PVD)». Розмір премії, яку ми сплачуємо, залежить від вашого «відсотка виплати».
```
- **Unit 0** (bertscore_f1=93.11; BLEU=8.42, chrF=42.66, TER=71.88; len_ratio=0.742, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Інституту страхування працівників (UWV). Інформація від UWV стосується вашої непрацездатності. У цьому листі ви дізнаєтеся, що це означає для вас.
```
- **Unit 3** (bertscore_f1=94.47; BLEU=27.48, chrF=49.37, TER=58.46; len_ratio=0.761, num_f1=1.00, acr_f1=1.00, punct_pres=0.95)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашого PVD?
У стовпці «Безпреміальне накопичення пенсії» ви бачите відсоток (%). Це та частина, за яку ви отримуєте PVD. Цю частину пенсійного внеску ми сплачуємо. Змінюється ваш «відсоток виплат»? Тоді змінюється і відсоток «безпреміального накопичення пенсії». А отже, і та частина пенсійного внеску, яку ми сплачуємо.
```
- **Unit 4** (bertscore_f1=94.66; BLEU=21.58, chrF=53.31, TER=63.64; len_ratio=0.862, num_f1=1.00, acr_f1=0.00, punct_pres=0.75)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні самостійно повідомляти про зміни у вашій непрацездатності
Ви отримали новий лист від UWV? Тоді ви повинні надіслати нам копію цього листа. Частина премії, яку ми сплачуємо, зміниться.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.92; BLEU=2.98, chrF=19.40, TER=83.67; len_ratio=0.518, num_f1=1.00, acr_f1=0.50, punct_pres=0.25)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваша PVD змінилася
Ви отримуєте виплату WAO/WIA. UWV надав нам нову інформацію про вашу виплату WAO/WIA. У наведеному нижче огляді ви можете прочитати, що це означає для вас.
```
- **Unit 1** (bertscore_f1=92.55; BLEU=20.21, chrF=40.51, TER=64.47; len_ratio=0.692, num_f1=1.00, acr_f1=0.50, punct_pres=0.64)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте у нас «пенсію без сплати внесків»
Це пов’язано з тим, що ви є непрацездатним. А також тому, що ви отримуєте виплату WAO/WIA від UWV. Тому ми сплачуємо (частину) вашого пенсійного внеску. Ми називаємо це «участю без сплати внесків (PVD)». Сума внеску, яку ми сплачуємо, залежить від вашого «відсотка виплат» (ступеня непрацездатності).
```
- **Unit 0** (bertscore_f1=93.11; BLEU=8.42, chrF=42.66, TER=71.88; len_ratio=0.742, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Інституту страхування працівників (UWV). Інформація від UWV стосується вашої непрацездатності. У цьому листі ви дізнаєтеся, що це означає для вас.
```
- **Unit 3** (bertscore_f1=95.35; BLEU=34.18, chrF=53.80, TER=50.77; len_ratio=0.795, num_f1=1.00, acr_f1=1.00, punct_pres=0.95)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашої PVD?
У стовпчику «Накопичення пенсії без сплати внесків» ви бачите відсоток (%). Це частка, на яку поширюється PVD. Цю частину пенсійного внеску сплачуємо ми. Чи змінюється ваш «відсоток виплат»? Тоді змінюється і відсоток «накопичення пенсії без сплати внесків». А отже, змінюється і частина пенсійного внеску, яку сплачуємо ми.
```
- **Unit 4** (bertscore_f1=95.77; BLEU=20.27, chrF=56.14, TER=60.61; len_ratio=0.933, num_f1=1.00, acr_f1=0.00, punct_pres=0.75)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні самостійно повідомляти про зміни у вашій непрацездатності
Ви отримали нового листа від UWV? Тоді ви повинні надіслати нам копію цього листа. У такому разі частина внеску, яку ми сплачуємо, зміниться.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.93; BLEU=2.97, chrF=20.17, TER=87.76; len_ratio=0.497, num_f1=1.00, acr_f1=0.50, punct_pres=0.33)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваш PVD змінився.
Ви отримуєте допомогу WAO/WIA. UWV надав нам нову інформацію про вашу допомогу WAO/WIA. У наведеному нижче огляді пояснюється, що це означає для вас.
```
- **Unit 1** (bertscore_f1=91.00; BLEU=16.07, chrF=35.05, TER=72.37; len_ratio=0.603, num_f1=1.00, acr_f1=0.50, punct_pres=0.48)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте у нас безвідсоткову пенсію.
Це пов'язано з вашою інвалідністю. А також з тим, що ви отримуєте допомогу WAO/WIA від UWV. Тому ми сплачуємо (частину) вашого пенсійного внеску. Це називається безвідсотковою участю (PVD). Розмір внеску, який ми сплачуємо, залежить від вашого відсотка виплати.
```
- **Unit 3** (bertscore_f1=91.62; BLEU=14.27, chrF=38.93, TER=75.38; len_ratio=0.827, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашого PVD?
У стовпці «Нарахування безвідсоткової пенсії» ви побачите відсоток (%). Це частина пенсійної премії, яку ви отримуватимете. Ми сплачуємо цю частину пенсійної премії. Чи зміниться відсоток вашої виплати? Відсоток нарахування пенсії без відрахування внесків також зміниться. Це також стосується частини пенсійного внеску, яку ми сплачуємо.
```
- **Unit 0** (bertscore_f1=91.79; BLEU=8.47, chrF=36.11, TER=78.12; len_ratio=0.742, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Агентства зі страхування працівників (UWV). Ця інформація від UWV стосується вашої інвалідності. У цьому листі пояснюється, що це означає для вас.
```
- **Unit 4** (bertscore_f1=94.67; BLEU=30.75, chrF=55.36, TER=63.64; len_ratio=1.089, num_f1=1.00, acr_f1=0.00, punct_pres=0.50)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні самостійно повідомляти про будь-які зміни щодо вашої інвалідності.
Якщо ви отримаєте новий лист від Агентства страхування працівників (UWV), ви повинні надіслати нам копію цього листа. Частина внеску, яку ми сплачуємо, тоді зміниться.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=90.01; BLEU=2.88, chrF=18.45, TER=85.71; len_ratio=0.500, num_f1=1.00, acr_f1=0.50, punct_pres=0.25)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваша PVD змінилася
Ви отримуєте виплати WAO/WIA. UWV надав нам нову інформацію про ваші виплати WAO/WIA. У наведеному нижче огляді ви прочитаєте, що це означає для вас.
```
- **Unit 1** (bertscore_f1=90.70; BLEU=4.24, chrF=27.78, TER=81.58; len_ratio=0.601, num_f1=1.00, acr_f1=0.50, punct_pres=0.44)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте 'премійне пенсійне забезпечення' у нас
Це тому, що ви непрацездатні. І тому, що ви отримуєте виплати WAO/WIA від UWV. Тому ми платимо (частину) вашого пенсійного внеску. Це називається 'участь без сплати премій (PVD)'. Розмір премії, яку ми платимо, залежить від вашого 'відсотка виплат'.
```
- **Unit 0** (bertscore_f1=93.01; BLEU=8.88, chrF=44.19, TER=68.75; len_ratio=0.764, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Інституту виконання страхування працівників (UWV). Ця інформація стосується вашої непрацездатності. У цьому листі ви дізнаєтеся, що це означає для вас.
```
- **Unit 3** (bertscore_f1=94.09; BLEU=22.53, chrF=47.27, TER=58.46; len_ratio=0.773, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашої PVD?
У колонці 'Премійне пенсійне накопичення' ви побачите відсоток (%). Це та частина, за яку ви отримуєте PVD. Цю частину пенсійного внеску ми платимо. Якщо змінюється ваш 'відсоток виплат', то змінюється і відсоток 'премійного пенсійного накопичення'. І, отже, змінюється і частина пенсійного внеску, яку ми платимо.
```
- **Unit 4** (bertscore_f1=94.68; BLEU=16.24, chrF=47.49, TER=75.76; len_ratio=0.884, num_f1=1.00, acr_f1=0.00, punct_pres=0.62)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні самостійно повідомляти про зміни у вашій непрацездатності
Якщо ви отримаєте новий лист від UWV, вам потрібно надіслати нам копію цього листа. Тоді зміниться частина премії, яку ми платимо.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.49; BLEU=2.92, chrF=20.98, TER=85.71; len_ratio=0.503, num_f1=1.00, acr_f1=0.50, punct_pres=0.25)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваш PVD змінився
Ви отримуєте допомогу WAO/WIA. UWV надало нам нову інформацію про вашу допомогу WAO/WIA. У наведеному нижче огляді ви прочитаєте, що це означає для вас.
```
- **Unit 1** (bertscore_f1=92.46; BLEU=22.49, chrF=40.12, TER=69.74; len_ratio=0.613, num_f1=1.00, acr_f1=0.50, punct_pres=0.76)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте у нас «пенсію без сплати внесків»
Це тому, що ви є непрацездатними. І тому, що ви отримуєте допомогу WAO/WIA від UWV. Тому ми сплачуємо (частину) вашого пенсійного внеску. Це називається «участь без сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від вашого «відсотка виплат».
```
- **Unit 0** (bertscore_f1=93.94; BLEU=18.61, chrF=47.56, TER=65.62; len_ratio=0.837, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Управління з реалізації програм страхування працівників (UWV). Інформація від UWV стосується вашої непрацездатності. У цьому листі ви прочитаєте, що це означає для вас.
```
- **Unit 3** (bertscore_f1=95.78; BLEU=34.72, chrF=55.69, TER=47.69; len_ratio=0.777, num_f1=1.00, acr_f1=1.00, punct_pres=0.95)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашого PVD?
У колонці «Накопичення пенсії без сплати внесків» ви бачите відсоток (%). Це частка, щодо якої ви отримуєте PVD. Цю частину пенсійного внеску сплачуємо ми. Чи змінюється ваш «відсоток виплат»? Тоді змінюється і відсоток «накопичення пенсії без сплати внесків». А отже, і частина пенсійного внеску, яку сплачуємо ми.
```
- **Unit 4** (bertscore_f1=96.05; BLEU=27.13, chrF=60.93, TER=60.61; len_ratio=0.849, num_f1=1.00, acr_f1=0.00, punct_pres=0.62)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні самостійно повідомляти про зміни вашої непрацездатності
Отримали новий лист від UWV? Тоді ви маєте надіслати нам копію цього листа. Тоді зміниться частина внеску, яку сплачуємо ми.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=90.09; BLEU=3.16, chrF=20.86, TER=81.63; len_ratio=0.560, num_f1=1.00, acr_f1=0.50, punct_pres=0.25)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваша PVD змінилася
Ви отримуєте виплату за законом WAO/WIA. UWV надав нам нову інформацію про вашу виплату за законом WAO/WIA. У наведеному нижче огляді ви побачите, що це означає для вас.
```
- **Unit 1** (bertscore_f1=91.65; BLEU=12.87, chrF=33.24, TER=72.37; len_ratio=0.645, num_f1=1.00, acr_f1=0.50, punct_pres=0.76)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте «пенсію без сплати премії» в нас
Це відбувається тому, що ви непрацездатні. І тому, що ви отримуєте виплату за законом WAO/WIA від UWV. Тому ми сплачуємо (частину) вашої пенсійної премії. Ми називаємо це «участь без сплати премії (PVD)». Висота премії, яку ми сплачуємо, залежить від вашого «відсотку виплати».
```
- **Unit 0** (bertscore_f1=93.11; BLEU=8.42, chrF=42.29, TER=71.88; len_ratio=0.768, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Інституту виконання страхування працівників (UWV). Інформація UWV стосується вашої непрацездатності. У цьому листі ви дізнаєтеся, що це означає для вас.
```
- **Unit 3** (bertscore_f1=94.28; BLEU=15.37, chrF=44.52, TER=63.08; len_ratio=0.773, num_f1=1.00, acr_f1=1.00, punct_pres=1.00)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашої PVD?
У колонці «Накопичення пенсії без сплати премії» ви бачите відсоток (%). Це частина, за яку ви отримуєте PVD. Ми сплачуємо цю частину пенсійної премії. Змінився ваш «відсоток виплати»? Тоді змінюється також відсоток «накопичення пенсії без сплати премії». І, відповідно, частина пенсійної премії, яку ми сплачуємо.
```
- **Unit 4** (bertscore_f1=95.00; BLEU=20.96, chrF=54.74, TER=63.64; len_ratio=0.862, num_f1=1.00, acr_f1=0.00, punct_pres=0.75)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні повідомляти про зміни вашої непрацездатності самостійно
Отримали ви новий лист від UWV? Тоді вам потрібно надіслати нам копію цього листа. Частина премії, яку ми сплачуємо, зміниться.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=90.24; BLEU=3.27, chrF=26.72, TER=85.71; len_ratio=0.628, num_f1=1.00, acr_f1=0.50, punct_pres=0.00)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваш PVD змінився
Ви отримуєте допомогу за непрацездатність (WAO/WIA). UWV надав нам нову інформацію про вашу допомогу за непрацездатність (WAO/WIA). У нижченаведеному огляді ви дізнаєтеся, що це означає для вас.
```
- **Unit 1** (bertscore_f1=91.46; BLEU=4.47, chrF=30.55, TER=81.58; len_ratio=0.633, num_f1=1.00, acr_f1=0.50, punct_pres=0.20)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви накопичуєте "пенсію без премії" у нас
Це відбувається тому, що ви непрацездатні. І тому, що ви отримуєте допомогу за непрацездатність (WAO/WIA) від UWV. Тому ми платимо (частину) вашої пенсійної премії. Це називається "участь без премії (PVD)". Розмір премії, яку ми платимо, залежить від вашого "відсотка допомоги".
```
- **Unit 0** (bertscore_f1=93.21; BLEU=8.47, chrF=42.99, TER=71.88; len_ratio=0.785, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ми отримали інформацію від Інституту виконання страхування працівників (UWV). Інформація від UWV стосується вашої непрацездатності. У цьому листі ви дізнаєтеся, що це означає для вас.
```
- **Unit 3** (bertscore_f1=93.91; BLEU=12.24, chrF=38.97, TER=69.23; len_ratio=0.761, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашого PVD?
У колонці "Накопичення пенсії без премії" ви бачите відсоток (%). Це частина, за яку ви отримуєте PVD. Цю частину пенсійної премії ми платимо. Змінюється ваш "відсоток допомоги"? Тоді змінюється також відсоток "накопичення пенсії без премії". І тому також змінюється частина пенсійної премії, яку ми платимо.
```
- **Unit 4** (bertscore_f1=94.25; BLEU=19.96, chrF=47.36, TER=66.67; len_ratio=0.884, num_f1=1.00, acr_f1=0.00, punct_pres=0.75)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Ви повинні повідомляти про зміни у своїй непрацездатності самостійно
Отримуєте ви новий лист від UWV? Тоді ви повинні надіслати нам копію цього листа. Частина премії, яку ми платимо, змінюється тоді.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=90.18; BLEU=3.46, chrF=28.45, TER=84.21; len_ratio=0.669, num_f1=1.00, acr_f1=0.67, punct_pres=0.24)
  - REF:
```
Вами в нас здійснюються накопичення за «пенсійною програмою зі звільненням від сплати внесків»
Це відбувається в зв'язку з тим, що Ви є непрацездатною особою. А також в зв'язку з тим, що Ви отримуєте від Інституту допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Тому ми сплачуємо (в певній частині) Ваші пенсійні внески. Це ми називаємо «участю в програмі зі звільненням від сплати внесків (PVD)». Розмір внеску, який ми сплачуємо, залежить від «відсотка призначеної Вам допомоги».
```
  - MT:
```
Ви створюєте ‘премієвільний пенсійний капітал’ серед нас
Це відбувається тому, що ви не працюєте через хворобу. І тому, що ви отримуєте виплату за працездатність від UWV. Тому ми виплачуватимемо (частину) вашої пенсійної премії. Це називається ‘премієвільна участь (PVD)’. Висота виплаченої премії залежить від вашого ‘відсотка виплати’.
```
- **Unit 2** (bertscore_f1=90.61; BLEU=3.45, chrF=29.90, TER=83.67; len_ratio=0.729, num_f1=1.00, acr_f1=0.67, punct_pres=0.42)
  - REF:
```
У Вашій PVD відбулися зміни.
Вам було призначено допомогу, обумовлену Законом «Про роботу та доходи за працездатністю». Інститутом нам було надано оновлену інформацію щодо призначеної Вам допомоги, обумовленої Законом «Про роботу та доходи за працездатністю». З наведеної нижче довідки Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Ваш PVD змінився
Ви отримуєте виплату за працездатність від UWV. Інститут виконавчих робітничих страхових виплат надав нам нову інформацію щодо вашої виплати за працездатність. У нижченаведеному звіту ви зможете прочитати, що це означає для вас.
```
- **Unit 3** (bertscore_f1=92.62; BLEU=12.60, chrF=37.24, TER=72.31; len_ratio=0.829, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Що це означає для Вашої PVD?
В колонці «Накопичення за пенсійною програмою зі звільненням від сплати внесків» Ви побачите відсоток (%). Це та частина, в якій Ви отримуєте право на PVD. Вказану частину пенсійного внеску сплачуємо ми. Змінюється «відсоток призначеної Вам допомоги»? Відповідно, змінюється й відсоток «накопичення за пенсійною програмою зі звільненням від сплати внесків». А отже, й та частина пенсійного внеску, яку сплачуємо ми.
```
  - MT:
```
Що це означає для вашого PVD?
У колонці ‘Премієвільна пенсійна капіталізація’ ви побачите відсоток (%). Це частина, щодо якої ви отримуєте PVD. Ця частина пенсійної премії виплачується нами. Якщо зміниться ваш ‘відсоток виплати’, зміниться також відсоток ‘премієвільної пенсійної капіталізації’. І відповідно зміниться частина пенсійної премії, яку ми виплачуватимемо.
```
- **Unit 0** (bertscore_f1=92.85; BLEU=8.41, chrF=37.40, TER=75.00; len_ratio=0.820, num_f1=1.00, acr_f1=0.00, punct_pres=1.00)
  - REF:
```
Нами була отримана інформація від Інституту з реалізації програм страхування працівників (Інститут). Надана Інститутом інформація стосується втрати Вами працездатності. З цьому листа Ви можете дізнатися про те, що це для Вас означає.
```
  - MT:
```
Нам надійшла інформація від Інституту виконання робітничих страхових виплат (UWV). Інформація від UWV стосується вашої працездатності. У цій листі ви зможете прочитати, що це означає для вас.
```
- **Unit 4** (bertscore_f1=93.79; BLEU=16.79, chrF=46.79, TER=75.76; len_ratio=0.951, num_f1=1.00, acr_f1=0.00, punct_pres=0.75)
  - REF:
```
Про будь-які зміни в частині Вашої непрацездатності Ви маєте повідомляти самостійно.
Отримали від Інституту новий лист? Тоді Ви маєте надіслати нам копію цього листа. Частина внеску, яку сплачуємо ми, в такому разі зміниться.
```
  - MT:
```
Вам необхідно повідомляти про зміни своєї працездатності самостійно
Отримали ви новий лист від UWV? Тоді необхідно відправити нам копію цього листа. Частина пенсійної премії, яку ми виплачуватимемо, зміниться тоді.
```
</details>

### arabic

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=88.98; BLEU=4.81, chrF=25.44, TER=86.49; len_ratio=0.742, num_f1=1.00, acr_f1=0.57, punct_pres=0.00)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد تغير PVD الخاص بك
لديك ميزة WAO / WIA. زودتنا UWV بمعلومات جديدة حول مزايا WAO / WIA الخاصة بك. في النظرة العامة أدناه ، يمكنك قراءة ما يعنيه هذا بالنسبة لك.
```
- **Unit 3** (bertscore_f1=89.80; BLEU=7.53, chrF=33.73, TER=80.82; len_ratio=0.817, num_f1=1.00, acr_f1=1.00, punct_pres=0.25)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني هذا بالنسبة ل PVD الخاص بك؟
في العمود "استحقاق المعاش التقاعدي غير القائم على الاشتراكات" سترى نسبة مئوية (٪). هذا هو الجزء الذي تحصل عليه PVD. نحن ندفع هذا الجزء من مساهمة المعاش. هل تتغير "نسبة العائد" الخاصة بك؟ ثم ستتغير أيضا النسبة المئوية ل "استحقاق المعاش التقاعدي غير القائم على الاشتراكات". وبالتالي أيضا جزء من مساهمة التقاعد التي ندفعها.
```
- **Unit 1** (bertscore_f1=90.42; BLEU=6.41, chrF=30.92, TER=87.10; len_ratio=0.766, num_f1=1.00, acr_f1=0.57, punct_pres=0.26)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
تحصل على "معاش تقاعدي غير قائم على الاشتراكات" معنا
هذا لأنك عاجز عن العمل. ولأنك تتلقى ميزة WAO / WIA من UWV. هذا هو السبب في أننا ندفع (جزءا من) مساهمتك في المعاش التقاعدي. نسمي هذا "المشاركة غير المساهمة (PVD)". يعتمد مبلغ القسط الذي ندفعه على "نسبة العائد" الخاصة بك.
```
- **Unit 4** (bertscore_f1=93.48; BLEU=16.92, chrF=42.48, TER=64.10; len_ratio=0.764, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك الإبلاغ عن أي تغييرات تطرأ على عجزك عن العمل بنفسك
هل تلقيت رسالة جديدة من UWV؟ ثم يجب أن ترسل لنا نسخة من تلك الرسالة. سيتغير جزء القسط الذي ندفعه بعد ذلك.
```
- **Unit 0** (bertscore_f1=94.57; BLEU=31.85, chrF=54.84, TER=58.06; len_ratio=0.860, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقينا معلومات من وكالة تأمين الموظفين (UWV). المعلومات الواردة من UWV تتعلق بعجزك عن العمل. في هذه الرسالة يمكنك قراءة ما يعنيه هذا بالنسبة لك.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=90.01; BLEU=11.87, chrF=32.05, TER=75.68; len_ratio=0.747, num_f1=1.00, acr_f1=1.00, punct_pres=0.00)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد تغيرت PVD الخاصة بك
أنت تحصل على إعانة WAO/WIA. وقد زودتنا UWV بمعلومات جديدة عن إعانة WAO/WIA الخاصة بك. ستجد في النظرة العامة أدناه ما يعنيه ذلك بالنسبة لك.
```
- **Unit 1** (bertscore_f1=91.53; BLEU=9.12, chrF=33.26, TER=83.87; len_ratio=0.712, num_f1=1.00, acr_f1=1.00, punct_pres=0.05)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
أنت تراكم ”معاشًا تقاعديًا بدون أقساط“ لدينا
وذلك لأنك عاجز عن العمل. ولأنك تتلقى إعانة WAO/WIA من UWV. ولذلك ندفع (جزءًا من) أقساط معاشك التقاعدي. وهذا ما نسميه ”المشاركة بدون أقساط (PVD)“. يعتمد مقدار الاشتراك الذي ندفعه على ”نسبة الإعانة“ الخاصة بك.
```
- **Unit 3** (bertscore_f1=91.54; BLEU=12.25, chrF=38.33, TER=73.97; len_ratio=0.795, num_f1=1.00, acr_f1=1.00, punct_pres=0.00)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني ذلك بالنسبة لـ PVD الخاصة بك؟
في عمود ”تراكم المعاش التقاعدي بدون أقساط“، ترى نسبة مئوية (%). هذه هي النسبة التي تحصل عليها من PVD. نحن ندفع هذه النسبة من قسط المعاش التقاعدي. هل تغيرت ”نسبة الاستحقاق“ الخاصة بك؟ إذاً، ستتغير أيضاً نسبة ”تراكم المعاش التقاعدي بدون أقساط“. وبالتالي، ستتغير أيضاً النسبة التي ندفعها من قسط المعاش التقاعدي.
```
- **Unit 4** (bertscore_f1=93.83; BLEU=17.71, chrF=47.47, TER=53.85; len_ratio=0.773, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك الإبلاغ عن أي تغييرات في عجزك عن العمل
هل تلقيت رسالة جديدة من UWV؟ إذاً يجب عليك إرسال نسخة من هذه الرسالة إلينا. عندئذٍ سيتغير الجزء الذي ندفعه من الاشتراك.
```
- **Unit 0** (bertscore_f1=94.31; BLEU=23.22, chrF=50.90, TER=64.52; len_ratio=1.047, num_f1=1.00, acr_f1=1.00, punct_pres=0.86)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقينا معلومات من معهد تنفيذ تأمينات العمال (UWV). تتعلق المعلومات الواردة من معهد تنفيذ تأمينات العمال (UWV) بعدم قدرتك على العمل. ستجد في هذه الرسالة ما يعنيه ذلك بالنسبة لك.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=92.69; BLEU=27.91, chrF=45.37, TER=75.81; len_ratio=0.901, num_f1=1.00, acr_f1=1.00, punct_pres=0.53)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
أنت تكتسب "حقوقاً تقاعدية معفاة من الأقساط" لدينا
يعود ذلك إلى كونك مسجلاً كعاجز عن العمل، وبسبب حصولك على إعانة (WAO/WIA) من مؤسسة (UWV). بناءً على ذلك، نقوم نحن بدفع (جزء من) قسط التقاعد الخاص بك. نطلق على هذا النظام اسم "المشاركة المعفاة من الأقساط (PVD)". ويعتمد مقدار القسط الذي ندفعه على "نسبة الإعانة" الخاصة بك.
```
- **Unit 4** (bertscore_f1=93.52; BLEU=17.67, chrF=43.02, TER=69.23; len_ratio=0.907, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك إبلاغنا بأي تغييرات في حالة العجز عن العمل بنفسك
في حال تلقيت خطاباً جديداً من مؤسسة (UWV)، يجب عليك إرسال نسخة من ذلك الخطاب إلينا؛ حيث سيترتب على ذلك تغيير في جزء القسط الذي نقوم بدفعه.
```
- **Unit 0** (bertscore_f1=93.90; BLEU=21.45, chrF=51.58, TER=64.52; len_ratio=0.791, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقينا معلومات من مؤسسة تأمينات الموظفين (UWV) تتعلق بحالتك الخاصة بالعجز عن العمل. ونوضح لك في هذه الرسالة ما يعنيه ذلك بالنسبة لك.
```
- **Unit 3** (bertscore_f1=94.25; BLEU=27.39, chrF=50.63, TER=56.16; len_ratio=0.776, num_f1=1.00, acr_f1=1.00, punct_pres=0.56)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني هذا بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
ستجد في خانة "تراكم التقاعد المعفى من الأقساط" نسبة مئوية (%). هذا هو الجزء الذي تحصل عليه كـ PVD، وهو الجزء الذي نتكفل نحن بدفعه من قسط التقاعد. إذا تغيرت "نسبة الإعانة" الخاصة بك، فستتغير أيضاً نسبة "تراكم التقاعد المعفى من الأقساط"، وبالتالي يتغير الجزء الذي ندفعه من قسط التقاعد.
```
- **Unit 2** (bertscore_f1=94.42; BLEU=38.78, chrF=53.41, TER=67.57; len_ratio=1.028, num_f1=1.00, acr_f1=1.00, punct_pres=0.73)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد طرأ تغيير على نظام المشاركة المعفاة من الأقساط (PVD) الخاص بك
بما أنك تحصل على إعانة (WAO/WIA)، فقد زودتنا مؤسسة (UWV) بمعلومات جديدة تتعلق بهذه الإعانة. يمكنك الاطلاع على ما يعنيه ذلك بالنسبة لك في الجدول الموضح أدناه.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=90.95; BLEU=15.50, chrF=38.18, TER=76.71; len_ratio=0.838, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني هذا بالنسبة لنسبة المشاركة غير القائمة على الاشتراكات (PVD) الخاصة بك؟
في عمود "استحقاق المعاش التقاعدي غير القائم على الاشتراكات"، ستجد نسبة مئوية (%). هذه هي النسبة التي ستتلقاها من قسط المعاش التقاعدي. نحن ندفع هذه النسبة. هل ستتغير نسبة استحقاقك؟ ستتغير نسبة استحقاق المعاش التقاعدي المعفى من الأقساط. وهذا يعني أيضًا تغيير حصتنا من قسط المعاش التقاعدي.
```
- **Unit 1** (bertscore_f1=91.34; BLEU=16.60, chrF=35.53, TER=74.19; len_ratio=0.816, num_f1=1.00, acr_f1=1.00, punct_pres=0.58)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
أنت الآن بصدد استحقاق معاش تقاعدي غير قائم على الاشتراكات لدينا.
يعود ذلك إلى إعاقتك، وإلى حصولك على إعانة WAO/WIA من وكالة تأمين الموظفين (UWV). لذلك، ندفع (جزءًا من) قسط معاشك التقاعدي. يُسمى هذا "المشاركة غير القائمة على الاشتراكات" (PVD). يعتمد مبلغ القسط الذي ندفعه على نسبة استحقاقك.
```
- **Unit 0** (bertscore_f1=92.50; BLEU=27.10, chrF=46.71, TER=61.29; len_ratio=0.587, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) تتعلق بإعاقتك. توضح هذه الرسالة ما يعنيه ذلك بالنسبة لك.
```
- **Unit 4** (bertscore_f1=93.99; BLEU=21.93, chrF=41.04, TER=69.23; len_ratio=0.819, num_f1=1.00, acr_f1=1.00, punct_pres=0.80)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك إبلاغنا بأي تغييرات تطرأ على إعاقتك بنفسك.
إذا تلقيت خطابًا جديدًا من وكالة تأمين الموظفين (UWV)، فيجب عليك إرسال نسخة منه إلينا. وبناءً على ذلك، ستتغير حصتنا من القسط.
```
- **Unit 2** (bertscore_f1=94.17; BLEU=32.44, chrF=51.41, TER=56.76; len_ratio=0.945, num_f1=1.00, acr_f1=1.00, punct_pres=0.36)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد تغيرت نسبة المشاركة غير القائمة على الاشتراكات (PVD) الخاصة بك.
أنت تتلقى إعانة WAO/WIA. وقد زودتنا وكالة تأمين الموظفين (UWV) بمعلومات جديدة حول هذه الإعانة. يوضح الجدول أدناه ما يعنيه ذلك بالنسبة لك.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=90.48; BLEU=8.48, chrF=28.96, TER=81.08; len_ratio=0.687, num_f1=1.00, acr_f1=1.00, punct_pres=0.00)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد تغيرت PVD الخاصة بكم
أنتم تتلقون إعانة WAO/WIA. قدم لنا UWV معلومات جديدة حول إعانتكم WAO/WIA. في الجدول أدناه، ستقرأون ما يعنيه ذلك بالنسبة لكم.
```
- **Unit 1** (bertscore_f1=90.99; BLEU=10.06, chrF=31.48, TER=87.10; len_ratio=0.746, num_f1=1.00, acr_f1=1.00, punct_pres=0.26)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
أنتم تكتسبون "معاش تقاعدي بدون اشتراك" لدينا
وذلك لأنكم تعانون من عجز عن العمل. ولأنكم تتلقون إعانة WAO/WIA من UWV. لذا، نحن ندفع (جزء من) اشتراك معاشكم التقاعدي. نسمي هذا "المشاركة بدون اشتراك (PVD)". تعتمد قيمة الاشتراك التي ندفعها على "نسبة الإعانة" الخاصة بكم.
```
- **Unit 3** (bertscore_f1=91.71; BLEU=13.73, chrF=40.31, TER=69.86; len_ratio=0.792, num_f1=1.00, acr_f1=1.00, punct_pres=0.31)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني ذلك بالنسبة لـ PVD الخاصة بكم؟
في عمود "بناء المعاش التقاعدي بدون اشتراك"، سترون نسبة مئوية (%). هذه هي النسبة التي تحصلون عليها من PVD. نحن ندفع هذا الجزء من اشتراك المعاش التقاعدي. إذا تغيرت "نسبة الإعانة" الخاصة بكم، فإن نسبة "بناء المعاش التقاعدي بدون اشتراك" ستتغير أيضًا. وبالتالي، يتغير الجزء من اشتراك المعاش التقاعدي الذي ندفعه.
```
- **Unit 4** (bertscore_f1=93.27; BLEU=17.68, chrF=47.15, TER=64.10; len_ratio=0.856, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليكم إبلاغنا بأي تغييرات في حالة عجزكم عن العمل بأنفسكم
إذا تلقيتم رسالة جديدة من UWV، يجب عليكم إرسال نسخة من تلك الرسالة إلينا. سيتغير الجزء من الاشتراك الذي ندفعه بناءً على ذلك.
```
- **Unit 0** (bertscore_f1=94.02; BLEU=10.58, chrF=42.17, TER=70.97; len_ratio=0.895, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقينا معلومات من معهد تنفيذ تأمينات العمال (UWV). تتعلق المعلومات التي وردت من UWV بعجزكم عن العمل. في هذه الرسالة، ستقرأون ما يعنيه ذلك بالنسبة لكم.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.46; BLEU=9.72, chrF=31.13, TER=78.38; len_ratio=0.760, num_f1=1.00, acr_f1=1.00, punct_pres=0.18)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد تغيّرت مشاركتك دون أقساط (PVD)
لديك مخصّصات WAO/WIA. وقد قدّم لنا UWV معلومات جديدة عن مخصّصات WAO/WIA لديك. في النظرة العامة أدناه تقرأ ما يعنيه ذلك بالنسبة لك.
```
- **Unit 1** (bertscore_f1=91.41; BLEU=4.56, chrF=27.56, TER=85.48; len_ratio=0.692, num_f1=1.00, acr_f1=1.00, punct_pres=0.05)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
أنت تبني لدينا «معاشًا تقاعديًا دون دفع أقساط»
وذلك لأنك عاجز عن العمل. ولأنك تتلقى مخصّصات WAO/WIA من UWV. لذلك ندفع نحن (جزءًا من) قسط معاشك التقاعدي. نسمي ذلك «المشاركة دون أقساط (PVD)». يعتمد مقدار القسط الذي ندفعه على «نسبة المخصّصات» لديك.
```
- **Unit 3** (bertscore_f1=92.43; BLEU=16.64, chrF=40.64, TER=69.86; len_ratio=0.792, num_f1=1.00, acr_f1=1.00, punct_pres=0.00)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني هذا بالنسبة لمشاركتك دون أقساط (PVD)؟
في عمود «تكوين المعاش التقاعدي دون أقساط» ترى نسبة مئوية (%). هذا هو الجزء الذي تحصل عنه على PVD. نحن ندفع هذا الجزء من قسط المعاش التقاعدي. هل تتغيّر «نسبة المخصّصات» لديك؟ عندها تتغيّر أيضًا نسبة «تكوين المعاش التقاعدي دون أقساط». وبالتالي يتغيّر أيضًا الجزء من قسط المعاش التقاعدي الذي ندفعه نحن.
```
- **Unit 0** (bertscore_f1=92.77; BLEU=19.12, chrF=42.77, TER=77.42; len_ratio=0.797, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقّينا معلومات من معهد تنفيذ تأمينات الموظفين (UWV). تتعلّق معلومات UWV بعجزك عن العمل. في هذه الرسالة تقرأ ما يعنيه ذلك بالنسبة لك.
```
- **Unit 4** (bertscore_f1=94.94; BLEU=24.70, chrF=49.23, TER=56.41; len_ratio=0.741, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك الإبلاغ بنفسك عن تغيّرات عجزك عن العمل
إذا تلقيت رسالة جديدة من UWV، فعليك أن ترسل لنا نسخة من تلك الرسالة. عندها يتغيّر الجزء من القسط الذي ندفعه نحن.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=88.48; BLEU=5.43, chrF=20.43, TER=91.89; len_ratio=0.682, num_f1=1.00, acr_f1=0.57, punct_pres=0.00)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
تم تغيير PVD الخاص بك
لديك منحة WAO / WIA. قدّم UWV لنا معلومات جديدة حول منحة WAO / WIA الخاصة بك. في نظرة عامة أدناه ، ستتعرف على ما يعنيه ذلك لك.
```
- **Unit 3** (bertscore_f1=89.03; BLEU=9.18, chrF=24.85, TER=84.93; len_ratio=0.676, num_f1=1.00, acr_f1=1.00, punct_pres=0.31)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني هذا لبرنامج PVD الخاص بك؟
في عمود "مسنّات بدون رسوم" ، ترى نسبة مئوية (%). هذا هو الجزء الذي تحصل عليه على برنامج PVD. ندفع نحن هذا الجزء من رسوم المسنّات. هل تتغير "نسبة المنحة" الخاصة بك؟ ثم يتغير أيضًا نسبة "مسنّات بدون رسوم". وبالتالي ، يتغير أيضًا جزء من رسوم المسنّات التي ندفعها.
```
- **Unit 1** (bertscore_f1=89.61; BLEU=5.02, chrF=20.92, TER=91.94; len_ratio=0.650, num_f1=1.00, acr_f1=0.57, punct_pres=0.26)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
ت积لم "مسنّات بدون رسوم" لدينا
ذلك لأنك معاق في العمل. ولأنك تحصل على منحة WAO / WIA من UWV. لذلك ، ندفع نحن (جزءًا من) رسوم مسنّاتك. نسمي هذا "المشاركة بدون رسوم (PVD)". يعتمد ارتفاع الرسوم التي ندفعها على "نسبة المنحة" الخاصة بك.
```
- **Unit 0** (bertscore_f1=92.52; BLEU=8.99, chrF=35.96, TER=80.65; len_ratio=0.756, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقينا معلومات من مؤسسة تنفيذ تأمين العمال (UWV). وتتعلق معلومات UWV بإعاقة عملك. في هذه الرسالة ، ستتعرف على ما يعنيه ذلك لك.
```
- **Unit 4** (bertscore_f1=93.02; BLEU=16.30, chrF=39.60, TER=66.67; len_ratio=0.769, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك إخطارنا بأي تغييرات في إعاقة عملك بنفسك
هل حصلت على رسالة جديدة من UWV؟ ثم يجب عليك إرسال نسخة من تلك الرسالة إلينا. يتغير جزء من الرسوم التي ندفعها بعد ذلك.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 2** (bertscore_f1=89.04; BLEU=4.24, chrF=21.56, TER=89.19; len_ratio=0.613, num_f1=1.00, acr_f1=1.00, punct_pres=0.00)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
لقد تغير PVD الخاص بك
لديك منحة WAO/WIA. قدم لنا UWV معلومات جديدة حول منحة WAO/WIA الخاصة بك. في الجدول أدناه، ستقرأ ما يعني ذلك لك.
```
- **Unit 1** (bertscore_f1=91.77; BLEU=13.51, chrF=34.71, TER=82.26; len_ratio=0.709, num_f1=1.00, acr_f1=1.00, punct_pres=0.26)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
تبني "معاش تقاعدي خالٍ من الأقساط" لدينا
ذلك لأنك عاجز عن العمل. ولأنك تحصل على منحة WAO/WIA من UWV. لذلك ندفع (جزءًا من) أقساط معاشك التقاعدي. نسمي ذلك "المشاركة الخالية من الأقساط (PVD)". يعتمد ارتفاع الأقساط التي ندفعها على "نسبة المنحة" الخاصة بك.
```
- **Unit 3** (bertscore_f1=92.28; BLEU=18.24, chrF=43.65, TER=65.75; len_ratio=0.790, num_f1=1.00, acr_f1=1.00, punct_pres=0.44)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني ذلك لمشاركتك الخالية من الأقساط (PVD)؟
في عمود "بناء المعاش التقاعدي الخالي من الأقساط"، ترى نسبة (%). هذه هي النسبة التي تحصل على PVD. ندفع هذا الجزء من أقساط المعاش التقاعدي. هل تتغير "نسبة المنحة" الخاصة بك؟ ثم تتغير أيضًا نسبة "بناء المعاش التقاعدي الخالي من الأقساط". وبالتالي يتغير أيضًا الجزء من أقساط المعاش التقاعدي الذي ندفعه.
```
- **Unit 0** (bertscore_f1=92.95; BLEU=8.39, chrF=32.88, TER=74.19; len_ratio=0.733, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
لقد تلقينا معلومات من معهد تنفيذ تأمين العمال (UWV). تتعلق المعلومات من UWV بإعاقة عملك. في هذه الرسالة، ستقرأ ما يعني ذلك لك.
```
- **Unit 4** (bertscore_f1=93.10; BLEU=15.66, chrF=41.09, TER=66.67; len_ratio=0.708, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب عليك إبلاغنا بتغييرات إعاقة عملك بنفسك
هل تتلقى رسالة جديدة من UWV؟ يجب عليك إرسال نسخة من تلك الرسالة إلينا. سيتم تغيير الجزء من الأقساط الذي ندفعه.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=89.12; BLEU=8.71, chrF=27.04, TER=80.82; len_ratio=0.703, num_f1=1.00, acr_f1=1.00, punct_pres=0.12)
  - REF:
```
ماذا يعني ذلك بالنسبة لمشاركتك المعفاة من الأقساط (PVD)؟
في عمود "تكوين المعاش التقاعدي المعفى من الأقساط" سترى نسبة مئوية (%)، تمثّل هذه النسبة الجزء الذي تستفيد عنه من المشاركة المعفاة من الأقساط (PVD) وهو جزء قسط المعاش التقاعدي الذي نتكفل نحن بدفعه.
وإذا تغيّرت نسبة الإعانة الخاصة بك، إذا تغيرت 'نسبة الإعانة' الخاصة بك، فستتغير تبعاً لذلك "تكوين المعاش التقاعدي المعفى من الأقساط" وبالتالي يتغير أيضاً الجزء الذي نسدده من قسط معاشك.
```
  - MT:
```
ماذا يعني ذلك بالنسبة لانضمامك بدون تكاليف؟
في العمود 'بناء التقاعد بدون تكاليف'، ستجد نسبة مئوية (%). هذا هو الجزء الذي ستتلقى PVD. هذا الجزء من تكاليف التقاعد، نحن الذين سنقوم بتحملها. تغير 'نسبة التعويض'؟ فذلك يعني تغير نسبة 'بناء التقاعد بدون تكاليف'، وبالتالي الجزء من تكاليف التقاعد الذي سنقوم بتحملها.
```
- **Unit 1** (bertscore_f1=89.66; BLEU=9.20, chrF=22.00, TER=87.10; len_ratio=0.644, num_f1=1.00, acr_f1=0.80, punct_pres=0.26)
  - REF:
```
أنت تُكوّن معنا معاش تقاعدي غير إسهامي (معفى من دفع الأقساط).   
يعود ذلك إلى كونك عاجزاً عن العمل وتتلقى إعانة من وكالة  تأمين الموظفين (UWV) بموجب قانون العجز عن العمل (WAO/WIA) وبناءً عليه، نتكفل نحن بدفع (جزء من) أقساط  معاشك التقاعدي؛ وهذا ما نطلق عليه 'المشاركة المعفاة من الأقساط (PVD)'. تتحدد قيمة القسط الذي نسدده بناءً على " نسبة الإعانة الخاصة بك".
```
  - MT:
```
كنت قد بنيت 'النظام التقاعدي بدون تكاليف' معنا
ذلك لأنك تعذر العمل. و لأنك تتلقى تعويضًا من المؤسسة WAO/WIA. لذلك، نحن (جزء من) تكاليف التقاعد. هذا ما نسميه 'الانضمام بدون تكاليف (PVD)'. ارتفاع تكاليفنا يعتمد على 'نسبة التعويض'.
```
- **Unit 2** (bertscore_f1=90.34; BLEU=3.99, chrF=23.86, TER=89.19; len_ratio=0.622, num_f1=1.00, acr_f1=1.00, punct_pres=0.09)
  - REF:
```
لقد تغيرت (نسبة) مشاركتك المعفاة من الأقساط (PVD) 
بما أنك تتقاضى تعويض عجز عن العمل (WAO/WIA)، فقد زودتنا وكالة  تأمين الموظفين (UWV)  بمعلومات جديدة تتعلق بهذا التعويض و يوضح لك الجدول أدناه ما يعنيه ذلك بالنسبة لوضعك.
```
  - MT:
```
انخفضت PVD الخاصة بك
لديك تعويض WAO/WIA. قدمت المؤسسة UWV لنا معلومات جديدة عن تعويضك. في الجدول التالي، ستجد ماذا يعني ذلك بالنسبة لك.
```
- **Unit 4** (bertscore_f1=91.23; BLEU=12.18, chrF=34.39, TER=71.79; len_ratio=0.796, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
يجب عليك الإبلاغ بنفسك عن أي تغييرات في حالتك من العجز عن العمل.
إذا تلقيت رسالة جديدة من وكالة  تأمين الموظفين (UWV)، فعليك إرسال نسخة من تلك الرسالة إلينا وعندها سيتغيّر الجزء من قسط المعاش التقاعدي الذي نقوم بدفعه.
```
  - MT:
```
يجب أن تبلغنا عن تغيرات تعذرك العمل بنفسك
إذا تلقيت رسالة جديدة من المؤسسة UWV؟ يجب أن ترسل لنا نسخة من هذه الرسالة. إذا تغير الجزء من التكلفة الذي نحن الذين سنقوم بتحملها.
```
- **Unit 0** (bertscore_f1=92.22; BLEU=11.59, chrF=36.81, TER=83.87; len_ratio=0.994, num_f1=1.00, acr_f1=1.00, punct_pres=0.57)
  - REF:
```
تلقينا معلومات من وكالة تأمين الموظفين (UWV) و تتعلق هذه المعلومات الواردة من مؤسسة (UWV) بوضع العجز عن العمل الخاص بك. ستجد في هذا الخطاب توضيحاً لما يعنيه ذلك بالنسبة لك.
```
  - MT:
```
نحن قد получنا معلومات من المؤسسة التنفيذية للضمان الاجتماعي للعمال (UWV). المعلومات التي قدمتها المؤسسة تتعلق بتعذرك العمل. في هذه الرسالة، ستجد ماذا يعني ذلك بالنسبة لك.
```
</details>

### german

<details>
<summary>azure-translator (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=94.67; BLEU=21.78, chrF=53.64, TER=60.42; len_ratio=0.997, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie erwerben bei uns eine "beitragsunabhängige Rente"
Dies liegt daran, dass Sie arbeitsunfähig sind. Und weil Sie eine WAO/WIA-Leistung vom UWV erhalten. Deshalb zahlen wir Ihren Rentenbeitrag (teilweise). Wir nennen das "beitragsfreie Beteiligung" (PVD). Die Höhe der Prämie, die wir zahlen, hängt von Ihrem "Auszahlungsprozentsatz" ab.
```
- **Unit 0** (bertscore_f1=95.17; BLEU=38.01, chrF=60.75, TER=48.00; len_ratio=1.014, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen von der Arbeitnehmerversicherungsanstalt (UWV) erhalten. Die Informationen des UWV beziehen sich auf Ihre Arbeitsunfähigkeit. In diesem Brief können Sie nachlesen, was das für Sie bedeutet.
```
- **Unit 3** (bertscore_f1=95.33; BLEU=42.07, chrF=65.55, TER=40.35; len_ratio=1.026, num_f1=1.00, acr_f1=1.00, punct_pres=0.35)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet das für Ihre PVD?
In der Spalte "Beitragsunabhängiger Rentenanwart" sehen Sie einen Prozentsatz (%). Dies ist der Teil, auf dem Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich Ihr "Auszahlungsprozentsatz"? Dann ändert sich auch der prozentuale Anteil der "beitragsunabhängigen Rentenanwartschaften". Und damit auch den Teil des Rentenbeitrags, den wir zahlen.
```
- **Unit 2** (bertscore_f1=95.65; BLEU=36.25, chrF=58.40, TER=47.06; len_ratio=0.969, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert
Sie haben einen WAO/WIA-Vorteil. Das UWV hat uns neue Informationen über Ihre WAO/WIA-Leistung zur Verfügung gestellt. In der folgenden Übersicht können Sie nachlesen, was das für Sie bedeutet.
```
- **Unit 4** (bertscore_f1=95.94; BLEU=28.27, chrF=61.75, TER=55.88; len_ratio=1.000, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Änderungen Ihrer Arbeitsunfähigkeit müssen Sie selbst melden
Haben Sie einen neuen Brief vom UWV erhalten? Dann müssen Sie uns eine Kopie dieses Schreibens zukommen lassen. Der Teil der Prämie, den wir zahlen, ändert sich dann.
```
</details>

<details>
<summary>deepl (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=95.00; BLEU=31.87, chrF=59.56, TER=54.17; len_ratio=1.029, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen bei uns eine „beitragsfreie Rente” auf
Das liegt daran, dass Sie arbeitsunfähig sind. Und daran, dass Sie eine WAO/WIA-Leistung vom UWV erhalten. Deshalb zahlen wir (einen Teil) Ihrer Rentenbeiträge. Dies bezeichnen wir als „beitragsfreie Teilnahme (PVD)”. Die Höhe des von uns gezahlten Beitrags hängt von Ihrem „Leistungsprozentsatz” ab.
```
- **Unit 3** (bertscore_f1=95.69; BLEU=32.61, chrF=64.14, TER=45.61; len_ratio=1.016, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet das für Ihre PVD?
In der Spalte „Beitragsfreier Rentenaufbau” sehen Sie einen Prozentsatz (%). Dies ist der Anteil, für den Sie PVD erhalten. Diesen Teil der Rentenbeitragszahlung übernehmen wir. Ändert sich Ihr „Leistungsprozentsatz”? Dann ändert sich auch der Prozentsatz des „beitragsfreien Rentenaufbaus”. Und damit auch der Teil der Rentenbeitragszahlung, den wir übernehmen.
```
- **Unit 0** (bertscore_f1=95.96; BLEU=53.64, chrF=72.62, TER=36.00; len_ratio=1.067, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Ausführungsinstitut für Arbeitnehmerversicherungen (UWV) erhalten. Die Informationen des UWV beziehen sich auf Ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was dies für Sie bedeutet.
```
- **Unit 4** (bertscore_f1=96.31; BLEU=24.58, chrF=55.39, TER=52.94; len_ratio=0.960, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden
Erhalten Sie ein neues Schreiben vom UWV? Dann müssen Sie uns eine Kopie dieses Schreibens zusenden. Der Teil der Prämie, den wir bezahlen, ändert sich dann.
```
- **Unit 2** (bertscore_f1=96.38; BLEU=41.44, chrF=59.94, TER=41.18; len_ratio=0.899, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert
Sie beziehen eine WAO/WIA-Leistung. Das UWV hat uns neue Informationen über Ihre WAO/WIA-Leistung übermittelt. In der folgenden Übersicht erfahren Sie, was das für Sie bedeutet.
```
</details>

<details>
<summary>gemini-3-pro (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=95.33; BLEU=33.23, chrF=59.35, TER=54.17; len_ratio=0.962, num_f1=1.00, acr_f1=1.00, punct_pres=0.60)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen bei uns eine „beitragsfreie Rente“ auf
Dies liegt daran, dass Sie arbeitsunfähig sind und eine WAO/WIA-Leistung vom UWV beziehen. Daher übernehmen wir (einen Teil) Ihres Rentenbeitrags. Wir nennen dies „beitragsfreie Teilnahme (PVD)“. Die Höhe des Beitrags, den wir zahlen, hängt von Ihrem „Leistungsprozentsatz“ ab.
```
- **Unit 3** (bertscore_f1=96.14; BLEU=42.22, chrF=67.60, TER=36.84; len_ratio=0.979, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet dies für Ihre PVD?
In der Spalte „Beitragsfreier Rentenaufbau“ sehen Sie einen Prozentsatz (%). Dies ist der Anteil, für den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich Ihr „Leistungsprozentsatz“? Dann ändert sich auch der Prozentsatz des „beitragsfreien Rentenaufbaus“. Und folglich auch der Teil des Rentenbeitrags, den wir übernehmen.
```
- **Unit 4** (bertscore_f1=96.55; BLEU=23.65, chrF=58.40, TER=55.88; len_ratio=0.965, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst mitteilen
Erhalten Sie ein neues Schreiben vom UWV? Dann müssen Sie uns eine Kopie dieses Schreibens senden. Der Teil des Beitrags, den wir zahlen, ändert sich dann.
```
- **Unit 2** (bertscore_f1=97.05; BLEU=58.00, chrF=69.49, TER=29.41; len_ratio=0.907, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert
Sie beziehen eine WAO/WIA-Leistung. Das UWV hat uns neue Informationen zu Ihrer WAO/WIA-Leistung übermittelt. In der unten stehenden Übersicht lesen Sie, was das für Sie bedeutet.
```
- **Unit 0** (bertscore_f1=98.66; BLEU=72.72, chrF=89.64, TER=12.00; len_ratio=1.000, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die Informationen des UWV betreffen Ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was dies für Sie bedeutet.
```
</details>

<details>
<summary>google-translate (worst 5 by bertscore_f1)</summary>

- **Unit 0** (bertscore_f1=91.84; BLEU=16.92, chrF=43.87, TER=68.00; len_ratio=0.905, num_f1=1.00, acr_f1=0.67, punct_pres=0.86)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen von der britischen Arbeitsagentur (UWV) erhalten. Diese Informationen betreffen Ihre Behinderung. Dieses Schreiben erläutert Ihnen die Bedeutung dieser Informationen.
```
- **Unit 4** (bertscore_f1=92.39; BLEU=3.86, chrF=41.19, TER=85.29; len_ratio=1.154, num_f1=1.00, acr_f1=1.00, punct_pres=0.00)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen uns Änderungen Ihres Erwerbsunfähigkeitsstatus selbst melden. Sollten Sie ein neues Schreiben der Arbeitslosenversicherung (UWV) erhalten, senden Sie uns bitte eine Kopie davon. Der von uns zu übernehmende Beitragsanteil ändert sich dann entsprechend.
```
- **Unit 3** (bertscore_f1=92.75; BLEU=15.41, chrF=47.66, TER=66.67; len_ratio=1.044, num_f1=1.00, acr_f1=1.00, punct_pres=0.55)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet dies für Ihre PVD?
In der Spalte „Beitragsfreie Rentenanwartschaft“ sehen Sie einen Prozentsatz (%). Dies ist der Anteil der Rentenbeiträge, den Sie erhalten. Wir übernehmen diesen Anteil der Rentenbeiträge. Ändert sich Ihr Leistungsanspruch? Der Prozentsatz der beitragsfreien Rentenansprüche ändert sich ebenfalls. Dies betrifft auch den Anteil der von uns zu übernehmenden Rentenbeiträge.
```
- **Unit 1** (bertscore_f1=92.93; BLEU=16.56, chrF=44.72, TER=75.00; len_ratio=1.044, num_f1=1.00, acr_f1=1.00, punct_pres=0.53)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie erwerben bei uns eine beitragsfreie Rente.
Dies liegt an Ihrer Behinderung und daran, dass Sie Leistungen nach dem Waisenprogramm WAO/WIA von der UWV beziehen. Daher übernehmen wir einen Teil Ihrer Rentenbeiträge. Dies wird als beitragsfreie Teilnahme (PVD) bezeichnet. Die Höhe des von uns übernommenen Beitrags hängt von Ihrem Leistungsanspruch ab.
```
- **Unit 2** (bertscore_f1=95.46; BLEU=28.33, chrF=51.01, TER=58.82; len_ratio=1.150, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert.
Sie beziehen Leistungen nach dem Waisenprogramm WAO/WIA. Die UWV hat uns neue Informationen zu Ihren Leistungen nach dem Waisenprogramm WAO/WIA übermittelt. Die folgende Übersicht erläutert die Bedeutung dieser Informationen für Sie.
```
</details>

<details>
<summary>gpt-4 (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=95.18; BLEU=36.95, chrF=61.63, TER=45.83; len_ratio=0.953, num_f1=1.00, acr_f1=0.67, punct_pres=0.40)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen bei uns 'beitragsfreie Rente' auf
Das liegt daran, dass Sie arbeitsunfähig sind und eine WAO/WIA-Leistung vom UWV erhalten. Deshalb zahlen wir (einen Teil) Ihrer Rentenversicherungsbeiträge. Das nennen wir 'beitragsfreie Teilnahme (BFT)'. Die Höhe des Beitrags, den wir zahlen, hängt von Ihrem 'Leistungssatz' ab.
```
- **Unit 3** (bertscore_f1=95.93; BLEU=29.51, chrF=57.40, TER=45.61; len_ratio=1.018, num_f1=1.00, acr_f1=0.00, punct_pres=0.35)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet das für Ihre BFT?
In der Spalte 'Beitragsfreie Rentenbildung' sehen Sie einen Prozentsatz (%) stehen. Das ist der Teil, für den Sie BFT erhalten. Diesen Teil der Rentenversicherungsbeiträge zahlen wir. Ändert sich Ihr 'Leistungssatz'? Dann ändert sich auch der Prozentsatz der 'beitragsfreien Rentenbildung'. Und somit auch der Teil des Rentenversicherungsbeitrags, den wir zahlen.
```
- **Unit 2** (bertscore_f1=96.23; BLEU=38.94, chrF=58.79, TER=41.18; len_ratio=0.881, num_f1=1.00, acr_f1=0.67, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre BFT hat sich geändert
Sie erhalten eine WAO/WIA-Leistung. Das UWV hat uns neue Informationen über Ihre WAO/WIA-Leistung gegeben. In der folgenden Übersicht erfahren Sie, was das für Sie bedeutet.
```
- **Unit 4** (bertscore_f1=97.17; BLEU=47.79, chrF=74.18, TER=38.24; len_ratio=0.938, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden
Erhalten Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken. Der Teil des Beitrags, den wir zahlen, ändert sich dann.
```
- **Unit 0** (bertscore_f1=98.13; BLEU=58.06, chrF=83.98, TER=16.00; len_ratio=0.986, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Diese Informationen des UWV betreffen Ihre Arbeitsunfähigkeit. In diesem Brief erfahren Sie, was das für Sie bedeutet.
```
</details>

<details>
<summary>gpt-5-2 (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=95.85; BLEU=43.27, chrF=68.68, TER=39.58; len_ratio=1.006, num_f1=1.00, acr_f1=1.00, punct_pres=0.53)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen bei uns eine „beitragsfreie Altersvorsorge“ auf
Das liegt daran, dass Sie arbeitsunfähig sind. Und weil Sie eine WAO/WIA-Leistung vom UWV erhalten. Deshalb zahlen wir (einen Teil) Ihres Rentenbeitrags. Das nennen wir „beitragsfreie Teilnahme (PVD)“. Die Höhe des Beitrags, den wir zahlen, hängt von Ihrem „Leistungsprozentsatz“ ab.
```
- **Unit 3** (bertscore_f1=96.35; BLEU=41.04, chrF=67.93, TER=36.84; len_ratio=0.961, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet das für Ihre PVD?
In der Spalte „Beitragsfreie Rentenaufbau“ sehen Sie einen Prozentsatz (%) stehen. Dies ist der Anteil, für den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich Ihr „Leistungsprozentsatz“? Dann ändert sich auch der Prozentsatz „beitragsfreier Rentenaufbau“. Und damit auch der Teil des Rentenbeitrags, den wir zahlen.
```
- **Unit 4** (bertscore_f1=96.86; BLEU=27.91, chrF=63.18, TER=50.00; len_ratio=0.960, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden
Erhalten Sie ein neues Schreiben vom UWV? Dann müssen Sie uns eine Kopie dieses Schreibens schicken. Der Teil des Beitrags, den wir zahlen, ändert sich dann.
```
- **Unit 2** (bertscore_f1=96.99; BLEU=51.95, chrF=68.10, TER=32.35; len_ratio=0.881, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert
Sie erhalten eine WAO/WIA-Leistung. Das UWV hat uns neue Informationen zu Ihrer WAO/WIA-Leistung gegeben. In der nachstehenden Übersicht lesen Sie, was das für Sie bedeutet.
```
- **Unit 0** (bertscore_f1=98.30; BLEU=66.72, chrF=87.05, TER=12.00; len_ratio=0.981, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die Informationen des UWV betreffen Ihre Arbeitsunfähigkeit. In diesem Schreiben lesen Sie, was das für Sie bedeutet.
```
</details>

<details>
<summary>llama-3-3-70b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=95.10; BLEU=34.41, chrF=58.85, TER=47.92; len_ratio=0.965, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen bei uns "beitragsfreies Rentenkapital" auf
Das liegt daran, dass Sie arbeitsunfähig sind. Und weil Sie eine WAO/WIA-Rente vom UWV erhalten. Deshalb zahlen wir (einen Teil) Ihrer Rentenprämie. Wir nennen dies "beitragsfreie Teilnahme (PVD)". Die Höhe der Prämie, die wir zahlen, hängt von Ihrem "Rentenprozentsatz" ab.
```
- **Unit 0** (bertscore_f1=95.43; BLEU=43.02, chrF=65.02, TER=44.00; len_ratio=1.005, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Institut für die Arbeitslosenversicherung (UWV) erhalten. Die Informationen des UWV beziehen sich auf Ihre Arbeitsunfähigkeit. In diesem Brief erfahren Sie, was dies für Sie bedeutet.
```
- **Unit 3** (bertscore_f1=95.82; BLEU=34.48, chrF=59.09, TER=40.35; len_ratio=0.990, num_f1=1.00, acr_f1=1.00, punct_pres=0.35)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet dies für Ihre PVD?
In der Spalte "Beitragsfreie Rentenanspruchsbildung" sehen Sie einen Prozentsatz (%) stehen. Dies ist der Teil, für den Sie PVD erhalten. Diesen Teil der Rentenprämie zahlen wir. Ändert sich Ihr "Rentenprozentsatz"? Dann ändert sich auch der Prozentsatz "beitragsfreie Rentenanspruchsbildung". Und damit auch der Teil der Rentenprämie, den wir zahlen.
```
- **Unit 2** (bertscore_f1=96.02; BLEU=38.61, chrF=54.87, TER=44.12; len_ratio=0.846, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert
Sie haben eine WAO/WIA-Rente. Das UWV hat uns neue Informationen über Ihre WAO/WIA-Rente gegeben. In der folgenden Übersicht erfahren Sie, was dies für Sie bedeutet.
```
- **Unit 4** (bertscore_f1=96.85; BLEU=46.75, chrF=70.64, TER=38.24; len_ratio=0.930, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden
Erhalten Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken. Der Teil der Prämie, den wir zahlen, ändert sich dann.
```
</details>

<details>
<summary>meta-llama-3-1-405b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 1** (bertscore_f1=96.09; BLEU=44.01, chrF=69.44, TER=39.58; len_ratio=0.994, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen bei uns eine "beitragsfreie Rente" auf
Das liegt daran, dass Sie arbeitsunfähig sind. Und weil Sie eine WAO/WIA-Auszahlung vom UWV erhalten. Deshalb zahlen wir (einen Teil) Ihrer Rentenbeiträge. Dies nennen wir "beitragsfreie Teilnahme (PVD)". Die Höhe des Beitrags, den wir zahlen, hängt von Ihrem "Auszahlungsprozentsatz" ab.
```
- **Unit 0** (bertscore_f1=96.22; BLEU=44.17, chrF=67.56, TER=32.00; len_ratio=0.995, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Ausführungsinstitut für Arbeitnehmerversicherungen (UWV) erhalten. Die Informationen des UWV betreffen Ihre Arbeitsunfähigkeit. In diesem Brief lesen Sie, was dies für Sie bedeutet.
```
- **Unit 3** (bertscore_f1=96.22; BLEU=34.66, chrF=63.62, TER=40.35; len_ratio=0.964, num_f1=1.00, acr_f1=1.00, punct_pres=0.35)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet dies für Ihre PVD?
In der Spalte "Beitragsfreie Rentenaufbau" sehen Sie einen Prozentsatz (%) stehen. Dies ist der Teil, für den Sie PVD erhalten. Diesen Teil der Rentenbeiträge zahlen wir. Ändert sich Ihr "Auszahlungsprozentsatz"? Dann ändert sich auch der Prozentsatz "beitragsfreier Rentenaufbau". Und damit auch der Teil der Rentenbeiträge, den wir zahlen.
```
- **Unit 2** (bertscore_f1=96.25; BLEU=43.85, chrF=57.86, TER=41.18; len_ratio=0.877, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD hat sich geändert
Sie haben eine WAO/WIA-Auszahlung. Das UWV hat uns neue Informationen über Ihre WAO/WIA-Auszahlung gegeben. In der folgenden Übersicht lesen Sie, was dies für Sie bedeutet.
```
- **Unit 4** (bertscore_f1=96.89; BLEU=39.34, chrF=68.43, TER=44.12; len_ratio=0.943, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst mitteilen
Erhalten Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes senden. Der Teil des Beitrags, den wir zahlen, ändert sich dann.
```
</details>

<details>
<summary>meta-llama-3-1-8b-instruct (worst 5 by bertscore_f1)</summary>

- **Unit 3** (bertscore_f1=94.09; BLEU=22.83, chrF=51.81, TER=49.12; len_ratio=0.948, num_f1=1.00, acr_f1=1.00, punct_pres=0.35)
  - REF:
```
Was bedeutet dies für Ihre PVD?
In der Spalte ‘Beitragsfreier Pensions-Aufbau´ finden Sie eine Angabe in Prozent (%). Das ist der Teil,
auf den Sie PVD erhalten. Diesen Teil des Rentenbeitrags zahlen wir. Ändert sich ihre ‘Auszahlungs
Prozente’? Dann ändert sich auch der Prozentsatz ‘beitragsfreier Pensions-Aufbau’. Und damit dann
auch der Anteil des Rentenbeitrags, den wir bezahlen.
```
  - MT:
```
Was bedeutet das für Ihre PVD?
In der Spalte 'Premievrije pensioenopbouw' sehen Sie ein Prozentsatz (%) stehen. Das ist das Teil, für das Sie PVD erhalten. Dieser Teil der Rentenprämie zahlen wir. Verändert sich Ihr 'Auszahlungsprozentsatz'? Dann ändert sich auch das Prozentsatz 'premievrije pensioenopbouw'. Und damit auch der Teil der Rentenprämie, den wir zahlen.
```
- **Unit 1** (bertscore_f1=94.74; BLEU=32.25, chrF=53.56, TER=50.00; len_ratio=0.944, num_f1=1.00, acr_f1=1.00, punct_pres=0.33)
  - REF:
```
Sie bauen beitragsfreie Pension bei uns auf
Das liegt daran, dass sie arbeitsunfähig sind. Und weil Sie Sozialleistungen nach WAO/WIA-von der
UWV erhalten. Darum zahlen wir (einen Teil) ihres Rentenbeitrags Dies nennen wir beitragsfreie
Teilnahme (PVD)’. Die Höhe des Beitrags, den wir zahlen ist abhängig von Ihren
`Auszahlungsprozenten’.
```
  - MT:
```
Sie bauen 'premievrije pensioen' bei uns auf
Das liegt daran, dass Sie arbeitsunfähig sind. Und weil Sie eine WAO/WIA-Rente vom UWV erhalten. Deshalb zahlen wir (einen Teil Ihrer) Rentenprämie. Wir nennen das 'premievrije deelname (PVD)'. Die Höhe der Prämie, die wir zahlen, hängt von Ihrem 'Auszahlungsprozentsatz' ab.
```
- **Unit 2** (bertscore_f1=95.62; BLEU=33.08, chrF=50.87, TER=52.94; len_ratio=0.833, num_f1=1.00, acr_f1=1.00, punct_pres=0.71)
  - REF:
```
Ihre PVD hat sich geändert
Sie erhalten Sozialleistungen nach WAO/WIA. Das UWV hat uns neue Informationen zu ihren
Sozialleistungen nach WAO/WIA mitgeteilt. In der unten stehenden Übersicht lesen Sie, was das für Sie
bedeutet.
```
  - MT:
```
Ihre PVD ist geändert worden
Sie erhalten eine WAO/WIA-Rente. Das UWV hat uns neue Informationen über Ihre WAO/WIA-Rente gegeben. Im folgenden Überblick lesen Sie, was das für Sie bedeutet.
```
- **Unit 4** (bertscore_f1=96.56; BLEU=27.11, chrF=61.91, TER=50.00; len_ratio=0.912, num_f1=1.00, acr_f1=1.00, punct_pres=0.50)
  - REF:
```
Sie müssen Veränderungen Ihrer Arbeitsunfähigkeit selbst melden
Bekommen Sie einen neuen Brief vom UWV? Dann müssen Sie uns eine Kopie dieses Briefes schicken.
Dann verändert sich der Anteil des Beitrags Komma den wir zahlen.
```
  - MT:
```
Sie müssen Änderungen Ihrer Arbeitsunfähigkeit selbst melden
Erhalten Sie eine neue Brief vom UWV? Dann müssen Sie uns eine Kopie dieser Brief schicken. Der Teil der Prämie, den wir zahlen, ändert sich dann.
```
- **Unit 0** (bertscore_f1=97.31; BLEU=47.46, chrF=75.26, TER=48.00; len_ratio=1.100, num_f1=1.00, acr_f1=0.67, punct_pres=1.00)
  - REF:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die
Informationen des UWG betreffen ihre Arbeitsunfähigkeit. In diesem Schreiben erfahren Sie, was das
für Sie bedeutet.
```
  - MT:
```
Wir haben Informationen vom Uitvoeringsinstituut Werknemersverzekeringen (UWV) erhalten. Die Informationen des UWV beziehen sich auf Ihre Arbeitsunfähigkeit. In dieser Brief werden Sie darüber informiert, was dies für Sie bedeutet.
```
</details>
