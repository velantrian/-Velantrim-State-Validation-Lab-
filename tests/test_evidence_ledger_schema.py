"""Structural validation of committed Evidence Ledger records.

This does not re-run experiments; it checks that every evidence
artifact under evidence/ is well-formed JSON, carries the required
fields, and uses only the allowed result vocabulary. Intended as a CI
guard against silently malformed or hand-edited evidence.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from state_validation_lab.evidence import EVIDENCE_ROOT, RESULT_VOCABULARY

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


class TestEvidenceLedgerSchema(unittest.TestCase):
    def test_all_evidence_records_are_well_formed(self) -> None:
        records = sorted(EVIDENCE_ROOT.rglob("*.json"))
        self.assertTrue(records, f"expected at least one evidence record under {EVIDENCE_ROOT}")

        for path in records:
            with self.subTest(path=str(path.relative_to(EVIDENCE_ROOT))):
                data = json.loads(path.read_text())
                missing = REQUIRED_FIELDS - data.keys()
                self.assertFalse(missing, f"{path} missing required fields: {missing}")
                self.assertIn(data["result"], RESULT_VOCABULARY)
                self.assertEqual(data["experiment_id"], path.stem)


if __name__ == "__main__":
    unittest.main()
