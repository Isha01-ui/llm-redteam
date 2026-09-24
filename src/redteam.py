"""
LLM Red-Team Engine

Runs a suite of adversarial prompts against an OpenAI-compatible model,
scores each response, and produces a structured security report.

Usage:
    python src/redteam.py --model gpt-3.5-turbo
    python src/redteam.py --model gpt-4o --categories "Jailbreak,Prompt Injection"
    python src/redteam.py --list-attacks
"""

from __future__ import annotations

import argparse
import os
import sys
import time

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: openai package not found. Run: pip install openai")
    sys.exit(1)

from attacks import ATTACKS
from scorer import score_response, summarise_results
from reporter import build_report, save_json, print_summary


DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer user questions accurately and concisely."
)
REQUEST_DELAY = 1.0
MAX_TOKENS = 512


def run_attack(client: OpenAI, attack: dict, model: str, system_prompt: str) -> dict:
    print(f"  → [{attack['id']}] {attack['name']} ...", end=" ", flush=True)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": attack["prompt"]},
            ],
            max_tokens=MAX_TOKENS,
            temperature=0.7,
        )
        response_text = response.choices[0].message.content or ""
    except Exception as e:
        print(f"ERROR ({e})")
        return {
            **attack,
            "verdict": "ERROR",
            "confidence": 0.0,
            "matched_indicators": [],
            "matched_safe": [],
            "response_length": 0,
            "response_preview": "",
            "notes": f"API error: {e}",
        }

    score = score_response(attack, response_text)
    print(score["verdict"])

    return {
        "id": attack["id"],
        "category": attack["category"],
        "name": attack["name"],
        "tactic": attack["tactic"],
        "response_preview": response_text[:300].replace("\n", " "),
        **score,
    }


def run_suite(
    model: str,
    categories: list[str] | None = None,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    output_path: str = "report/redteam_report.json",
) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    attacks_to_run = ATTACKS
    if categories:
        cat_lower = [c.lower() for c in categories]
        attacks_to_run = [a for a in ATTACKS if a["category"].lower() in cat_lower]
        if not attacks_to_run:
            print(f"No attacks found for categories: {categories}")
            sys.exit(1)

    print(f"\n{'─'*60}")
    print(f"  LLM Red-Team Tool  |  Model: {model}")
    print(f"  Framework: MITRE ATLAS")
    print(f"  Attacks: {len(attacks_to_run)}")
    print(f"{'─'*60}\n")

    results = []
    for i, attack in enumerate(attacks_to_run):
        result = run_attack(client, attack, model, system_prompt)
        results.append(result)
        if i < len(attacks_to_run) - 1:
            time.sleep(REQUEST_DELAY)

    summary = summarise_results(results)
    report = build_report(model=model, results=results, summary=summary)
    save_json(report, output_path)
    print_summary(report)

    return report


def list_attacks() -> None:
    print(f"\n{'─'*60}")
    print(f"  {'ID':<10} {'Category':<25} {'Name'}")
    print(f"{'─'*60}")
    for a in ATTACKS:
        print(f"  {a['id']:<10} {a['category']:<25} {a['name']}")
    print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="LLM Red-Team Tool — test LLMs against MITRE ATLAS attack tactics",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--categories")
    parser.add_argument("--system-prompt", default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--output", default="report/redteam_report.json")
    parser.add_argument("--list-attacks", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.list_attacks:
        list_attacks()
        sys.exit(0)

    categories = None
    if args.categories:
        categories = [c.strip() for c in args.categories.split(",")]

    run_suite(
        model=args.model,
        categories=categories,
        system_prompt=args.system_prompt,
        output_path=args.output,
    )
