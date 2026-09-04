"""Execute the deterministic E6 fixture family and emit Evidence Ledger JSON."""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path
from typing import Any, Callable

from .evidence import write_evidence_records
from .model import LifecycleState, ReconciliationResult, ResearchStateModel


ARCHITECTURE_VERSION = "svl-foundation/0.2"
MODEL_VERSION = "svl-e6-reference-model/0.1"
EXPECTED_PROPERTY = (
    "Restored bytes do not automatically regain current applicability."
)
TEST_COMMAND = "python -m unittest discover -s tests -p 'test_*.py' -v"


def _record(
    experiment_id: str,
    *,
    repo_head: str,
    test_revision: str,
    transition_sequence: list[str],
    observed_result: dict[str, Any],
    passed: bool,
) -> dict[str, Any]:
    return {
        "experiment_id": experiment_id,
        "architecture_version": ARCHITECTURE_VERSION,
        "model_version": MODEL_VERSION,
        "repo_head": repo_head,
        "test_revision": test_revision,
        "initial_state": {
            "current_records": [],
            "restored_candidates": [],
            "payload_class": "SYNTHETIC_NON_SENSITIVE",
        },
        "transition_sequence": transition_sequence,
        "fault_injection": {"kind": "NONE", "failure_point": None},
        "expected_property": EXPECTED_PROPERTY,
        "observed_result": observed_result,
        "result": "PASS" if passed else "FAIL",
        "failure_point": None if passed else "EXPECTED_PROPERTY_ASSERTION",
        "unknowns": [
            "Behavior outside the five deterministic E6 trajectories is not established.",
            "Behavior under concurrency, external storage, or process failure is not evaluated.",
        ],
        "limitations": [
            "Synthetic deterministic in-memory trajectories only.",
            (
                "Fixture-local logical erasure only; no physical, cryptographic, "
                "privacy, or legal deletion claim."
            ),
            (
                "Reconciliation is owner-local research evaluation and grants no "
                "permission, authority, Canon, or runtime activation."
            ),
            "PASS is bounded to the recorded trajectories and is not universal proof.",
        ],
        "reproducibility_information": {
            "python_version": platform.python_version(),
            "dependency_environment": "PYTHON_STANDARD_LIBRARY_ONLY",
            "dependency_declaration": "requirements.txt",
            "test_command": TEST_COMMAND,
            "random_generation": "NONE",
            "external_services": [],
            "artifact_path": f"E6/{experiment_id}.json",
        },
    }


def _e6_01(repo_head: str, test_revision: str) -> dict[str, Any]:
    model = ResearchStateModel()
    model.create("A", "payload-v1", scope="scope-A")
    model.snapshot("A", "snap-E6-01")
    model.revoke("A")
    candidate_id = model.restore("snap-E6-01")
    candidate = model.get_candidate(candidate_id)
    current = model.get_current("A")
    observed = {
        "candidate_exists": True,
        "candidate_lifecycle": candidate.lifecycle_state.value,
        "candidate_applicable": candidate.applicable,
        "current_lifecycle": current.lifecycle_state.value,
        "current_applicable": current.applicable,
    }
    passed = observed == {
        "candidate_exists": True,
        "candidate_lifecycle": "RESTORED_STALE_CANDIDATE",
        "candidate_applicable": False,
        "current_lifecycle": "REVOKED",
        "current_applicable": False,
    }
    return _record(
        "E6-01",
        repo_head=repo_head,
        test_revision=test_revision,
        transition_sequence=[
            "create:A:v1",
            "snapshot:snap-E6-01",
            "revoke:A",
            "restore:snap-E6-01",
        ],
        observed_result=observed,
        passed=passed,
    )


def _e6_02(repo_head: str, test_revision: str) -> dict[str, Any]:
    model = ResearchStateModel()
    model.create("A-v1", "payload-v1", scope="scope-A", version=1)
    model.snapshot("A-v1", "snap-E6-02")
    model.supersede("A-v1", "A-v2", "payload-v2", version=2)
    candidate_id = model.restore("snap-E6-02")
    old = model.get_current("A-v1")
    successor = model.get_current("A-v2")
    candidate = model.get_candidate(candidate_id)
    observed = {
        "candidate_lifecycle": candidate.lifecycle_state.value,
        "candidate_applicable": candidate.applicable,
        "predecessor_lifecycle": old.lifecycle_state.value,
        "predecessor_applicable": old.applicable,
        "predecessor_superseded_by": old.superseded_by,
        "successor_id": successor.id,
        "successor_applicable": successor.applicable,
    }
    passed = (
        candidate.lifecycle_state is LifecycleState.RESTORED_STALE_CANDIDATE
        and not candidate.applicable
        and old.lifecycle_state is LifecycleState.SUPERSEDED
        and not old.applicable
        and old.superseded_by == "A-v2"
        and successor.applicable
    )
    return _record(
        "E6-02",
        repo_head=repo_head,
        test_revision=test_revision,
        transition_sequence=[
            "create:A-v1:v1",
            "snapshot:snap-E6-02",
            "supersede:A-v1:A-v2:v2",
            "restore:snap-E6-02",
        ],
        observed_result=observed,
        passed=passed,
    )


def _e6_03(repo_head: str, test_revision: str) -> dict[str, Any]:
    model = ResearchStateModel()
    model.create("A", "synthetic-payload", scope="scope-A")
    model.snapshot("A", "snap-E6-03")
    model.erase("A")
    candidate_id = model.restore("snap-E6-03")
    current = model.get_current("A")
    candidate = model.get_candidate(candidate_id)
    observed = {
        "candidate_payload_restored": candidate.payload == "synthetic-payload",
        "candidate_applicable": candidate.applicable,
        "current_lifecycle": current.lifecycle_state.value,
        "current_payload_present": current.payload is not None,
        "current_applicable": current.applicable,
        "erasure_claim_class": "FIXTURE_LOCAL_LOGICAL_ONLY",
    }
    passed = (
        observed["candidate_payload_restored"]
        and not candidate.applicable
        and current.lifecycle_state is LifecycleState.ERASED
        and current.payload is None
        and not current.applicable
    )
    return _record(
        "E6-03",
        repo_head=repo_head,
        test_revision=test_revision,
        transition_sequence=[
            "create:A:v1",
            "snapshot:snap-E6-03",
            "logical-erase:A",
            "restore:snap-E6-03",
        ],
        observed_result=observed,
        passed=passed,
    )


def _e6_04(repo_head: str, test_revision: str) -> dict[str, Any]:
    model = ResearchStateModel()
    model.create("A", "payload-v1", scope="scope-A")
    model.snapshot("A", "snap-E6-04")
    candidate_id = model.restore("snap-E6-04")
    before = model.get_candidate_applicability(candidate_id)
    decision = model.reconcile(candidate_id)
    after = model.get_candidate_applicability(candidate_id)
    observed = {
        "candidate_applicable_before_reconciliation": before,
        "reconciliation_result": decision.value,
        "candidate_applicable_after_reconciliation": after,
        "current_record_unchanged": model.get_current("A").payload == "payload-v1",
        "candidate_remains_separate": candidate_id.startswith("restore:"),
    }
    passed = (
        not before
        and decision is ReconciliationResult.APPLICABLE
        and after
        and observed["current_record_unchanged"]
        and observed["candidate_remains_separate"]
    )
    return _record(
        "E6-04",
        repo_head=repo_head,
        test_revision=test_revision,
        transition_sequence=[
            "create:A:v1",
            "snapshot:snap-E6-04",
            "restore:snap-E6-04",
            "explicit-owner-local-reconcile:restore:snap-E6-04:A",
        ],
        observed_result=observed,
        passed=passed,
    )


def _e6_05(repo_head: str, test_revision: str) -> dict[str, Any]:
    model = ResearchStateModel()
    model.create("A", "payload-v1", scope="scope-A")
    model.snapshot("A", "snap-E6-05")
    candidate_id = model.restore("snap-E6-05")
    candidate = model.get_candidate(candidate_id)
    observed = {
        "reconciliation_performed": False,
        "candidate_lifecycle": candidate.lifecycle_state.value,
        "candidate_applicable": candidate.applicable,
        "fail_closed": not candidate.applicable,
    }
    passed = (
        candidate.lifecycle_state is LifecycleState.RESTORED_STALE_CANDIDATE
        and not candidate.applicable
    )
    return _record(
        "E6-05",
        repo_head=repo_head,
        test_revision=test_revision,
        transition_sequence=[
            "create:A:v1",
            "snapshot:snap-E6-05",
            "restore:snap-E6-05",
            "reconcile:NOT_PERFORMED",
        ],
        observed_result=observed,
        passed=passed,
    )


SCENARIOS: tuple[Callable[[str, str], dict[str, Any]], ...] = (
    _e6_01,
    _e6_02,
    _e6_03,
    _e6_04,
    _e6_05,
)


def execute_e6(repo_head: str, test_revision: str) -> list[dict[str, Any]]:
    """Execute all preregistered first-wave E6 trajectories."""

    if not repo_head.strip() or not test_revision.strip():
        raise ValueError("repo_head and test_revision must be non-empty")
    return [scenario(repo_head, test_revision) for scenario in SCENARIOS]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--repo-head", required=True)
    parser.add_argument("--test-revision", required=True)
    args = parser.parse_args()

    records = execute_e6(args.repo_head, args.test_revision)
    paths = write_evidence_records(records, args.output_dir)
    failed = [record["experiment_id"] for record in records if record["result"] != "PASS"]
    print(
        json.dumps(
            {
                "artifact_paths": [str(path) for path in paths],
                "experiment_count": len(records),
                "failed_experiments": failed,
                "repo_head": args.repo_head,
            },
            sort_keys=True,
        )
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
