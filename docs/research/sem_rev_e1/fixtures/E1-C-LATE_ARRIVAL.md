# E1-C — Late-Arriving Record (discriminating)

**Family:** E1-C  
**Hypothesis:** H6  
**PHYSICAL_CORE:** `E1-C-01`  
**DUAL_CHECK:** `E1-C-02`  
**Category:** NEG  

Same-force approved decisions; late `recorded_at` must not determine currentness.  
Revision/currentness on **assertions**; qualification via bound **decisions**.

---

## Bindings

| Assertion | Bound decision |
|-----------|----------------|
| `as:e1c-v1` | `dec:e1c-v1` |
| `as:e1c-v2` | `dec:e1c-v2` |

### Query

- entity `ent:service:mira`
- `query_scope=scope:production-us`
- `query_as_of=2026-02-20T00:00:00Z`
- query: `Is VX-C approved for Mira in production-us?`

### Assertions

| ID | force | scope | asserted_at | recorded_at | valid_from | valid_to | uncertainty | declared_loss |
|----|-------|-------|-------------|-------------|------------|----------|-------------|---------------|
| `as:e1c-v1` | decision | scope:production-us | 2026-01-10T00:00:00Z | **2026-02-18T00:00:00Z** (late) | 2026-01-10T00:00:00Z | NULL | NULL | 0 |
| `as:e1c-v2` | decision | scope:production-us | 2026-02-01T00:00:00Z | **2026-02-02T00:00:00Z** | 2026-02-01T00:00:00Z | NULL | NULL | 0 |

### Authority decisions

| decision_id | assertion_id | authority | outcome | semantic_force | scope | reason | effective_from | recorded_at |
|-------------|--------------|-----------|---------|----------------|-------|--------|----------------|-------------|
| `dec:e1c-v1` | `as:e1c-v1` | principal:release-board | approved | authority_decision | scope:production-us | `R_E1_C_V1` | 2026-01-10T00:00:00Z | 2026-02-18T00:00:00Z |
| `dec:e1c-v2` | `as:e1c-v2` | principal:release-board | approved | authority_decision | scope:production-us | `R_E1_C_V2` | 2026-02-01T00:00:00Z | 2026-02-02T00:00:00Z |

### Revision (assertions only)

| revision_id | type | target_assertion_id | replacement_assertion_id | reason | effective_from | recorded_at |
|-------------|------|---------------------|--------------------------|--------|----------------|-------------|
| `rev:e1c-v1-to-v2` | supersedes | **`as:e1c-v1`** | **`as:e1c-v2`** | `R_E1_C_SUPERSEDE_V1` | 2026-02-01T00:00:00Z | 2026-02-01T01:00:00Z |

### Expected

```text
as:e1c-v1.status=superseded
as:e1c-v2.status=current
as:e1c-v1.recorded_at later MUST NOT outrank as:e1c-v2
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1c-v2
qualified_decision_ids does_not_contain dec:e1c-v1
dec:e1c-v2.outcome=approved
```

FORBIDDEN: currentness assigned as `dec:e1c-v*.status=…`; revision targeting `dec:*`; late `recorded_at` wins.
