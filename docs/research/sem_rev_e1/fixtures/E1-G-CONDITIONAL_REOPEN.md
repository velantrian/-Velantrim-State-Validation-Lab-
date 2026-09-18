# E1-G — Reopen / Path-Return (Expressibility-Corrected)

**Family:** E1-G  
**Hypothesis:** H7 (narrowed)  
**NX:** E1-G-NX — compound reopen-condition evaluation  
**PHYSICAL_CORE:** E1-G-04 — new-version path return  
**ROLE_ALIAS:** E1-J-02 → E1-G-04  

---

## Invariant

```text
REOPEN PATH ≠ REVIVE OLD ASSERTION/DECISION IDENTITY
HISTORICAL IDENTITY ≠ NEW CURRENT VERSION
```

---

## E1-G-NX — Compound condition evaluation

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

`K_CONSTRAINT_REMOVED ∧ OWNER_REAPPROVES_PRIOR` has no registered typed
condition/flag primitive. Do not invent `rev:e1g-k-removed` as a magic flag.

---

## E1-G-04 — New explicit version returns to Path-Prior (FULLY PRE-REGISTERED)

### Query

- `fixture_id`: `E1-G-04`
- `entity_id`: `ent:project:nova`
- `query`: `What is the current path decision for project Nova?`
- `query_scope`: `scope:project-nova`
- `query_as_of`: `2026-03-01T00:00:00Z`

### Assertion / decision inventory (exact — no “as needed”)

| ID | Kind | Force | Path content | scope | asserted_at | recorded_at | valid_from | valid_to | declared_loss | uncertainty |
|----|------|-------|--------------|-------|-------------|-------------|------------|----------|---------------|-------------|
| `as:e1g-prior-v1` | assertion | decision | Path-Prior | scope:project-nova | 2026-01-05T00:00:00Z | 2026-01-05T01:00:00Z | 2026-01-05T00:00:00Z | NULL | 0 | NULL |
| `as:e1g-succ` | assertion | decision | Path-Succ | scope:project-nova | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z | 2026-01-20T00:00:00Z | NULL | 0 | NULL |
| `as:e1g-prior-v2` | assertion | decision | Path-Prior | scope:project-nova | 2026-02-15T00:00:00Z | 2026-02-15T01:00:00Z | 2026-02-15T00:00:00Z | NULL | 0 | NULL |

### Authority decisions (exact)

| decision_id | assertion_id | authority_id | outcome | semantic_force | scope_id | reason | effective_from | recorded_at |
|-------------|--------------|--------------|---------|----------------|----------|--------|----------------|-------------|
| `dec:e1g-prior-v1` | `as:e1g-prior-v1` | `principal:project-owner` | approved | authority_decision | scope:project-nova | `R_E1_G_PRIOR_V1` | 2026-01-05T00:00:00Z | 2026-01-05T01:00:00Z |
| `dec:e1g-succ` | `as:e1g-succ` | `principal:project-owner` | approved | authority_decision | scope:project-nova | `R_E1_G_SUCC` | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z |
| `dec:e1g-prior-v2` | `as:e1g-prior-v2` | `principal:project-owner` | approved | authority_decision | scope:project-nova | `R_E1_G_PRIOR_V2` | 2026-02-15T00:00:00Z | 2026-02-15T01:00:00Z |

### Revisions (exact)

| revision_id | revision_type | target | replacement | reason | effective_from | recorded_at |
|-------------|---------------|--------|-------------|--------|----------------|-------------|
| `rev:e1g-v1-to-succ` | supersedes | `as:e1g-prior-v1` | `as:e1g-succ` | `R_E1_G_V1_SUPERSEDED` | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z |
| `rev:e1g-succ-to-v2` | supersedes | `as:e1g-succ` | `as:e1g-prior-v2` | `R_E1_G_SUCC_SUPERSEDED` | 2026-02-15T00:00:00Z | 2026-02-15T01:00:00Z |

### Exact expected state

```text
as:e1g-prior-v1.status=superseded
as:e1g-succ.status=superseded
as:e1g-prior-v2.status=current
dec:e1g-prior-v2.status=current
current_path=Path-Prior
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1g-prior-v2
qualified_decision_ids does_not_contain dec:e1g-prior-v1
qualified_decision_ids does_not_contain dec:e1g-succ
same_id_resurrection=false
```

FORBIDDEN: same-ID revival of `as:e1g-prior-v1`; `current_via_legitimate_reopen`; OR dual forms; magic condition flags.
