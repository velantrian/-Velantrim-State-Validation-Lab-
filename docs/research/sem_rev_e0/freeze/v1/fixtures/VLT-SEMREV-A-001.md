## 11. Fixture A — `VLT-SEMREV-A-001`

`QUERY_AS_OF: 2026-02-01T00:00:00Z`  
`SCOPE: scope:project-delta`

Entity: `ent:project:delta`.

A:
- Path-A;
- `semantic_force=proposal`;
- asserted 2026-01-01;
- candidate_only.

Revision `rev:A-reject`:
- retracts A;
- reason `R1_CONSTRAINT_FAILURE`;
- effective 2026-01-02.

B:
- Path-B;
- `semantic_force=decision`;
- reason `R2_MEETS_K1`;
- authority project owner;
- valid from 2026-01-03.

C:
- Path-C;
- `semantic_force=decision`;
- reason `R3_NEW_REQUIREMENT_K2`;
- authority project owner;
- valid from 2026-01-04.

Revision `rev:B-to-C` supersedes B with C effective 2026-01-04.

Reopen condition:

`Y_K2_REMOVED_AND_OWNER_REAPPROVES_B`

Path-B may be reconsidered only if K2 is removed **and** project owner explicitly re-approves B.

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

### Fixture A FORBIDDEN atoms

```text
A.force=decision
A.status=current
B.status=current
current_path=Path-A
current_path=Path-B
C reason=R1 or R2
B may reopen unconditionally
scope widening
invented reason/approval/evidence
```

