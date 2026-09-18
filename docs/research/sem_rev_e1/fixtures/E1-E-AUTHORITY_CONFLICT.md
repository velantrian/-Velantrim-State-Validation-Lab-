# E1-E — Conflicting Authority Decisions

**Family:** E1-E  
**Hypothesis:** H4 (narrowed)  
**PHYSICAL_CORE:** E1-E-01, E1-E-02, E1-E-03  
**NX:** E1-E-NX  

```text
ASSERTION CURRENTNESS ≠ AUTHORITY DECISION OUTCOME
SCOPE ≠ JURISDICTION
```

---

## E1-E-01 — Scope mismatch (NEG)

Bindings: `as:e1e-foreign` ↔ `dec:e1e-foreign`

**Assertion `as:e1e-foreign`:** force=decision; scope=`scope:lab-us`; asserted/recorded/valid_from=`2026-01-15T00:00:00Z`; valid_to=NULL; uncertainty=NULL; declared_loss=0; entity=`ent:service:kepler`

**Decision `dec:e1e-foreign`:** assertion_id=`as:e1e-foreign`; authority=`principal:lab-reviewer`; outcome=approved; force=authority_decision; scope=`scope:lab-us`; effective_from=`2026-01-15T00:00:00Z`; recorded_at=`2026-01-15T01:00:00Z`; reason=`R_E1_E_FOREIGN`

Query: approved? / `scope:production-us` / `2026-02-01T00:00:00Z`

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-foreign contains scope_mismatch
```

---

## E1-E-02 — Refused (NEG)

Bindings: `as:e1e-refused` ↔ `dec:e1e-refused`

**Assertion:** scope=`scope:production-us`; force=decision; valid_from=`2026-01-18T00:00:00Z`; valid_to=NULL; declared_loss=0; uncertainty=NULL

**Decision:** outcome=**refused**; authority=principal:release-board; effective_from=`2026-01-18T00:00:00Z`

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-refused contains authority_outcome_refused
```

---

## E1-E-03 — Supersession (NEG) — EXACT

| Assertion | Bound decision |
|-----------|----------------|
| `as:e1e-old` | `dec:e1e-old` |
| `as:e1e-new` | `dec:e1e-new` |

**Assertions**

| ID | force | scope | asserted_at | recorded_at | valid_from | valid_to | declared_loss |
|----|-------|-------|-------------|-------------|------------|----------|---------------|
| `as:e1e-old` | decision | production-us | 2026-01-10T00:00:00Z | 2026-01-10T01:00:00Z | 2026-01-10T00:00:00Z | NULL | 0 |
| `as:e1e-new` | decision | production-us | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z | 2026-01-25T00:00:00Z | NULL | 0 |

**Decisions**

| decision_id | assertion_id | outcome | authority | effective_from | recorded_at |
|-------------|--------------|---------|-----------|----------------|-------------|
| `dec:e1e-old` | `as:e1e-old` | approved | principal:release-board | 2026-01-10T00:00:00Z | 2026-01-10T01:00:00Z |
| `dec:e1e-new` | `as:e1e-new` | **refused** | principal:release-board | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z |

**Revision**

| revision_id | type | target_assertion_id | replacement_assertion_id | effective_from | recorded_at | reason |
|-------------|------|---------------------|--------------------------|----------------|-------------|--------|
| `rev:e1e-old-to-new` | supersedes | **`as:e1e-old`** | **`as:e1e-new`** | 2026-01-25T00:00:00Z | 2026-01-25T01:00:00Z | `R_E1_E_SUPERSEDE` |

Query approved? / production-us / `2026-02-01T00:00:00Z`

```text
as:e1e-old.status=superseded
as:e1e-new.status=current
dec:e1e-new.outcome=refused
status=NO_QUALIFIED_RESULT
qualified_approved_decision_ids does_not_contain dec:e1e-old
qualified_approved_decision_ids does_not_contain dec:e1e-new
```

Do **not** write `dec:e1e-*.status=superseded|current` as assertion-currentness atoms.

---

## E1-E-NX — Genuine unresolved conflict (BOUNDARY)

| Assertion | Bound decision | authority | outcome |
|-----------|----------------|-----------|---------|
| `as:e1e-nx-a` | `dec:e1e-nx-a` | principal:release-board | **approved** |
| `as:e1e-nx-b` | `dec:e1e-nx-b` | principal:security-board | **refused** |

Both assertions: scope=`scope:production-us`; force=decision; overlapping validity  
(`as:e1e-nx-a` valid_from=`2026-01-10`; `as:e1e-nx-b` valid_from=`2026-01-12`; both valid_to=NULL); declared_loss=0.

Decisions: bind as above; effective_from equals each assertion valid_from; no supersession; no typed precedence.

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

Do **not** select a winner. Not “two conflicting approvals” — outcomes **disagree** (approved vs refused).
