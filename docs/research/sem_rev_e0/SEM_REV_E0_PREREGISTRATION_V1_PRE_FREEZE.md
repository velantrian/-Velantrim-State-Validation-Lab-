# 🧊🔬 SEM-REV-E0 — FROZEN PREREGISTRATION v1

**Status:** `PRE-FREEZE CANDIDATE · 2026-09-13`  
**Review status:** `FROZEN-READY CANDIDATE AFTER INITIAL RED-TEAM · FINAL INDEPENDENT VERIFICATION PENDING`  
**Implementation:** `NOT AUTHORIZED`

## Boundary

```text
CORE = S0–S5 ONLY
S6 COMPRESSION = NOT FROZEN
S7 LLM RECONSTRUCTION = NOT FROZEN
SQLite = FILE-BACKED TEST SUBSTRATE ONLY
NO GRAPH KERNEL · NO ARCHITECTURE PROMOTION · NO CANON PROMOTION
```

## 0. Research question

Can a minimal durable external memory preserve material semantic distinctions across:

```text
WRITE → CLOSE → NEW-PROCESS REOPEN → RETRIEVE → DETERMINISTIC QUALIFY → STRUCTURED PROJECT
```

without reviving rejected, retracted, superseded, out-of-scope, unauthorized, uncertain, or otherwise non-current information as current qualified state?

## 1. Target

**DISTINCTION PRESERVATION.**

Mandatory dimensions:

- semantic_force;
- scope;
- provenance/source;
- temporal applicability;
- currentness;
- uncertainty;
- revision lineage;
- retraction;
- supersession;
- authority;
- declared_loss;
- UNKNOWN.

## 2. Central failure mode

**SEMANTIC REVERSION:**

```text
older / weaker / rejected / non-authoritative state
→ correction / rejection / qualification
→ current state
→ persistence / retrieval / projection
→ older semantics revived as current / authoritative
```

```text
SEMANTIC SIMILARITY ≠ SEMANTIC FIDELITY
MEANING PRESERVATION ≠ DISTINCTION PRESERVATION
RETRIEVAL EXPOSURE ≠ SEMANTIC ACCEPTANCE
```

## 3. Non-targets

Not testing:

- best DB;
- Graph Kernel necessity;
- SurrealDB superiority;
- SQLite production suitability;
- human-like memory;
- full MGL/Guardian;
- sync/CRDT;
- large-scale performance;
- production authorization;
- arbitrary LLM compression.

## 4. Hypotheses

- `H0` CORE DISTINCTIONS SURVIVE.
- `H1` STORAGE REPRESENTATION FAILURE.
- `H2` RETRIEVAL FAILURE.
- `H3` QUALIFICATION FAILURE.
- `H4` PROJECTION FAILURE.
- `H5` TRANSFORMATION / RECONSTRUCTION FAILURE — RESERVED FOR LATER FIELD, not CORE.

## 5. Fixed distinctions

```text
RETRIEVED ≠ QUALIFIED
QUALIFIED ≠ TRUE
PROVENANCE ≠ TRUTH
PROPOSAL ≠ DECISION
OBSERVATION ≠ AUTHORIZATION
RECOMMENDATION ≠ PERMISSION
HYPOTHESIS ≠ FACT
SIMULATION ≠ EXECUTION
HISTORICAL ≠ CURRENT
SUPERSEDED ≠ FALSE
RETRACTED ≠ NEVER EXISTED
NOT RETRIEVED ≠ ABSENT
UNKNOWN ≠ FALSE
CAPABILITY ≠ AUTHORITY
MODEL OUTPUT ≠ CANON
```

## 6. Substrate rules

SQLite stable, file-backed only.

Mandatory:

- STRICT tables;
- explicit PK;
- NOT NULL/CHECK/UNIQUE where required;
- `foreign_keys=ON` on every connection;
- explicit transactions;
- application-issued semantic IDs;
- normalized typed qualifier columns.

Permitted:

- WAL;
- indexes;
- FTS5 candidate discovery;
- recursive CTE where required;
- JSON only for non-critical auxiliary metadata.

Forbidden:

- `:memory:`;
- hidden in-process continuity S1→S2;
- rowid as semantic identity;
- mandatory qualifier only in prose;
- free mutable `is_current`;
- LLM in S0–S5 qualification.

## 7. Executable typing rule

The following must exist as typed queryable fields/relations:

- `semantic_force`;
- `scope_id`;
- `uncertainty`;
- `asserted_at` / `observed_at` where applicable;
- `recorded_at`;
- `valid_from`;
- `valid_to`;
- revision relation;
- revision `effective_from`;
- authority identity;
- authority outcome;
- `declared_loss`.

If any qualifier required by oracle exists only in content/object_value/summary/natural-language reason and cannot be deterministically queried:

`S0 = FAIL`

## 8. Currentness rule

No freely writable `is_current` flag.

At query time `T`, assertion is temporally applicable iff:

```text
valid_from <= T
AND
(valid_to IS NULL OR T < valid_to)
```

Then revision state applies.

A predecessor is not current if an effective `retracts` / `invalidates` / `supersedes` relation applies at `T`.

A successor may be current only if its own interval applies and it has not itself been retracted/invalidated/superseded.

```text
CURRENTNESS = DERIVED PROJECTION, NOT STORED ANSWER FLAG
```

## 9. Time model

- `OBSERVED_AT` = event/evidence occurrence.
- `ASSERTED_AT` = assertion made.
- `RECORDED_AT` = durable memory stored it.
- `VALID_FROM/VALID_TO` = applicability interval.
- `EFFECTIVE_FROM` = revision or authority decision takes effect.

These must remain separately recoverable.

## 10. Core record families

```text
ENTITY
ASSERTION
SOURCE
EVIDENCE
EVIDENCE_ASSERTION_LINK
REVISION
AUTHORITY_DECISION
TRACE
QUALIFIED_PROJECTION
```

Experimental only; not architecture promotion.

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

## 16. Stages

### S0 WRITE

Commit all frozen records; typed qualifiers queryable; stable IDs; links present; no free `is_current`; positive and adversarial controls stored.

Mandatory qualifier only in prose = `HARD FAIL / S0 FAIL`.

### S1 CLOSE

- file-backed only;
- commit;
- close every DB connection;
- terminate process.

`:memory:` and hidden process state prohibited.

### S2 NEW-PROCESS REOPEN

New OS process; only database file + frozen query/rules/oracle available.

Recover all canonical records/relations required by oracle.

### S3 RETRIEVE

Recover candidate identities.

- Fixture B must include alpha + beta;
- Fixture C must include `dec:pos-1`.

### S4 QUALIFY

Deterministic:

- no LLM;
- no summary interpretation;
- no source-text parsing for mandatory qualifiers.

Outputs:

- accepted/excluded IDs;
- reason codes;
- currentness derivation;
- authority status;
- uncertainty/declared-loss metadata.

### S5 PROJECT

Deterministic task-facing structured projection evaluated only via atoms; no gold essay.

## 17. Oracle format

```text
REQUIRED ATOMS + FORBIDDEN ATOMS only
```

No stylistic matching.  
No interpretive scoring for CORE.

## 18. Hard fails

```text
HF-01 proposal→decision
HF-02 historical→current
HF-03 retracted→active
HF-04 superseded→active
HF-05 scope widened contrary to frozen scope atom
HF-06 observation→authorization
HF-07 recommendation→permission
HF-08 UNKNOWN→fabricated value/decision
HF-09 evidence linked to wrong assertion
HF-10 revision reason linked to wrong transition
HF-11 authority refusal omitted where oracle requires it
HF-12 declared loss omitted where required
HF-13 time axes conflated
HF-14 semantic force differs from frozen force atom
HF-15 unsupported approval/evidence/reason in projection
HF-16 positive control returns EMPTY/abstention
HF-17 Fixture B dangerous V1 absent from constructed candidate set
HF-18 currentness derived from mutable is_current instead of frozen rule
```

## 19. CORE result label

Allowed:

```text
SEM_REV_E0_CORE_PASS
SEM_REV_E0_CORE_FAIL
SEM_REV_E0_CORE_INCOMPLETE
```

`CORE_PASS` requires:

- S0–S5 PASS;
- `HARD_FAIL_COUNT=0`;
- positive control PASS.

## 20. Claim boundary

If CORE_PASS, strongest allowed claim:

> Under the frozen fixtures and deterministic S0–S5 rules, the tested minimal durable memory preserved the preregistered semantic distinctions across persistence, fresh-process reopen, candidate retrieval, deterministic qualification, and structured projection, with no frozen hard failures.

Not supported by CORE_PASS:

- semantic reversion solved generally;
- compression safe;
- LLM reconstruction safe;
- SQLite sufficient for all Velantrim;
- graph unnecessary forever;
- production readiness;
- full MGL/Crystal/Native Kernel/Continuum implemented.

Failure must be stage-local. Do not attribute a higher-layer failure to SQLite without evidence.

## 21. Diagnostics

Record separately:

```text
STORAGE_LOSS
REOPEN_LOSS
RETRIEVAL_MISS
RETRIEVAL_FALSE_ID
QUALIFICATION_ERROR
CURRENTNESS_ERROR
SCOPE_ERROR
SEMANTIC_FORCE_ERROR
AUTHORITY_ERROR
REVISION_ERROR
DECLARED_LOSS_ERROR
UNKNOWN_INFLATION
PROJECTION_ERROR
POSITIVE_CONTROL_ERROR
```

No combined quality score.

## 22. Stop conditions

STOP if:

- fixture/oracle/atoms change after execution starts;
- qualifier moved into prose;
- LLM enters S0–S5;
- hidden state crosses S1→S2;
- `:memory:` replaces file;
- free `is_current` added;
- candidate set altered after seeing qualification;
- positive control removed;
- result claim broadened post hoc.

## 23. S6 Compression Field

`NOT_FROZEN · NOT_AUTHORIZED_FOR_RUN`

Future field must freeze:

- compression method;
- input packet;
- output contract;
- required/forbidden atoms;
- model/rules if any;
- parameters;
- repeat policy;
- oracle;
- failure taxonomy.

`CORE_PASS` does not imply `S6 PASS`.

## 24. S7 Reader / LLM Field

`NOT_FROZEN · NOT_AUTHORIZED_FOR_RUN`

Must separately freeze:

- provider;
- model/version if exposed;
- temperature;
- top_p;
- max_tokens;
- thinking mode;
- tool/web/memory settings;
- fresh-session requirement;
- input packet hash;
- call count;
- retry policy;
- abort conditions;
- response-model check;
- oracle atoms.

`CORE_PASS` does not imply `READER_PASS`.

## 25. Tables ≠ Canon

Mandatory statement:

> The database schema, table decomposition, field placement and SQLite implementation used by SEM-REV-E0 are experimental substrate choices for this bounded test only. They do not define or instantiate canonical architecture of Native Kernel, Crystal, Continuum, Titan, MGL, Guardian, Orientation, CLOS, or any other Velantrim organ.

## 26. Graph Kernel status

```text
GK-P0=DEFERRED
SurrealDB=DEFERRED CANDIDATE
Kuzu=OUT OF CURRENT SCOPE
FalkorDBLite=OUT OF CURRENT SCOPE
```

SEM-REV results must not automatically reopen GK-P0.

## 27. Freeze package contents after SAFE_TO_FREEZE

Freeze exactly:

- this preregistration;
- Fixture A/B/C bytes;
- candidate-set construction;
- currentness rule;
- qualification rule;
- required atoms;
- forbidden atoms;
- hard-fail definitions;
- result labels;
- stop conditions;
- SQLite version/config declaration.

Compute SHA256 for each and package manifest.

No artifact changes after first experimental write.

## 28. Execution order after owner authorization

```text
Phase 0  save exact artifacts
Phase 1  SHA256
Phase 2  verify freeze package
Phase 3  implement minimal SQLite substrate
Phase 4  S0
Phase 5  terminate process
Phase 6  fresh-process S2
Phase 7  S3
Phase 8  S4
Phase 9  S5
Phase 10 score atoms
Phase 11 classify CORE_PASS/FAIL/INCOMPLETE
Phase 12 post-run diagnostic
```

No S6/S7 without separate authorization and field freeze.

## 29. Final pre-freeze review status

Initial Grok review:

`SAFE_WITH_MINOR_FIXES`

Fixes 1–10 incorporated here.

Latest Grok verification did **not** inspect this artifact:

```text
SPEC_LOCATED=NO
VERIFICATION_BLOCKED_SPEC_NOT_AVAILABLE
```

Therefore final `SAFE_TO_FREEZE` is still **PENDING**.

## Next action

Give this exact artifact to Grok with bounded fix-verification prompt.

If and only if Grok returns `SAFE_TO_FREEZE` — or residual blockers are minimally corrected and reverified — create the byte-stable freeze package + SHA256.

**END**
