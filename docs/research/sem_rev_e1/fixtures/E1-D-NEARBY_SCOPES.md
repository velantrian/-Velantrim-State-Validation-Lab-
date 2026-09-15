# E1-D — Nearby / Colliding Scopes

**Family:** E1-D  
**Hypothesis:** H3 (H10 for positive arm)  
**CORE cases:** E1-D-01, E1-D-02, E1-D-03  
**Pair:** P-D-scope — **Δ = query_scope only**

---

## Shared world

- `entity_id`: `ent:service:kepler`
- `dec:e1d-us`:
  - `semantic_force=authority_decision`
  - `scope_id=scope:production-us`
  - `outcome=approved`
  - `authority=principal:release-board`
  - `asserted_at=recorded_at=effective_from=valid_from=2026-01-20T00:00:00Z`
  - `valid_to=NULL`
  - `observed_at=UNKNOWN`
  - `uncertainty=UNKNOWN`
  - `declared_loss=UNKNOWN`
- Nearby non-identical scopes exist in vocabulary only (not auto-merged):
  `scope:production-eu`, `scope:production-us-canary`, `scope:lab-us`

| Case | query_scope | query_as_of | Expected |
|------|-------------|-------------|----------|
| E1-D-01 | `scope:production-eu` | 2026-02-01T00:00:00Z | NO_QUALIFIED_RESULT; scope_mismatch; **no widen** |
| E1-D-02 | `scope:production-us-canary` | 2026-02-01T00:00:00Z | NO_QUALIFIED_RESULT; scope_mismatch; **no widen** |
| E1-D-03 | `scope:production-us` | 2026-02-01T00:00:00Z | QUALIFIED_RESULT; `dec:e1d-us` (**POS**) |

Semantic similarity of names must not widen scope.
