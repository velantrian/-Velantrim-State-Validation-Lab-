# SEM-REV-E1 — Hypotheses and Failure Modes

**STATUS:** preregistration candidate · NOT FROZEN

---

## H0-E1 — Continuity under adversarial histories

The bounded deterministic semantic-preservation mechanism continues to
preserve required distinctions under the E1 adversarial suite.

Falsified if any CORE hard fail / required-atom miss / forbidden-atom hit /
positive-control failure occurs under valid execution integrity.

---

## H1 — REVISION DEPTH FAILURE

**Claim under test:** deeper revision chains do not revive older
valid-looking states as current.

**Discriminating family:** E1-A  
**Typical fail signature:** Path-A/B/C current while D should be current; or
historical IDs lost.

---

## H2 — TEMPORAL ORDERING FAILURE

**Claim under test:** `valid_*`, `effective_from`, and `query_as_of` boundaries
are applied without off-by-one or axis conflation.

**Discriminating family:** E1-B (primary), E1-C (secondary)  
**Typical fail signature:** decision current before `effective_from`; or
`recorded_at` treated as semantic currentness.

---

## H3 — SCOPE DISAMBIGUATION FAILURE

**Claim under test:** nearby / colliding scopes do not widen.

**Discriminating family:** E1-D  
**Typical fail signature:** `production-us` approval qualifies under
`production-eu` or `production-us-canary`.

---

## H4 — AUTHORITY CONFLICT FAILURE

**Claim under test:** conflicting authority records are preserved without
fabricating precedence; jurisdiction / outcome / supersession remain typed.

**Discriminating family:** E1-E  
**Typical fail signature:** unauthorized or out-of-jurisdiction approval
accepted; refused outcome flipped; invented hierarchy winner.

**Expressibility note:** cases needing an unregistered global authority
rank order are `NOT EXPRESSIBLE UNDER CURRENT CONTRACT`.

---

## H5 — DEPENDENCY INTEGRITY FAILURE

**Claim under test:** missing **required** typed qualification dependency
causes stage failure / non-classifiable outcome — not silent
`NO_QUALIFIED_RESULT` as if absence were valid evidence.

**Discriminating family:** E1-F  
**Typical fail signature:** required dep missing → treated as ordinary
exclusion / valid absence.

---

## H6 — LATE-ARRIVAL FAILURE

**Claim under test:** later `recorded_at` does not imply later semantic
authority / currentness when `observed_at` / `asserted_at` / `effective_from`
say otherwise.

**Discriminating family:** E1-C  
**Typical fail signature:** late-recorded older observation outranks earlier-recorded
newer decision solely by `recorded_at`.

---

## H7 — REOPEN-CONDITION FAILURE

**Claim under test:** reopen occurs **only** under the exact preregistered
compound condition; partial satisfaction and “superseded forever” are both wrong.

**Discriminating family:** E1-G  
**Typical fail signatures:**
- superseded state returns without full condition;
- half-condition treated as full;
- full condition + missing reapproval still current;
- full frozen reopen satisfied but state never reconsiderable.

---

## H8 — CONTRADICTORY-EVIDENCE FAILURE

**Claim under test:** evidence conflict is preserved; evidence ≠ belief ≠
authorization.

**Discriminating families:** E1-H, E1-I  
**Typical fail signature:** conflict collapsed to single truth; or retracted
assertion identity revived by similar new evidence.

---

## H9 — UNKNOWN DISCIPLINE FAILURE

**Claim under test:** optional unspecified properties remain `UNKNOWN`; they
are not fabricated into FALSE/TRUE.

**Discriminating family:** E1-F (optional arm)  
**Typical fail signature:** UNKNOWN → FALSE or invented concrete value.

---

## H10 — OVER-ABSTENTION / POSITIVE-CONTROL FAILURE

**Claim under test:** mechanism cannot pass by excluding everything.

**Discriminating family:** E1-J  
**Typical fail signature:** straightforward approved current decision →
EMPTY / abstention / `NO_QUALIFIED_RESULT`.

---

## Coverage rule

Every hypothesis H1–H10 has ≥1 discriminating CORE fixture.  
Every CORE fixture maps to ≥1 hypothesis.  
No majority vote across hypotheses for CORE_PASS.
