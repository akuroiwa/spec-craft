# Feature Specification: Multilingual SVG Pipeline and Multi-domain Build Integration

**Feature Branch**: `004-multilingual-svg-pipeline`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 4: Multilingual SVG Pipeline and Multi-domain Build Integration"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Multilingual SVG Generation (Priority: P1)

As a creator, I want to define character dialogue or labels in Obsidian so that they are automatically injected into SVG templates and output to language-specific directories.

**Why this priority**: This fulfills the requirement for multi-language support in assets (Manga, diagrams) and demonstrates the "Strategic" control over "Tactical" builds.

**Independent Test**: Can be tested by providing an SVG template with placeholders (e.g., `{{dialogue}}`) and a dictionary file in `obsidian/ja/scene1.md`, then verifying the generated SVG in `build/ja/scene1.svg`.

**Acceptance Scenarios**:

1. **Given** an SVG template and a Markdown file with translation properties, **When** I trigger the `build_svg` tool, **Then** a new SVG is created with the translated text in the correct `build/<lang>/` subdirectory.
2. **Given** multiple languages (ja, en), **When** the build is executed, **Then** separate versions for each language are generated simultaneously.

---

### User Story 2 - Parametric CAD Generation (Priority: P2)

As an engineer, I want the AI to generate parametric CAD models based on my strategic requirements in Obsidian so that I can iteratively refine designs.

**Why this priority**: Integrates the `gemini-jscad` expertise into the `spec-craft` pipeline, expanding the tool beyond 2D assets.

**Independent Test**: Can be tested by asking the AI to "Build the motor mount from my CAD spec" and verifying that a `.js` and `.stl` file are created in `build/cad/`.

**Acceptance Scenarios**:

1. **Given** a CAD specification in Obsidian, **When** I trigger the `build_cad` tool, **Then** the AI generates valid JSCAD code and converts it to STL.

---

### User Story 3 - Build Management (Priority: P3)

As a developer, I want the build directory to be automatically organized by domain and language so that I can easily find and manage my project's output.

**Why this priority**: Ensures that the tool scales as the project grows and maintains a clean workspace.

**Independent Test**: Can be tested by running multiple builds and verifying the structure of the `build/` directory.

**Acceptance Scenarios**:

1. **Given** multiple generation tasks, **When** the builds complete, **Then** the files are placed in `build/manga/<lang>/`, `build/cad/`, etc.

---

### Edge Cases

- **Missing Font Support**: What if the SVG font is not available on the system during text injection? (Assumed: Fallback to standard web fonts).
- **Invalid JSCAD Syntax**: What if the generated JSCAD code is broken? (Assumed: AI reports the error and suggests a fix).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST implement a `BuildManager` to coordinate output to the `build/` directory.
- **FR-002**: System MUST provide an `SVGDriver` capable of parsing SVG XML and substituting text elements based on ID or placeholder patterns.
- **FR-003**: System MUST provide a `CADDriver` that integrates with `jscad-tool.js` (or equivalent) to generate STL files.
- **FR-004**: System MUST support hierarchical directory structures in `build/` based on language (e.g., `build/ja/`, `build/en/`).
- **FR-005**: System MUST provide MCP tools `trigger_svg_build` and `trigger_cad_build`.

### Key Entities *(include if feature involves data)*

- **SVG Template**: A base SVG file with defined text containers or IDs.
- **Dictionary**: Key-value pairs extracted from Obsidian Markdown files for text replacement.
- **Build Result**: Metadata about the generated asset (path, timestamp, status).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: SVG text replacement takes less than 500ms per file.
- **SC-002**: 100% of CAD builds successfully generate both a source `.js` and a target `.stl`.
- **SC-003**: The `build/` directory structure matches the domain/language mapping defined in the spec.
- **SC-004**: All generated assets are properly tracked in the build metadata.

## Assumptions

- **SVG Formats**: Assumes standard SVG 1.1 or 2.0.
- **JSCAD**: Assumes the availability of `node` and the `jscad-tool.js` wrapper in the user's environment.
- **Obsidian Source**: Assumes translation dictionaries are stored in predictable Markdown locations (e.g., frontmatter or specific headers).
