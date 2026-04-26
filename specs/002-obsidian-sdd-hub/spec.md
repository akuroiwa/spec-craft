# Feature Specification: Obsidian-Driven SDD Hub - Storyboard Integration and Agent Management

**Feature Branch**: `002-obsidian-hub-storyboard`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 2: Obsidian-Driven SDD Hub - Storyboard Integration and Agent Management"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Storyboard Evolution (Priority: P1)

As a creator, I want the AI to read my Obsidian storyboards so that it can understand the long-term "strategy" and propose tactical "tasks" for specific scenes or chapters.

**Why this priority**: This fulfills the core vision of Obsidian as the "strategy" layer. It connects the roadmap to actionable SDD cycles.

**Independent Test**: Can be tested by providing a sample storyboard in `obsidian/storyboard.md` and verifying that the MCP tool can extract key elements (characters, plot points, scene requirements).

**Acceptance Scenarios**:

1. **Given** a storyboard file with YAML metadata and Markdown headers, **When** I ask the AI to analyze the current strategy, **Then** it accurately summarizes characters, settings, and pending chapters.
2. **Given** a specific chapter description in Obsidian, **When** I ask for the next step, **Then** the AI suggests a `/speckit.specify` command with a relevant title.

---

### User Story 2 - Domain-Specific Guidance (Priority: P2)

As a creator, I want the AI to have built-in knowledge of manga, video, and CAD principles so that I don't have to manually provide complex prompts for every task.

**Why this priority**: Encapsulating domain knowledge in-code (FastMCP Prompts) makes the tool "smarter" and easier to use.

**Independent Test**: Can be tested by invoking the MCP `Prompts` (e.g., `manga_storyboard_guide`, `cad_design_philosophy`) and verifying that the guidance follows the established rules (frame division, jscad logic, etc.).

**Acceptance Scenarios**:

1. **Given** a request to design a character, **When** the AI uses the internal `character_design` prompt, **Then** it asks for both visual attributes and personality traits as defined in the spec-craft philosophy.
2. **Given** a CAD-related task, **When** the AI references the `cad_logic` prompt, **Then** it applies principles derived from `gemini-jscad`.

---

### User Story 3 - Agent Capability Management (Priority: P3)

As a developer, I want the AI to detect missing capabilities and suggest relevant extensions so that the environment is always ready for the requested generation tasks.

**Why this priority**: Ensures that the "tactical" implementation (e.g., image generation via Nano Banana) is actually possible before starting a task.

**Independent Test**: Can be tested by simulating a missing extension (e.g., `nano-banana`) and verifying that the AI suggests the installation command.

**Acceptance Scenarios**:

1. **Given** a request for image generation, **When** the required extension is not found, **Then** the AI provides a clear instruction on how to install it (e.g., `gemini-cli extension install ...`).

---

### Edge Cases

- **Ambiguous Storyboard Structure**: What if the Obsidian file doesn't follow the expected format? (Assumed: AI provides a "best-effort" summary and suggests a template).
- **Extension Installation Failure**: What if the suggested installation fails? (Assumed: AI provides troubleshooting steps or alternative manual methods).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide an MCP tool to parse and summarize files in the `obsidian/` directory.
- **FR-002**: System MUST include internal FastMCP Prompts for "Strategy vs Tactics", "Manga Storyboarding", "Video Production", and "CAD Logic".
- **FR-003**: System MUST be able to check for the presence of specific `gemini-cli` extensions (e.g., by checking `.specify/extensions.yml` or running list commands).
- **FR-004**: System MUST update the project `README.md` to explain the "Strategy (Obsidian) vs Tactics (spec-kit)" relationship.
- **FR-005**: Storyboard parser MUST identify "Frame Division" (Manga), "Camera Work/Timing" (Video), and "Component Logic" (CAD).

### Key Entities *(include if feature involves data)*

- **Storyboard**: A structured Markdown file in Obsidian containing creative strategy.
- **Prompt Definition**: In-code instructions provided by the MCP server to the LLM.
- **Extension Status**: Information about which agent extensions are currently installed and enabled.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: AI can extract all YAML properties and top-level headers from an Obsidian file in under 2 seconds.
- **SC-002**: 100% of domain-specific prompts (Manga, Video, CAD) are accessible via the MCP server's `list_prompts` capability.
- **SC-003**: The AI successfully identifies at least one missing extension and provides the correct installation command when prompted for an unsupported generation task.
- **SC-004**: The Strategy/Tactics analogy is clearly visible in the `README.md` and referenced by the AI in conversations.

## Assumptions

- **Obsidian Structure**: Users will use standard Markdown features (headers, lists, YAML) to structure their creative strategy.
- **Agent Environment**: The user is using a tool that supports MCP (like `gemini-cli`) and its extension system.
- **CAD Knowledge**: The CAD-related prompts will be based on the established `gemini-jscad` repository patterns.
