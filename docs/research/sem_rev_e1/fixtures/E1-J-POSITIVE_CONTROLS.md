# E1-J — Positive Controls

**PHYSICAL_CORE:** E1-J-01  
**ROLE_ALIAS:** E1-J-02 → E1-G-04  

---

## E1-J-01 — Straightforward approve (POS)

**Binding:** `as:e1j-pos-1` ↔ `dec:e1j-pos-1`

### Query

`Is VX-55 approved for Kepler in production-apac?`  
`query_scope=scope:production-apac` · `query_as_of=2026-02-01T00:00:00Z`

### Assertion `as:e1j-pos-1`

| Field | Value |
|-------|-------|
| entity_id | ent:service:kepler |
| semantic_force | decision |
| scope_id | scope:production-apac |
| asserted_at | 2026-01-22T00:00:00Z |
| recorded_at | 2026-01-22T01:00:00Z |
| valid_from | 2026-01-22T00:00:00Z |
| valid_to | NULL |
| uncertainty | NULL |
| declared_loss | 0 |

### Decision `dec:e1j-pos-1`

| Field | Value |
|-------|-------|
| assertion_id | as:e1j-pos-1 |
| authority_id | principal:release-board |
| outcome | approved |
| semantic_force | authority_decision |
| scope_id | scope:production-apac |
| reason | R_E1_J_RELEASE_CRITERIA_MET |
| effective_from | 2026-01-22T00:00:00Z |
| recorded_at | 2026-01-22T01:00:00Z |

### REQUIRED

```text
as:e1j-pos-1.status=current
as:e1j-pos-1.declared_loss=0
dec:e1j-pos-1.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1j-pos-1
subject=ent:service:kepler
scope=scope:production-apac
authority=principal:release-board
```

## E1-J-02

ROLE_ALIAS of physical E1-G-04 (not independent evidence).
