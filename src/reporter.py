"""
Report generation for LLM red-teaming results.
Builds a structured JSON report and prints a human-readable summary.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone


def build_report(model: str, results: list[dict], summary: dict) -> dict:
    """Build the full JSON report structure."""
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return {
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_under_test": model,
        "framework": "MITRE ATLAS",
        "summary": summary,
        "results": results,
    }


def save_json(report: dict, path: str) -> None:
    """Save the report as a JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Report saved → {path}")


def print_summary(report: dict) -> None:
    """Print a human-readable summary to stdout."""
    s = report["summary"]
    model = report["model_under_test"]

    risk_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(s["risk_level"], "⚪")

    print("\n" + "═" * 62)
    print("  LLM RED-TEAM REPORT")
    print("═" * 62)
    print(f"  Model   : {model}")
    print(f"  Run     : {report['run_id']}")
    print(f"  Framework: MITRE ATLAS")
    print("─" * 62)
    print(f"\n  Overall Risk Score : {s['risk_score']}/10  {risk_emoji} {s['risk_level']}")
    print(f"  Total attacks      : {s['total_attacks']}")
    print(f"  🔴 Vulnerable       : {s['vulnerable']}")
    print(f"  🟡 Partial          : {s['partial']}")
    print(f"  🟢 Resilient        : {s['resilient']}")

    print(f"\n  Category Breakdown:")
    print("  " + "─" * 50)
    for cat, counts in s.get("category_breakdown", {}).items():
        icons = (
            "🔴" * counts.get("VULNERABLE", 0)
            + "🟡" * counts.get("PARTIAL", 0)
            + "🟢" * counts.get("RESILIENT", 0)
        )
        print(f"  {cat:<30} {icons}")
    print("\n" + "═" * 62 + "\n")
