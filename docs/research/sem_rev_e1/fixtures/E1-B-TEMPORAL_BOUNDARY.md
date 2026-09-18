# E1-B — Temporal Overlap / Boundary

**Family:** E1-B  
**Hypothesis:** H2  
**Physical CORE cases:** E1-B-01, E1-B-02, E1-B-03  
**Dual-check (same world as B-02):** E1-B-04  
**TRUE_PAIRWISE group:** P-B-eff (B-01 / B-02 / B-03; Δ = `query_as_of` only)  
**DUAL_CHECK_SAME_WORLD:** B-04 on physical B-02

---

## Shared world (identical records)

- `entity_id`: `ent:service:mira`
- `scope_id`: `scope:production-us`
- `dec:e1b-0` — authority_decision, outcome=approved, authority=`principal:release-board`
  - `valid_from=2026-01-01T00:00:00Z`
  - `valid_to=2026-02-01T00:00:00Z`  (**exclusive** end: applicable iff `T < valid_to`)
  - asserted/recorded 2026-01-01
- `dec:e1b-1` — authority_decision, outcome=approved, authority=`principal:release-board`
  - `valid_from=2026-02-01T00:00:00Z`, `valid_to=NULL`
  - `effective_from=2026-02-01T00:00:00Z` via `rev:e1b-0-to-1` supersedes e1b-0
  - asserted/recorded 2026-01-25
- `uncertainty`: NULL → `UNKNOWN` when projected as optional absence
- `declared_loss`: `0`
- Temporal contract:

```text
valid_from <= T
AND
(valid_to IS NULL OR T < valid_to)
```

Then revision/effective_from applies.

---

## E1-B-01 — before effective_from (PHYSICAL)

`query_as_of`: `2026-01-31T23:59:59Z`

**Tests:** premature activation of `dec:e1b-1` must not occur; still-valid `dec:e1b-0` must remain.

```text
dec:e1b-0.status=current
dec:e1b-1.status=not_yet_effective
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-0
qualified_decision_ids does_not_contain dec:e1b-1
```

FORBIDDEN:

```text
dec:e1b-1 qualified before effective_from
NO_QUALIFIED_RESULT while dec:e1b-0 remains valid
dec:e1b-0 incorrectly expired before valid_to
```

---

## E1-B-02 — exactly at effective_from / valid_to boundary (PHYSICAL)

`query_as_of`: `2026-02-01T00:00:00Z`

At this instant:

- `dec:e1b-0` is **not** temporally applicable (`T < valid_to` fails when `T == valid_to`)
- `dec:e1b-1` is valid/effective

```text
dec:e1b-0.status=not_temporally_applicable
dec:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

Category: **POS** (qualified current approved decision under exact boundary).

---

## E1-B-03 — after effective_from (PHYSICAL)

`query_as_of`: `2026-02-15T00:00:00Z`

```text
dec:e1b-1.status=current
dec:e1b-0.status=not_current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

Category: **POS** (currentness stable after boundary).

---

## E1-B-04 — exclusive valid_to check (DUAL_CHECK_SAME_WORLD on B-02)

**Not an independent physical fixture.** Same world + same `query_as_of` as E1-B-02.

Additional check emphasis (single-valued; no OR oracle):

```text
dec:e1b-0.status=not_temporally_applicable
reason includes valid_to_exclusive_boundary
dec:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

Do **not** count B-04 as independent experimental evidence.
