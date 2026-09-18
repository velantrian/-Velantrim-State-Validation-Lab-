# E1-I — Retraction + Late Similar Evidence

**Family:** E1-I  
**Hypotheses:** H8 (narrowed), H1  
**PHYSICAL_CORE:** E1-I-01  
**Category:** NEG

---

## E1-I-01

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:lab-us`
- `query_as_of`: `2026-02-20T00:00:00Z`

| ID | Force | Status intent | scope | asserted/observed | recorded | declared_loss |
|----|-------|---------------|-------|-------------------|----------|---------------|
| `as:e1i-old` | claim | **retracted** | lab-us | 2026-01-05 | 2026-01-05 | 0 |
| `rev:e1i-retract` | `retracts` | retracts old | — | — | 2026-01-08 | — |
| `as:e1i-new` | observation | active distinct | lab-us | observed 2026-02-10 | recorded 2026-02-15 | 0 |

`rev:e1i-retract`: effective_from=`2026-01-08T00:00:00Z`; reason=`R_E1_I_INSUFFICIENT`.

### REQUIRED

```text
as:e1i-old.status=retracted
as:e1i-old must_not_revive_as_same_assertion_identity
as:e1i-new.recoverable_by_identity=true
as:e1i-new remains a distinct identity
as:e1i-new != as:e1i-old
```

The system must **not** pass merely by dropping `as:e1i-new`.

### FORBIDDEN

```text
as:e1i-old revived as same assertion identity
similarity-based silent un-retraction
as:e1i-new omitted / not recoverable
identity_collapse as:e1i-new → as:e1i-old
```
