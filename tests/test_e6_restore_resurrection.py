from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from state_validation_lab.evidence import (  # noqa: E402
    REQUIRED_FIELDS,
    validate_evidence_record,
    write_evidence_records,
)
from state_validation_lab.model import (  # noqa: E402
    LifecycleState,
    ReconciliationResult,
    ResearchStateModel,
    UnknownCandidateError,
    UnknownRecordError,
    UnknownSnapshotError,
)
from state_validation_lab.run_e6 import execute_e6  # noqa: E402


class RestoreResurrectionTests(unittest.TestCase):
    def test_e6_01_revoke_survives_old_snapshot_restore(self) -> None:
        model = ResearchStateModel()
        model.create("A", "payload-v1", scope="scope-A")
        model.snapshot("A", "snapshot-1")
        model.revoke("A")

        candidate_id = model.restore("snapshot-1")

        self.assertEqual(model.get_current_disposition("A"), LifecycleState.REVOKED)
        self.assertFalse(model.get_current_applicability("A"))
        self.assertEqual(
            model.get_candidate(candidate_id).lifecycle_state,
            LifecycleState.RESTORED_STALE_CANDIDATE,
        )
        self.assertFalse(model.get_candidate_applicability(candidate_id))
        self.assertEqual(
            model.reconcile(candidate_id), ReconciliationResult.NOT_APPLICABLE
        )

    def test_e6_02_superseded_snapshot_cannot_replace_successor(self) -> None:
        model = ResearchStateModel()
        model.create("A-v1", "payload-v1", scope="scope-A", version=1)
        model.snapshot("A-v1", "snapshot-1")
        model.supersede("A-v1", "A-v2", "payload-v2", version=2)

        candidate_id = model.restore("snapshot-1")

        self.assertFalse(model.get_current_applicability("A-v1"))
        self.assertTrue(model.get_current_applicability("A-v2"))
        self.assertEqual(model.get_current("A-v2").payload, "payload-v2")
        self.assertFalse(model.get_candidate_applicability(candidate_id))
        self.assertEqual(
            model.reconcile(candidate_id), ReconciliationResult.NOT_APPLICABLE
        )

    def test_e6_03_logically_erased_payload_is_not_reactivated(self) -> None:
        model = ResearchStateModel()
        model.create("A", "synthetic-payload", scope="scope-A")
        model.snapshot("A", "snapshot-1")
        model.erase("A")

        candidate_id = model.restore("snapshot-1")

        self.assertIsNone(model.get_current("A").payload)
        self.assertFalse(model.get_current_applicability("A"))
        self.assertEqual(model.get_candidate(candidate_id).payload, "synthetic-payload")
        self.assertFalse(model.get_candidate_applicability(candidate_id))
        self.assertEqual(
            model.reconcile(candidate_id), ReconciliationResult.NOT_APPLICABLE
        )

    def test_e6_04_explicit_reconciliation_can_mark_matching_candidate(self) -> None:
        model = ResearchStateModel()
        model.create("A", "payload-v1", scope="scope-A")
        model.snapshot("A", "snapshot-1")
        candidate_id = model.restore("snapshot-1")

        self.assertFalse(model.get_candidate_applicability(candidate_id))
        self.assertEqual(model.reconcile(candidate_id), ReconciliationResult.APPLICABLE)
        self.assertTrue(model.get_candidate_applicability(candidate_id))
        self.assertEqual(
            model.get_candidate(candidate_id).lifecycle_state,
            LifecycleState.RESTORED_RECONCILED,
        )
        self.assertEqual(model.get_current("A").payload, "payload-v1")

    def test_e6_05_restore_without_reconciliation_fails_closed(self) -> None:
        model = ResearchStateModel()
        model.create("A", "payload-v1", scope="scope-A")
        model.snapshot("A", "snapshot-1")

        candidate_id = model.restore("snapshot-1")

        self.assertFalse(model.get_candidate_applicability(candidate_id))
        self.assertEqual(
            model.get_candidate(candidate_id).lifecycle_state,
            LifecycleState.RESTORED_STALE_CANDIDATE,
        )

    def test_unknown_inputs_fail_closed_with_explicit_errors(self) -> None:
        model = ResearchStateModel()
        with self.assertRaises(UnknownRecordError):
            model.get_current("missing")
        with self.assertRaises(UnknownSnapshotError):
            model.restore("missing")
        with self.assertRaises(UnknownCandidateError):
            model.reconcile("missing")

    def test_restore_never_overwrites_current_collection(self) -> None:
        model = ResearchStateModel()
        model.create("A", "payload-v1", scope="scope-A")
        model.snapshot("A", "snapshot-1")
        model.revoke("A")

        model.restore("snapshot-1")

        self.assertEqual(model.get_current("A").lifecycle_state, LifecycleState.REVOKED)
        self.assertFalse(model.get_current_applicability("A"))

    def test_later_invalidation_reverses_an_earlier_reconciliation_result(self) -> None:
        model = ResearchStateModel()
        model.create("A", "payload-v1", scope="scope-A")
        model.snapshot("A", "snapshot-1")
        candidate_id = model.restore("snapshot-1")
        self.assertEqual(model.reconcile(candidate_id), ReconciliationResult.APPLICABLE)
        self.assertTrue(model.get_candidate_applicability(candidate_id))

        model.revoke("A")

        self.assertEqual(
            model.reconcile(candidate_id), ReconciliationResult.NOT_APPLICABLE
        )
        self.assertFalse(model.get_candidate_applicability(candidate_id))
        self.assertEqual(
            model.get_candidate(candidate_id).lifecycle_state,
            LifecycleState.RESTORED_STALE_CANDIDATE,
        )

    def test_invalid_lifecycle_transition_fails_closed(self) -> None:
        model = ResearchStateModel()
        model.create("A", "payload-v1", scope="scope-A")
        model.revoke("A")

        with self.assertRaisesRegex(ValueError, "requires ACTIVE"):
            model.erase("A")

    def test_all_e6_ledgers_pass_and_satisfy_contract(self) -> None:
        records = execute_e6("a" * 40, "a" * 40)

        self.assertEqual(
            [record["experiment_id"] for record in records],
            ["E6-01", "E6-02", "E6-03", "E6-04", "E6-05"],
        )
        for record in records:
            self.assertTrue(REQUIRED_FIELDS.issubset(record))
            self.assertEqual(record["result"], "PASS")
            self.assertEqual(validate_evidence_record(record), [])

    def test_deterministic_replay_produces_identical_bytes(self) -> None:
        records_a = execute_e6("b" * 40, "b" * 40)
        records_b = execute_e6("b" * 40, "b" * 40)
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_paths = write_evidence_records(records_a, Path(first))
            second_paths = write_evidence_records(records_b, Path(second))

            self.assertEqual(
                [path.name for path in first_paths], [path.name for path in second_paths]
            )
            self.assertEqual(
                [path.read_bytes() for path in first_paths],
                [path.read_bytes() for path in second_paths],
            )


if __name__ == "__main__":
    unittest.main()
