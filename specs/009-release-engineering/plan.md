# Implementation Plan: Release Engineering - CI/CD and PyPI Publication

**Branch**: `009-release-eng-cicd-pypi` | **Date**: 2026-04-25 | **Spec**: [specs/009-release-engineering/spec.md](spec.md)
**Input**: Feature specification from `/specs/009-release-engineering/spec.md`

## Summary
Establish a professional CI/CD pipeline using GitHub Actions to automate testing and PyPI publication. Refine the `pyproject.toml` configuration to ensure all static assets and extension manifests are correctly bundled in the distribution.

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: `uv`, `pytest`, `astral-sh/setup-uv`, `pypa/gh-action-pypi-publish`  
**CI/CD Platform**: GitHub Actions  
**Publication Strategy**: Trusted Publishing (OIDC)  
**Performance Goals**: CI workflow < 3 minutes.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **III. Test-First Implementation**: OK. CI pipeline automates all existing and future tests.
- **V. Package Management with uv**: OK. Workflows are built around `uv` for speed and consistency.
- **VII. In-Code Prompt Definition**: OK. All prompts remain in-code, ensuring a self-contained package.

## Project Structure

### Documentation (this feature)

```text
specs/009-release-engineering/
├── plan.md              # This file
├── research.md          # GHA and OIDC research
├── data-model.md        # Workflow and Distribution entities
├── quickstart.md        # Release guide
├── contracts/
│   └── workflows.md     # CI/CD workflow contracts
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
.github/
└── workflows/
    ├── test.yml         # Matrix testing on PR/Push
    └── publish.yml      # PyPI publishing on Tag/Release
pyproject.toml           # Updated to include [tool.setuptools.package-data]
MANIFEST.in              # Explicit asset inclusion
```

**Structure Decision**: Standard GitHub Actions and Python packaging layout.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
