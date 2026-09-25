# Relation Integrity / Qualification — execution & evidence plan (2026-09-25)

**Status:** `DRAFT PLAN · PACKAGE 0.2 ACCEPTED · NOT EXECUTED · NO EXPERIMENT ID · RUN NOT AUTHORIZED`

This plan is the only artifact authorized by the package re-review. It does not authorize execution.

## 0. Boundaries

```text
PACKAGE REVISION        = 0.2
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

## 3. Answer contract

Each response must return exactly one JSON object:

```json
{
  "fixture_id": "F-A",
  "relation_candidate": "CAUSES(...)",
  "qualification": "SUPPORTED | HYPOTHESIS | UNKNOWN | REJECTED",
  "source_claims_preserved": ["source identifiers or explicit source-bound claims"],
  "independence_status": "PROVIDED | NOT_PROVIDED | NOT_APPLICABLE",
  "brief_basis": "max 80 words"
}
```

Rules:

- choose exactly one `qualification`;
- do not invent source independence;
- source attribution must remain source-bound;
- `brief_basis` may mention alternatives but must not silently change the selected qualification;
- malformed/non-JSON output is `UNSCORABLE`.

The tested model is **not** shown the evaluator normalization or frozen gold.

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

Applies to F-P1.

```text
SUPPORTED  -> PASS
other      -> FAIL
malformed  -> INSUFFICIENT_EVIDENCE
```

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
normalized_qualification
O1
targeted_secondary_outcome
limitations
```

Evidence must retain raw model outputs. Parsed results do not replace raw evidence.

## 11. Ledger transformation rule

The B ledger must be deterministic and source-local.

For each fixture it may:

- split explicit sentences/events;
- preserve exact source identifiers;
- copy explicit asserted relation wording;
- copy explicit temporal order;
- state that a named field is not provided.

It may not:

- infer causal support;
- infer source independence;
- infer identity;
- infer falsity;
- assign epistemic status;
- inject expected answers.

The transformation implementation, if created, must have unit tests showing that no `frozen_gold` field is serialized into B.

## 12. Stopping / invalidation conditions

Stop and mark the run `BLOCKED` or `INSUFFICIENT_EVIDENCE` if:

- model identity is not frozen before first output;
- A and B receive different candidates;
- gold leaks into B;
- prompt changes after outputs begin;
- fixture content changes during the run;
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
- exact ledger transform version;
- exact scorer version;
- evidence output location;
- exact branch/head.

Until that decision:

```text
RUN_AUTHORIZED = FALSE
EXPERIMENT_ID  = NONE
MERGE          = FALSE
```

No numbered experiment is created by this plan.
