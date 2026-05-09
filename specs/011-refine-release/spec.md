# Feature Specification: Final Refinement of JSCAD/Bonsai Drivers and Release Preparation

**Feature Branch**: `011-refine-jscad-bonsai`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 11: Final Refinement of JSCAD/Bonsai Drivers and Release Preparation"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Reliable JSCAD/Bonsai Builds (Priority: P1)

As a creator, I want the JSCAD and Bonsai drivers to generate correct code and assets so that I can trust the tactical output matches my strategic design.

**Why this priority**: Core functionality must be correct before release. Previous tests showed import errors in JSCAD and logical mix-ups in Bonsai.

**Independent Test**: Trigger a CAD build and a Bonsai script generation; verify that the resulting files have correct imports (`booleans` in JSCAD, `bonsai` operators in Blender) and produce valid artifacts.

**Acceptance Scenarios**:

1. **Given** a CAD spec, **When** I trigger a build, **Then** both STL and SVG are generated correctly using `npx @jscad/cli`.
2. **Given** a Bonsai spec, **When** I trigger a build, **Then** a Python script using `bpy.ops.bim` and `import bonsai` is generated.

---

### User Story 2 - Complete Japanese Manual (Priority: P2)

As a Japanese user, I want the entire manual to be available in my native language so that I can use the tool effectively.

**Why this priority**: Essential for the user's primary environment and overall accessibility.

**Independent Test**: Run the Sphinx build and verify that all pages (Installation, Strategy, Domain Guides) are fully translated in the Japanese version.

**Acceptance Scenarios**:

1. **Given** the PO files, **When** I run the build, **Then** all sections previously left in English are now in Japanese, while preserving technical code blocks.

---

### User Story 3 - Staging Release on Test PyPI (Priority: P3)

As a maintainer, I want to verify the entire distribution process on Test PyPI so that I can ensure the package is correctly formed and installable before the public release.

**Why this priority**: Final safety check to prevent broken releases on main PyPI.

**Independent Test**: Successfully upload the package to Test PyPI and install it in a fresh virtual environment, then run a smoke test.

**Acceptance Scenarios**:

1. **Given** a built distribution, **When** I upload to Test PyPI, **Then** the package is accepted and can be installed via `pip`.

---

### Edge Cases

- **Missing Bonsai Add-on**: What if the environment checker detects Blender but not the Bonsai add-on? (Assumed: AI provides the download link for the Bonsai add-on).
- **Test PyPI Name Conflict**: What if the name `spec-craft` is taken on Test PyPI? (Assumed: Use a temporary suffix if necessary for testing).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST update `CADDriver` to ensure sequential or parallel execution for multiple formats (STL+SVG).
- **FR-002**: `BonsaiDriver` MUST be updated to use the correct `bonsai` module names and operators identified in research.
- **FR-003**: `check_environment` MUST be updated to detect the Bonsai Blender add-on and `@jscad` npm packages.
- **FR-004**: System MUST complete all Japanese translations in `.po` files.
- **FR-005**: System MUST provide a release automation check specifically for Test PyPI.

### Key Entities *(include if feature involves data)*

- **Final Manual**: The completed multi-language Sphinx documentation.
- **Staging Package**: The distribution uploaded to Test PyPI.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of JSCAD builds generate both STL and SVG without manual intervention.
- **SC-002**: 100% of the manual pages are localized (JA) with no missing segments.
- **SC-003**: Environment check identifies missing Bonsai/JSCAD dependencies 100% of the time.
- **SC-004**: Package installs and starts the MCP server in under 60 seconds from Test PyPI.

## Assumptions

- **Credentials**: Assumes Test PyPI tokens are configured or Trusted Publishing is enabled.
- **Node.js**: Assumes `npx` is available for build verification.
