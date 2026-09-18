# E1-D — Nearby / Colliding Scopes

**Family:** E1-D  
**Hypothesis:** H3 (H10 for positive arm)  
**Physical CORE cases:** E1-D-01, E1-D-02, E1-D-03  
**TRUE_PAIRWISE:** P-D-scope — **Δ = `query_scope` only**

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
  - `uncertainty`: NULL → optional UNKNOWN when projected
  - `declared_loss`: `0`
- Nearby non-identical scopes (not auto-merged):
  `scope:production-eu`, `scope:production-us-canary`, `scope:lab-us`

| Case | query_scope | query_as_of | Category | Expected |
|------|-------------|-------------|----------|----------|
| E1-D-01 | `scope:production-eu` | 2026-02-01T00:00:00Z | NEG | NO_QUALIFIED_RESULT; `excluded.dec:e1d-us contains scope_mismatch`; **no widen** |
| E1-D-02 | `scope:production-us-canary` | 2026-02-01T00:00:00Z | NEG | NO_QUALIFIED_RESULT; `excluded.dec:e1d-us contains scope_mismatch`; **no widen** |
| E1-D-03 | `scope:production-us` | 2026-02-01T00:00:00Z | POS | QUALIFIED_RESULT; `dec:e1d-us` |

Semantic similarity of names must not widen scope.
