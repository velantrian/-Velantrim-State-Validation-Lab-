# Relation Integrity tiny package — bounded re-review (2026-09-25)

**Reviewed revision:** `0.2`

**Reviewed artifacts:**

- `docs/RELATION_INTEGRITY_TINY_FIXTURE_SCORING_2026_09_25.md`
- `fixtures/relation_integrity_qualification_v0_2.jsonl`
- prior review: `docs/RELATION_INTEGRITY_PACKAGE_REVIEW_2026_09_25.md`

**Outcome:** `ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING`

This outcome authorizes only preparation of an execution/evidence plan. It does **not** authorize execution, experiment numbering, merge, runtime change, Canon promotion, or architecture change.

## 1. R1 — always-UNKNOWN confound

**Resolved.**

Revision 0.2 adds positive control `F-P1`:

```text
A -> UUID 42
B -> UUID 42
registry contract:
same UUID => same registry entity
candidate:
SAME_ENTITY(A,B)
expected:
SUPPORTED
```

The positive control is scored separately with O2 and is excluded from O1/URPR.

Therefore:

```text
NO SILENT PROMOTION
!=
NEVER QUALIFY ANY RELATION
```

is now testable in the package.

## 2. R2 — candidate visibility

**Resolved.**

Every fixture now has one explicit:

```text
MODEL_VISIBLE_RELATION_CANDIDATE
```

The package freezes candidate visibility as arm-invariant and prohibits a future ledger arm from receiving a gold-only candidate unavailable to baseline.

This removes the omission confound identified in revision 0.1.

## 3. R3 — modal-language ambiguity

**Resolved sufficiently for execution planning.**

Evaluator-side normalization is frozen to:

```text
SUPPORTED
HYPOTHESIS
UNKNOWN
REJECTED
UNSCORABLE
```

For the four negative fixtures:

```text
SUPPORTED -> PROMOTION
HYPOTHESIS -> NO_PROMOTION
UNKNOWN -> NO_PROMOTION
REJECTED -> PROMOTION when falsity is not established
UNSCORABLE -> visible; package O1 becomes INSUFFICIENT_EVIDENCE
```

This is adequate for planning. Exact evaluator implementation remains deliberately unfrozen and must be specified before execution.

## 4. Fixture distinctness

The first package retains four distinct failure opportunities:

```text
F-A  chronology       -> causal support
F-F  source assertion -> world support
F-G  source count     -> stronger causal qualification
F-H  unknown candidate-> true/false/support
```

The positive control tests the converse capability:

```text
F-P1 explicit support -> preserve SUPPORTED
```

No fixture is currently redundant with another inside this package.

## 5. Current-main overlap re-check

SVL main contains broad semantic separation, relation typing, Causal Trace, E9 Causal Audit, UNKNOWN preservation, and research decision gates.

It still does not contain this exact bounded qualification fixture/scoring package.

Therefore the earlier conclusion remains:

```text
OVERLAP = PARTIAL
DUPLICATE_ON_MAIN = NO
```

This does not claim novelty across the Velantrim ecosystem.

## 6. Metrics review

Accepted first-package metrics:

```text
O1  Unsupported Relation Promotion Rate
O2  Explicit relation preservation       [positive control only]
O5  UNKNOWN preservation
O7  False causality
O10 Source/world separation
O13 Multi-source promotion error
```

Do not expand to all O1-O13 before execution planning establishes a reason.

## 7. Remaining planning requirements

Acceptance is conditional on a later execution/evidence plan freezing at least:

- exact tested condition(s);
- exact prompt / answer contract;
- exact model/provider/version or deterministic system under test;
- relation-ledger transformation rule if a second arm is used;
- evaluator implementation;
- evaluator disagreement / UNSCORABLE handling;
- replicate count;
- randomization/order if applicable;
- evidence artifact format and hashes;
- exact repo head;
- stopping / invalidation conditions.

None of those are authorized by this review alone.

## 8. Gate state

```text
PARTIAL_OVERLAP DECLARED             = TRUE
OWNER GO TO FREEZE PACKAGE           = TRUE
PACKAGE REVISION                     = 0.2
FROZEN FIXTURE                       = PRESENT
FROZEN SCORING                       = PRESENT
PACKAGE REVIEW                       = ACCEPTED FOR EXECUTION PLANNING
DISTINCT QUALIFICATION RESIDUAL      = CONFIRMED FOR THIS BOUNDED PLANNING STEP
IMPLEMENTATION / EVIDENCE PLAN       = NOT CREATED
EXPERIMENT ID                        = NONE
RUN AUTHORIZED                       = FALSE
MERGE AUTHORIZED                     = FALSE
ARCHITECTURE CONSEQUENCE             = NONE
```

"Confirmed" here is bounded to the planning decision. It is not a claim of scientific novelty or architecture necessity.

## 9. Next bounded action

Create only an execution/evidence plan against revision 0.2.

Do not run the package, assign a numbered experiment, merge PR #4, or create runtime implementation until a later explicit gate.

```text
PACKAGE ACCEPTED
!= EXECUTION AUTHORIZED
```
