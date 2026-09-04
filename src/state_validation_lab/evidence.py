"""Evidence Ledger recording helper (RESEARCH-ONLY).

Writes one structured JSON record per executed experiment under
evidence/<family>/<experiment_id>.json. This is a research artifact
writer, not an audit, compliance, or production logging system.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

RESULT_VOCABULARY = {
    "PASS",
    "FAIL",
    "UNKNOWN",
    "NOT_APPLICABLE",
    "BLOCKED",
    "INSUFFICIENT_EVIDENCE",
}

REPO_ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_ROOT = REPO_ROOT / "evidence"


def _git_head() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            check=True,
            text=True,
        )
        return out.stdout.strip()
    except Exception:
        return "UNKNOWN"


def write_record(
    *,
    experiment_id: str,
    architecture_version: str,
    initial_state: Any,
    transition_sequence: list[str],
    fault_injection: str | None,
    expected_property: str,
    observed_result: Any,
    result: str,
    failure_point: str | None,
    unknowns: list[str],
    limitations: list[str],
    test_command: str,
) -> Path:
    if result not in RESULT_VOCABULARY:
        raise ValueError(f"result {result!r} not in allowed vocabulary {sorted(RESULT_VOCABULARY)}")

    family = experiment_id.split("-", 1)[0]
    record = {
        "experiment_id": experiment_id,
        "architecture_version": architecture_version,
        "repo_head": _git_head(),
        "test_revision": experiment_id,
        "initial_state": initial_state,
        "transition_sequence": transition_sequence,
        "fault_injection": fault_injection,
        "expected_property": expected_property,
        "observed_result": observed_result,
        "result": result,
        "failure_point": failure_point,
        "unknowns": unknowns,
        "limitations": limitations,
        "reproducibility_information": {
            "python_version": sys.version.split()[0],
            "test_command": test_command,
        },
    }

    out_dir = EVIDENCE_ROOT / family
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{experiment_id}.json"
    out_path.write_text(json.dumps(record, indent=2, default=str) + "\n")
    return out_path
