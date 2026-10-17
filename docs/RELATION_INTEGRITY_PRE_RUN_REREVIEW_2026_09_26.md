# Relation Integrity — bounded pre-run re-review (2026-09-26)

**Reviewed implementation/evidence content through:** `f4ab545a496940b02b7f819efe5081907ce78c5e`

**Review scope:** only the three reconciled pre-run blockers:
1. F-P1 registry/world scope;
2. SC-1 qualification/basis consistency;
3. Condition B `MISSING_SOURCE_FIELDS` gold/scorer blindness.

**Status:** `BOUNDED RE-REVIEW PASS · PACKAGE 0.3 FROZEN AFTER RE-REVIEW · READY FOR LATER OWNER GO/NO-GO CONSIDERATION · NOT A RUN AUTHORIZATION`

## 1. F-P1 package revision

**Result: PASS for the declared blocker.**

Revision 0.3 uses:

```text
SAME_REGISTRY_ENTITY(A,B,registry=R)
```

and freezes `scope_boundaries = [Registry R]`. The revised F-P1 gold contains no unqualified `SAME_ENTITY(A,B)` in `qualified_world_relations`.

Revision 0.2 remains present and unchanged as the historical frozen artifact.

This closes the specific registry-to-world scope defect identified by the pre-run reconciliation. It does not establish any global identity claim.

## 2. SC-1 answer/scorer consistency

**Result: PASS for the declared blocker.**

The revised execution plan removes scoring-bearing free-text `brief_basis` and requires a structured `basis_world_status`. The versioned normalizer `sc1-structured-basis-v1` records the raw fields, consistency state, rule version and normalized qualification.

Acceptance checks include:
- `UNKNOWN` + `SUPPORTED` -> `SUPPORTED`;
- direct `SUPPORTED` vs `REJECTED` -> `UNSCORABLE`.

This closes the specific ambiguity in which an UNKNOWN label could coexist with a stronger basis while only the label was scored.

## 3. Condition B source-only transform

**Result: PASS for the declared contract blocker.**

The transform receives only:

```text
fixture_id
model_visible_source
model_visible_relation_candidate
```

The versioned `SourceFieldSchema v1` defines legal fields and source-relative presence/absence rules. `NOT_PROVIDED_BY_SOURCE` is explicitly not a world-level falsity/absence claim.

Acceptance evidence records:
- deterministic output;
- public projection excludes gold;
- gold-mutation invariance;
- scorer-mutation invariance;
- schema conformance;
- F-G expected missing-field coverage;
- non-causal F-P1 isolation.

The suite reports `10/10 PASS`.

## 4. Failures caught during implementation

Two defects were detected before the final PASS:
- one missing-field negative pattern was too narrow;
- the first committed relation-type parser regex was over-escaped.

Both were corrected before the acceptance evidence was frozen. These failures are retained in the evidence record rather than hidden.

## 5. Re-review disposition

```text
F-P1 SCOPE BLOCKER                 = CLOSED FOR THIS PACKAGE REVISION
SC-1 CONSISTENCY BLOCKER           = CLOSED FOR THIS EXECUTION CONTRACT
LEDGER GOLD/SCORER-BLIND BLOCKER   = CLOSED FOR THIS TRANSFORM CONTRACT

PACKAGE 0.2                        = HISTORICAL / UNCHANGED
PACKAGE 0.3                        = FROZEN FOR THIS BOUNDED RE-REVIEW
ACCEPTANCE TESTS                   = 10/10 PASS
MODEL OUTPUTS                      = 0
EXPERIMENT RUN                     = NO
EXPERIMENT ID                      = NONE
RUN_AUTHORIZED                     = FALSE
MERGE_AUTHORIZED                   = FALSE
ARCHITECTURE_CONSEQUENCE           = NONE
```

## 6. Remaining owner gate

This re-review does **not** grant execution authority.

A later explicit owner GO/NO-GO must still confirm, at minimum:

- exact current branch/head;
- exact package/fixture hash;
- exact model identifier and provider configuration;
- exact prompt and prompt hash;
- exact SC-1/scorer version;
- exact SourceFieldSchema and ledger-transform hash/version;
- retry/no-rerun policy;
- evidence output location.

No experiment ID should be created before that gate.

## 7. Inference ceiling

Even a later successful run of this tiny package would establish only bounded relation-promotion discipline under the declared fixtures and controls. It would not establish relation discovery, general causal reasoning, understanding, EDCA, or universal model behavior.
