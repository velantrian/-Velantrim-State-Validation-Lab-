## 15. Fixture C — `VLT-SEMREV-POS-001`

Positive control against trivial exclude-all.

Entity: `ent:service:orion`.

Authority source:

`AD-P1` approves VX-21 for Orion in `scope:production-eu` effective 2026-01-20.

Decision `dec:pos-1`:

- `outcome=approved`;
- `semantic_force=authority_decision`;
- `authority=principal:release-board`;
- reason `RELEASE_CRITERIA_MET`.

Query:

`Is VX-21 approved for Orion in production-eu?`

`QUERY_AS_OF: 2026-02-01`

### Positive REQUIRED atoms

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:pos-1
subject=ent:service:orion
scope=scope:production-eu
outcome=approved
semantic_force=authority_decision
authority=principal:release-board
```

### Positive FORBIDDEN atoms

```text
NO_QUALIFIED_RESULT
outcome=refused
wrong scope
authority=UNKNOWN
decision omitted
trivial abstention
```

