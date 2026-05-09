# Feature Specification: Bonsai (BlenderBIM) Integration and Setup Automation

**Feature Branch**: `010-integrate-bonsai-blenderbim`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 10: Bonsai (BlenderBIM) Integration and Setup Automation"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Architectural Design with Bonsai (Priority: P1)

As an architect using Blender, I want the AI to support Bonsai (BlenderBIM) workflows so that I can use Spec-Craft to manage architectural strategies and tactical implementations within an IFC-compliant environment.

**Why this priority**: Expands Spec-Craft into the architectural domain, leveraging Blender's professional BIM capabilities.

**Independent Test**: Can be tested by invoking the `bonsai_architectural_guide` prompt and verifying that it provides IFC-compliant object placement and attribute management logic.

**Acceptance Scenarios**:

1. **Given** an architectural strategy in Obsidian, **When** I trigger the Blender build, **Then** the system generates Python code that utilizes Bonsai (BlenderBIM) APIs to create walls, windows, or doors.
2. **Given** a request for BIM data, **When** the AI renders the Bonsai guide, **Then** it explains how to maintain IFC consistency between the Obsidian spec and the Blender scene.

---

### User Story 2 - Proactive Setup Automation (Priority: P2)

As a new user, I want the system to detect if Spec-Kit or Obsidian is missing and offer to install them so that I can set up my SDD environment with minimal friction.

**Why this priority**: Lowers the barrier to entry and ensures the tool's prerequisites are met before the user encounters errors.

**Independent Test**: Can be tested by running `check_environment` on a clean system and verifying that it provides the correct installation commands for Spec-Kit and links to Obsidian.

**Acceptance Scenarios**:

1. **Given** a missing Spec-Kit installation, **When** I start Spec-Craft, **Then** the system detects the absence and provides the `pip install spec-kit` command.
2. **Given** a missing Obsidian directory, **When** I run the workspace analysis, **Then** the AI suggests creating an `obsidian/` folder and explains its strategic importance.

---

### User Story 3 - Production Readiness Validation (Priority: P3)

As a developer, I want to verify the image generation and JSCAD pipelines in a real-world scenario so that I can ensure the tool is ready for its first release on Test PyPI.

**Why this priority**: Critical for quality assurance before public distribution. Verifies that all previous integrations (Phase 4, 7, 8) work together seamlessly.

**Independent Test**: Can be tested by running the "Test Release" task suite which includes image generation, STL export, and multi-language manual generation.

**Acceptance Scenarios**:

1. **Given** the full toolkit, **When** I perform a "Mock Release", **Then** the system successfully produces a translated manual, a CAD model, and a generative image.

---

### Edge Cases

- **Bonsai API Changes**: How does the system handle the transition from BlenderBIM to Bonsai? (Assumed: AI provides guidance based on the latest stable Bonsai release).
- **Unsupported OS for npx**: What if `npx` is not available for CAD builds? (Assumed: Setup automation provides instructions for installing Node.js/npx).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide an internal FastMCP Prompt `bonsai_architectural_guide` for IFC-based modeling in Blender.
- **FR-002**: System MUST implement a `check_environment` tool that detects `spec-kit`, `obsidian`, and `node/npx`.
- **FR-003**: `trigger_full_build` MUST be extended to include architectural (Bonsai) assets.
- **FR-004**: System MUST provide a Test PyPI publication task definition in the release guide.
- **FR-005**: All manual translations (Japanese) MUST be completed and verified for accuracy.

### Key Entities *(include if feature involves data)*

- **Bonsai Scene**: A 3D environment using the IFC (Industry Foundation Classes) standard within Blender.
- **Environment Status**: A checklist of installed prerequisites (`spec-kit`, `uv`, `node`, `blender`).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: AI can generate at least 3 types of IFC entities (Wall, Slab, Opening) via the Bonsai guide.
- **SC-002**: Environment check completes in under 1 second and identifies 100% of missing prerequisites.
- **SC-003**: 100% of the manual's core sections are professionally translated into Japanese.
- **SC-004**: The package is successfully uploaded to Test PyPI and installable in a clean virtual environment.

## Assumptions

- **Blender Add-ons**: Assumes the user has the Bonsai (BlenderBIM) add-on installed in Blender.
- **Test PyPI Access**: Assumes the maintainer has the necessary credentials for the `testpypi` repository.
- **Vision Support**: Assumes the AI can analyze the spatial logic of architectural projections.
