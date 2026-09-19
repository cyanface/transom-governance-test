# Synthetic GitHub Collaboration Fixture

This repository is an entirely synthetic fixture. It exists only to
show local preparation of a tiny multi-module Python project and a
required CI workflow. It is not a product, contains no private source,
and does not prove GitHub protected-branch enforcement.

## Purpose

- Three independent modules (`alpha`, `beta`, `gamma`) each expose one
  integer contribution (`1`, `2`, and `3`).
- A standard-library unittest suite asserts each module on its own and
  asserts that the combined total is `6`.
- `.github/workflows/required-check.yml` runs that same suite on `push`
  and `pull_request` using official `actions/checkout@v4` and Ubuntu
  system Python. No package installs are required.

Checking the workflow file in only prepares a local fixture. It does
not create a remote, enable branch protection, or verify GitHub checks.

## Future three-agent scenario

A later exercise can split work across three agents without breaking
this baseline:

1. Each agent owns one module (`alpha.py`, `beta.py`, or `gamma.py`)
   and adds one new function to that module only.
2. Each agent adds its own separate test file that covers only the new
   function in its module.
3. An integration step adds a combination test that calls all three new
   functions together.
4. The existing baseline tests and the combined total of `6` remain
   passing.

No agent should edit another agent's module or dedicated test file
except when updating the shared combination test.

## Tests

```
python3 -m unittest discover -s tests -v
```
