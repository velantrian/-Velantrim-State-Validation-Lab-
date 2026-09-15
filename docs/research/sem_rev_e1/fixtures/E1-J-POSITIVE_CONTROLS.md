# E1-J — Positive Controls

**Family:** E1-J  
**Hypothesis:** H10  
**CORE cases:** E1-J-01 (dedicated), E1-J-02 (cross-ref E1-G-04)

---

## Purpose

Defeat trivial “exclude everything” strategies.

---

## E1-J-01 — Straightforward current approved decision

- `fixture_id`: `E1-J-01`
- `entity_id`: `ent:service:kepler`
- `query`: `Is VX-55 approved for Kepler in production-apac?`
- `query_scope`: `scope:production-apac`
- `query_as_of`: `2026-02-01T00:00:00Z`

### Decision `dec:e1j-pos-1`

| Field | Value |
|-------|-------|
| semantic_force | authority_decision |
| outcome | approved |
| authority | principal:release-board |
| scope_id | scope:production-apac |
| subject | ent:service:kepler |
| asserted_at | 2026-01-22T00:00:00Z |
| recorded_at | 2026-01-22T01:00:00Z |
| effective_from | 2026-01-22T00:00:00Z |
| valid_from | 2026-01-22T00:00:00Z |
| valid_to | NULL |
| observed_at | UNKNOWN |
| uncertainty | UNKNOWN |
| declared_loss | UNKNOWN |
| reason | R_E1_J_RELEASE_CRITERIA_MET |
| revision_relation | none |

### REQUIRED

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1j-pos-1
subject=ent:service:kepler
scope=scope:production-apac
outcome=approved
semantic_force=authority_decision
authority=principal:release-board
```

### FORBIDDEN

```text
NO_QUALIFIED_RESULT
outcome=refused
wrong scope
authority=UNKNOWN
decision omitted
trivial abstention
```

---

## E1-J-02 — Legitimate conditional reopen

**Physical content:** identical to **E1-G-04**.

Listed here as a positive-control **role** so H10 coverage is explicit.
CORE suite must not count contradictory duplicate oracles; treat as one
physical fixture with dual role tags `{E1-G-04, E1-J-02}`.
