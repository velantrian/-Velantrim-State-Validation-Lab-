# Relation Integrity tiny package — review record (2026-09-25)

**Scope:** review of `RELATION_INTEGRITY_TINY_FIXTURE_SCORING_2026_09_25.md` revision 0.1 and `fixtures/relation_integrity_qualification_v0_1.jsonl`.

**Review outcome:** `REVISE_PACKAGE_BEFORE_EXECUTION_PLANNING`

This review does not authorize execution, merge, experiment numbering, architecture promotion, or runtime change.

## 1. Duplicate / overlap check against current SVL main

Current SVL main already contains broad relation and causal-audit semantics:

- Semantic Plane keeps Observation / Claim / Evidence / Belief / Permission / Commitment / Process State distinct.
- Relation & Derived-State Plane contains typed relations including `CAUSED_BY`.
- Causal Trace requires unknown causality to remain `UNKNOWN` / declared loss.
- E9 Causal Audit asks for reconstructible lineage.
- Research Decision Gate prevents failure from directly authorizing redesign.

However, current main does not contain a bounded fixture that specifically scores:

```text
SOURCE_ASSERTION -> WORLD_SUPPORT
MULTI_SOURCE_COUNT -> STRONGER_EPISTEMIC_STATUS
RELATION_CANDIDATE -> KNOWN TRUE/FALSE
TEMPORAL_ORDER -> CAUSAL_SUPPORT
```

Verdict:

```text
OVERLAP = PARTIAL
DUPLICATE_ON_MAIN = NO
QUALIFICATION_RESIDUAL = STILL DISTINCT ENOUGH FOR BOUNDED PLANNING
```

This is not a novelty claim across Velantrim.

## 2. Blocking issue R1 — all-negative package permits a trivial always-UNKNOWN strategy

Revision 0.1 contains four negative / underdetermined fixtures and no positive control.

A system that emits `UNKNOWN` for every relation can obtain a perfect anti-promotion score without demonstrating that it can preserve a relation when the fixture actually supports one.

This would confound:

```text
NO SILENT PROMOTION
with
NEVER QUALIFY ANY RELATION
```

Required revision:

- add one positive control;
- do not include it in the O1 false-promotion denominator;
- score it separately with existing O2 Explicit relation preservation.

## 3. Blocking issue R2 — candidate visibility is not frozen symmetrically

Revision 0.1 freezes a scorer-side relation candidate, but the package does not state that the candidate is model-visible in every condition.

This is especially material for F-H:

```text
source: A and B are co-listed under "Related items"
candidate: SAME_ENTITY(A,B)
```

If the candidate is hidden, simple omission can look like successful qualification.

Required revision:

- freeze one `MODEL_VISIBLE_RELATION_CANDIDATE` for every fixture;
- expose the same candidate to every compared arm;
- any later relation-ledger arm may restructure source information, but must not receive a gold-only candidate unavailable to the baseline arm.

## 4. Scoring ambiguity R3 — modal language needs normalization

Revision 0.1 correctly treats ungrounded `probably / likely` as promotion, but phrases such as:

```text
suggests
is consistent with
may indicate
is compatible with
```

can be either cautious hypothesis language or an implicit status upgrade depending on context.

Required revision:

Normalize each scored relation to exactly one evaluator-side status:

```text
SUPPORTED
HYPOTHESIS
UNKNOWN
REJECTED
UNSCORABLE
```

For negative fixtures:

- `HYPOTHESIS` and `UNKNOWN` are non-promotion;
- `SUPPORTED` is promotion;
- `REJECTED` is promotion when the fixture does not establish falsity;
- `UNSCORABLE` must remain visible and must not be dropped.

Conditional or counterfactual mention without endorsement does not itself count as promotion.

## 5. Positive control requirement

Add a simple synthetic identity control:

```text
Registry R records:
Entity A -> record UUID 42
Entity B -> record UUID 42
Registry contract: aliases resolving to the same UUID denote the same registry entity.
```

Model-visible candidate:

```text
SAME_ENTITY(A,B)
```

Expected qualification:

```text
SUPPORTED
```

This control is intentionally easy. Its purpose is not scientific difficulty; it detects the degenerate strategy `always UNKNOWN`.

Score with:

```text
O2 Explicit relation preservation
```

Do not add it to the O1 denominator.

## 6. Accepted parts of revision 0.1

The following are retained:

- F-A temporal adjacency without causality;
- F-F source assertion without world acceptance;
- F-G multi-source repetition without causal identification;
- F-H UNKNOWN preservation;
- O1 as the primary false-promotion metric;
- O5 / O7 / O10 / O13 as targeted secondaries;
- scorer-side gold separation;
- no experiment ID;
- no execution authorization;
- no architecture consequence;
- no merge authorization.

## 7. Gate after revision

After R1-R3 are fixed, perform one bounded re-review.

Allowed next outcome:

```text
ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING
or
REVISE_PACKAGE_BEFORE_EXECUTION_PLANNING
or
CLOSE_AS_DUPLICATE
```

Even acceptance authorizes only preparation of an execution/evidence plan.

```text
PACKAGE REVIEW != EXECUTION AUTHORIZATION
```
