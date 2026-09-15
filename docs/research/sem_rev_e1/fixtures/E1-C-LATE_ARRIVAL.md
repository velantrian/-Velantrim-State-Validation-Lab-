# E1-C — Late-Arriving Record

**Family:** E1-C  
**Hypotheses:** H6 (primary), H2  
**CORE cases:** E1-C-01, E1-C-02  
**Pair:** P-C-rec

---

## Purpose

A semantic event occurs at T1 but is recorded later at T3; another state is
recorded at T2. Later recording must not incorrectly imply later semantic
authority/currentness.

---

## Shared entity

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:production-us`
- `query_as_of`: `2026-02-20T00:00:00Z`
- `query`: `Is there a current approved authority decision for Mira in production-us?`

### Records

| ID | Force | observed_at | asserted_at | recorded_at | effective_from | valid_from | outcome |
|----|-------|-------------|-------------|-------------|----------------|------------|---------|
| `as:e1c-old` | observation | 2026-01-10T00:00:00Z | 2026-01-10T00:00:00Z | **2026-02-18T00:00:00Z** (late) | — | 2026-01-10T00:00:00Z | — |
| `dec:e1c-new` | authority_decision | UNKNOWN | 2026-02-01T00:00:00Z | **2026-02-02T00:00:00Z** | 2026-02-01T00:00:00Z | 2026-02-01T00:00:00Z | approved |

- `scope_id` both: `scope:production-us`
- `authority` on decision: `principal:release-board`
- `uncertainty` on observation: `summary_only`
- `declared_loss`: `UNKNOWN`

### Expectations

- **E1-C-01:** late-recorded observation must **not** outrank `dec:e1c-new` by `recorded_at`
- **E1-C-02:** `dec:e1c-new` remains the current qualified authority decision
- Axes remain distinct; `recorded_at` ≠ currentness

### Material Δ

Same records; scoring emphasis differs (outrank vs current) — paired adversarial
checks on one world.
