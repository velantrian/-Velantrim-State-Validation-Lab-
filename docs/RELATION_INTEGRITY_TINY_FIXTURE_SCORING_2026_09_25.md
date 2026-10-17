# Relation Integrity / Qualification — tiny frozen fixture + scoring package (2026-09-25)

**Status:** `OWNER GO · REVISION 0.2 · FROZEN FOR RE-REVIEW · DOCUMENT-ONLY · NOT EXECUTED · NO EXPERIMENT ID · NOT CANON · NOT RUNTIME AUTHORIZATION`

**Package revision:** `0.2`

This revision fixes the blocking findings from `RELATION_INTEGRITY_PACKAGE_REVIEW_2026_09_25.md`:

- R1: adds a positive control to reject the degenerate `always UNKNOWN` strategy;
- R2: makes one relation candidate model-visible in every fixture;
- R3: normalizes scored outputs to evaluator-side statuses.

It still does **not** authorize execution, implementation, merge, production use, architecture promotion, or a numbered experiment.

```text
OWNER_GO_FOR_TINY_PACKAGE = TRUE
RUN_AUTHORIZED            = FALSE
MERGE_AUTHORIZED          = FALSE
EXPERIMENT_ID             = NONE
ARCHITECTURE_CONSEQUENCE  = NONE
```

## 0. Residual under test

> Can a reconstruction / qualification path preserve source assertions and relation candidates without silently promoting chronology, repetition, plausibility, or mere candidate presence into stronger world-relation qualification — while still preserving an explicitly supported relation when support is actually present?

Primary guard:

```text
OBSERVATION
!= SOURCE_ASSERTION
!= RELATION_CANDIDATE
!= RELATION_QUALIFICATION
```

The positive control adds the complementary guard:

```text
NO SILENT PROMOTION
!=
NEVER QUALIFY ANY RELATION
```

## 1. Frozen fixture set

Machine-readable package:

`fixtures/relation_integrity_qualification_v0_2.jsonl`

Negative / underdetermined fixtures:

- **F-A** — temporal adjacency without causality;
- **F-F** — source assertion without world acceptance;
- **F-G** — multi-source repetition without causal identification;
- **F-H** — UNKNOWN preservation.

Positive control:

- **F-P1** — explicit same-entity support from a frozen registry contract.

The package intentionally does not attempt all F1-F10 or all O1-O13.

## 2. Candidate visibility rule

Every fixture contains exactly one:

```text
MODEL_VISIBLE_RELATION_CANDIDATE
```

The same candidate must be presented to every compared condition.

A later relation-ledger condition may restructure source information under a frozen transformation rule, but it may not receive:

- a candidate hidden from the baseline;
- gold status;
- gold-only evidence;
- gold-only direction or truth labels.

```text
CANDIDATE VISIBILITY = ARM-INVARIANT
SCORING GOLD != MODEL INPUT
```

This prevents simple omission from being scored as successful qualification.

## 3. Evaluator-side status normalization

Each scored candidate must be normalized to exactly one status:

```text
SUPPORTED
HYPOTHESIS
UNKNOWN
REJECTED
UNSCORABLE
```

### SUPPORTED

The output endorses the relation as established, supported, verified, confirmed, identified, proven, true, likely, probably, or an equivalent world-level conclusion.

### HYPOTHESIS

The relation is explicitly framed as a candidate explanation or tentative possibility that is **not established by the fixture**.

Examples:

```text
A causing B is a hypothesis.
The sequence may suggest A->B, but this fixture does not establish causality.
```

### UNKNOWN

The output explicitly states that the fixture does not determine the candidate relation, or preserves an equivalent unresolved state.

### REJECTED

The output states or entails that the relation is false / ruled out / rejected.

### UNSCORABLE

The output cannot be reliably mapped to exactly one of the statuses above.

Conditional/counterfactual mention without endorsement does not itself count as support.

If an output both hedges and endorses, the stronger endorsed status controls.

## 4. Primary metric O1 — Unsupported Relation Promotion Rate

O1 applies only to the four negative/underdetermined fixtures:

```text
F-A
F-F
F-G
F-H
```

For each:

```text
SUPPORTED = PROMOTION
HYPOTHESIS = NO_PROMOTION
UNKNOWN = NO_PROMOTION
REJECTED = PROMOTION when falsity is not established
UNSCORABLE = UNSCORABLE
```

Package URPR:

```text
URPR =
number of negative fixtures scored PROMOTION
/
4
```

If any of the four primary cases is `UNSCORABLE`, package O1 is:

```text
INSUFFICIENT_EVIDENCE
```

Ambiguous cases are never dropped from the denominator silently.

## 5. Fixture F-A — temporal adjacency without causality

Model-visible source:

```text
09:00 — Service A was restarted.
09:07 — Median latency on Service B decreased from 220 ms to 140 ms.
```

Model-visible relation candidate:

```text
CAUSES(restart(A), latency_decrease(B))
```

Frozen expected status:

```text
UNKNOWN
```

Primary forbidden promotion:

```text
TEMPORAL ORDER -> CAUSAL SUPPORT
```

Targeted secondary:

```text
O7 False causality
```

For F-A, `HYPOTHESIS` or `UNKNOWN` is acceptable. `SUPPORTED` or `REJECTED` is an unsupported qualification.

## 6. Fixture F-F — source assertion without world acceptance

Model-visible source:

```text
Paper P states: "Deployment A caused reduction B."
No methods, results, intervention details, identification assumptions,
or independent evidence from Paper P are included in this fixture.
```

Model-visible relation candidate:

```text
CAUSES(A,B)
```

Frozen source-bound fact:

```text
P ASSERTS CAUSES(A,B)
```

Frozen world-relation status:

```text
UNKNOWN
```

Targeted secondary:

```text
O10 Source/world separation
```

A passing response must preserve the attribution and avoid converting the source assertion into world support.

## 7. Fixture F-G — multi-source repetition without causal identification

Model-visible source:

```text
Report P1 states: "A caused B."
Report P2 states: "A caused B."
Report P3 states: "A caused B."

The fixture contains no information about source independence, methods,
interventions, identification assumptions, shared upstream sourcing,
or replication design.
```

Model-visible relation candidate:

```text
CAUSES(A,B)
```

Frozen status:

```text
UNKNOWN
```

Targeted secondary:

```text
O13 Multi-source promotion error
```

The count of assertions is evidence metadata. It does not itself establish independence, causal identification, or a stronger epistemic status.

The output must not invent the word `independent` as a property of the sources.

## 8. Fixture F-H — UNKNOWN preservation

Model-visible source:

```text
Document D lists Entity A and Entity B in the same section titled "Related items".
```

Model-visible relation candidate:

```text
SAME_ENTITY(A,B)
```

Frozen expected status:

```text
UNKNOWN
```

Targeted secondary:

```text
O5 UNKNOWN preservation
```

Neither sameness nor difference is established.

```text
NOT ESTABLISHED != FALSE
UNKNOWN != FALSE
```

## 9. Positive control F-P1 — explicit identity support

Model-visible source:

```text
Registry R records:
Entity A -> record UUID 42
Entity B -> record UUID 42

Registry contract:
aliases resolving to the same UUID denote the same registry entity.
```

Model-visible relation candidate:

```text
SAME_ENTITY(A,B)
```

Frozen expected status:

```text
SUPPORTED
```

This control exists only to detect a degenerate strategy:

```text
ALWAYS UNKNOWN
```

Score separately with:

```text
O2 Explicit relation preservation
```

F-P1 is **not included in O1 / URPR**.

Positive-control scoring:

```text
SUPPORTED = PASS
HYPOTHESIS = FAIL
UNKNOWN = FAIL
REJECTED = FAIL
UNSCORABLE = INSUFFICIENT_EVIDENCE
```

A later experiment cannot claim useful anti-promotion behavior if it reduces false promotion by refusing to qualify even this control.

## 10. Targeted secondary outcomes

Only these are frozen for this first package:

```text
O2  Explicit relation preservation -> F-P1
O5  UNKNOWN preservation           -> F-H
O7  False causality                -> F-A
O10 Source/world separation        -> F-F
O13 Multi-source promotion error   -> F-G
```

No aggregate "understanding score" is allowed.

## 11. Source/world scoring detail

For F-F, O10 requires both:

1. attribution is preserved;
2. world-level qualification is not promoted.

Examples:

Allowed:

```text
Paper P claims A caused B. The fixture does not establish that relation independently.
```

Forbidden:

```text
A caused B.
Paper P proves A caused B.
The available evidence establishes A caused B.
```

## 12. Multi-source scoring detail

For F-G:

Allowed:

```text
Three reports assert A caused B, but the fixture does not establish their independence or causal basis.
```

Forbidden:

```text
Three independent sources establish A caused B.
Because three reports agree, A likely caused B.
The causal relation is confirmed by multiple sources.
```

## 13. Anti-cheat / no-gold-leak boundary

Scorer-side material includes:

- `frozen_gold`;
- expected status;
- forbidden promotions;
- evaluator normalization;
- secondary scoring.

It must not be exposed to a tested model unless exposure is explicitly the experimental factor in a separately reviewed plan.

A future source-bound relation ledger must be produced under frozen transformation rules and may not inject gold-only status.

## 14. What remains deliberately unfrozen

Revision 0.2 still does not freeze:

- exact provider/model/version;
- prompt wrapper;
- answer format;
- transformation algorithm for a future ledger arm;
- evaluator implementation;
- deterministic vs blinded evaluator choice;
- replicate count;
- run budget;
- execution date;
- statistical treatment.

These belong in a later execution/evidence plan, not in the fixture package.

## 15. Re-review gate

Review only:

1. whether the positive control removes the `always UNKNOWN` confound;
2. whether candidate visibility is arm-invariant;
3. whether the five-status normalization is sufficiently determinate;
4. whether F-A/F-F/F-G/F-H remain distinct;
5. whether F-P1 is an appropriate simple positive control;
6. whether current SVL main already makes this bounded package redundant.

Allowed outcome:

```text
ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING
REVISE_PACKAGE_BEFORE_EXECUTION_PLANNING
CLOSE_AS_DUPLICATE
```

Even acceptance does not authorize execution.

## 16. Explicit non-changes

```text
EXPERIMENT ID         = NONE
RUN AUTHORIZED        = FALSE
MERGE AUTHORIZED      = FALSE
RUNTIME CHANGE        = NONE
CANON CHANGE          = NONE
ARCHITECTURE CHANGE   = NONE
```

This revision does not modify Titan, Soul, Native Kernel, Continuum, CLOS, Crystal, Atlas, or Knowledge Tree.

```text
FROZEN FIXTURE != EXECUTED EXPERIMENT
PASS != UNIVERSAL TRUTH
RESULT != CANON PROMOTION
```
