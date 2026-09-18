# E1-J — Positive Controls

**Family:** E1-J  
**Hypothesis:** H10  
**Physical CORE:** E1-J-01  
**ROLE_ALIAS:** E1-J-02 → E1-G-04 (new-version path return)

---

## Purpose

Defeat trivial “exclude everything” strategies.

---

## E1-J-01 — Straightforward current approved decision (PHYSICAL POS)

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
| uncertainty | NULL → optional UNKNOWN if projected |
| declared_loss | **0** |
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
declared_loss=0
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

## E1-J-02 — ROLE_ALIAS of E1-G-04

Positive-control **role tag** on the physical E1-G-04 new-version path-return
fixture. **Not** independent experimental evidence.
