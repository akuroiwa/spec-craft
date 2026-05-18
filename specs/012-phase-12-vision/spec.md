# Feature Specification: Vision Feedback and Isolated Editing Environment

**Feature Branch**: `012-phase-12-vision`  
**Created**: 2026-05-12  
**Status**: Draft  
**Input**: User description: "Phase 12: Vision Feedback and Isolated Editing Environment"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Visual Verification of 3D Assets (Priority: P1)

As a creator, I want the AI to visually verify the 3D models it generates in Blender so that I can ensure the architectural or artistic intent matches the strategy.

**Why this priority**: Closing the loop between script generation and visual outcome is critical for non-textual assets. SVG line art is high-fidelity and low-token for AI analysis.

**Independent Test**: Trigger a Blender render task; verify that an SVG file is generated containing the wireframe/contour of the 3D scene and that the AI can describe its basic proportions.

**Acceptance Scenarios**:

1. **Given** a 3D scene script, **When** the `render_blender_svg` tool is called, **Then** Blender runs headlessly with the Freestyle SVG Exporter enabled and saves an SVG to the build directory.
2. **Given** a generated SVG, **When** analyzed by the AI, **Then** the AI can identify spatial discrepancies (e.g., "the wall is missing") compared to the Obsidian spec.

---

### User Story 2 - High-Precision Code Editing (Priority: P2)

As an AI agent, I want to use a project-specific Emacs environment with LSP and Linting support so that I can write technically correct, idiomatically sound code for the project.

**Why this priority**: Improves implementation quality by using professional-grade validation tools (Eglot, Flymake) in a dedicated sandbox, preventing pollution of the user's global configuration.

**Independent Test**: Initialize the Emacs environment; verify that a local `init.el` is created and that the AI can perform a headless edit on a Python file via `emacsclient`.

**Acceptance Scenarios**:

1. **Given** no local Emacs config, **When** `setup_emacs` is called, **Then** a `.spec-craft/emacs/` directory is created with a pre-configured `init.el` supporting `python-ts-mode`.
2. **Given** a running Emacs daemon, **When** `edit_with_emacs` is called with Elisp commands, **Then** the target file is modified and saved without manual user intervention.

---

### User Story 3 - Comprehensive Prerequisite Checking (Priority: P3)

As a user, I want the toolkit to tell me if I'm missing Blender add-ons or NPM packages for the new features so that I can maintain a functional SDD environment.

**Why this priority**: Reduces friction when adopting new features like Freestyle rendering or JSCAD v2.

**Independent Test**: Run `check_environment` and verify it correctly lists "Freestyle SVG Exporter" and "@jscad/modeling" status.

**Acceptance Scenarios**:

1. **Given** Blender is installed but the SVG addon is disabled, **When** checking environment, **Then** the tool provides the command or link to enable/install it.

---

### Edge Cases

- **Emacs Daemon Conflict**: What if multiple projects use the same daemon name? (Requirement: Use unique socket names based on project path).
- **Blender Addon Absence**: What if the standard `render_freestyle_svg` is missing from the Blender installation? (Assumed: AI provides a link to download or repair the installation).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `BlenderDriver` MUST support injecting Python code to enable and configure the Freestyle SVG Exporter.
- **FR-002**: System MUST provide a `trigger_blender_render` tool to execute scripts headlessly and capture SVG output.
- **FR-003**: System MUST implement an `EmacsManager` to handle `emacs --daemon` lifecycle with `--init-directory`.
- **FR-004**: System MUST provide a default `init.el` template featuring `eglot`, `flymake`, and `python-ts-mode`.
- **FR-005**: `check_environment` MUST be updated to verify the presence of the Bonsai addon and JSCAD NPM packages.

### Key Entities *(include if feature involves data)*

- **SVG Projection**: A 2D representation of a 3D scene optimized for AI vision.
- **Emacs Sandbox**: A filesystem-isolated directory for editor configuration and ELPA packages.
- **LSP Session**: A language server protocol connection managed via Eglot within the sandbox.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of Blender renders produce a valid, viewable SVG file in `build/3d/`.
- **SC-002**: AI can perform a complex refactoring (e.g., rename class) via Emacs in under 5 seconds.
- **SC-003**: `check_environment` covers 100% of the new domain-specific dependencies.
- **SC-004**: Zero manual editing of the project's global `~/.emacs.d` occurs during AI operations.

## Assumptions

- **Emacs Version**: Assumes Emacs 29+ is available for `--init-directory` support (Fallback: use manual `HOME` redirection if older).
- **Python-ts-mode**: Assumes tree-sitter libraries are available on the host system.
- **Blender Version**: Assumes Blender 4.x which bundles the Freestyle SVG addon.
