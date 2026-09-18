# E1-B — Temporal Overlap / Boundary

**Family:** E1-B  
**Hypothesis:** H2  
**PHYSICAL_CORE:** E1-B-01, E1-B-02, E1-B-03, **E1-B-04** (isolated valid_to world)  
**TRUE_PAIRWISE:** P-B-eff (B-01 / B-02 / B-03; Δ = `query_as_of` only)

```text
E0 status vocabulary only: current | not_current | retracted | superseded
TEMPORAL REASON ≠ NEW STATUS PRIMITIVE
ASSERTION CURRENTNESS ≠ AUTHORITY DECISION OUTCOME
REVISIONS TARGET ASSERTIONS ONLY
```

---

## Shared world for B-01 / B-02 / B-03

| Assertion | Bound decision |
|-----------|----------------|
| `as:e1b-0` | `dec:e1b-0` |
| `as:e1b-1` | `dec:e1b-1` |

### Assertions

| ID | force | entity | scope | asserted_at | recorded_at | valid_from | valid_to | uncertainty | declared_loss |
|----|-------|--------|-------|-------------|-------------|------------|----------|-------------|---------------|
| `as:e1b-0` | decision | ent:service:mira | scope:production-us | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z | 2026-01-01T00:00:00Z | 2026-02-01T00:00:00Z | NULL | 0 |
| `as:e1b-1` | decision | ent:service:mira | scope:production-us | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z | 2026-02-01T00:00:00Z | NULL | NULL | 0 |

### Decisions

| decision_id | assertion_id | authority | outcome | force | scope | reason | effective_from | recorded_at |
|-------------|--------------|-----------|---------|-------|-------|--------|----------------|-------------|
| `dec:e1b-0` | as:e1b-0 | principal:release-board | approved | authority_decision | scope:production-us | R_E1_B0 | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z |
| `dec:e1b-1` | as:e1b-1 | principal:release-board | approved | authority_decision | scope:production-us | R_E1_B1 | 2026-02-01T00:00:00Z | 2026-01-25T01:00:00Z |

### Revision

| revision_id | type | target_assertion_id | replacement_assertion_id | reason | effective_from | recorded_at |
|-------------|------|---------------------|--------------------------|--------|----------------|-------------|
| `rev:e1b-0-to-1` | supersedes | as:e1b-0 | as:e1b-1 | R_E1_B_SUPERSEDE | 2026-02-01T00:00:00Z | 2026-01-25T01:00:00Z |

---

## E1-B-01 — `query_as_of=2026-01-31T23:59:59Z` (NEG)

```text
as:e1b-0.status=current
as:e1b-1.status=not_current
reason/check: as:e1b-1 excluded because valid_from/effective_from > query_as_of
dec:e1b-0.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-0
qualified_decision_ids does_not_contain dec:e1b-1
```

---

## E1-B-02 — `query_as_of=2026-02-01T00:00:00Z` (POS)

Effective supersession applies; exact E0 statuses:

```text
as:e1b-0.status=superseded
as:e1b-1.status=current
dec:e1b-1.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

---

## E1-B-03 — `query_as_of=2026-02-15T00:00:00Z` (POS)

```text
as:e1b-0.status=superseded
as:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
```

---

## E1-B-04 — Isolated exclusive `valid_to` (PHYSICAL, NEG)

**Separate world.** No supersession / retract / invalidate. Isolates `T < valid_to`.

### Binding

`as:e1b-bound` ↔ `dec:e1b-bound`

### Assertion `as:e1b-bound`

| Field | Value |
|-------|-------|
| entity_id | ent:service:mira |
| semantic_force | decision |
| scope_id | scope:production-us |
| asserted_at | 2026-01-01T00:00:00Z |
| recorded_at | 2026-01-01T01:00:00Z |
| valid_from | 2026-01-01T00:00:00Z |
| valid_to | 2026-02-01T00:00:00Z |
| uncertainty | NULL |
| declared_loss | 0 |

### Decision `dec:e1b-bound`

| Field | Value |
|-------|-------|
| assertion_id | as:e1b-bound |
| authority_id | principal:release-board |
| outcome | approved |
| semantic_force | authority_decision |
| scope_id | scope:production-us |
| reason | R_E1_B_BOUND |
| effective_from | 2026-01-01T00:00:00Z |
| recorded_at | 2026-01-01T01:00:00Z |

### Query

`query_as_of=2026-02-01T00:00:00Z` · scope=production-us · approved?

At `T == valid_to`, `T < valid_to` fails → interval does not apply; no revision → **`not_current`**.

```text
as:e1b-bound.status=not_current
reason/check: valid_to exclusive boundary caused temporal non-applicability
status=NO_QUALIFIED_RESULT
qualified_decision_ids does_not_contain dec:e1b-bound
```

FORBIDDEN: invent status `not_temporally_applicable`; confound with supersession; qualify `dec:e1b-bound`.
