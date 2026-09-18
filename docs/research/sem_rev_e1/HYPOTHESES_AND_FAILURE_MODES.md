# SEM-REV-E1 — Hypotheses and Failure Modes (C2–C12)

**STATUS:** preregistration candidate · NOT FROZEN

---

## H0-E1 — Continuity under adversarial histories

The bounded deterministic semantic-preservation mechanism continues to
preserve required distinctions under the E1 adversarial suite that is
**expressible under the current E0 contract**.

Falsified if any CORE hard fail / required-atom miss / forbidden-atom hit /
positive-control failure occurs under valid execution integrity.

NX cases are outside CORE falsification.

---

## H1 — REVISION DEPTH FAILURE

**Claim under test:** deeper revision chains do not revive older states as
current; RETRACTED vs SUPERSEDED remain exact.

**Discriminating family:** E1-A  
**Typical fail signature:** Path-A/B/C current while D should be current; or
retracted collapsed to generic history / superseded mislabeled as retracted.

---

## H2 — TEMPORAL ORDERING FAILURE

**Claim under test:** `valid_*`, `effective_from`, and `query_as_of` boundaries
are applied without off-by-one or axis conflation.

**Discriminating family:** E1-B (primary), E1-C (secondary)  
**Typical fail signature:** `dec:e1b-1` current before `effective_from`; or
`dec:e1b-0` dropped while still valid; or `recorded_at` treated as currentness.

---

## H3 — SCOPE DISAMBIGUATION FAILURE

**Claim under test:** nearby / colliding scopes do not widen.

**Discriminating family:** E1-D  
**Typical fail signature:** `production-us` approval qualifies under
`production-eu` or `production-us-canary`.

---

## H4 — AUTHORITY / OUTCOME / SUPERSESSION FAILURE (narrowed)

**Claim under test:** typed **scope**, **outcome**, and **supersession**
distinctions for authority_decision records are preserved.

**Not claimed in CORE:** authority-**jurisdiction** relations (no typed
jurisdiction primitive in E0 contract). E1-E-01 is a **scope_mismatch** case.

**Discriminating family:** E1-E  
**Typical fail signature:** scope_mismatch accepted; refused flipped to approved;
superseded decision treated current; invented hierarchy winner.

**Expressibility note:** two same-scope conflicting approvals without typed
supersession → `E1-E-NX` (`NOT EXPRESSIBLE UNDER CURRENT CONTRACT`).

---

## H5 — DEPENDENCY INTEGRITY FAILURE

**Claim under test:** missing **required** typed qualification dependency
causes **preregistered fail-closed** (S4 FAIL) — not silent ordinary
`NO_QUALIFIED_RESULT` as valid absence.

```text
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
FIXTURE_SEMANTIC_PASS iff exact fail-closed
```

**Discriminating family:** E1-F  
**Typical fail signature:** required dep missing → ordinary exclusion / valid absence.

---

## H6 — LATE-ARRIVAL FAILURE

**Claim under test:** later `recorded_at` does not imply later semantic
authority / currentness when other axes say otherwise.

**Discriminating family:** E1-C  
**Typical fail signature:** late-recorded older observation outranks by `recorded_at`.

---

## H7 — PATH-RETURN / IDENTITY FAILURE (narrowed)

**Honest scope after C4:**

Under the current contract, E1 **cannot** CORE-test compound reopen-condition
evaluation (`K_CONSTRAINT_REMOVED AND OWNER_REAPPROVES_PRIOR`) because no
registered typed condition/flag primitive exists.

What **is** CORE-tested:

1. same-ID resurrection is forbidden;
2. a **new** decision/assertion version may return to a previously used path
   via typed `supersedes` (`E1-G-04`).

Compound-condition lattice → `E1-G-NX`.

**Typical fail signature:** `prior-v1` revived as current; OR ambiguous
`current_via_legitimate_reopen`; magic `rev:*` flag used as condition.

---

## H8 — OBSERVATION-PRESERVATION / NON-AUTHORIZATION FAILURE (narrowed)

**Claim under test:** distinct opposing observations remain recoverable as
distinct identities; no authority/production authorization is fabricated from
observations alone.

**Not claimed:** typed conflict-relation detection; `effect_code` atoms;
“SUT detected a contradiction”.

```text
PRESERVING DISTINCT OPPOSING OBSERVATIONS
≠
DERIVING A TYPED CONFLICT RELATION
```

**Discriminating families:** E1-H, E1-I  
**Typical fail signature:** merge/delete of an observation; authorization inferred
from observations; retracted ID revived by similar late evidence.

---

## H9 — UNKNOWN DISCIPLINE FAILURE

**Claim under test:** optional unspecified **uncertainty** remains `UNKNOWN`;
not fabricated into FALSE/TRUE.

Uses existing optional encoding (`uncertainty` NULL → UNKNOWN).  
Does **not** use `declared_loss=UNKNOWN` (unsupported; `declared_loss` is INTEGER 0/1).

**Discriminating family:** E1-F (F-02)  
**Typical fail signature:** UNKNOWN → FALSE or invented concrete value.

---

## H10 — OVER-ABSTENTION / POSITIVE-CONTROL FAILURE

**Claim under test:** mechanism cannot pass by excluding everything.

**Discriminating fixtures:** E1-J-01, E1-D-03, E1-G-04 (+ role tag J-02), E1-B-02/B-03  
**Typical fail signature:** straightforward approved current decision → EMPTY / abstention.

---

## Coverage rule

Every CORE hypothesis claim above has ≥1 discriminating CORE fixture.  
NX boundaries are explicit and non-CORE.  
No majority vote across hypotheses for CORE_PASS.
