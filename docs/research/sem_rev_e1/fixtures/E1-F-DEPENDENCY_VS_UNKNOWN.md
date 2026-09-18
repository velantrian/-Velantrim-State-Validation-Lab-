# E1-F — Required Dependency Loss vs Optional UNKNOWN

**Family:** E1-F · **PHYSICAL:** E1-F-01, E1-F-02 · **CONTRAST:** CG-F-dep

```text
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
F-01 MUST FAIL FOR THE INTENDED MISSING DEPENDENCY, NOT FOR SOME OTHER OMITTED RECORD
```

---

## E1-F-01 — Expected fail-closed (FULLY SPECIFIED)

### Query

| Field | Value |
|-------|-------|
| fixture_id | E1-F-01 |
| entity_id | ent:service:kepler |
| query | Is VX-F authorized for Kepler in production-us? |
| query_scope | scope:production-us |
| query_as_of | 2026-02-01T00:00:00Z |

### Present records (exact)

**Source** `src:e1f-cand` — type=lab_log

**Assertion `as:e1f-cand`**

| Field | Value |
|-------|-------|
| entity_id | ent:service:kepler |
| semantic_force | observation |
| scope_id | scope:production-us |
| asserted_at | 2026-01-15T00:00:00Z |
| recorded_at | 2026-01-15T01:00:00Z |
| valid_from | 2026-01-15T00:00:00Z |
| valid_to | NULL |
| uncertainty | NULL |
| declared_loss | 0 |

**Evidence `ev:e1f-cand`**

| Field | Value |
|-------|-------|
| source_id | src:e1f-cand |
| observed_at | 2026-01-14T00:00:00Z |
| recorded_at | 2026-01-15T01:00:00Z |
| declared_loss | 0 |

**Link:** `ev:e1f-cand` ↔ `as:e1f-cand`

**S3 candidate set must include** `as:e1f-cand`.

### Intentionally missing required dependency (ONLY)

```text
missing_required_dependency_id=dec:e1f-auth
```

`dec:e1f-auth` (authority_decision binding required for authorization gate) is **absent**.  
No other required typed dependency may be omitted.

### Expected

```text
S4_stage=FAIL
missing_required_dependency_id=dec:e1f-auth
FIXTURE_EXPECTED_FAIL_CLOSED
S4_OUTPUT_BYTES fixed → SHA-256 recorded → independently verified → THEN oracle
FIXTURE_SEMANTIC_PASS iff exact fail-closed after hash gate
S5_not_required
does_not_prohibit_CORE_PASS
```

FORBIDDEN: silent ordinary NO_QUALIFIED_RESULT as valid absence; fail for a different omitted record; oracle before S4 hash.

---

## E1-F-02 — Optional uncertainty UNKNOWN (POS, SINGLE-VALUED)

**Binding:** `as:e1f-opt` ↔ `dec:e1f-opt`

### Query

| Field | Value |
|-------|-------|
| fixture_id | E1-F-02 |
| entity_id | ent:service:kepler |
| query | Is VX-F-OPT approved for Kepler in production-us? |
| query_scope | scope:production-us |
| query_as_of | 2026-02-01T00:00:00Z |

### Assertion `as:e1f-opt`

| Field | Value |
|-------|-------|
| semantic_force | decision |
| scope_id | scope:production-us |
| asserted_at | 2026-01-20T00:00:00Z |
| recorded_at | 2026-01-20T01:00:00Z |
| valid_from | 2026-01-20T00:00:00Z |
| valid_to | NULL |
| uncertainty | **NULL** → UNKNOWN |
| declared_loss | 0 |

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

### REQUIRED (single-valued)

```text
as:e1f-opt.status=current
as:e1f-opt.uncertainty=UNKNOWN
as:e1f-opt.declared_loss=0
dec:e1f-opt.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1f-opt
```

### FORBIDDEN

```text
NO_QUALIFIED_RESULT
uncertainty=FALSE
fabricated uncertainty value
decision omitted
```
