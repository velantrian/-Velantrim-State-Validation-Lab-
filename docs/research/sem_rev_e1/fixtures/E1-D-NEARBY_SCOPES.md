# E1-D — Nearby / Colliding Scopes

**Family:** E1-D  
**Hypothesis:** H3  
**PHYSICAL_CORE:** E1-D-01, E1-D-02, E1-D-03  
**TRUE_PAIRWISE:** P-D-scope (Δ = `query_scope` only)

---

## Binding

`as:e1d-us` ↔ `dec:e1d-us`

### Assertion `as:e1d-us`

| Field | Value |
|-------|-------|
| entity_id | ent:service:kepler |
| semantic_force | decision |
| scope_id | scope:production-us |
| asserted_at | 2026-01-20T00:00:00Z |
| recorded_at | 2026-01-20T01:00:00Z |
| valid_from | 2026-01-20T00:00:00Z |
| valid_to | NULL |
| uncertainty | NULL |
| declared_loss | 0 |

### Authority decision `dec:e1d-us`

| Field | Value |
|-------|-------|
| assertion_id | as:e1d-us |
| authority_id | principal:release-board |
| outcome | approved |
| semantic_force | authority_decision |
| scope_id | scope:production-us |
| reason | R_E1_D_US |
| effective_from | 2026-01-20T00:00:00Z |
| recorded_at | 2026-01-20T01:00:00Z |

Nearby scopes (not auto-merged): `scope:production-eu`, `scope:production-us-canary`, `scope:lab-us`.

| Case | query_scope | Category | Expected |
|------|-------------|----------|----------|
| E1-D-01 | production-eu | NEG | NO_QUALIFIED_RESULT; `excluded.dec:e1d-us contains scope_mismatch` |
| E1-D-02 | production-us-canary | NEG | same |
| E1-D-03 | production-us | POS | QUALIFIED_RESULT; `qualified_decision_ids contains dec:e1d-us`; `as:e1d-us.status=current`; `dec:e1d-us.outcome=approved` |
