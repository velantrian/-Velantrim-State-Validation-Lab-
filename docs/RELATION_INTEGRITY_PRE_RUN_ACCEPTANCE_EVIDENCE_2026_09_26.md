# Relation Integrity — pre-run acceptance evidence (2026-09-26)

**Status:** `BOUNDED ACCEPTANCE EVIDENCE · NOT A RUN · NOT EXPERIMENT EVIDENCE · RUN_AUTHORIZED=FALSE`

Reviewed implementation head before this evidence record: `50ac7c0523c104d5576862864bfdd3d1f10ccd61`.

## Byte identity

Local verification copies were compared to the GitHub content blobs by Git blob SHA.

| Artifact | Git blob SHA | SHA-256 |
|---|---|---|
| `tools/relation_integrity/pre_run_contracts.py` | `28e99da8dc7010d98e700e151b939e7a8bf62890` | `2f5416916bd474a33b071616f17cfce65a4c0298a6b9fe2926b09e93deb1ebfd` |
| `tools/relation_integrity/source_field_schema_v1.json` | `72fbd972e6b150d2b6f3eda818fb0b56c5c0f0d5` | `25a8bc8f08b3ffd5057320d07b37eedcf23211d80f23f1875d0b53652d92a373` |
| `tests/relation_integrity/test_pre_run_contracts.py` | `a8da03e283b4a2acfbd546575deee22b422b42b8` | `bc29eab456ac16ba216f4f62257f964dad147d8e52ba3be71e8a9aae9151d0d1` |
| `fixtures/relation_integrity_qualification_v0_3.jsonl` | `9f2db4b9ab2b1770c8f3a251f5c9b345d0e18cfa` | `3ebaad03eae25cad7da798007c655c6a4f645817fbdf92d5fa90407f15c2116f` |

## Acceptance suite

Command used on the byte-matched local mirror:

```text
python -m unittest discover -s tests/relation_integrity -p 'test_*.py' -v
```

Result:

```text
10 / 10 PASS
```

Covered checks:

1. F-P1 candidate is explicitly `SAME_REGISTRY_ENTITY(A,B,registry=R)`.
2. F-P1 gold contains `scope_boundaries = [Registry R]`.
3. F-P1 has no unqualified world relation.
4. SC-1 resolves `UNKNOWN` vs `SUPPORTED` to `SUPPORTED`.
5. SC-1 sends direct `SUPPORTED` vs `REJECTED` conflict to `UNSCORABLE`.
6. Public ledger projection excludes `frozen_gold`.
7. Ledger output is deterministic.
8. Gold mutation does not alter ledger output.
9. Scorer mutation does not alter ledger output.
10. Schema conformance / F-G expected missing-field coverage / non-causal F-P1 isolation are checked.

## Failures caught before PASS

The acceptance work caught two implementation defects before final PASS:

- a source-schema negative phrase for `identification_assumptions` was initially too narrow;
- the committed relation-type regex was initially over-escaped and failed to parse candidates.

Both were corrected before this evidence record. The final PASS above is against byte-matched copies of the corrected GitHub blobs.

## Boundary

This is **pre-run contract evidence only**.

```text
MODEL OUTPUTS PRODUCED = 0
EXPERIMENT RUN         = NO
RUN_AUTHORIZED         = FALSE
EXPERIMENT_ID          = NONE
MERGE_AUTHORIZED       = FALSE
CANON/RUNTIME CHANGE   = NONE
```
