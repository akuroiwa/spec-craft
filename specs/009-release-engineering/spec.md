# Feature Specification: Release Engineering - CI/CD and PyPI Publication

**Feature Branch**: `009-release-eng-cicd-pypi`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 9: Release Engineering - CI/CD and PyPI Publication"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Automated Quality Assurance (Priority: P1)

As a developer, I want all tests to run automatically when I push changes to GitHub so that I can ensure the technical integrity of the toolkit and prevent regressions.

**Why this priority**: Continuous testing is the foundation of reliable software. It ensures that every commit maintains the standards defined in the project constitution.

**Independent Test**: Can be tested by pushing a commit to a branch and verifying that the GitHub Actions "Test" workflow triggers and completes successfully.

**Acceptance Scenarios**:

1. **Given** a pull request or push to `main`, **When** the code is uploaded to GitHub, **Then** a GitHub Action runs `uv run pytest` across multiple Python versions (3.10, 3.11, 3.12).
2. **Given** a failing test, **When** the CI workflow runs, **Then** the build fails and notifies the developer.

---

### User Story 2 - Automated Release to PyPI (Priority: P2)

As a maintainer, I want the package to be automatically published to PyPI when I create a new version tag so that users can easily install the latest stable version of Spec-Craft.

**Why this priority**: Simplifies the distribution process and ensures that the version on PyPI always matches the official releases in the repository.

**Independent Test**: Can be tested by creating a GitHub Release (or tag) and verifying that the "Publish" workflow uploads the distribution to PyPI (or TestPyPI).

**Acceptance Scenarios**:

1. **Given** a new tag (e.g., `v0.1.0`), **When** the tag is pushed to GitHub, **Then** a GitHub Action builds the wheel/sdist and uploads them to PyPI using trusted publishing.

---

### User Story 3 - Robust Package Distribution (Priority: P3)

As a user, I want the installed package to include all necessary resources (static UI, extension manifests) so that the tool functions correctly immediately after `pip install`.

**Why this priority**: Ensures that the package is self-contained. Missing assets (like the Three.js viewer or extension YAML) would break core functionality.

**Independent Test**: Can be tested by building the package locally (`uv build`) and inspecting the resulting wheel for the presence of `src/spec_craft/static/` and `extension/` files.

**Acceptance Scenarios**:

1. **Given** the `pyproject.toml` configuration, **When** the package is built, **Then** the `spec_craft/static/` and `extension/` directories are included in the distribution metadata.

---

### Edge Cases

- **Environment Mismatches**: What if the CI environment lacks `npx` or `node` for CAD tests? (Assumed: CI environment includes Node.js setup).
- **Broken Manifest**: What if the `extension.yml` is invalid? (Assumed: Package build includes a validation step for the manifest).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST include a GitHub Actions workflow `.github/workflows/test.yml` for automated testing.
- **FR-002**: System MUST include a GitHub Actions workflow `.github/workflows/publish.yml` for PyPI distribution.
- **FR-003**: `pyproject.toml` MUST be updated to include all non-Python data files (static resources and extension manifests).
- **FR-004**: The release process MUST automate version extraction from the package or tag.
- **FR-005**: CI MUST verify that all 29+ existing tests pass in a clean environment.

### Key Entities *(include if feature involves data)*

- **GitHub Workflow**: Automation definition for testing and deployment.
- **PyPI Distribution**: The wheel and source distribution files.
- **Trusted Publisher**: OpenID Connect (OIDC) configuration between GitHub and PyPI.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: CI pipeline completes the full test suite in under 3 minutes.
- **SC-002**: Automated publishing successfully uploads to PyPI within 5 minutes of tag creation.
- **SC-003**: 100% of non-code assets (JS, HTML, YAML) are present in the final `.whl` file.
- **SC-004**: Zero manual steps are required for release beyond tagging and pushing.

## Assumptions

- **PyPI Access**: Assumes the user has a PyPI account and has configured Trusted Publishing for the `spec-craft` project.
- **Node.js in CI**: Assumes the `actions/setup-node` action will be used to provide the environment for CAD-related checks.
- **GitHub Permissions**: Assumes the repository is hosted on GitHub and the maintenance tokens have appropriate permissions.
