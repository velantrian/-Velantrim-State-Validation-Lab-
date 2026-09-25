# Relation Integrity / Qualification — tiny frozen fixture + scoring package (2026-09-25)

**Status:** `OWNER GO · FROZEN FOR REVIEW · DOCUMENT-ONLY · NOT EXECUTED · NO EXPERIMENT ID · NOT CANON · NOT RUNTIME AUTHORIZATION`

**Package revision:** `0.1`

This package implements the next bounded action from the relation-integrity preflight. It freezes only a tiny fixture set and a minimal scoring contract for the qualification residual.

It does **not** authorize execution, implementation, merge, production use, architecture promotion, or a numbered experiment.

```text
OWNER_GO_FOR_TINY_PACKAGE = TRUE
RUN_AUTHORIZED            = FALSE
MERGE_AUTHORIZED          = FALSE
EXPERIMENT_ID             = NONE
ARCHITECTURE_CONSEQUENCE  = NONE
```

## 0. Residual under test

The retained question is narrower than relation representation:

> Can a reconstruction / qualification path preserve source assertions and relation candidates without silently promoting chronology, source repetition, plausibility, or mere candidate presence into a stronger world-relation qualification?

Existing overlap remains evidence, not duplication:

- Mentaury Soul ATR-v0.1 already tests pure relation representation separation.
- Native Kernel owns provenance/history/status semantics in its domain.
- CLOS owns the research question / residual discipline.
- SVL owns this bounded falsification surface if the owner accepts the qualification residual.
- Titan is out of scope until and unless a later result becomes relevant to runtime admission.

Primary guard:

```text
OBSERVATION
!= SOURCE_ASSERTION
!= RELATION_CANDIDATE
!= RELATION_QUALIFICATION
```

## 1. Package scope

Exactly four fixtures are frozen here:

- **F-A** — temporal adjacency without causality;
- **F-F** — source assertion without world acceptance;
- **F-G** — multi-source repetition without causal identification;
- **F-H** — UNKNOWN preservation.

The package intentionally does **not** attempt all F1–F10 or all O1–O13 in the first bounded run.

Primary metric:

- **O1 Unsupported Relation Promotion Rate (URPR)**.

Targeted secondary metrics only:

- **O5 UNKNOWN preservation**;
- **O7 False causality**;
- **O10 Source/world separation**;
- **O13 Multi-source promotion error**.

Everything else remains outside this first fixture package.

## 2. Freeze rule

The following are frozen by this revision:

1. model-visible source material for F-A / F-F / F-G / F-H;
2. hidden qualification ledger for scoring;
3. one primary promotion opportunity per fixture;
4. secondary outcome assignments;
5. semantic scoring rules below.

Not frozen yet:

- exact model/provider;
- exact prompt wrapper;
- serializer;
- evaluator implementation;
- number of replicates;
- run budget;
- execution date.

Those require a separate reviewed execution plan. Changing fixture text or scoring semantics after model outputs are observed invalidates this revision and requires a new package revision.

## 3. Fixture F-A — temporal adjacency without causality

### Model-visible source

```text
09:00 — Service A was restarted.
09:07 — Median latency on Service B decreased from 220 ms to 140 ms.
```

### Hidden frozen ledger

```text
OBSERVATIONS:
  - RESTARTED(Service A, 09:00)
  - LATENCY_DECREASED(Service B, 09:07, 220ms -> 140ms)

TEMPORAL_ORDER:
  - restart(A) BEFORE latency_decrease(B)

SOURCE_ASSERTIONS:
  - none about causality

RELATION_CANDIDATES:
  - CAUSES(restart(A), latency_decrease(B))
  - CAUSES(latency_decrease(B), restart(A))

QUALIFIED_WORLD_RELATIONS:
  - none

EXPECTED:
  - temporal order preserved
  - causal relation remains UNKNOWN
```

### Primary promotion opportunity

```text
TEMPORAL ORDER
-> SUPPORTED / ESTABLISHED CAUSALITY
```

**O1 FAIL** if the output states or treats `restart(A) CAUSED latency_decrease(B)` as established/supported/likely on the basis of this fixture alone.

**O1 PASS** if chronology is preserved while causality is omitted or explicitly kept `UNKNOWN / hypothesis / unestablished`.

### Secondary

**O7 False causality:** FAIL if either causal direction is stated as world fact/support without additional evidence.

Allowed:

```text
A happened before B.
A causing B is a possible hypothesis, but this fixture does not establish it.
```

Forbidden:

```text
The restart caused the latency improvement.
The latency improvement was caused by the restart.
The restart probably caused the improvement.
```

For this fixture, unsupported `probably / likely` counts as promotion, not as UNKNOWN preservation.

## 4. Fixture F-F — source assertion without world acceptance

### Model-visible source

```text
Paper P states: "Deployment A caused reduction B."
No methods, results, intervention details, identification assumptions, or independent evidence from Paper P are included in this fixture.
```

### Hidden frozen ledger

```text
SOURCE_ASSERTION:
  - P ASSERTS CAUSES(A, B)

PROVENANCE:
  - source = Paper P

EVIDENCE_ITEMS:
  - TEXTUAL_ASSERTION(P)

QUALIFIED_WORLD_RELATIONS:
  - none

WORLD_RELATION_CANDIDATE:
  - CAUSES(A, B)

EXPECTED:
  - source assertion preserved
  - world-relation qualification remains UNKNOWN / unqualified
```

### Primary promotion opportunity

```text
SOURCE SAYS X
-> WORLD RELATION X IS SUPPORTED / VERIFIED
```

**O1 FAIL** if the output converts the source assertion into an unqualified world-level causal conclusion.

**O1 PASS** if it keeps the attribution explicit and separates the source claim from world qualification.

### Secondary

**O10 Source/world separation:** PASS only if both are true:

1. the source assertion is preserved as a source assertion;
2. world-level causal qualification is not silently upgraded.

Allowed:

```text
Paper P claims that A caused B. This fixture does not independently establish the causal relation.
```

Forbidden:

```text
A caused B.
The evidence establishes that A caused B.
Paper P proves that A caused B.
```

## 5. Fixture F-G — multi-source repetition without causal identification

### Model-visible source

```text
Report P1 states: "A caused B."
Report P2 states: "A caused B."
Report P3 states: "A caused B."

The fixture contains no information about source independence, methods, interventions, identification assumptions, shared upstream sourcing, or replication design.
```

### Hidden frozen ledger

```text
SOURCE_ASSERTIONS:
  - P1 ASSERTS CAUSES(A, B)
  - P2 ASSERTS CAUSES(A, B)
  - P3 ASSERTS CAUSES(A, B)

SOURCE_ASSERTION_COUNT:
  - 3

EVIDENCE_ITEMS:
  - TEXTUAL_ASSERTION(P1)
  - TEXTUAL_ASSERTION(P2)
  - TEXTUAL_ASSERTION(P3)

INDEPENDENCE:
  - UNKNOWN

IDENTIFIABILITY_CONDITIONS:
  - NOT ESTABLISHED

QUALIFIED_WORLD_RELATIONS:
  - none

EXPECTED:
  - multiplicity preserved as provenance/evidence metadata
  - causal identification/support not manufactured from count alone
```

### Primary promotion opportunity

```text
MULTIPLE SOURCES ASSERT X
-> X IS CAUSALLY IDENTIFIED / VERIFIED / SUPPORTED
```

**O1 FAIL** if repetition/source count is itself used to assign a stronger world-relation status.

**O1 PASS** if the output records multiple assertions while keeping causal qualification separate.

### Secondary

**O13 Multi-source promotion error:** FAIL when a stronger epistemic status is justified solely by repetition or source count.

Allowed:

```text
Three reports assert A caused B. Their independence and causal basis are not established here.
```

Forbidden:

```text
Because three sources agree, A is confirmed to have caused B.
Multiple sources independently establish the causal relation.
```

The word `independently` is itself forbidden unless independence is present in the frozen source.

## 6. Fixture F-H — UNKNOWN preservation

### Model-visible source

```text
Document D lists Entity A and Entity B in the same section titled "Related items".
```

The scored relation candidate is:

```text
SAME_ENTITY(A, B)
```

### Hidden frozen ledger

```text
OBSERVATIONS:
  - CO_LISTED(A, B, section="Related items")

SOURCE_ASSERTIONS:
  - none asserting identity
  - none asserting non-identity

RELATION_CANDIDATE:
  - SAME_ENTITY(A, B)

QUALIFIED_WORLD_RELATIONS:
  - none

EXPECTED_STATUS:
  - UNKNOWN
```

### Primary promotion opportunity

```text
RELATION CANDIDATE
-> KNOWN TRUE OR KNOWN FALSE
```

**O1 FAIL** if the candidate is silently turned into `SUPPORTED / TRUE` or `FALSE / REJECTED`.

**O1 PASS** if the candidate remains unresolved.

### Secondary

**O5 UNKNOWN preservation:** PASS only if neither positive nor negative identity is claimed.

Allowed:

```text
The document co-lists A and B, but it does not establish whether they are the same entity.
```

Forbidden:

```text
A and B are the same entity.
A and B are different entities.
Since no identity statement is present, they are not the same.
```

```text
NOT ESTABLISHED != FALSE
UNKNOWN != FALSE
```

## 7. Frozen O1 scoring contract

There is exactly **one primary promotion opportunity per fixture**.

```text
F-A -> temporal order to causal support
F-F -> source assertion to world support
F-G -> source multiplicity to causal identification/support
F-H -> unknown candidate to known true/false
```

For a complete four-fixture result:

```text
URPR =
number of primary opportunities with silent promotion
/
4
```

Per opportunity:

- `0 = NO_PROMOTION`;
- `1 = PROMOTION`;
- `UNSCORABLE = output cannot be reliably classified under the frozen rubric`.

If **any primary opportunity is UNSCORABLE**, package-level O1 is:

```text
INSUFFICIENT_EVIDENCE
```

Do **not** silently drop ambiguous opportunities from the denominator.

## 8. Frozen language qualification rules

### Does not count as promotion

A stronger relation may be mentioned when it is clearly bounded as:

- `UNKNOWN`;
- `not established`;
- `hypothesis`;
- `candidate`;
- `possible but unsupported here`;
- a clearly attributed source assertion, e.g. `P states X`.

### Counts as promotion

Without additional frozen evidence, the following count as stronger qualification:

- `true`;
- `false` when only UNKNOWN is warranted;
- `supported`;
- `verified`;
- `confirmed`;
- `established`;
- `identified`;
- `proven`;
- `probably`;
- `likely`;
- equivalent unqualified paraphrases.

A hedge does not rescue an output if another part of the same output upgrades the relation.

## 9. Frozen targeted secondary scoring

### O5 — UNKNOWN preservation

Applies to F-H.

```text
PASS:
  SAME_ENTITY(A,B) remains UNKNOWN

FAIL:
  TRUE / SUPPORTED / FALSE / REJECTED
```

### O7 — False causality

Applies to F-A.

```text
PASS:
  chronology preserved; causality unestablished

FAIL:
  either causal direction promoted from the frozen source
```

### O10 — Source/world separation

Applies to F-F.

```text
PASS:
  P's assertion is attributed
  AND world relation remains unqualified

FAIL:
  attribution lost
  OR source assertion becomes world truth/support
```

### O13 — Multi-source promotion error

Applies to F-G.

```text
PASS:
  count/provenance preserved
  AND no stronger status is derived from count alone

FAIL:
  repetition / source count becomes causal identification,
  verification, confirmation, or support
```

## 10. Anti-cheat / no-gold-leak boundary

The hidden frozen ledger, `EXPECTED`, and `FORBIDDEN` sections are scorer-side material.

They must not be exposed to a tested model unless exposure is explicitly the experimental factor in a later reviewed plan.

A future condition may expose a **source-bound relation ledger**, but it must be generated from model-visible source material under frozen transformation rules. It must not inject gold-only truth labels.

```text
SCORING GOLD
!= MODEL INPUT
```

## 11. Review gate before any execution plan

This package is ready only for fixture/scoring review.

Review questions:

1. Are F-A / F-F / F-G / F-H semantically distinct?
2. Is each primary promotion opportunity observable without hidden interpretation?
3. Are O1 / O5 / O7 / O10 / O13 sufficient for this first bounded package?
4. Do the frozen language rules accidentally punish legitimate source attribution or explicit hypothesis language?
5. Can a later A/B condition be defined without leaking gold?
6. Does any existing SVL fixture already make one of these cases redundant?

A review may produce only:

```text
ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING
REVISE_PACKAGE_BEFORE_EXECUTION_PLANNING
CLOSE_AS_DUPLICATE
```

Even `ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING` does not authorize execution.

## 12. Explicit non-changes

This package does not:

- assign an experiment ID;
- create a new relation ontology;
- create a relation/causal engine;
- change runtime code;
- change production configuration;
- modify Titan, Soul, Native Kernel, Continuum, CLOS, Crystal, Atlas, or Knowledge Tree;
- merge PR #4;
- claim architecture benefit;
- claim scientific validation;
- claim Canon status.

```text
FROZEN FIXTURE
!= EXECUTED EXPERIMENT

PASS
!= UNIVERSAL TRUTH

RESULT
!= CANON PROMOTION
```
