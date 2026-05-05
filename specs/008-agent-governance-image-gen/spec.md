# Feature Specification: Agent Governance and Image Generation Workflow

**Feature Branch**: `008-phase-8-agent`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 8: Agent Governance and Image Generation Workflow"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Advanced Extension Discovery (Priority: P1)

As a user, I want the AI to guide me to the official extension directory so that I can find the latest generative tools for my agent.

**Why this priority**: Ensures users have access to the most up-to-date extensions, which is critical for the evolving AI ecosystem.

**Independent Test**: Can be tested by invoking the `agent_extension_guide` prompt and verifying that it includes the link to `https://geminicli.com/extensions/` and clear search instructions.

**Acceptance Scenarios**:

1. **Given** a request for new capabilities, **When** the AI renders the extension guide, **Then** it provides a link to the official registry and agent-specific search tips.

---

### User Story 2 - Generative Workflow Integration (Priority: P2)

As a creator, I want the AI to use installed generative extensions (like Nano Banana) to generate images based on my Obsidian storyboards so that I can see my strategy come to life.

**Why this priority**: Fulfills the "Strategic to Asset" vision for non-code artifacts like manga scenes or concept art.

**Independent Test**: Can be tested by providing an Obsidian scene description and triggering an image generation task, then verifying the output is saved in `build/manga/`.

**Acceptance Scenarios**:

1. **Given** an Obsidian storyboard with visual descriptions, **When** the AI triggers the image generation workflow, **Then** it uses the appropriate extension to create an image and organizes it via the Build Manager.

---

### User Story 3 - Proactive Capability Detection (Priority: P3)

As a developer, I want the AI to proactively check if required generative tools are installed before starting a creative task so that I avoid workflow interruptions.

**Why this priority**: Improves user experience by identifying environmental gaps early in the SDD cycle.

**Independent Test**: Can be tested by asking the AI to "Generate a manga scene" in an environment without the required extension and verifying it suggests the specific installation command before proceeding.

**Acceptance Scenarios**:

1. **Given** a generation request, **When** the system detects a missing capability, **Then** the AI halts and provides precise installation instructions for the current agent.

---

### Edge Cases

- **Multiple Extensions for One Task**: What if multiple extensions provide image generation? (Assumed: AI suggests the most popular one or asks the user for preference).
- **Extension Registry Offline**: What if the external URL is unreachable? (Assumed: AI falls back to the in-code static mapping).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST update the `agent_extension_guide` prompt to include the URL `https://geminicli.com/extensions/`.
- **FR-002**: System MUST define a standard "Generative Asset Workflow" in MCP prompts (Manga -> Image, Music -> MIDI/MP3).
- **FR-003**: System MUST provide a mechanism to check for specific "Generative Capabilities" (e.g., searching for `nanobanana` in registered commands).
- **FR-004**: System MUST include a `generative_workflow_guide` prompt that explains how to transition from Obsidian storyboard to asset generation.
- **FR-005**: AI MUST provide specific installation instructions for Gemini CLI, Claude, and Copilot generative extensions.

### Key Entities *(include if feature involves data)*

- **Extension Registry**: An external resource for discovering agent tools.
- **Generative Capability**: A tag or command signature that identifies an extension as a creator of images, music, or video.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of generative prompts correctly reference the official extension registry.
- **SC-002**: AI can successfully identify a missing generative extension and suggest the `gemini-cli extension install` command in under 2 seconds.
- **SC-003**: The manual build process for a generative asset (storyboard to image) is documented in under 3 turns.
- **SC-004**: Generated assets are correctly placed in hierarchical `build/` directories 100% of the time.

## Assumptions

- **Extension Availability**: Assumes that extensions like `nano-banana` exist and follow the command patterns identified in the research phase.
- **User Environment**: Assumes the user is using an agent that supports external extensions (e.g., `gemini-cli`).
- **Vision Integration**: Assumes the AI can analyze the generated assets once the extensions are installed.
