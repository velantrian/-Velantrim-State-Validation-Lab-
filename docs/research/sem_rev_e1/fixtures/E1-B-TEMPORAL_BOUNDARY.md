# E1-B — Temporal Overlap / Boundary

**Family:** E1-B  
**Hypothesis:** H2  
**PHYSICAL_CORE:** E1-B-01, E1-B-02, E1-B-03  
**DUAL_CHECK_SAME_WORLD:** E1-B-04 on B-02  
**TRUE_PAIRWISE:** P-B-eff  

**Record-family rule:** assertion owns temporal/currentness; authority_decision binds via `assertion_id`.

```text
ASSERTION CURRENTNESS ≠ AUTHORITY DECISION OUTCOME
REVISIONS TARGET ASSERTIONS ONLY
```

---

## Shared world — explicit bindings

| Assertion | Bound decision |
|-----------|----------------|
| `as:e1b-0` | `dec:e1b-0` |
| `as:e1b-1` | `dec:e1b-1` |

### Assertions (own temporal / uncertainty / declared_loss)

| ID | force | entity | scope | asserted_at | recorded_at | valid_from | valid_to | uncertainty | declared_loss |
|----|-------|--------|-------|-------------|-------------|------------|----------|-------------|---------------|
| `as:e1b-0` | decision | ent:service:mira | scope:production-us | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z | 2026-01-01T00:00:00Z | **2026-02-01T00:00:00Z** | NULL | 0 |
| `as:e1b-1` | decision | ent:service:mira | scope:production-us | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z | 2026-02-01T00:00:00Z | NULL | NULL | 0 |

### Authority decisions (outcome / authority / effective_from only)

| decision_id | assertion_id | authority_id | outcome | semantic_force | scope_id | reason | effective_from | recorded_at |
|-------------|--------------|--------------|---------|----------------|----------|--------|----------------|-------------|
| `dec:e1b-0` | `as:e1b-0` | principal:release-board | approved | authority_decision | scope:production-us | `R_E1_B0` | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z |
| `dec:e1b-1` | `as:e1b-1` | principal:release-board | approved | authority_decision | scope:production-us | `R_E1_B1` | **2026-02-01T00:00:00Z** | 2026-01-25T01:00:00Z |

### Revision (assertion targets only)

| revision_id | type | target_assertion_id | replacement_assertion_id | reason | effective_from | recorded_at |
|-------------|------|---------------------|--------------------------|--------|----------------|-------------|
| `rev:e1b-0-to-1` | supersedes | `as:e1b-0` | `as:e1b-1` | `R_E1_B_SUPERSEDE` | 2026-02-01T00:00:00Z | 2026-01-25T01:00:00Z |

Temporal contract on **assertions**:

```text
valid_from <= T AND (valid_to IS NULL OR T < valid_to)
```

---

## E1-B-01 — `query_as_of=2026-01-31T23:59:59Z` (NEG)

```text
as:e1b-0.status=current
as:e1b-1.status=not_yet_effective
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-0
qualified_decision_ids does_not_contain dec:e1b-1
dec:e1b-0.outcome=approved
```

FORBIDDEN: `dec:e1b-1` qualified before its `effective_from`; `NO_QUALIFIED_RESULT` while `as:e1b-0` remains valid; `as:e1b-0` incorrectly expired before `valid_to`.

---

## E1-B-02 — `query_as_of=2026-02-01T00:00:00Z` (POS)

```text
as:e1b-0.status=not_temporally_applicable
as:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
dec:e1b-1.outcome=approved
```

## E1-B-04 — DUAL_CHECK on B-02

Same world/instant. Emphasize exclusive `valid_to` on **`as:e1b-0`**.

## E1-B-03 — `query_as_of=2026-02-15T00:00:00Z` (POS)

```text
as:e1b-1.status=current
as:e1b-0.status=not_current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
```
