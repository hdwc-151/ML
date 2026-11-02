# GitHub Actions — Build and Deploy Troubleshooting

## Current known-good configuration

The workflow at `.github/workflows/deploy.yml` currently uses:
- `ubuntu-24.04` (avoid moving runner images implicitly with `ubuntu-latest` when diagnosing platform-specific failures);
- `actions/checkout@v4`;
- `actions/setup-python@v5` with Python `3.13`;
- dependency installation, `pip check`, import smoke check;
- `jupyter-book build .`;
- `peaceiris/actions-gh-pages@v4` to publish `_build/html`.

Do not change a passing workflow without a concrete failure or maintenance reason.

## Incident record: Python 3.13.12 unavailable on Ubuntu 26.04

Observed in run #19 for commit `448573ac090c5d189aab068c739e4c6042151fb7`:
- Runner image: Ubuntu 26.04.
- `actions/setup-python@v5` requested Python `3.13.12`.
- Error: `The version '3.13.12' with architecture 'x64' was not found for Ubuntu 26.04.`
- Dependency installation, book build and deploy were skipped because setup-python failed.

This was **not** a Jupyter Book error and **not** a deploy token error. It was a Python distribution availability mismatch for that runner image.

The workflow was corrected to use the available Python 3.13 release on a pinned Ubuntu 24.04 runner. Run #20 for commit `9264b676ce510044c698bb3fea7b8f0fcb162857` completed all steps successfully, including build and deploy.

## Diagnostic sequence

1. Open the failed run, not just the green/red commit badge.
2. Identify the first failed step. Later skipped steps are consequences, not independent failures.
3. Open the job log and record runner OS, architecture, requested runtime and exact error.
4. If setup-python fails, verify the requested patch exists in the actions/python-versions manifest for that OS/architecture. Prefer a supported minor version unless patch-level reproducibility is essential.
5. If dependency installation fails, inspect Python compatibility, package pins, resolver output and `pip check`.
6. If build fails, inspect MyST/Jupyter Book errors, missing TOC paths, notebook execution, missing assets and Sphinx extension compatibility.
7. If deploy fails, check Pages source/settings, token permissions, branch policy and publish directory.

## Common failure → action

| Failure point | Typical cause | Fix |
|---|---|---|
| Checkout | invalid ref, permissions, transient GitHub issue | verify branch/ref and rerun only if transient |
| Setup Python | requested version unavailable on runner | pin runner image or choose available Python version |
| Install | incompatible pins, missing build dependency | make dependency set explicit; reproduce in clean venv |
| Import check | package discovery or import-time side effects | fix package metadata and keep imports lightweight |
| Jupyter Book build | missing TOC file, notebook execution error, Sphinx conflict | build locally with same Python/dependencies; fix first error |
| Pages deploy | permissions, Pages config, empty/wrong publish directory | grant contents write, verify Pages setup and `_build/html` |

## Reproduce locally

Use the same Python minor version as CI:

```bash
python --version
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt
python -m pip check
python -c "import utils; print('utils import OK')"
jupyter-book build .
```

For a clean reproduction, use a fresh virtual environment. A developer's already-populated environment can hide missing dependencies.

## Keep CI honest

- Green CI proves only the checks that actually ran.
- `import utils` is a smoke test, not an algorithm correctness test.
- A successful book build does not prove every numerical result is scientifically valid.
- Add unit tests and notebook validation as the project grows.
- Avoid running several deployments concurrently; the workflow's concurrency group cancels older in-progress runs so the newest commit wins.
- Do not rewrite Git history just to repaint old commit statuses. Fix the current workflow and rerun historical jobs only when there is a reason.

## Verified run references

- Failed run #19: https://github.com/hdwc-151/ML/actions/runs/41433677108
- Successful run #20: https://github.com/hdwc-151/ML/actions/runs/41433721288
