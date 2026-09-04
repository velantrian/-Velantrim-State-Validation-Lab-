# E6 Evidence Ledger

This directory owns the stable E6 fixture manifest. Executed Evidence Ledger
records are generated into `.artifacts/evidence/E6/` so ordinary test runs do
not modify tracked files and so each record can bind to the exact tested Git
revision.

Generate a run with:

```bash
PYTHONPATH=src python -m state_validation_lab.run_e6 \
  --output-dir .artifacts/evidence/E6 \
  --repo-head "$(git rev-parse HEAD)" \
  --test-revision "$(git rev-parse HEAD)"
```

CI uploads the five generated JSON files as the `e6-evidence-<head>` workflow
artifact. A committed file cannot truthfully contain the hash of the commit
that contains itself, so exact-head run records are not committed back into the
same source revision.

`PASS` is bounded to the recorded deterministic trajectories and is not a
truth, Canon, safety, production-readiness, or authority claim.
