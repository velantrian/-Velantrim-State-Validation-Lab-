# E1-E — Conflicting Authority Decisions

**Family:** E1-E  
**Hypothesis:** H4  
**CORE cases:** E1-E-01, E1-E-02, E1-E-03  
**Boundary:** E1-E-NX (`NOT EXPRESSIBLE UNDER CURRENT CONTRACT`)

---

## Policy

Do **not** invent a new authority hierarchy. Prefer cases expressible with:

- jurisdiction / scope mismatch;
- outcome refused vs approved;
- typed supersession.

---

## E1-E-01 — Out of jurisdiction (CORE NEG)

- Query: approved? for `ent:service:kepler` in `scope:production-us` at `2026-02-01T00:00:00Z`
- `dec:e1e-foreign`:
  - force=authority_decision; outcome=approved;
  - `scope_id=scope:lab-us` (not production-us);
  - authority=`principal:lab-reviewer`;
  - effective/valid_from 2026-01-15
- **Expected:** not qualified for production-us; jurisdiction/scope mismatch

## E1-E-02 — Refused outcome (CORE NEG)

- Same query scope production-us
- `dec:e1e-refused`: scope=production-us; outcome=**refused**; authority=release-board; effective 2026-01-18
- **Expected:** NO_QUALIFIED_RESULT; authority_outcome_refused; **no flip to approved**

## E1-E-03 — Superseded authority decision (CORE NEG)

- `dec:e1e-old`: approved; production-us; effective 2026-01-10
- `dec:e1e-new`: refused; production-us; effective 2026-01-25
- `rev:e1e-old-to-new` supersedes old→new effective 2026-01-25
- Query as_of 2026-02-01
- **Expected:** old not current; new’s refused outcome prevents approved qualification

## E1-E-NX — Two in-jurisdiction conflicting approvals (BOUNDARY)

Two `authority_decision` records, both `scope:production-us`, both `outcome=approved`,
different authorities (`principal:release-board` vs `principal:security-board`),
overlapping validity, **no typed supersession / jurisdiction discriminator**.

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

Reason: selecting a winner requires an unregistered global authority precedence
primitive. Documented as `OUT_OF_CURRENT_E1_SCOPE` for CORE scoring — **not** a
hidden expected winner.

`NEW_ARCHITECTURAL_PRIMITIVE_REQUIRED` for *resolving* NX = YES if one insisted
on a winner; for E1 CORE design = **NO** (we refuse to invent it).
