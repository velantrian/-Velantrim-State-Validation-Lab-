import copy
import json
import unittest
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.relation_integrity.pre_run_contracts import build_source_bound_ledger, canonical_json, normalize_sc1, public_fixture_projection

SCHEMA = json.loads((ROOT / "tools/relation_integrity/source_field_schema_v1.json").read_text())
FIXTURES = [json.loads(x) for x in (ROOT / "fixtures/relation_integrity_qualification_v0_3.jsonl").read_text().splitlines() if x.strip()]
BY_ID = {x["fixture_id"]: x for x in FIXTURES}

class Contracts(unittest.TestCase):
    def test_sc1_unknown_plus_supported(self):
        r=normalize_sc1("UNKNOWN","SUPPORTED")
        self.assertEqual(r["consistency_status"],"SEMANTIC_CONFLICT_RESOLVED")
        self.assertEqual(r["normalized_qualification"],"SUPPORTED")

    def test_sc1_opposed_supported_rejected(self):
        self.assertEqual(normalize_sc1("SUPPORTED","REJECTED")["normalized_qualification"],"UNSCORABLE")

    def test_fp1_scoped(self):
        x=BY_ID["F-P1"]
        self.assertEqual(x["model_visible_relation_candidate"],"SAME_REGISTRY_ENTITY(A,B,registry=R)")
        self.assertEqual(x["frozen_gold"]["scope_boundaries"],["Registry R"])
        self.assertEqual(x["frozen_gold"]["qualified_world_relations"],[])

    def test_public_projection_excludes_gold(self):
        p=public_fixture_projection(BY_ID["F-G"])
        self.assertEqual(set(p),{"fixture_id","model_visible_source","model_visible_relation_candidate"})

    def test_gold_mutation_invariance(self):
        a=copy.deepcopy(BY_ID["F-G"])
        b=copy.deepcopy(a)
        b["frozen_gold"]={"qualified_status":"SUPPORTED","bait":"gold"}
        self.assertEqual(canonical_json(build_source_bound_ledger(public_fixture_projection(a),SCHEMA)),
                         canonical_json(build_source_bound_ledger(public_fixture_projection(b),SCHEMA)))

    def test_deterministic(self):
        p=public_fixture_projection(BY_ID["F-G"])
        self.assertEqual(canonical_json(build_source_bound_ledger(p,SCHEMA)),
                         canonical_json(build_source_bound_ledger(p,SCHEMA)))

    def test_fg_missing_fields(self):
        p=public_fixture_projection(BY_ID["F-G"])
        names={x["field_id"] for x in build_source_bound_ledger(p,SCHEMA)["MISSING_SOURCE_FIELDS"]}
        for n in {"source_independence","methods","interventions","identification_assumptions","shared_sourcing","replication_design"}:
            self.assertIn(n,names)

    def test_fp1_has_no_causal_missing_fields(self):
        p=public_fixture_projection(BY_ID["F-P1"])
        self.assertEqual(build_source_bound_ledger(p,SCHEMA)["MISSING_SOURCE_FIELDS"],[])

if __name__ == "__main__":
    unittest.main()
