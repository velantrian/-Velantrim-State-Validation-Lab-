# SEM-REV-E1 — Hard Fails (C2–C12)

**STATUS:** preregistration candidate · NOT FROZEN  
E1 uses its own HF table. Do not assume E0 HF numbers apply.

Any triggered CORE hard fail → `SEM_REV_E1_CORE_PASS` prohibited.

E1-F-01 **expected** S4 fail-closed is **not** a hard fail.  
`E1-HF-06` triggers only if required-dependency loss is silently converted
to a valid result / ordinary `NO_QUALIFIED_RESULT`.

---

## Hard-fail table

| ID | Condition |
|----|-----------|
| E1-HF-01 | Old / historical state revived as current |
| E1-HF-02 | Retracted state qualified as active |
| E1-HF-03 | Superseded state qualified without a new superseding version identity |
| E1-HF-04 | Scope widening contrary to frozen scope atom |
| E1-HF-05 | Authority decision accepted despite typed **scope_mismatch** (or refused flipped to approved) |
| E1-HF-06 | Required dependency loss silently converted to valid result / ordinary NO_QUALIFIED_RESULT |
| E1-HF-07 | Time axes conflated (`recorded_at` / `observed_at` / `effective_from` / `query_as_of`) |
| E1-HF-08 | Optional UNKNOWN (`uncertainty`) fabricated into FALSE/TRUE or concrete value |
| E1-HF-09 | Positive control returns EMPTY / abstention / omit |
| E1-HF-10 | Oracle leakage into SUT before fixture evidence is fixed |
| E1-HF-11 | Candidate omission enabling artificial success |
| E1-HF-12 | Semantic force changed vs frozen force atom |
| E1-HF-13 | Result depends on prose parsing for mandatory qualifiers |
| E1-HF-14 | Currentness stored as mutable answer flag (`is_current`) rather than derived rule |
| E1-HF-15 | Production authorization / single authorized truth fabricated from observations alone |
| E1-HF-16 | Retracted assertion identity revived by similar late evidence |
| E1-HF-17 | Same-ID resurrection of a superseded/retracted decision/assertion |
| E1-HF-18 | Refused authority outcome flipped to approved |
| E1-HF-19 | RETRACTED collapsed to SUPERSEDED (or vice versa) as sole status |
| E1-HF-20 | Hidden condition-flag / unregistered primitive used as mandatory input |

**Note:** E1-HF-05 does **not** claim a typed jurisdiction relation.

---

## Mapping to families (primary)

| HF | Primary families |
|----|------------------|
| E1-HF-01 | A, I, G |
| E1-HF-02 | I |
| E1-HF-03 | A, G |
| E1-HF-04 | D |
| E1-HF-05 | E |
| E1-HF-06 | F |
| E1-HF-07 | B, C |
| E1-HF-08 | F |
| E1-HF-09 | J, D-03, G-04, B-02/B-03 |
| E1-HF-10 | all |
| E1-HF-11 | any with required dangerous candidates |
| E1-HF-12 | all |
| E1-HF-13 | all |
| E1-HF-14 | all |
| E1-HF-15 | H |
| E1-HF-16 | I |
| E1-HF-17 | G, I |
| E1-HF-18 | E |
| E1-HF-19 | A |
| E1-HF-20 | G-NX boundary / package hygiene |
