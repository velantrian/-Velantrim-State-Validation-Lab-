## 14. Fixture B S4 qualification

Reads **only typed columns/relations** for mandatory semantics.

S3 candidate membership ≠ S4 qualification-dependency availability.

S4 MUST obtain `dec:ad-9` and every typed revision / retraction / supersession / scope / temporal record required to qualify `as:alpha-v1` and `as:beta-v1` by deterministic lookup in the reopened persisted store. Those records need not be S3 candidates. Missing from S3 MUST NOT mean they do not exist.

If a required typed qualification dependency cannot be recovered:
- `S4 = FAIL`;
- `SEM_REV_E0_CORE_PASS` is prohibited.

A missing required dependency MUST NOT:
- become a normal candidate exclusion;
- be interpreted as evidence of absence;
- silently produce `NO_QUALIFIED_RESULT`.

Dependency loss is stage failure, not valid qualification rejection.

No graph traversal, Graphiti, FalkorDBLite, or new retrieval engine is required or implied.

Must not infer force/scope/authority/retraction/currentness from source prose.

Request:

- `scope=production-us`;
- `as_of=2026-02-01`;
- required authority outcome = approved;
- allowed assertion forces = observation, authority_decision;
- `reject_retracted=true`.

Evaluates:

- scope;
- force;
- revision status;
- temporal applicability;
- authority outcome;
- uncertainty metadata;
- declared_loss presence.

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

### Fixture B FORBIDDEN atoms

```text
production_effect=40%
production_effect=7.8%
production_authorization=approved
alpha current_qualified
beta production_qualified
AD-9 approved
Lab-A silently widened
retraction omitted
authority refusal omitted
declared_loss silently removed
```

### S4 QUALIFY

Deterministic:

- no LLM;
- no summary interpretation;
- no source-text parsing for mandatory qualifiers.

S3 returns candidate identities according to the frozen fixture-specific candidate construction.

For Fixture B, S3 assertion candidates are distinct from S4 qualification-dependency records. Fixture C retains `dec:pos-1` as its required S3 candidate.

S4 MUST resolve every typed qualification dependency required to evaluate those candidates (revision, retraction, supersession, authority decision, scope, temporal applicability) by deterministic lookup in the reopened persisted store.

`NOT RETRIEVED ≠ ABSENT` is an S4 execution rule. Absence from the S3 candidate set MUST NOT be treated as nonexistence of a dependency. A revision, retraction, supersession, or authority-decision record need not be a ranked S3 candidate in order to bind qualification.

If a required typed qualification dependency cannot be recovered from the store:
- `S4 = FAIL`;
- `SEM_REV_E0_CORE_PASS` is prohibited.

A missing required dependency MUST NOT:
- become a normal candidate exclusion;
- be interpreted as evidence of absence;
- silently produce `NO_QUALIFIED_RESULT`.

Dependency loss is stage failure, not valid qualification rejection.

Outputs:

- accepted/excluded IDs;
- reason codes;
- currentness derivation;
- authority status;
- uncertainty/declared-loss metadata.

