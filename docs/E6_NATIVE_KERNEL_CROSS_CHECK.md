# E6 Native Kernel semantic cross-check

## Checked state

- State Validation Lab starting base: `d6bf0820318f42932d3aed0ac2bf59f66839a28d`
- Native Kernel read-only reference: `ce216f52d3da9bcf270b5fa0dece81ab7e8ec641`
- Cross-check mode: owner-local semantic comparison only
- Native Kernel files changed: none

## Result

`NO_MATERIAL_SEMANTIC_CONFLICT`

| SVL E6 wording | Native Kernel controlling distinction | Result |
|---|---|---|
| Restored bytes do not restore current applicability | Representation/bytes are not represented reality or semantic identity; change and loss remain accountable | Compatible |
| Restore creates a stale candidate | Candidate/disposition and current applicability remain scoped; storage does not create truth or authority | Compatible |
| Supersession keeps the predecessor non-current | `Supersession ≠ deletion or falsity`; predecessor/successor lineage remains distinguishable | Compatible |
| Fixture `erase` removes processable payload | Logical disposition is distinct from physical deletion, cryptographic erasure, and forgetting/loss | Compatible after explicit scope label |
| Reconciliation produces a bounded applicability result | Authority is role- and scope-specific; resolution for scope is not objective truth | Compatible |
| Missing/unknown objects fail closed | `Unknown ≠ False`; unsupported/failure states must remain explicit | Compatible |
| Deterministic fixture PASS | Reference-laboratory evidence is not Architecture Canon, universal proof, runtime thaw, or production authority | Compatible |

## Important difference retained

Native Kernel's current provisional interpretation is stronger and more
careful than a single `erased` boolean: it separates logical disposition,
physical erasure, cryptographic erasure, and epistemic forgetting/loss. The E6
model therefore calls `erase()` a **fixture-local logical lifecycle
transition** and makes no physical, cryptographic, privacy, compliance, or
global non-existence claim.

The Native Kernel A2/A3/A5/A6 catalogues are reference taxonomies rather than
a mandatory universal state machine after IAR-1-R1. E6 uses its tiny enum only
as an owner-local falsification instrument; it does not copy Native Kernel
runtime, contracts, Event vocabulary, reducer semantics, or authority.
