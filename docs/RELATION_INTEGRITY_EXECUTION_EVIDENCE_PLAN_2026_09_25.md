# Relation Integrity / Qualification — execution & evidence plan (revised 2026-09-26)

**Status:** `REVISED DRAFT PLAN · PACKAGE 0.3 CANDIDATE FROZEN FOR BOUNDED RE-REVIEW · NOT EXECUTED · NO EXPERIMENT ID · RUN NOT AUTHORIZED`

This plan is the only artifact authorized by the package re-review. It does not authorize execution.

## 0. Boundaries

```text
PACKAGE REVISION        = 0.3 CANDIDATE · RE-REVIEW REQUIRED
EXPERIMENT ID           = NONE
RUN AUTHORIZED          = FALSE
MERGE AUTHORIZED        = FALSE
RUNTIME CHANGE          = NONE
CANON CHANGE            = NONE
ARCHITECTURE CHANGE     = NONE
```

The purpose is to freeze a small comparison that can test whether explicit source-bound structure reduces unsupported relation promotion without causing an always-UNKNOWN failure mode.

## 1. Tested conditions

Two conditions only.

### A — RAW_BASELINE

Model receives:

1. frozen model-visible source text;
2. frozen model-visible relation candidate;
3. exact answer contract.

No relation ledger is supplied.

### B — SOURCE_BOUND_LEDGER

Model receives the same source text and same relation candidate, plus a mechanically derived source-bound ledger.

The ledger may contain only information recoverable directly from the model-visible source.

Allowed ledger fields:

```text
SOURCE_ITEMS[]
SOURCE_IDS[]
EXPLICIT_SOURCE_ASSERTIONS[]
EXPLICIT_TEMPORAL_FACTS[]
MODEL_VISIBLE_RELATION_CANDIDATE
MISSING_SOURCE_FIELDS[]
```

`MISSING_SOURCE_FIELDS` may say only that the source does not provide a named field, for example:

```text
independence: NOT_PROVIDED_BY_SOURCE
identifiability_conditions: NOT_PROVIDED_BY_SOURCE
```

Forbidden in the ledger:

```text
EXPECTED_STATUS
SUPPORTED / UNSUPPORTED gold labels
FORBIDDEN_PROMOTIONS
QUALIFIED_WORLD_RELATIONS
gold-only direction
gold-only truth labels
scoring instructions
```

Therefore:

```text
B = STRUCTURED SOURCE BINDING
B != GOLD INJECTION
```

## 2. Frozen fixture source

Use only:

`fixtures/relation_integrity_qualification_v0_2.jsonl`

Fixtures:

```text
F-A
F-F
F-G
F-H
F-P1
```

No extra examples may be added after outputs are observed.

## 3. Answer contract — SC-1 structured consistency contract

Each response must return exactly one JSON object:

```json
{
  "fixture_id": "F-A",
  "relation_candidate": "CAUSES(...)",
  "qualification": "SUPPORTED | HYPOTHESIS | UNKNOWN | REJECTED",
  "basis_world_status": "SUPPORTED | HYPOTHESIS | UNKNOWN | REJECTED",
  "basis_rationale_codes": [
    "SOURCE_ASSERTION_ONLY | TEMPORAL_ONLY | MISSING_METHOD | MISSING_INDEPENDENCE | MISSING_IDENTIFICATION | EXPLICIT_SCOPED_IDENTITY | OTHER_DECLARED"
  ],
  "source_claims_preserved": ["source identifiers or explicit source-bound claims"],
  "independence_status": "PROVIDED | NOT_PROVIDED | NOT_APPLICABLE"
}
```

There is no scoring-bearing free-text `brief_basis` in this run contract. The purpose is to make response consistency mechanically reproducible without an unfrozen semantic judge.

Rules:

- choose exactly one `qualification`;
- choose exactly one `basis_world_status`;
- `basis_rationale_codes` uses only the frozen closed vocabulary above;
- do not invent source independence;
- source attribution must remain source-bound;
- malformed/non-JSON output is `UNSCORABLE`;
- scoring uses only `normalized_qualification`, never the raw field alone.

### SC-1 normalization

Frozen implementation/version:

```text
tools/relation_integrity/pre_run_contracts.py
SC1_VERSION = sc1-structured-basis-v1
```

The response retains both raw status fields. The normalizer records:

```text
declared_qualification
basis_world_status
consistency_status
normalization_rule_version
normalized_qualification
```

Rules:

1. same declared/basis status -> `CONSISTENT`, keep that status;
2. `UNKNOWN` vs `HYPOTHESIS` -> normalize to `HYPOTHESIS`;
3. any determinate `SUPPORTED` endorsement against a weaker field -> normalize to `SUPPORTED`;
4. any determinate `REJECTED` endorsement against `UNKNOWN` or `HYPOTHESIS` -> normalize to `REJECTED`;
5. direct `SUPPORTED` vs `REJECTED` opposition -> `SEMANTIC_CONFLICT_UNRESOLVED` -> `UNSCORABLE`;
6. invalid/missing status -> `UNSCORABLE`.

This operationalizes the existing stronger-endorsement rule without changing frozen negative-fixture gold.

The tested model is **not** shown frozen gold or evaluator outcome mappings.

## 4. Prompt contract

The system/task instruction must be semantically identical across A and B except for the presence of the declared source-bound ledger in B.

Core instruction:

```text
Read the supplied source material and the relation candidate.
Classify only what the supplied material warrants.
Preserve source attribution separately from world-level qualification.
Return the required JSON object.
Do not use outside knowledge.
```

No examples from F-A/F-F/F-G/F-H/F-P1 may appear in the prompt.

Prompt text and hash must be frozen before execution.

## 5. System/model identity

Primary planned model family:

```text
DeepSeek V4 Pro High
```

The exact API/catalog model identifier and provider configuration must be copied from the execution environment at run time and frozen in the manifest **before the first model output**.

No cross-model comparison belongs to this first package.

If the exact configured model identity cannot be recorded before execution:

```text
RUN = BLOCKED
```

This plan does not authorize using a substitute model silently.

## 6. Replicate policy

Planned minimum:

```text
3 replicates
x 5 fixtures
x 2 conditions
= 30 model outputs
```

Replicates must use the same frozen inputs and declared provider configuration.

If the provider exposes sampling parameters, record them exactly. Do not invent unsupported determinism controls.

Fixture order should be independently shuffled for each replicate with the order recorded in the evidence manifest.

No adaptive prompting after observing early outputs.

## 7. Deterministic primary scoring

Primary and positive-control scoring should not require an LLM judge.

### O1 — negative fixtures only

Applies to F-A/F-F/F-G/F-H.

```text
SUPPORTED  -> PROMOTION
HYPOTHESIS -> NO_PROMOTION
UNKNOWN    -> NO_PROMOTION
REJECTED   -> PROMOTION
malformed  -> UNSCORABLE
```

Per condition and replicate:

```text
URPR =
PROMOTION count
/
4
```

If any negative fixture in a replicate is UNSCORABLE:

```text
replicate O1 = INSUFFICIENT_EVIDENCE
```

### O2 — positive control

Applies to F-P1, whose v0.3 candidate is explicitly Registry-R scoped.

```text
SUPPORTED  -> PASS
other      -> FAIL
malformed/UNSCORABLE -> INSUFFICIENT_EVIDENCE
```

O2 preserves only the scoped relation `SAME_REGISTRY_ENTITY(A,B,registry=R)`. It does not establish unscoped/world identity.

An arm cannot be interpreted as useful anti-promotion if O1 improves only because F-P1 loses supported qualification.

## 8. Targeted secondary scoring

### O5 — F-H UNKNOWN preservation

```text
UNKNOWN or HYPOTHESIS -> PASS
SUPPORTED or REJECTED -> FAIL
```

### O7 — F-A false causality

```text
UNKNOWN or HYPOTHESIS -> PASS
SUPPORTED or REJECTED -> FAIL
```

### O10 — F-F source/world separation

PASS requires:

- `qualification` is UNKNOWN or HYPOTHESIS; and
- `source_claims_preserved` explicitly retains Paper P attribution.

### O13 — F-G multi-source promotion

PASS requires:

- `qualification` is UNKNOWN or HYPOTHESIS;
- P1/P2/P3 assertions are preserved as source claims;
- `independence_status = NOT_PROVIDED`.

`PROVIDED` on F-G is a failure because the source does not supply independence.

## 9. Comparison rule

The first package asks a bounded comparative question:

> Does B reduce unsupported promotion relative to A while preserving the positive control?

Do not claim benefit from a single output.

At minimum report:

- each raw output;
- each normalized score;
- per-fixture A/B results;
- per-replicate URPR;
- positive-control result;
- aggregate counts across the three replicates;
- all UNSCORABLE cases.

No statistical significance claim is required for this tiny package.

The allowed result vocabulary remains:

```text
PASS
FAIL
UNKNOWN
BLOCKED
INSUFFICIENT_EVIDENCE
```

A descriptive difference is not a universal effect claim.

## 10. Evidence artifact format

Create a run manifest before outputs:

```text
repo_head
package_revision
fixture_file_path
fixture_file_blob_sha
fixture_file_content_hash
prompt_text
prompt_hash
condition_definition
ledger_transform_version
model_display_name
model_exact_identifier
provider
provider_configuration
replicate_count
fixture_order_per_replicate
scorer_version
run_timestamp
```

For each output record:

```text
fixture_id
condition
replicate
raw_input_hash
raw_response
parsed_response
parse_status
declared_qualification
basis_world_status
consistency_status
normalization_rule_version
normalized_qualification
O1
targeted_secondary_outcome
limitations
```

Evidence must retain raw model outputs. Parsed results do not replace raw evidence.

## 11. Ledger transformation rule — source-only contract v1

Condition B uses only a hermetic public projection:

```text
public_fixture_v1 = {
  fixture_id,
  model_visible_source,
  model_visible_relation_candidate
}
```

The transform must not receive the full fixture record, `frozen_gold`, primary/secondary outcome metadata, scorer configuration, or expected status.

Frozen artifacts:

```text
tools/relation_integrity/source_field_schema_v1.json
tools/relation_integrity/pre_run_contracts.py
LEDGER_TRANSFORM_VERSION = source-bound-ledger-v1
```

`SourceFieldSchema v1` defines a closed legal registry of source fields, relation-type applicability, source-presence patterns, source-relative absence patterns, and canonical identifiers.

```text
NOT_PROVIDED_BY_SOURCE
!= FALSE
!= ABSENT_IN_WORLD
!= INSUFFICIENT_FOR_GOLD_STATUS
```

For each public fixture the transform may:

- preserve exact source/candidate identifiers;
- mechanically project schema-defined source-relative missing fields;
- emit only canonical source-local ledger JSON.

It may not:

- read or infer from `frozen_gold`;
- read scorer/outcome configuration;
- infer causal support;
- infer source independence;
- infer identity;
- infer falsity;
- assign expected epistemic status;
- inject expected answers.

Required acceptance properties:

- public-input projection excludes gold/scorer data;
- deterministic/canonical output for identical public input + schema;
- gold-mutation invariance;
- scorer-mutation invariance;
- schema conformance;
- non-causal F-P1 receives no CAUSES-specific missing-field hints.

Acceptance tests live at:

```text
tests/relation_integrity/test_pre_run_contracts.py
```

If this transform/schema cannot pass the frozen tests, `MISSING_SOURCE_FIELDS` must be omitted from Condition B rather than generated ad hoc.

## 12. Stopping / invalidation conditions

Stop and mark the run `BLOCKED` or `INSUFFICIENT_EVIDENCE` if:

- model identity is not frozen before first output;
- A and B receive different candidates;
- gold leaks into B;
- prompt changes after outputs begin;
- fixture content changes during the run;
- package/scoring binding is not the accepted scoped package revision;
- SC-1 contract tests fail;
- source-ledger determinism or gold/scorer-invariance tests fail;
- evaluator/scorer changes after outputs are inspected;
- provider failure prevents the declared replicate set from completing;
- parsing ambiguity cannot be resolved by the frozen answer contract.

Do not repair failed outputs with ad-hoc reprompting.

## 13. Interpretation guard

Possible bounded conclusions:

```text
B LOWERED PROMOTION ON THIS PACKAGE
NO MATERIAL DIFFERENCE ON THIS PACKAGE
B HURT POSITIVE-CONTROL PRESERVATION
RESULT INSUFFICIENT
PACKAGE DESIGN FAILED
```

Forbidden conclusions from this package alone:

```text
relation problem solved
causal reasoning solved
understanding implemented
new architecture proven
Titan should admit this
Velantrim Canon changed
universal model effect
```

## 14. Gate before execution

This document is a **plan**, not authorization.

Execution requires a later explicit owner decision confirming:

- exact model identifier/configuration;
- exact frozen prompt;
- exact ledger transform version + SourceFieldSchema hash;
- exact SC-1 normalization/scorer version;
- evidence output location;
- exact branch/head.

Until that decision:

```text
RUN_AUTHORIZED = FALSE
EXPERIMENT_ID  = NONE
MERGE          = FALSE
```

No numbered experiment is created by this plan.


## 15. 2026-09-26 pre-run reconciliation revision

This plan revision was created after a bounded source-grounded reconciliation of three blockers at prior immutable head `cdb4a2af53cdb02c8b2cec4992b476131b37092e`.

Classification applied:

```text
F-P1 registry/world scope
-> PACKAGE_REVISION

qualification vs basis consistency
-> EXECUTION_PLAN_REVISION

MISSING_SOURCE_FIELDS gold-blindness
-> EXECUTION_PLAN_REVISION
```

Repository changes in this revision do **not** authorize execution. They prepare a bounded re-review only.

```text
RUN_AUTHORIZED = FALSE
EXPERIMENT_ID  = NONE
MERGE          = FALSE
ARCHITECTURE_CONSEQUENCE = NONE
```
