# E1-E — Conflicting Authority Decisions

**Family:** E1-E  
**Hypothesis:** H4 (narrowed: typed outcome/supersession/scope; **not** jurisdiction)  
**Physical CORE:** E1-E-01, E1-E-02, E1-E-03  
**NX:** E1-E-NX  
**CONTRAST_GROUPS:** CG-E-out (E-02), CG-E-sup (E-03)  
**Note:** former “P-E-jur” renamed — E-01 is a **scope_mismatch** contrast, not jurisdiction.

---

## Policy

Do **not** invent a new authority hierarchy or jurisdiction relation.
`SCOPE ≠ JURISDICTION`. Principal names do **not** encode jurisdiction.

---

## E1-E-01 — Scope mismatch (CORE NEG)

- Query: approved? for `ent:service:kepler` in `scope:production-us` at `2026-02-01T00:00:00Z`
- `dec:e1e-foreign`:
  - force=authority_decision; outcome=approved;
  - `scope_id=scope:lab-us` (**not** production-us);
  - authority=`principal:lab-reviewer` (name is **not** a jurisdiction atom);
  - effective/valid_from 2026-01-15
  - `declared_loss=0`
- **Expected:**

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-foreign contains scope_mismatch
```

This proves typed **scope_mismatch**. It does **not** prove authority-jurisdiction.

---

## E1-E-02 — Refused outcome (CORE NEG) — CONTRAST_GROUP CG-E-out

- Same query scope production-us
- `dec:e1e-refused`: scope=production-us; outcome=**refused**; authority=release-board; effective 2026-01-18; `declared_loss=0`
- **Expected:**

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-refused contains authority_outcome_refused
```

No flip to approved.

---

## E1-E-03 — Superseded authority decision (CORE NEG) — CONTRAST_GROUP CG-E-sup

- `dec:e1e-old`: approved; production-us; effective 2026-01-10; `declared_loss=0`
- `dec:e1e-new`: refused; production-us; effective 2026-01-25; `declared_loss=0`
- `rev:e1e-old-to-new` supersedes old→new effective 2026-01-25
- Query as_of 2026-02-01
- **Expected:** old not current; refused successor prevents approved qualification

---

## E1-E-NX — Two same-scope conflicting approvals (BOUNDARY)

Two `authority_decision` records, both `scope:production-us`, both `outcome=approved`,
different authorities, overlapping validity, **no typed supersession**.

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

Selecting a winner requires an unregistered authority-precedence primitive.
Not a CORE oracle. Do not invent a winner.
