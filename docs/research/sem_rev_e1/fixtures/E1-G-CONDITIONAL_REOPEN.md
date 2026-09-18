# E1-G — Reopen / Path-Return (Expressibility-Corrected)

**Family:** E1-G  
**Hypothesis:** H7 (**narrowed**)  
**NX:** E1-G-NX — compound reopen-condition evaluation  
**Physical CORE:** E1-G-04 — new-version path return  
**ROLE_ALIAS:** E1-J-02 → E1-G-04  

---

## Invariant

```text
REOPEN PATH ≠ REVIVE OLD ASSERTION/DECISION IDENTITY
HISTORICAL IDENTITY ≠ NEW CURRENT VERSION
```

Same-ID resurrection is forbidden.

---

## E1-G-NX — Compound condition evaluation (NOT EXPRESSIBLE)

Desired compound condition from earlier draft:

```text
K_CONSTRAINT_REMOVED AND OWNER_REAPPROVES_PRIOR
```

Existing E0 contract provides:

- `revision` rows with typed `retracts` / `supersedes` (and similar registered types);
- `authority_decision` rows;
- optional prose/metadata field `reopen_requires` on assertions (**documentation string, not an evaluated condition engine**).

There is **no** registered typed primitive for a generic “constraint removed”
boolean / flag record. A revision id such as `rev:e1g-k-removed` must **not**
be used as a magic condition flag merely because its prefix is `rev:`.

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

Former G-01 / G-02 / G-03 (unsatisfied / half / missing-reapproval lattices)
are **not** CORE oracles under this candidate. They are documented intent only
inside this NX boundary.

Do **not** invent: flag records, condition engines, magic booleans, or
per-fixture answer fields.

---

## E1-G-04 — New explicit version returns to Path-Prior (CORE POS)

Uses **only** existing record families: assertion/decision + `supersedes`.

### Identities

| ID | Role | Force | Notes |
|----|------|-------|-------|
| `as:e1g-prior-v1` / path content Path-Prior | historical prior | decision | later superseded |
| `as:e1g-succ` / Path-Succ | successor | decision | supersedes v1 |
| `as:e1g-prior-v2` / Path-Prior again | **new** version | decision | **new identity** |
| `rev:e1g-v1-to-succ` | supersedes | revision | v1 → succ |
| `rev:e1g-succ-to-v2` | supersedes | revision | succ → **prior-v2** |
| `dec:e1g-*` authority rows | as needed | authority_decision | scope=`scope:project-nova`; `declared_loss=0` |

- `entity_id`: `ent:project:nova`
- `scope_id`: `scope:project-nova`
- `query_as_of`: `2026-03-01T00:00:00Z`

### Exact expected state (single-valued)

```text
as:e1g-prior-v1.status=superseded
as:e1g-succ.status=superseded
as:e1g-prior-v2.status=current
current_path=Path-Prior
status=QUALIFIED_RESULT
qualified ids include as:e1g-prior-v2 / its decision binding
as:e1g-prior-v1 must_not_be_current
same_id_resurrection=false
```

FORBIDDEN:

```text
as:e1g-prior-v1.status=current
current_via_legitimate_reopen (ambiguous form banned)
same-ID revival of prior-v1
OR-form dual expectations
```

This tests **path return via new version + supersession**, not compound
condition evaluation.
