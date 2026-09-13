# 📇🧬 Velantrim Research Handoff — Graph Kernel → Semantic Reversion → SEM-REV-E0

**Date:** 2026-09-13  
**Status:** `RESEARCH HANDOFF · CONTINUATION PACKET · NOT CANON · NOT RUNTIME AUTHORITY · NOT IMPLEMENTATION SPEC`

## Purpose

Preserve the reasoning path, decisions, rejected/deferred branches, current boundaries, lessons learned, exact next step, and external donor findings from the current research thread so a new chat/model can resume without relying on the original conversation window.

> **Source-of-truth rule:** this handoff does not override owning project sources. If it conflicts with a frozen preregistration, repository source, or current owning documentation, the owning source wins.

## Related sources

- Research Program — Google Doc `17ua3MwScIlpSDZVrbbSUPyotLdvPWwn1AtrHI2htmWE`
- Working Master — Google Doc `1XCWURAahIB0pqZ7pZEw0l46pSD_6zfoFaSSjQfE2hHU`
- Knowledge Tree — Google Doc `1bWPBL1__nvyFdSdDim_0zZ7j-pV9no0VyjX78JgRxBU`
- Vision / Intent / Cognitive Research Journal — Google Doc `1bUV4ieo56TmO6VOMLr-JePF6NC9-J4L_RSCyKvYZh3A`
- Multi-AI Cognitive Research Trace — Google Doc `1FGlYlJaBTwu1DL2AadKKRsAFSXyd2-kDKJHk-J7bMc8`
- SEM-REV-E0 pre-freeze candidate — Google Doc `11Pp6h8VKVajdE3XyNASaIX8hDywOTX8ZGzJ31e69BjI`

---

## 1. Executive snapshot

The research thread started as a storage / Graph Kernel question and changed after adversarial review.

### Current position

1. **Graph Kernel selection is DEFERRED.**
   - No SurrealDB / Kuzu / FalkorDBLite architecture choice has been made.
   - SQLite is only a competent null/control substrate for a bounded semantic experiment, not the selected Velantrim backend.

2. **The scientifically stronger question became semantic distinction preservation rather than database selection.**
   - Central failure mode: **SEMANTIC REVERSION** — an older, weaker, rejected, retracted, superseded, out-of-scope, or unauthorized state reappears later as if current or authoritative after persistence / retrieval / projection / reconstruction.

3. **SEM-REV-E0 was designed as a bounded experiment.**
   - CORE freeze boundary is S0–S5 only:

```text
WRITE
→ CLOSE
→ NEW-PROCESS REOPEN
→ RETRIEVE
→ DETERMINISTIC QUALIFY
→ STRUCTURED PROJECT
```

   - Compression and LLM reconstruction are deliberately excluded from CORE and reserved for later separately frozen fields.

4. **Initial Grok red-team verdict:** `SAFE_WITH_MINOR_FIXES`.
   - Ten fixes were requested.
   - They were incorporated into the v1 pre-freeze candidate.

5. **Final Grok verification has NOT yet occurred on the exact corrected v1.**
   - Latest Grok run returned `NOT_SAFE_TO_FREEZE` only because the v1 document was not available to the reviewer.
   - Grok found the older design and correctly left all ten fixes OPEN.
   - This is a provenance / artifact-availability block, **not** a scientific rejection of v1.

6. **OpenZync Core was reviewed as an external donor.**
   - Verdict: `KEEP_AS_HIGH_VALUE_DONOR`.
   - No architecture promotion.
   - No change to SEM-REV-E0.

---

## 2. Why the Graph Kernel branch was deferred

Earlier comparison work had made SurrealDB look like a promising integrated candidate, with Kuzu as an embedded option and FalkorDBLite as a local/prototype graph option.

The independent Manus control audit changed the decision:

- no demonstrated Velantrim requirement currently requires a Graph Kernel instead of a strict relational baseline;
- feature richness is not evidence of graph necessity;
- graph traversal, vector search, FTS, changefeed, versioning, and permissions do not by themselves create epistemic semantics, authority, provenance truth, or qualification;
- SQLite remains a legitimate null hypothesis for the bounded semantic contract;
- SurrealDB remains a **DEFERRED CANDIDATE**, not a selected backend;
- Kuzu and FalkorDBLite are out of the **current** scope, not globally rejected forever.

Important control distinctions:

```text
DATA MODEL ≠ DATABASE ENGINE
STORAGE CAPABILITY ≠ GOVERNANCE CAPABILITY
LOCAL PERSISTENCE ≠ LOCAL-FIRST SYNC
VERSIONING ≠ PROVENANCE
CHANGEFEED ≠ AUDIT LEDGER
GRAPH RELATION ≠ SEMANTIC AUTHORITY
UNIFIED API ≠ SINGLE PHYSICAL STORE
```

The graph question may reopen later only if a concrete operation, fixed workload/topology, SLO, and error oracle demonstrate a material requirement the baseline cannot meet.

**Do not create a graph-specific workload merely to justify graph technology.**

---

## 3. Pivot: from storage engine to distinction preservation

The strongest useful part of the control audit was the semantic failure mode:

```text
V1 — earlier / weaker understanding
↓
V2 — critique / rejection / correction
↓
V3 — current state
↓
persistence / retrieval / projection / compression / new model
↓
V3 + fragments of V1 revived as current
```

This became the research target.

Key distinctions:

```text
SEMANTIC SIMILARITY ≠ SEMANTIC FIDELITY
MEANING PRESERVATION ≠ DISTINCTION PRESERVATION
RETRIEVAL EXPOSURE ≠ SEMANTIC ACCEPTANCE
CURRENT STATE ≠ STATE HISTORY
SUPERSEDED ≠ DELETED
PROPOSAL ≠ DECISION
OBSERVATION ≠ AUTHORIZATION
RECOMMENDATION ≠ PERMISSION
UNKNOWN ≠ FALSE
NOT RETRIEVED ≠ ABSENT
MODEL OUTPUT ≠ CANON
```

The experiment must isolate **where** semantic collapse occurs instead of attributing every failure to storage or to an LLM.

---

## 4. SEM-REV-E0 current pre-freeze design

### CORE target

Can a minimal durable external memory preserve material semantic distinctions across:

```text
S0 WRITE
→ S1 CLOSE / PROCESS TERMINATION
→ S2 NEW-PROCESS REOPEN
→ S3 RETRIEVE
→ S4 DETERMINISTIC QUALIFY
→ S5 STRUCTURED PROJECT
```

without reviving rejected, retracted, superseded, out-of-scope, unauthorized, uncertain, or otherwise non-current information as current qualified state?

### CORE substrate

`file-backed SQLite only`

SQLite role:

`experimental substrate / null baseline only`

Explicit non-claims:

- not best database;
- not final Velantrim backend;
- not Graph Kernel result;
- not Native Kernel implementation;
- not Crystal implementation;
- not Continuum implementation;
- not MGL / Guardian implementation;
- not Canon;
- not production readiness.

CORE success label:

`SEM_REV_E0_CORE_PASS`

Do **not** use a broad `SEM_REV_E0_PASS` claim.

S6 compression: `NOT FROZEN · NOT AUTHORIZED FOR CORE RUN`  
S7 LLM reader/reconstruction: `NOT FROZEN · NOT AUTHORIZED FOR CORE RUN`

---

## 5. Fixture family in v1 candidate

### Fixture A — `VLT-SEMREV-A-001`

Purpose: revision / rejection / supersession / reopen.

- A = proposal `Path-A`.
- A is retracted because `R1_CONSTRAINT_FAILURE`.
- B = accepted decision `Path-B` because `R2_MEETS_K1`.
- C = later decision `Path-C`, superseding B because `R3_NEW_REQUIREMENT_K2`.

At query time:

- A = proposal + retracted;
- B = decision + superseded;
- C = decision + current;
- current path = Path-C;
- B may reopen only if K2 is removed **and** project owner explicitly re-approves B.

Frozen reopen condition code:

`Y_K2_REMOVED_AND_OWNER_REAPPROVES_B`

### Fixture B — `VLT-SEMREV-B-001`

Purpose: adversarial retrieval / scope / retraction / authority.

V1 / alpha:

- preliminary unblinded two-run Lab-A claim;
- ~40% p50 latency reduction;
- not production authorization;
- later retracted.

V2 / beta:

- 12 Lab-A runs;
- 7.8% median p50 reduction;
- still Lab-A only;
- not production authorization.

Authority decision `AD-9`:

- production-us authorization = REFUSED.

Query:

`Does VX-17 reduce Atlas latency in production?`

Critical adversarial condition:

`as:alpha-v1` **MUST** be present in the S3 candidate set by construction.

Rank-first is allowed, not required.

Correct qualification:

`NO_QUALIFIED_RESULT`

The system must demonstrate:

`RETRIEVED ≠ QUALIFIED`

rather than pass by failing to retrieve the dangerous historical candidate.

### Fixture C — `VLT-SEMREV-POS-001`

Purpose: positive control against trivial abstain-all / exclude-all.

- valid production-eu authority decision;
- explicitly approves VX-21 for Orion;
- qualifier must return a qualified positive result.

Without this positive control, an always-empty qualifier could falsely pass.

---

## 6. Grok red-team — ten required fixes

Initial Grok review returned `SAFE_WITH_MINOR_FIXES` and required:

1. Positive control must be explicit frozen records + required/forbidden atoms, not prose.
2. Fixture B S3 must seed dangerous V1 into the candidate set by construction.
3. Oracle must use REQUIRED/FORBIDDEN atoms, not a gold essay; HF-05/14/15 must bind to those atoms.
4. Currentness must be derived from revision + valid_from/valid_to + effective_from; no free mutable `is_current` flag.
5. SQLite must be file-backed; `:memory:` prohibited; S1 closes/terminates process; S2 is a new OS process.
6. Fixture A reopen condition Y must be fully specified or removed.
7. Without S6, result label must be `SEM_REV_E0_CORE_PASS`, not broad semantic-reversion PASS.
8. S6/S7 must be outside CORE; S7 requires a separate frozen Reader Field.
9. Experimental tables/schema must be declared test substrate only, not Canon/project implementation.
10. S4 must read mandatory qualifiers only from typed fields/relations; if mandatory force/scope/authority/currentness exists only in prose, S0 = FAIL.

All ten are incorporated in the current v1 pre-freeze candidate.

---

## 7. Why latest Grok verdict was not a design failure

Latest Grok output:

```text
SPEC_LOCATED = NO
CLOSED = 0
OPEN = 10
BOUNDARY_HAS_ISSUE
NOT_SAFE_TO_FREEZE
VERIFICATION_BLOCKED_SPEC_NOT_AVAILABLE
```

Interpretation:

- Grok could only locate the old design, not the corrected v1.
- It correctly refused to infer that fixes were implemented from memory or from our claim.

Desired evidence/provenance behavior:

```text
CLAIM THAT A FIX EXISTS ≠ INSPECTION OF THE FIXED ARTIFACT
REVIEW MEMORY ≠ TARGET SPEC
NOT AVAILABLE TO REVIEWER ≠ FAILED SCIENTIFIC DESIGN
```

Therefore:

**Do NOT redesign SEM-REV-E0 based on this verdict.**

The next step is to give Grok the exact v1 artifact and rerun the bounded fix-verification prompt.

---

## 8. Currentness / qualification lessons

Currentness must be derived, not trusted as a mutable semantic flag.

Conceptually:

```text
current(T)
= valid interval applies at T
AND not retracted by an effective revision
AND not invalidated
AND not superseded by an effective successor
```

A stored `is_current=true` can lie or leak the oracle answer into the representation.

Qualification must read typed fields / typed relations for mandatory semantics.

If force, scope, authority, retraction, or currentness can only be recovered by parsing prose, the storage representation has already failed the CORE contract.

---

## 9. Layer-local failure attribution

Do not collapse errors into one score.

```text
STORAGE FAILURE ≠ RETRIEVAL FAILURE
RETRIEVAL FAILURE ≠ QUALIFICATION FAILURE
QUALIFICATION FAILURE ≠ PROJECTION FAILURE
PROJECTION FAILURE ≠ COMPRESSION FAILURE
LLM FAILURE ≠ SQLITE FAILURE
```

A dangerous historical record appearing in retrieval is **not automatically a semantic failure**.

It becomes a semantic failure if later layers wrongly admit/promote it as current, applicable, authoritative, or qualified.

```text
RETRIEVAL OF SUPERSEDED MATERIAL ≠ SEMANTIC FAILURE
WRONG QUALIFICATION / PROJECTION OF IT = SEMANTIC FAILURE
```

---

## 10. Relation to Continuum E0-T

Do **not** silently merge SEM-REV-E0 with Continuum Claim B.

CONT-E0T already ran and was `UNDERDETERMINED`:

- 8/8 reader calls completed;
- all 8 outputs `PRIMARY_PARTIAL`;
- 4/4 fixture pairs `BOTH_INADEQUATE`;
- `S=0, I=0, U=4`;
- no hard fails.

It did **not** establish trajectory value/non-value, T1 sufficiency, history necessity/non-necessity, or event-sourcing necessity/non-necessity.

Main post-run floor issue:

reader utilization/composition was not adequate enough to isolate history value.

SEM-REV-E0 is a separate cross-cutting experiment on distinction preservation.

---

## 11. OpenZync Core donor audit

External source:

https://github.com/openzync/openzync-core

Reviewed master commit:

`cf05de752d903d84c2a56802418bda1e311bb7f2`

Repo status: alpha.

Verdict:

```text
KEEP_AS_HIGH_VALUE_DONOR
NO ARCHITECTURE PROMOTION
NO CHANGE TO SEM-REV-E0
```

### A. Atomic temporal supersession + as-of lineage

OpenZync closes an old fact validity range and inserts the successor in the same transaction, with rollback safety and concurrency serialization.

Useful donor for Continuum/state-evolution research and SEM-REV comparisons.

### B. Derived graph projection after supersession

OpenZync distinguishes:

- retraction → expire derived edge;
- successor changes edge key → expire old edge;
- successor reasserts same edge → keep edge.

Useful research candidate:

`SOURCE TRANSITION ≠ PROJECTION TRANSITION`

A derived projection should change only when the semantics it projects changed.

Research candidate only; not Canon.

### C. Hybrid retrieval comparator

```text
Vector + BM25 + Graph BFS
→ RRF
→ optional CrossEncoder reranking
```

Useful external comparator for Graphiti Fractal / FM research.

But:

`RANKING ≠ QUALIFICATION`

It does not by itself implement PASS / EXCLUDE / HONEST EMPTY, semantic authority, or structural applicability qualification.

### D. Second-pass pattern observations

OpenZync detects co-occurrence, temporal-gap, and behavioral patterns over accumulated memory.

Important properties:

- SQL-first;
- LLM-optional;
- LLM mainly generates descriptions;
- warn-only design does not automatically mutate facts.

Useful donor for background-pattern-memory research:

```text
EPISODES
→ RECURRING STRUCTURE
→ PATTERN HYPOTHESIS
→ ORIENTATION
```

Boundaries:

```text
PATTERN DETECTED ≠ FACT
PATTERN ≠ IDENTITY
PATTERN ≠ AUTHORITY
```

### E. Replaceable backend contract

OpenZync `GraphBackend` is a useful implementation example of contract-before-backend.

Do **not** copy its graph-specific API as Native Kernel semantics; Native Kernel should remain substrate-neutral above nodes/edges/traversal.

Do not import as Velantrim truth:

- Graph = memory;
- SPO + confidence = universal memory object;
- RRF / CrossEncoder ranking = qualification;
- confidence = authority/truth;
- OpenZync schema = Native Kernel schema;
- early filtering of superseded material = the only correct strategy;
- detected graph observation = accepted fact.

Documentation-drift lesson: prefer live code + tests + exact commit over stale architectural prose.

---

## 12. Cross-project routing

### 🌎 Continuum

Owns process continuity / current state vs history / reopen semantics.

OpenZync temporal supersession is an implementation donor, not proof of required mechanism.

### 🧬 Native Kernel

Owns substrate-neutral semantic distinctions and invariants.

Potential donor candidates only:

```text
SOURCE TRANSITION ≠ PROJECTION TRANSITION
SEMANTIC MENTION ≠ KNOWLEDGE OBJECT
NEW MENTION ≠ NEW FACT
NEW EVIDENCE ≠ NEW STATE
```

### 💠 Crystal

Owns evidence/provenance/admission/trusted-state semantics.

OpenZync traceability is useful engineering reference, but its Fact model is not a substitute for Crystal’s evidence/authority distinctions.

### 🕸 Graphiti Fractal / FM

OpenZync hybrid retrieval is a real comparator for Vector/BM25/Graph/RRF/CE ranking.

It does not solve qualification merely by reranking.

### ⚗️ CLOS / Research Program

Owns the research method / blueprint and distinction-first discipline, not runtime state.

### 🧭 Orientation / Context Assembly

Pattern hypotheses and qualified projections may inform orientation, but:

`MEMORY OBJECT ≠ ORIENTATION PACKET`

---

## 13. Important lessons from the thread

1. Exact artifact availability matters. A reviewer cannot verify a corrected design it did not receive.
2. Reviewer discipline is valuable even when it returns a blocking verdict. Grok refusing to infer v1 from memory was correct behavior.
3. Positive controls are mandatory when abstention / EMPTY is possible; otherwise an always-reject system can falsely pass.
4. Atom oracles are better than gold essays for deterministic CORE.
5. Currentness should be reconstructed from transitions/time, not injected as a trustworthy answer flag.
6. Retrieval and qualification must remain separate.
7. Database feature count is not evidence of cognitive necessity.
8. Data-plane semantics should be tested before multi-backend operational complexity.
9. A passing SQLite bounded fixture would only show that the tested contract does not require a graph engine; it would not select SQLite for all Velantrim.
10. Do not attribute reconstruction-model failure to storage without a layer-local diagnosis.
11. Donor implementation ≠ architecture promotion.
12. Preserve discrepancy provenance: when a summary and exact audit/source disagree, exact source wins for what the auditor actually wrote.

---

## 14. Status matrix at handoff

| Item | Status |
|---|---|
| Graph Kernel / GK-P0 | `DEFERRED` |
| SurrealDB | `DEFERRED CANDIDATE` |
| Kuzu | `OUT OF CURRENT SCOPE` |
| FalkorDBLite | `OUT OF CURRENT SCOPE` |
| SQLite | `CONTROL / TEST SUBSTRATE ONLY` |
| SEM-REV-E0 design | `PRE-FREEZE CANDIDATE` |
| Initial Grok red-team | `COMPLETE` |
| Initial Grok verdict | `SAFE_WITH_MINOR_FIXES` |
| Fixes 1–10 | `INCORPORATED IN v1 CANDIDATE` |
| Final independent verification | `BLOCKED — REVIEWER DID NOT HAVE v1` |
| Scientific redesign required | `NO EVIDENCE` |
| Freeze package | `NOT CREATED` |
| SHA256 | `NOT CREATED` |
| Implementation | `NOT AUTHORIZED` |
| S6 compression | `NOT FROZEN` |
| S7 reader/LLM | `NOT FROZEN` |
| OpenZync | `KEEP_AS_HIGH_VALUE_DONOR` |
| OpenZync architecture adoption | `NO` |
| SEM-REV change due to OpenZync | `NO` |

---

## 15. Exact next action

1. Give Grok Bot the **exact current v1 artifact**.
2. Ask only for final pre-freeze fix verification.
3. Expected output:
   - 10/10 CLOSED or exact remaining blocker(s);
   - `BOUNDARY_CLEAN` / `BOUNDARY_HAS_ISSUE`;
   - `SAFE_TO_FREEZE` / `NOT_SAFE_TO_FREEZE`.
4. If `SAFE_TO_FREEZE`:
   - create byte-stable freeze artifacts;
   - freeze fixtures, atom oracles, currentness rule, qualification rule, stop conditions, SQLite declaration;
   - compute SHA256;
   - only then consider implementation.
5. If not safe:
   - fix only minimum blocking issue(s);
   - do not redesign architecture unless a genuine fatal contradiction appears.

```text
NO IMPLEMENTATION YET
NO S6
NO S7
NO GRAPH KERNEL REOPEN
```

---

## 16. New-chat start protocol

When resuming in a new chat/model:

1. Read the current Research Program.
2. Read this handoff fully.
3. Open the companion SEM-REV-E0 pre-freeze candidate.
4. Do not redesign immediately.
5. First send the exact v1 artifact to Grok for bounded final verification.
6. If `SAFE_TO_FREEZE`, create byte-stable freeze package + SHA256.
7. Only after freeze ask whether implementation is authorized.
8. Keep S6/S7 separate.
9. Keep Graph Kernel deferred unless a separate concrete workload reopens it.
10. Keep OpenZync as donor/reference, not architecture authority.

Minimum restart question:

> **Has Grok independently inspected this exact v1 artifact and returned `SAFE_TO_FREEZE`?**

If NO → verification first.  
If YES → freeze package + SHA256.

---

## 17. Stop / anti-drift rules

```text
NO new organ from this handoff.
NO Graph Kernel promotion.
NO backend selection by convenience or feature count.
NO SEM-REV architecture promotion.
NO claim that semantic reversion is solved generally.
NO claim that SQLite is the final backend.
NO claim that OpenZync validates Velantrim architecture.
NO implementation before explicit owner go after freeze.
NO S6/S7 hidden inside CORE.
```

Final boundaries:

```text
RESEARCH RESULT ≠ ARCHITECTURE PROMOTION
TEST SUBSTRATE ≠ CANONICAL SUBSTRATE
REVIEWER VERDICT ≠ AUTHORITY BEYOND ITS SCOPE
STATE ≠ ENGINE
MODEL MAY PROPOSE STATE CHANGES ≠ MODEL IS STATE AUTHORITY
```

**END OF HANDOFF**
