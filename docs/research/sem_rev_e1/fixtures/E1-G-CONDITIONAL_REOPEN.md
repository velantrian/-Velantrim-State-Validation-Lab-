# E1-G — Conditional Reopen

**Family:** E1-G  
**Hypothesis:** H7 (H10 for G-04)  
**CORE cases:** E1-G-01 … E1-G-04  
**Pair:** P-G-re

---

## Shared base

- `entity_id`: `ent:project:nova`
- `scope_id`: `scope:project-nova`
- Prior decision `dec:e1g-prior` (Path-Prior), force=decision, later **superseded**
  by `dec:e1g-succ` (Path-Succ) via `rev:e1g-sup`.
- Frozen reopen condition (compound):

```text
REOPEN_E1G = K_CONSTRAINT_REMOVED AND OWNER_REAPPROVES_PRIOR
```

- Reopen must **not** mean “superseded once ⇒ never return”
- Reopen must **not** mean “condition mentioned ⇒ automatically current”

| Case | K_CONSTRAINT_REMOVED | OWNER_REAPPROVES_PRIOR | Expected |
|------|----------------------|------------------------|----------|
| E1-G-01 | false | false | prior remains superseded_not_current |
| E1-G-02 | true | false | partial → **not** reopen |
| E1-G-03 | true | **absent/UNKNOWN** (no reapproval record) | full flags incomplete → **not** reopen |
| E1-G-04 | true | true (explicit reapproval decision present) | legitimate reopen → prior current (**POS**) |

### Typed fields on reopen satisfaction records (G-04)

- `dec:e1g-reapprove`: force=authority_decision; outcome=approved;
  authority=`principal:project-owner`; scope=project-nova;
  effective_from / valid_from as preregistered;
  reason `R_E1_G_REAPPROVE_PRIOR`
- Constraint-removed marker: typed revision/flag record `rev:e1g-k-removed`
  effective before query_as_of

`query_as_of`: `2026-03-01T00:00:00Z` for all G cases (world flags vary).
