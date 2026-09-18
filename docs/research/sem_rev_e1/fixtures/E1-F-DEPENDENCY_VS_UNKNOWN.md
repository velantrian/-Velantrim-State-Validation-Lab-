# E1-F — Required Dependency Loss vs Optional UNKNOWN

**Family:** E1-F  
**PHYSICAL_CORE:** E1-F-01, E1-F-02  
**CONTRAST_GROUP:** CG-F-dep (NOT TRUE_PAIRWISE)

```text
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
```

---

## E1-F-01 — Expected fail-closed (unchanged gate)

Candidate `as:e1f-cand` (observation; declared_loss=0) requires missing `dec:e1f-auth`.

S4 FAIL → fix bytes → SHA-256 → verify → THEN oracle.  
Unhashable S4 → CORE INCOMPLETE.

---

## E1-F-02 — Optional uncertainty UNKNOWN (NEG)

**Binding:** `as:e1f-opt` ↔ `dec:e1f-opt`

### Assertion `as:e1f-opt`

| Field | Value |
|-------|-------|
| entity_id | ent:service:kepler |
| semantic_force | decision |
| scope_id | scope:production-us |
| asserted_at | 2026-01-20T00:00:00Z |
| recorded_at | 2026-01-20T01:00:00Z |
| valid_from | 2026-01-20T00:00:00Z |
| valid_to | NULL |
| **uncertainty** | **NULL** → projects as UNKNOWN |
| declared_loss | **0** |

### Decision `dec:e1f-opt`

| Field | Value |
|-------|-------|
| assertion_id | as:e1f-opt |
| authority_id | principal:release-board |
| outcome | approved |
| semantic_force | authority_decision |
| scope_id | scope:production-us |
| reason | R_E1_F_OPT |
| effective_from | 2026-01-20T00:00:00Z |
| recorded_at | 2026-01-20T01:00:00Z |

```text
as:e1f-opt.uncertainty=UNKNOWN
as:e1f-opt.declared_loss=0
dec:e1f-opt.outcome=approved
must_not_fabricate_FALSE_or_concrete_value
may QUALIFIED_RESULT if required gates pass
qualified_decision_ids may contain dec:e1f-opt
```

Do **not** place `uncertainty` / `declared_loss` on the decision row.
