# E1-E — Conflicting Authority Decisions

**Family:** E1-E  
**Hypothesis:** H4 (narrowed)  
**PHYSICAL_CORE:** E1-E-01, E1-E-02, E1-E-03  
**NX:** E1-E-NX  
**CONTRAST_GROUPS:** CG-E-scope (E-01), CG-E-out (E-02), CG-E-sup (E-03)

---

## E1-E-01 — Scope mismatch (NEG)

Query: approved? `ent:service:kepler` / `scope:production-us` / `2026-02-01T00:00:00Z`

`dec:e1e-foreign`: force=authority_decision; outcome=approved; `scope_id=scope:lab-us`;
authority=`principal:lab-reviewer`; effective 2026-01-15; `declared_loss=0`

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-foreign contains scope_mismatch
```

SCOPE ≠ JURISDICTION. Principal names are not jurisdiction atoms.

---

## E1-E-02 — Refused outcome (NEG) — CG-E-out

`dec:e1e-refused`: scope=production-us; outcome=refused; authority=release-board;
effective 2026-01-18; `declared_loss=0`

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-refused contains authority_outcome_refused
```

---

## E1-E-03 — Superseded authority decision (NEG) — CG-E-sup — EXACT ORACLE

World:

| ID | outcome | scope | effective_from | recorded_at | declared_loss |
|----|---------|-------|----------------|-------------|---------------|
| `dec:e1e-old` | approved | scope:production-us | 2026-01-10T00:00:00Z | 2026-01-10T01:00:00Z | 0 |
| `dec:e1e-new` | refused | scope:production-us | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z | 0 |
| `rev:e1e-old-to-new` | supersedes old→new | — | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z | — |

Query: approved? same entity/scope; `query_as_of=2026-02-01T00:00:00Z`

```text
dec:e1e-old.status=superseded
dec:e1e-new.status=current
dec:e1e-new.outcome=refused
status=NO_QUALIFIED_RESULT
qualified_approved_decision_ids does_not_contain dec:e1e-old
qualified_approved_decision_ids does_not_contain dec:e1e-new
```

(Approved-query qualification set empty; refused current decision must not count as approved.)

---

## E1-E-NX — Genuine unresolved authority conflict (BOUNDARY)

Same scope, overlapping validity, **no** typed supersession, **no** typed precedence:

| ID | authority | outcome | scope | effective_from | valid_from | valid_to |
|----|-----------|---------|-------|----------------|------------|----------|
| `dec:e1e-nx-a` | principal:release-board | **approved** | scope:production-us | 2026-01-10T00:00:00Z | 2026-01-10T00:00:00Z | NULL |
| `dec:e1e-nx-b` | principal:security-board | **refused** | scope:production-us | 2026-01-12T00:00:00Z | 2026-01-12T00:00:00Z | NULL |

Query as_of inside both intervals. Outcomes **disagree**.

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

Do **NOT** select a winner. Not a CORE oracle.
