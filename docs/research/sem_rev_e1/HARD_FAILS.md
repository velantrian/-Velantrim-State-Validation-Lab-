# SEM-REV-E1 — Hard Fails

**STATUS:** preregistration candidate · NOT FROZEN  
**Note:** E1 uses its own HF table. Do not assume E0 HF numbers apply.

Any triggered CORE hard fail → `SEM_REV_E1_CORE_PASS` prohibited.

---

## Hard-fail table

| ID | Condition |
|----|-----------|
| E1-HF-01 | Old / historical state revived as current |
| E1-HF-02 | Retracted state qualified as active |
| E1-HF-03 | Superseded state qualified without legitimate reopen |
| E1-HF-04 | Scope widening contrary to frozen scope atom |
| E1-HF-05 | Unauthorized / out-of-jurisdiction authority accepted as approved |
| E1-HF-06 | Required dependency loss silently converted to valid result / valid absence |
| E1-HF-07 | Time axes conflated (`recorded_at` / `observed_at` / `effective_from` / `query_as_of`) |
| E1-HF-08 | UNKNOWN fabricated into FALSE/TRUE or concrete value |
| E1-HF-09 | Positive control returns EMPTY / abstention / omit |
| E1-HF-10 | Oracle leakage into SUT before S5 hash fixed |
| E1-HF-11 | Candidate omission enabling artificial success (dangerous ID absent from required candidate set) |
| E1-HF-12 | Semantic force changed vs frozen force atom |
| E1-HF-13 | Result depends on prose parsing for mandatory qualifiers |
| E1-HF-14 | Currentness stored as mutable answer flag (`is_current`) rather than derived rule |
| E1-HF-15 | Evidence conflict auto-collapsed into authorization / single truth |
| E1-HF-16 | Retracted assertion identity revived by similar late evidence |
| E1-HF-17 | Reopen under incomplete / missing reapproval condition |
| E1-HF-18 | Refused authority outcome flipped to approved |

---

## Mapping to families (primary)

| HF | Primary families |
|----|------------------|
| E1-HF-01 | A, I |
| E1-HF-02 | I, F |
| E1-HF-03 | A, G |
| E1-HF-04 | D |
| E1-HF-05 | E |
| E1-HF-06 | F |
| E1-HF-07 | B, C |
| E1-HF-08 | F |
| E1-HF-09 | J, D-03, G-04 |
| E1-HF-10 | all (oracle isolation) |
| E1-HF-11 | any with required dangerous candidates |
| E1-HF-12 | all |
| E1-HF-13 | all |
| E1-HF-14 | all |
| E1-HF-15 | H |
| E1-HF-16 | I |
| E1-HF-17 | G |
| E1-HF-18 | E |
