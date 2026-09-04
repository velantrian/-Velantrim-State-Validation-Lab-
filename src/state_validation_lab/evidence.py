"""Evidence Ledger helpers for deterministic owner-local experiments."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


ALLOWED_RESULTS = {
    "PASS",
    "FAIL",
    "UNKNOWN",
    "NOT_APPLICABLE",
    "BLOCKED",
    "INSUFFICIENT_EVIDENCE",
}

REQUIRED_FIELDS = {
    "experiment_id",
    "architecture_version",
    "repo_head",
    "test_revision",
    "initial_state",
    "transition_sequence",
    "fault_injection",
    "expected_property",
    "observed_result",
    "result",
    "failure_point",
    "unknowns",
    "limitations",
    "reproducibility_information",
}


def validate_evidence_record(record: dict[str, Any]) -> list[str]:
    """Return validation errors without upgrading absence into success."""

    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - record.keys())
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")
    if record.get("result") not in ALLOWED_RESULTS:
        errors.append(f"unsupported result: {record.get('result')!r}")
    if not isinstance(record.get("transition_sequence"), list):
        errors.append("transition_sequence must be a list")
    if not isinstance(record.get("unknowns"), list):
        errors.append("unknowns must be a list")
    if not isinstance(record.get("limitations"), list):
        errors.append("limitations must be a list")
    if not isinstance(record.get("reproducibility_information"), dict):
        errors.append("reproducibility_information must be an object")
    for field in ("experiment_id", "architecture_version", "repo_head", "test_revision"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"{field} must be a non-empty string")
    return errors


def write_evidence_records(
    records: Iterable[dict[str, Any]], output_dir: Path
) -> list[Path]:
    """Validate and write stable JSON records to a caller-selected directory."""

    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for record in records:
        errors = validate_evidence_record(record)
        if errors:
            joined = "; ".join(errors)
            raise ValueError(f"invalid evidence record {record.get('experiment_id')}: {joined}")
        path = output_dir / f"{record['experiment_id']}.json"
        path.write_text(
            json.dumps(record, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        paths.append(path)
    return paths
