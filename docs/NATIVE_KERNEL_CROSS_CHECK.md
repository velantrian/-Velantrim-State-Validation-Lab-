# Native Kernel Semantic Cross-Check — E6 (Restore Resurrection)

Per the assignment's Native Kernel cross-check requirement, this
document records the semantic comparison performed before finalizing
the E6 reference model. `velantrian/velantrim-native-kernel` was used
**read-only**, as a semantic reference; nothing in that repository was
modified, imported, or made an authority over this repository.

Native Kernel head at cross-check time: `ce216f52d3da9bcf270b5fa0dece81ab7e8ec641`.

## Finding 1 — Restore quarantine vs. explicit reconciliation

**SVL wording** (`ARCHITECTURE.md` §5, §11, E6-04/E6-05):
> Restored bytes may exist, but current applicability must not return
> without reconciliation with later history... only explicit
> owner-local reconciliation may determine whether state becomes
> applicable again.

**Native Kernel wording** (`docs/contracts/NORMATIVE_CONTRACTS_V1.md`,
"Restore rule"):
> A restored backup remains quarantined until restriction and erasure
> records are replayed. Data must not become queryable before the
> latest applicable deletion state is applied.

**Overlap:** both treat "restored bytes" and "restored current
applicability/queryability" as distinct, and both fail closed by
default after a restore.

**Difference:** Native Kernel's contract admits exactly one path back
to queryability — mechanically **replaying** the same restriction and
erasure records onto the restored copy (which, for an erased subject,
means the restored copy converges back to erased, not to applicable).
SVL's E6-04, as specified in this repository's own `ARCHITECTURE.md`,
admits a second path: an **explicit owner-local reconciliation
decision** that may grant applicability to a revoked/erased-then-
restored candidate when no live successor conflicts with it. This
implementation follows SVL's own spec (`ReconciliationError` requires
a non-empty rationale; `reconcile()` still hard-denies any grant when
a live supersession successor exists — see E6-02), but it is a
strictly less restrictive rule than Native Kernel's replay-only
contract.

**Drift:** difference, not a conflict. Native Kernel's Restore rule is
a domain-specific contract for its own deletion/backup subsystem; it
is not asserted onto SVL, and SVL's `ARCHITECTURE.md` explicitly
specifies the reconciliation decision node this model implements.
Implementing E6 per SVL's own wording does not collapse any of the
boundaries in `ARCHITECTURE.md` §2/§14 (no new truth, action,
permission, or Canon authority is created — `reconcile()` still cannot
be used to bypass a live successor).

**Recommended action:** no change to this wave. Flagged as a P2 note
for when E3 (Interrupted Deletion) or a later long-horizon experiment
is implemented: consider whether `reconcile()` should optionally
support a stricter "replay-of-destructive-history" mode alongside the
current free-text-rationale mode, so SVL can also falsify the
stricter Native-Kernel-style contract rather than only its own looser
one. Recorded, not acted on, in this wave.

## Finding 2 — Snapshot/Checkpoint terminology granularity

**SVL wording** (`ARCHITECTURE.md` §5, `model.py`): a single
`Snapshot` concept — a captured copy of a `StateRecord` at a given
version, used only to seed a later `restore()` candidate.

**Native Kernel wording** (`docs/adr/0002-state-checkpoints-are-
disposable.md`): explicitly distinguishes **State Checkpoint** (cached
reducer state), **Read Snapshot** (structural read-path
representation), and **Evaluation Snapshot** (frozen evaluation
dataset), and warns that "the term `snapshot` is currently overloaded
and may refer to" any of the three, which "must not be conflated."

**Overlap:** both treat a snapshot/checkpoint as disposable and
non-authoritative — Native Kernel's ADR-0002 invariant 1 ("Deleting
every State Checkpoint must not destroy authoritative history") and
SVL's `restore bytes != restore semantic validity` are compatible.

**Difference:** SVL's `Snapshot` is intentionally a single, coarser
research concept; it does not yet distinguish cached-state-for-replay
from a structural read snapshot from a frozen evaluation dataset.

**Drift:** no drift — SVL is a smaller research fixture and has not
claimed the three-way distinction. Recorded for awareness only.

**Recommended action:** none required for E6. If SVL later needs to
model replay acceleration (closer to E10/Long-Horizon Mutation), reuse
Native Kernel's three-way terminology rather than inventing new terms.

## Finding 3 — Logical vs. physical erasure

**SVL wording** (`ARCHITECTURE.md` §5, §14): `erased value != erased
history`; erasure is modeled as removing current processability while
provenance/history remains inspectable.

**Native Kernel wording** (`docs/A6_KNOWLEDGE_LIFECYCLE.md`):
`LOGICALLY_ERASED` ("marked non-available for ordinary use while its
Record remains inspectable under Authority") is explicitly distinct
from `PHYSICALLY_OR_CRYPTOGRAPHICALLY_ERASED` ("the bytes or the key
required to recover them have been destroyed"); `REVISED_OR_SUPERSEDED`
"never implies `LOGICALLY_ERASED` or `FORGOTTEN_OR_LOST` by itself."

**Overlap:** direct match. This repository's `model.py::erase()`
implements only logical erasure (`payload = None`, record retained
with full `provenance`), and `supersede()` never marks the predecessor
`erased`. This is already documented as a limitation in
`EXECUTION_STATUS.md`.

**Difference:** none identified.

**Drift:** none.

**Recommended action:** none. Keep the existing limitation note in
`EXECUTION_STATUS.md` so a reader does not mistake SVL's `erase()` for
physical/cryptographic erasure.

## Overall conclusion

No material semantic conflict was found that would require stopping
before implementing E6. Finding 1 is the only substantive difference
and is recorded as a follow-up note, not a blocker; it does not
require modifying Native Kernel, importing its runtime, or changing
SVL's ownership or authority boundaries.
