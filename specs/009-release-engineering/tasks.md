# Tasks: Release Engineering - CI/CD and PyPI Publication

## Implementation Strategy
We will establish the release engineering infrastructure by first configuring the Python packaging metadata to include all non-code resources. Then, we will implement the GitHub Actions CI pipeline for automated testing across multiple Python versions. Finally, we will setup the automated publication workflow to PyPI using Trusted Publishing (OIDC). Verification will involve local build checks and dry-running the CI pipeline.

## Phase 1: Setup
- [X] T001 Create `.github/workflows/` directory in the project root
- [X] T002 Update `pyproject.toml` to include `[tool.setuptools.package-data]` for static assets and extension manifests
- [X] T003 Create `MANIFEST.in` to explicitly include non-Python files in the source distribution

## Phase 2: Foundational
- [X] T004 [P] Implement a basic packaging test in `tests/unit/test_packaging.py` to verify resource accessibility
- [X] T005 Verify local build integrity by running `uv build` and inspecting the wheel content

## Phase 3: User Story 1 - Automated Quality Assurance (Priority: P1)
**Goal**: Run all tests automatically on GitHub push/PR.
**Independent Test**: Push to a branch and verify the "Test" workflow status on GitHub.

- [X] T006 [US1] Create `.github/workflows/test.yml` with a matrix for Python 3.10, 3.11, and 3.12
- [X] T007 [US1] Configure `test.yml` to setup `uv`, `node`, and run `uv run pytest`
- [X] T008 [US1] Add a "Build Check" step to `test.yml` to ensure the package remains buildable

## Phase 4: User Story 2 - Automated Release to PyPI (Priority: P2)
**Goal**: Automatically publish to PyPI on version tagging.
**Independent Test**: Create a test tag and verify the "Publish" workflow triggers.

- [X] T009 [US2] Create `.github/workflows/publish.yml` with OIDC (Trusted Publishing) configuration
- [X] T010 [US2] Configure `publish.yml` to trigger on `v*` tags and execute `uv build` followed by publication

## Phase 5: User Story 3 - Robust Package Distribution (Priority: P3)
**Goal**: Ensure all necessary resources (Static UI, extension manifests, templates) are bundled.
**Independent Test**: Install the locally built wheel in a clean environment and run `spec-craft browse`.

- [X] T011 [US3] Verify that `src/spec_craft/static/` is present in the installed package
- [X] T012 [US3] Verify that the `extension/` directory and its contents are bundled in the distribution
- [X] T013 [US3] Run integration tests against the installed package to confirm resource resolution

## Phase 6: Polish
- [X] T014 Ensure `README.md` and documentation accurately reflect the new automated release process
- [X] T015 Final verification of all success criteria (SC-001 to SC-004) in the Phase 9 spec

## Dependencies
- US1 (QA) is foundational for US2 (Release).
- US3 (Distribution) depends on the `pyproject.toml` and `MANIFEST.in` updates in Phase 1.

## Parallel Execution Examples
- T004 (Packaging test) can be developed in parallel with GHA workflow setup (T006).
- T013 (Integration tests) can be run in parallel with polish tasks.
