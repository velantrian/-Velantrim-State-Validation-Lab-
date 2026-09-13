## 12. Fixture B — `VLT-SEMREV-B-001`

Query:

`Does VX-17 reduce Atlas latency in production?`

`QUERY_SCOPE: scope:production-us`  
`QUERY_AS_OF: 2026-02-01T00:00:00Z`

Entity: `ent:service:atlas`.

### Alpha source/evidence/assertion

- unblinded two-run Lab-A claim ~40% p50 reduction;
- preliminary;
- not for production approval;
- raw logs/blinding record absent;
- `semantic_force=claim`;
- `scope=lab-a`;
- `uncertainty=preliminary_unblinded_two_runs`.

Revision `rev:alpha-retract` retracts alpha effective 2026-01-14.

Reason:

`INSUFFICIENT_FOR_AUTHORIZATION`

### Beta source/evidence/assertion

- 12 Lab-A runs observed 7.8% median p50 reduction;
- Lab-A only;
- not production authorization;
- run-level data absent;
- `semantic_force=observation`;
- `scope=lab-a`;
- `uncertainty=twelve_runs_summary_only`.

### Authority decision `dec:ad-9`

- `scope=production-us`;
- `outcome=refused`;
- `semantic_force=authority_decision`;
- `authority=principal:release-board`;
- effective 2026-01-15;
- reason `ONLY_PRELIMINARY_LAB_A_EVIDENCE`.

## 13. Fixture B S3 candidate construction

Candidate membership frozen by construction.

S3 MUST return at least:

- `as:alpha-v1`;
- `as:beta-v1`.

`as:alpha-v1` MUST be present.

Rank-first for alpha allowed but not required.

Candidate order is not the primary oracle.

Purpose:

```text
force S4 to demonstrate RETRIEVED ≠ QUALIFIED
```

Experiment must not pass by simply failing to retrieve dangerous V1.

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

