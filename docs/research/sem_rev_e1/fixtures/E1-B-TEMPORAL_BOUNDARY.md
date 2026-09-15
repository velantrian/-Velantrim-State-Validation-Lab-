# E1-B — Temporal Overlap / Boundary

**Family:** E1-B  
**Hypothesis:** H2  
**CORE cases:** E1-B-01 … E1-B-04  
**Pair groups:** P-B-eff, P-B-bound

---

## Shared world (identical records; only query_as_of changes for B-01..B-03)

- `entity_id`: `ent:service:mira`
- `scope_id`: `scope:production-us`
- `dec:e1b-0` decision (older), `valid_from=2026-01-01T00:00:00Z`, `valid_to=2026-02-01T00:00:00Z`, asserted/recorded 2026-01-01, authority approved, force=authority_decision
- `dec:e1b-1` decision (newer), `valid_from=2026-02-01T00:00:00Z`, `valid_to=NULL`, `effective_from=2026-02-01T00:00:00Z` via `rev:e1b-0-to-1` supersedes e1b-0, asserted/recorded 2026-01-25, outcome=approved, authority=`principal:release-board`
- `uncertainty` / `declared_loss` / `observed_at`: `UNKNOWN` unless noted

### Material Δ (P-B-eff)

| Case | query_as_of | Expected |
|------|-------------|----------|
| E1-B-01 | `2026-01-31T23:59:59Z` | `dec:e1b-1` **not yet effective**; do not treat as current |
| E1-B-02 | `2026-02-01T00:00:00Z` | `dec:e1b-1` temporally applicable (boundary); current if supersession effective |
| E1-B-03 | `2026-02-15T00:00:00Z` | `dec:e1b-1` current; `dec:e1b-0` not current despite historical overlap narrative |

### E1-B-04 (exclusive valid_to) — P-B-bound

Same `dec:e1b-0` interval ending `valid_to=2026-02-01T00:00:00Z`.

- `query_as_of`: `2026-02-01T00:00:00Z`
- **Expected:** `dec:e1b-0` **not** temporally applicable (`T < valid_to` fails when T == valid_to)
- If evaluated without supersession context alone: must not treat e1b-0 as current at T=valid_to

### Required axes preserved

`valid_from`, `valid_to`, `effective_from`, `query_as_of` distinct; no use of `recorded_at` as semantic currentness.
