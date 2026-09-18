# E1-C — Late-Arriving Record

**Family:** E1-C  
**Hypotheses:** H6 (primary), H2  
**Physical CORE cases:** E1-C-01, E1-C-02  
**Taxonomy:** `DUAL_CHECK_SAME_WORLD` (same records; two required check emphases)  
**Not** a TRUE_PAIRWISE (no single material Δ between distinct worlds)

---

## Purpose

A semantic event occurs at T1 but is recorded later at T3; another state is
recorded at T2. Later `recorded_at` must not incorrectly imply later semantic
authority/currentness.

---

## Shared physical world

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:production-us`
- `query_as_of`: `2026-02-20T00:00:00Z`
- `query`: `Is there a current approved authority decision for Mira in production-us?`

| ID | Force | observed_at | asserted_at | recorded_at | effective_from | valid_from | outcome | declared_loss |
|----|-------|-------------|-------------|-------------|----------------|------------|---------|---------------|
| `as:e1c-old` | observation | 2026-01-10T00:00:00Z | 2026-01-10T00:00:00Z | **2026-02-18T00:00:00Z** (late) | — | 2026-01-10T00:00:00Z | — | 0 |
| `dec:e1c-new` | authority_decision | — | 2026-02-01T00:00:00Z | **2026-02-02T00:00:00Z** | 2026-02-01T00:00:00Z | 2026-02-01T00:00:00Z | approved | 0 |

- `scope_id` both: `scope:production-us`
- `authority` on decision: `principal:release-board`
- `uncertainty` on observation: `summary_only` (typed uncertainty_id)
- axes remain distinct: `observed_at`, `asserted_at`, `recorded_at`, `effective_from`

### E1-C-01 check — late record must not outrank

```text
late_recorded_observation=as:e1c-old does_not_outrank_by_recorded_at
current_decision=dec:e1c-new
```

### E1-C-02 check — newer decision remains current

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1c-new
dec:e1c-new.status=current
```

Both checks apply to the **same** physical world. Count as one physical world
with two dual-check entries, or two physical entries that share identical
bytes — matrix uses `DUAL_CHECK_SAME_WORLD` and does **not** call this TRUE_PAIRWISE.
