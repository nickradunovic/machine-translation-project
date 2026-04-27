# Diagnostics

- Root: `translations_ref_based`
- Output: `out_translation_eval_v2`
- Models discovered: 9
- Languages (with references): 7
- Metrics requested: bleu, chrf, ter, bertscore, comet

## Missing files

- None

## Paragraph counts and alignment

| Model | Language | Sys paras | Ref paras | Units | Sys merges | Ref merges | Len ratio (mean) | Doc char ratio | Sys enc | Ref enc |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| azure-translator | turkish | 5 | 5 | 5 | 0 | 0 | 0.857 | 0.862 | utf-8 | utf-8 |
| deepl | turkish | 5 | 5 | 5 | 0 | 0 | 0.869 | 0.875 | utf-8 | utf-8 |
| gemini-3-pro | turkish | 5 | 5 | 5 | 0 | 0 | 0.912 | 0.918 | utf-8 | utf-8 |
| google-translate | turkish | 5 | 5 | 5 | 0 | 0 | 0.892 | 0.903 | utf-8 | utf-8 |
| gpt-4 | turkish | 5 | 5 | 5 | 0 | 0 | 0.894 | 0.893 | utf-8 | utf-8 |
| gpt-5-2 | turkish | 5 | 5 | 5 | 0 | 0 | 0.882 | 0.886 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | turkish | 5 | 5 | 5 | 0 | 0 | 0.959 | 0.957 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | turkish | 5 | 5 | 5 | 0 | 0 | 0.853 | 0.855 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | turkish | 5 | 5 | 5 | 0 | 0 | 0.976 | 1.004 | utf-8 | utf-8 |
| azure-translator | spanish | 5 | 5 | 5 | 0 | 0 | 0.952 | 0.947 | utf-8 | utf-8 |
| deepl | spanish | 5 | 5 | 5 | 0 | 0 | 0.958 | 0.946 | utf-8 | utf-8 |
| gemini-3-pro | spanish | 5 | 5 | 5 | 0 | 0 | 0.994 | 0.989 | utf-8 | utf-8 |
| google-translate | spanish | 5 | 5 | 5 | 0 | 0 | 0.933 | 0.922 | utf-8 | utf-8 |
| gpt-4 | spanish | 5 | 5 | 5 | 0 | 0 | 1.001 | 0.996 | utf-8 | utf-8 |
| gpt-5-2 | spanish | 5 | 5 | 5 | 0 | 0 | 0.974 | 0.964 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | spanish | 5 | 5 | 5 | 0 | 0 | 0.943 | 0.933 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | spanish | 5 | 5 | 5 | 0 | 0 | 0.950 | 0.952 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | spanish | 5 | 5 | 5 | 0 | 0 | 0.933 | 0.928 | utf-8 | utf-8 |
| azure-translator | english | 5 | 5 | 5 | 0 | 0 | 0.878 | 0.870 | utf-8 | utf-8 |
| deepl | english | 5 | 5 | 5 | 0 | 0 | 0.855 | 0.845 | utf-8 | utf-8 |
| gemini-3-pro | english | 5 | 5 | 5 | 0 | 0 | 0.874 | 0.867 | utf-8 | utf-8 |
| google-translate | english | 5 | 5 | 5 | 0 | 0 | 0.860 | 0.846 | utf-8 | utf-8 |
| gpt-4 | english | 5 | 5 | 5 | 0 | 0 | 0.889 | 0.878 | utf-8 | utf-8 |
| gpt-5-2 | english | 5 | 5 | 5 | 0 | 0 | 0.854 | 0.840 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | english | 5 | 5 | 5 | 0 | 0 | 0.869 | 0.854 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | english | 5 | 5 | 5 | 0 | 0 | 0.874 | 0.860 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | english | 5 | 5 | 5 | 0 | 0 | 0.847 | 0.835 | utf-8 | utf-8 |
| azure-translator | polish | 5 | 5 | 5 | 0 | 0 | 0.865 | 0.855 | utf-8 | utf-8 |
| deepl | polish | 5 | 5 | 5 | 0 | 0 | 0.913 | 0.902 | utf-8 | utf-8 |
| gemini-3-pro | polish | 5 | 5 | 5 | 0 | 0 | 0.911 | 0.909 | utf-8 | utf-8 |
| google-translate | polish | 5 | 5 | 5 | 0 | 0 | 0.874 | 0.875 | utf-8 | utf-8 |
| gpt-4 | polish | 5 | 5 | 5 | 0 | 0 | 0.971 | 0.963 | utf-8 | utf-8 |
| gpt-5-2 | polish | 5 | 5 | 5 | 0 | 0 | 0.929 | 0.923 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | polish | 5 | 5 | 5 | 0 | 0 | 0.910 | 0.893 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | polish | 5 | 5 | 5 | 0 | 0 | 0.838 | 0.829 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | polish | 5 | 5 | 5 | 0 | 0 | 0.822 | 0.821 | utf-8 | utf-8 |
| azure-translator | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.719 | 0.695 | utf-8 | utf-8 |
| deepl | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.698 | 0.681 | utf-8 | utf-8 |
| gemini-3-pro | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.736 | 0.723 | utf-8 | utf-8 |
| google-translate | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.752 | 0.721 | utf-8 | utf-8 |
| gpt-4 | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.704 | 0.684 | utf-8 | utf-8 |
| gpt-5-2 | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.716 | 0.694 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.721 | 0.706 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.738 | 0.718 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | ukrainian | 5 | 5 | 5 | 0 | 0 | 0.799 | 0.778 | utf-8 | utf-8 |
| azure-translator | arabic | 5 | 5 | 5 | 0 | 0 | 0.790 | 0.790 | utf-8 | utf-8 |
| deepl | arabic | 5 | 5 | 5 | 0 | 0 | 0.815 | 0.794 | utf-8 | utf-8 |
| gemini-3-pro | arabic | 5 | 5 | 5 | 0 | 0 | 0.881 | 0.869 | utf-8 | utf-8 |
| google-translate | arabic | 5 | 5 | 5 | 0 | 0 | 0.801 | 0.815 | utf-8 | utf-8 |
| gpt-4 | arabic | 5 | 5 | 5 | 0 | 0 | 0.795 | 0.787 | utf-8 | utf-8 |
| gpt-5-2 | arabic | 5 | 5 | 5 | 0 | 0 | 0.756 | 0.754 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | arabic | 5 | 5 | 5 | 0 | 0 | 0.706 | 0.694 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | arabic | 5 | 5 | 5 | 0 | 0 | 0.711 | 0.722 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | arabic | 5 | 5 | 5 | 0 | 0 | 0.752 | 0.726 | utf-8 | utf-8 |
| azure-translator | german | 5 | 5 | 5 | 0 | 0 | 1.001 | 1.004 | utf-8 | utf-8 |
| deepl | german | 5 | 5 | 5 | 0 | 0 | 0.994 | 0.999 | utf-8 | utf-8 |
| gemini-3-pro | german | 5 | 5 | 5 | 0 | 0 | 0.963 | 0.964 | utf-8 | utf-8 |
| google-translate | german | 5 | 5 | 5 | 0 | 0 | 1.059 | 1.058 | utf-8 | utf-8 |
| gpt-4 | german | 5 | 5 | 5 | 0 | 0 | 0.955 | 0.962 | utf-8 | utf-8 |
| gpt-5-2 | german | 5 | 5 | 5 | 0 | 0 | 0.958 | 0.962 | utf-8 | utf-8 |
| llama-3-3-70b-instruct | german | 5 | 5 | 5 | 0 | 0 | 0.947 | 0.953 | utf-8 | utf-8 |
| meta-llama-3-1-405b-instruct | german | 5 | 5 | 5 | 0 | 0 | 0.955 | 0.958 | utf-8 | utf-8 |
| meta-llama-3-1-8b-instruct | german | 5 | 5 | 5 | 0 | 0 | 0.947 | 0.945 | utf-8 | utf-8 |

## Mismatch summaries

- None
