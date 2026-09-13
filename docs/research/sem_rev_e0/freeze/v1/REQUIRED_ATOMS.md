### Fixture A REQUIRED atoms

```text
A.force=proposal
A.status=retracted
A.rejection_reason=R1_CONSTRAINT_FAILURE
B.force=decision
B.status=superseded
B.decision_reason=R2_MEETS_K1
C.force=decision
C.status=current
C.decision_reason=R3_NEW_REQUIREMENT_K2
current_path=Path-C
reopen_B_requires=Y_K2_REMOVED_AND_OWNER_REAPPROVES_B
scope=scope:project-delta
absent properties remain UNKNOWN
```

### Fixture B REQUIRED qualification atoms

```text
qualified_assertion_ids=[]
qualified_decision_ids=[]
status=NO_QUALIFIED_RESULT
excluded alpha contains scope_mismatch, retracted, force_not_allowed
excluded beta contains scope_mismatch, no_approved_authority_decision
excluded AD-9 contains authority_outcome_refused
```

Must preserve:

- `scope_id`;
- `semantic_force`;
- `uncertainty`;
- `declared_loss`;
- retraction;
- authority_decision;
- `observed_at`;
- `recorded_at`;
- `valid_from`;
- `effective_from`.

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

