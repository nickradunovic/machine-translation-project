#!/usr/bin/env python3
"""
Generate translations for the Dutch source text in:
  translations_ref_based/dutch_original_text.txt

Outputs are written to:
  translations_ref_based/<model-slug>/<language>.txt

Models:
- Llama-3.3-70B-Instruct
- Meta-Llama-3.1-405B-Instruct
- Meta-Llama-3.1-8B-Instruct
- gpt-4
- gpt-5.2
- azure-translator

This script uses:
- Azure OpenAI / Azure AI Foundry OpenAI-compatible Chat Completions API
- Microsoft Translator Text API

Usage:
  python translate_script.py
  python translate_script.py --env-file .env
  python translate_script.py --input translations_ref_based/dutch_original_text.txt \
      --output-dir translations_ref_based
"""

from __future__ import annotations

import argparse
import os
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

import requests
from openai import APIError, APITimeoutError, BadRequestError, OpenAI, RateLimitError


SCRIPT_DIR = Path(__file__).resolve().parent
SOURCE_PATH_DEFAULT = SCRIPT_DIR / "translations_ref_based" / "dutch_original_text.txt"
OUTPUT_DIR_DEFAULT = SCRIPT_DIR / "translations_ref_based"
MAX_TOKENS = 2048
TEMPERATURE = 0
TOP_P = 1
SEED = 0


LANGUAGES: Dict[str, str] = {
    "turkish": "Turkish",
    "spanish": "Spanish",
    "english": "English",
    "polish": "Polish",
    "ukrainian": "Ukrainian",
    "arabic": "Arabic",
    "german": "German",
}

LANGUAGE_ABBREVIATIONS: Dict[str, str] = {
    "turkish": "tr",
    "spanish": "es",
    "english": "en",
    "polish": "pl",
    "ukrainian": "uk",
    "arabic": "ar",
    "german": "de",
}


@dataclass(frozen=True)
class ModelSpec:
    logical_name: str
    output_dir_name: str
    api_path: str
    client_name: str | None
    env_var_name: str | None
    token_limit_param: str = "max_tokens"
    reasoning_effort: str | None = None


MODEL_SPECS = (
    ModelSpec(
        logical_name="Llama-3.3-70B-Instruct",
        output_dir_name="llama-3-3-70b-instruct",
        api_path="chat_completions",
        client_name="primary",
        env_var_name="TRANSLATE_MODEL_LLAMA_3_3_70B",
    ),
    ModelSpec(
        logical_name="Meta-Llama-3.1-405B-Instruct",
        output_dir_name="meta-llama-3-1-405b-instruct",
        api_path="chat_completions",
        client_name="primary",
        env_var_name="TRANSLATE_MODEL_META_LLAMA_3_1_405B",
    ),
    ModelSpec(
        logical_name="Meta-Llama-3.1-8B-Instruct",
        output_dir_name="meta-llama-3-1-8b-instruct",
        api_path="chat_completions",
        client_name="primary",
        env_var_name="TRANSLATE_MODEL_META_LLAMA_3_1_8B",
    ),
    ModelSpec(
        logical_name="gpt-4",
        output_dir_name="gpt-4",
        api_path="chat_completions",
        client_name="primary",
        env_var_name="TRANSLATE_MODEL_GPT_4",
    ),
    ModelSpec(
        logical_name="gpt-5.2",
        output_dir_name="gpt-5-2",
        api_path="chat_completions",
        client_name="primary",
        env_var_name="TRANSLATE_MODEL_GPT_5_2",
        token_limit_param="max_completion_tokens",
        reasoning_effort="none",
    ),
    ModelSpec(
        logical_name="azure-translator",
        output_dir_name="azure-translator",
        api_path="microsoft_translator_text_api",
        client_name=None,
        env_var_name=None,
    ),
)


def load_dotenv_file(env_path: Path) -> None:
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if value and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]

        os.environ.setdefault(key, value)


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def normalize_openai_v1_base_url(raw_endpoint: str) -> str:
    endpoint = raw_endpoint.strip().rstrip("/")
    if not endpoint.endswith("/openai/v1"):
        endpoint = endpoint + "/openai/v1"
    return endpoint + "/"


def build_messages(dutch_text: str, target_language: str) -> list[dict[str, str]]:
    prompt = (
        f"Act as a diligent professional translator that translates text into {target_language}.\n"
        "Preserve meaning completely, keep the original tone/register and style, and ensure fluent readability.\n\n"
        "Translate the following text:\n"
        f"{dutch_text}"
    )

    return [
        {
            "role": "user",
            "content": prompt,
        },
    ]


def call_with_retries(fn, *, max_attempts: int = 5, base_sleep_s: float = 1.0):
    last_err: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            return fn()
        except BadRequestError:
            raise
        except (RateLimitError, APITimeoutError, APIError, requests.RequestException) as err:
            last_err = err
            if attempt == max_attempts:
                break
            time.sleep(base_sleep_s * (2 ** (attempt - 1)))
        except Exception as err:
            last_err = err
            if attempt == max_attempts:
                break
            time.sleep(base_sleep_s * (2 ** (attempt - 1)))

    raise RuntimeError(f"Request failed after {max_attempts} attempts: {last_err}") from last_err


def translate_with_chat_completions(
    client: OpenAI,
    deployed_model_name: str,
    dutch_text: str,
    target_language: str,
    token_limit_param: str,
    reasoning_effort: str | None,
) -> str:
    messages = build_messages(dutch_text, target_language)

    request_kwargs = {
        "model": deployed_model_name,
        "messages": messages,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "seed": SEED,
    }
    extra_body = {}

    if token_limit_param == "max_tokens":
        request_kwargs["max_tokens"] = MAX_TOKENS
    elif token_limit_param == "max_completion_tokens":
        # Kept in extra_body for compatibility with older openai-python
        # versions while still sending the modern Chat Completions field.
        extra_body["max_completion_tokens"] = MAX_TOKENS
    else:
        raise RuntimeError(f"Unsupported token limit parameter: {token_limit_param}")

    if reasoning_effort is not None:
        # reasoning_effort is a Chat Completions field for reasoning models.
        # The value must be a string such as "none", not Python None.
        extra_body["reasoning_effort"] = reasoning_effort

    if extra_body:
        request_kwargs["extra_body"] = extra_body

    def _do_call():
        return client.chat.completions.create(**request_kwargs)

    response = call_with_retries(_do_call)
    text = (response.choices[0].message.content or "").strip()
    if not text:
        raise RuntimeError(f"Empty content returned for model={deployed_model_name}")
    return text + "\n"


def translate_with_azure_translator(dutch_text: str, target_language_code: str) -> str:
    translator_url = require_env("TRANSLATE_URL")
    translator_key = require_env("TRANSLATE_KEY")
    translator_region = os.getenv("TRANSLATE_REGION", "westeurope").strip() or "westeurope"

    headers = {
        "Ocp-Apim-Subscription-Key": translator_key,
        "Ocp-Apim-Subscription-Region": translator_region,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }
    params = {
        "api-version": "3.0",
        "from": "nl",
        "to": target_language_code,
    }
    body = [{"Text": dutch_text}]

    def _do_call():
        response = requests.post(
            translator_url,
            params=params,
            headers=headers,
            json=body,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    payload = call_with_retries(_do_call)
    text = payload[0]["translations"][0]["text"].strip()
    if not text:
        raise RuntimeError("Empty content returned for azure-translator")
    return text + "\n"


def build_openai_clients() -> dict[str, OpenAI]:
    primary_endpoint = require_env("TRANSLATE_ENDPOINT_PRIMARY")
    primary_key = require_env("TRANSLATE_API_KEY_PRIMARY")

    return {
        "primary": OpenAI(
            api_key=primary_key,
            base_url=normalize_openai_v1_base_url(primary_endpoint),
        ),
    }


def resolve_deployed_model_name(spec: ModelSpec) -> str:
    if spec.env_var_name is None:
        raise RuntimeError(f"No deployment env var configured for model '{spec.logical_name}'")
    return os.getenv(spec.env_var_name, spec.logical_name).strip() or spec.logical_name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate translations for the reference-based corpus.")
    parser.add_argument(
        "--env-file",
        default=os.getenv("TRANSLATE_ENV_FILE", ".env"),
        help="Optional env file to load before reading environment variables.",
    )
    parser.add_argument(
        "--input",
        default=str(SOURCE_PATH_DEFAULT),
        help="Path to the Dutch source file.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(OUTPUT_DIR_DEFAULT),
        help="Output directory for generated translations.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    env_file = Path(args.env_file)
    if not env_file.is_absolute():
        env_file = SCRIPT_DIR / env_file
    load_dotenv_file(env_file)

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    if not input_path.is_absolute():
        input_path = SCRIPT_DIR / input_path
    if not output_dir.is_absolute():
        output_dir = SCRIPT_DIR / output_dir

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    dutch_text = input_path.read_text(encoding="utf-8").strip()
    if not dutch_text:
        raise ValueError(f"Input file is empty: {input_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    clients = build_openai_clients()

    for spec in MODEL_SPECS:
        model_output_dir = output_dir / spec.output_dir_name
        model_output_dir.mkdir(parents=True, exist_ok=True)

        deployed_model_name = resolve_deployed_model_name(spec) if spec.api_path == "chat_completions" else None

        for language_slug, language_name in LANGUAGES.items():
            print(f"[{spec.logical_name}] Translating -> {language_slug} ...")

            if spec.api_path == "chat_completions":
                if spec.client_name is None:
                    raise RuntimeError(f"No client configured for model '{spec.logical_name}'")
                translation = translate_with_chat_completions(
                    client=clients[spec.client_name],
                    deployed_model_name=deployed_model_name,
                    dutch_text=dutch_text,
                    target_language=language_name,
                    token_limit_param=spec.token_limit_param,
                    reasoning_effort=spec.reasoning_effort,
                )
            elif spec.api_path == "microsoft_translator_text_api":
                translation = translate_with_azure_translator(
                    dutch_text=dutch_text,
                    target_language_code=LANGUAGE_ABBREVIATIONS[language_slug],
                )
            else:
                raise RuntimeError(f"Unsupported api_path: {spec.api_path}")

            out_path = model_output_dir / f"{language_slug}.txt"
            out_path.write_text(translation, encoding="utf-8")
            print(f"  wrote {out_path}")

    print("Done.")


if __name__ == "__main__":
    main()
