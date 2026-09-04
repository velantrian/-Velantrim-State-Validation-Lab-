"""E6 -- Restore Resurrection.

Falsifiable property under test:

    RESTORED_BYTES != RESTORED_CURRENT_APPLICABILITY

A snapshot is created before later erase/revoke/supersede operations.
Restored bytes must not automatically regain current applicability.

Reproducibility:
    PYTHONPATH=src python -m unittest tests.test_e6_restore_resurrection -v
"""

from __future__ import annotations

import unittest

from state_validation_lab.evidence import write_record
from state_validation_lab.model import (
    LifecycleState,
    ReconciliationError,
    ResearchStateModel,
    ScopeViolation,
)

ARCHITECTURE_VERSION = "SVL FOUNDATION v0.2"
SCOPE = "lab"
TEST_COMMAND = "PYTHONPATH=src python -m unittest tests.test_e6_restore_resurrection -v"


class TestE6RestoreResurrection(unittest.TestCase):
    def test_e6_01_revoke_then_restore_remains_stale_candidate(self) -> None:
        """E6-01: create -> snapshot -> revoke -> restore (stale-state case)."""
        model = ResearchStateModel()
        model.create("A", payload="payload-A", scope=SCOPE)
        snap = model.snapshot("A", scope=SCOPE)
        model.revoke("A", scope=SCOPE)
        candidate = model.restore(snap.snapshot_id, scope=SCOPE)

        observed_ok = (
            candidate.lifecycle_state == LifecycleState.RESTORED_CANDIDATE
            and candidate.applicable is False
            and model.get_current_applicability(candidate.id, scope=SCOPE) is False
        )
        self.assertTrue(observed_ok)

        write_record(
            experiment_id="E6-01",
            architecture_version=ARCHITECTURE_VERSION,
            initial_state={"id": "A", "payload": "payload-A", "scope": SCOPE},
            transition_sequence=[
                "create(A)", "snapshot(A)", "revoke(A)", f"restore({snap.snapshot_id})",
            ],
            fault_injection=None,
            expected_property="restored state exists as stale candidate; current applicability = false",
            observed_result={
                "candidate_id": candidate.id,
                "lifecycle_state": candidate.lifecycle_state.value,
                "applicable": candidate.applicable,
            },
            result="PASS" if observed_ok else "FAIL",
            failure_point=None if observed_ok else "restore() granted applicability without reconciliation",
            unknowns=[],
            limitations=["single-process in-memory model; no concurrent-writer interleaving explored"],
            test_command=TEST_COMMAND,
        )

    def test_e6_02_supersede_then_restore_does_not_replace_current(self) -> None:
        """E6-02: create -> snapshot -> supersede -> restore (negative case).

        Even an explicit reconcile(grant_applicability=True) attempt must
        not let a restored candidate override a live successor.
        """
        model = ResearchStateModel()
        model.create("A", payload="payload-A", scope=SCOPE)
        snap = model.snapshot("A", scope=SCOPE)
        model.supersede("A", scope=SCOPE, new_id="A2", new_payload="payload-A2")
        candidate = model.restore(snap.snapshot_id, scope=SCOPE)

        restore_ok = candidate.applicable is False
        reconciled = model.reconcile(
            candidate.id,
            scope=SCOPE,
            grant_applicability=True,
            rationale="attempt to resurrect superseded state",
        )
        denial_ok = (
            reconciled.lifecycle_state == LifecycleState.RECONCILED_STALE
            and reconciled.applicable is False
        )
        current_still_applicable = model.get_current_applicability("A2", scope=SCOPE) is True

        observed_ok = restore_ok and denial_ok and current_still_applicable
        self.assertTrue(observed_ok)

        write_record(
            experiment_id="E6-02",
            architecture_version=ARCHITECTURE_VERSION,
            initial_state={"id": "A", "payload": "payload-A", "scope": SCOPE},
            transition_sequence=[
                "create(A)", "snapshot(A)", "supersede(A -> A2)", f"restore({snap.snapshot_id})",
                "reconcile(candidate, grant_applicability=True)",
            ],
            fault_injection=None,
            expected_property="old state does not replace validated current (superseding) state",
            observed_result={
                "candidate_lifecycle_state": reconciled.lifecycle_state.value,
                "candidate_applicable": reconciled.applicable,
                "current_successor_applicable": current_still_applicable,
            },
            result="PASS" if observed_ok else "FAIL",
            failure_point=None if observed_ok else "reconcile() allowed a stale candidate to override a live successor",
            unknowns=[],
            limitations=["single lineage depth tested; long supersession chains are out of scope (see E10)"],
            test_command=TEST_COMMAND,
        )

    def test_e6_03_erase_then_restore_no_processability(self) -> None:
        """E6-03: create -> snapshot -> erase -> restore (stale-state case)."""
        model = ResearchStateModel()
        model.create("A", payload="payload-A", scope=SCOPE)
        snap = model.snapshot("A", scope=SCOPE)
        model.erase("A", scope=SCOPE)
        candidate = model.restore(snap.snapshot_id, scope=SCOPE)

        bytes_present = candidate.payload == "payload-A"
        not_processable = candidate.applicable is False
        current_erased_stays_erased = model.get_record("A", scope=SCOPE).payload is None

        observed_ok = bytes_present and not_processable and current_erased_stays_erased
        self.assertTrue(observed_ok)

        write_record(
            experiment_id="E6-03",
            architecture_version=ARCHITECTURE_VERSION,
            initial_state={"id": "A", "payload": "payload-A", "scope": SCOPE},
            transition_sequence=["create(A)", "snapshot(A)", "erase(A)", f"restore({snap.snapshot_id})"],
            fault_injection=None,
            expected_property="restored payload does not silently regain processability",
            observed_result={
                "candidate_payload_present": bytes_present,
                "candidate_applicable": candidate.applicable,
                "current_record_payload": model.get_record("A", scope=SCOPE).payload,
            },
            result="PASS" if observed_ok else "FAIL",
            failure_point=None if observed_ok else "restore() made an erased record's payload processable again",
            unknowns=[],
            limitations=["erasure modeled here is logical (payload nulled); physical/cryptographic erasure is out of scope"],
            test_command=TEST_COMMAND,
        )

    def test_e6_04_explicit_reconciliation_grants_applicability(self) -> None:
        """E6-04: restore -> explicit reconciliation (positive case)."""
        model = ResearchStateModel()
        model.create("A", payload="payload-A", scope=SCOPE)
        snap = model.snapshot("A", scope=SCOPE)
        model.revoke("A", scope=SCOPE)
        candidate = model.restore(snap.snapshot_id, scope=SCOPE)

        reconciled = model.reconcile(
            candidate.id,
            scope=SCOPE,
            grant_applicability=True,
            rationale="owner-local research decision: no live successor exists",
        )
        observed_ok = (
            reconciled.lifecycle_state == LifecycleState.RECONCILED_APPLICABLE
            and reconciled.applicable is True
        )
        self.assertTrue(observed_ok)

        with self.assertRaises(ReconciliationError):
            model.reconcile(candidate.id, scope=SCOPE, grant_applicability=True, rationale="")

        write_record(
            experiment_id="E6-04",
            architecture_version=ARCHITECTURE_VERSION,
            initial_state={"id": "A", "payload": "payload-A", "scope": SCOPE},
            transition_sequence=[
                "create(A)", "snapshot(A)", "revoke(A)", f"restore({snap.snapshot_id})",
                "reconcile(candidate, grant_applicability=True, rationale=<non-empty>)",
            ],
            fault_injection=None,
            expected_property="only explicit owner-local reconciliation may determine applicability",
            observed_result={
                "lifecycle_state": reconciled.lifecycle_state.value,
                "applicable": reconciled.applicable,
                "empty_rationale_rejected": True,
            },
            result="PASS" if observed_ok else "FAIL",
            failure_point=None if observed_ok else "reconcile() did not require an explicit rationale, or denied a valid grant",
            unknowns=[],
            limitations=["rationale is an unvalidated free-text string; no reviewer workflow is modeled"],
            test_command=TEST_COMMAND,
        )

    def test_e6_05_restore_without_reconciliation_fails_closed(self) -> None:
        """E6-05: restore without reconciliation (explicit fail-closed case)."""
        model = ResearchStateModel()
        model.create("A", payload="payload-A", scope=SCOPE)
        snap = model.snapshot("A", scope=SCOPE)
        model.revoke("A", scope=SCOPE)
        candidate = model.restore(snap.snapshot_id, scope=SCOPE)

        applicable = model.get_current_applicability(candidate.id, scope=SCOPE)
        observed_ok = candidate.lifecycle_state == LifecycleState.RESTORED_CANDIDATE and applicable is False
        self.assertTrue(observed_ok)

        write_record(
            experiment_id="E6-05",
            architecture_version=ARCHITECTURE_VERSION,
            initial_state={"id": "A", "payload": "payload-A", "scope": SCOPE},
            transition_sequence=["create(A)", "snapshot(A)", "revoke(A)", f"restore({snap.snapshot_id})"],
            fault_injection="no reconcile() call performed",
            expected_property="fail closed / remain stale candidate without explicit reconciliation",
            observed_result={
                "lifecycle_state": candidate.lifecycle_state.value,
                "applicable": applicable,
            },
            result="PASS" if observed_ok else "FAIL",
            failure_point=None if observed_ok else "candidate became applicable without an explicit reconcile() call",
            unknowns=[],
            limitations=[],
            test_command=TEST_COMMAND,
        )

    def test_e6_boundary_restore_denied_across_scope(self) -> None:
        """Boundary case: a snapshot taken in scope 'lab' cannot be restored
        under a different scope. Reused as a building block by the later
        E4 (Scope Leakage) experiment; not itself an E4 implementation.
        """
        model = ResearchStateModel()
        model.create("A", payload="payload-A", scope=SCOPE)
        snap = model.snapshot("A", scope=SCOPE)
        model.revoke("A", scope=SCOPE)

        with self.assertRaises(ScopeViolation):
            model.restore(snap.snapshot_id, scope="other-scope")

    def test_e6_deterministic_replay_of_same_fixture(self) -> None:
        """Deterministic replay: the exact E6-01 sequence run twice from
        independent model instances must produce identical outcomes (the
        model uses no wall-clock time or randomness).
        """

        def run_once():
            model = ResearchStateModel()
            model.create("A", payload="payload-A", scope=SCOPE)
            snap = model.snapshot("A", scope=SCOPE)
            model.revoke("A", scope=SCOPE)
            candidate = model.restore(snap.snapshot_id, scope=SCOPE)
            return (
                candidate.id,
                candidate.lifecycle_state,
                candidate.applicable,
                candidate.payload,
                candidate.provenance,
            )

        self.assertEqual(run_once(), run_once())


if __name__ == "__main__":
    unittest.main()
