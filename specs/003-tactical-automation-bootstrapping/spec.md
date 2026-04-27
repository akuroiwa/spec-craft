# Feature Specification: Tactical Automation and Constitutional Bootstrapping

**Feature Branch**: `003-tactical-automation-bootstrapping`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 3: Tactical Automation and Constitutional Bootstrapping"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Tactical Execution (Priority: P1)

As an AI agent, I want to execute spec-kit tactical commands (specify, plan, implement, etc.) directly via MCP tools so that the workflow becomes more fluid and automated for the user.

**Why this priority**: This bridges the gap between AI "thinking" (strategy) and actual project "doing" (tactics). It reduces manual copy-pasting of commands.

**Independent Test**: Can be tested by invoking the `execute_tactical_command` tool for a non-destructive command (like `check-prerequisites.sh`) and verifying the output.

**Acceptance Scenarios**:

1. **Given** a spec-kit project, **When** I trigger the `execute_tactical_command` tool for a valid script, **Then** the script is executed via a safe subprocess and the result is returned.
2. **Given** a request for a new feature, **When** the AI proposes a `/speckit.specify` command, **Then** the tool provides an option to execute the underlying script automatically.

---

### User Story 2 - Constitutional Bootstrap (Priority: P2)

As a developer starting a new project, I want the AI to automatically apply established "Craft Rules" (like multi-line commit procedures) to my constitution so that my project immediately follows best practices.

**Why this priority**: Ensures consistency and productivity across projects. It makes `spec-craft` a "force multiplier" for quality.

**Independent Test**: Can be tested by invoking the `bootstrap_constitution` prompt and verifying that it correctly formats the rules for injection.

**Acceptance Scenarios**:

1. **Given** a fresh project, **When** I ask the AI to "bootstrap my rules", **Then** the AI uses the internal `constitution-bootstrap` prompt to suggest standard SDD rules for the project's `constitution.md`.

---

### User Story 3 - Agent Extension Discovery (Priority: P3)

As a user of different AI agents (Claude, Copilot, Cursor), I want the AI to guide me to the correct extension installation path so that I can easily expand my agent's capabilities.

**Why this priority**: Improves accessibility and setup speed for users in different ecosystems.

**Independent Test**: Can be tested by asking for help with "Claude Code extensions" and verifying that the AI points to `.claude/commands/`.

**Acceptance Scenarios**:

1. **Given** an unsupported generation request, **When** the AI suggests an extension, **Then** it tailors the instructions based on the user's active agent (detected or asked).

---

### Edge Cases

- **Script Permission Errors**: What if the bash scripts are not executable? (Assumed: Tool attempts `chmod +x` or reports error).
- **Agent Detection**: How to know which agent is active? (Assumed: AI asks the user or checks common environment variables/directories).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide an MCP tool `execute_tactical_script` that runs files from `.specify/scripts/bash/`.
- **FR-002**: System MUST include an internal FastMCP Prompt `bootstrap_constitution` containing multi-line commit rules and SDD lifecycle guidelines.
- **FR-003**: System MUST include an internal FastMCP Prompt `agent_extension_guide` with a directory mapping for Copilot, Claude, Gemini, Cursor, and Windsurf.
- **FR-004**: `execute_tactical_script` MUST capture stdout/stderr and return them to the LLM.
- **FR-005**: System MUST validate that requested scripts exist within the `.specify` directory before execution.

### Key Entities *(include if feature involves data)*

- **Tactical Script**: A bash script in `.specify/scripts/bash/` that implements a spec-kit command.
- **Bootstrap Rules**: A collection of high-quality SDD principles stored in-code.
- **Agent Profiles**: Metadata mapping agent names to their extension directories.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The `execute_tactical_script` tool completes execution of basic check scripts in under 3 seconds.
- **SC-002**: AI can correctly identify and suggest the extension directory for at least 5 different agents.
- **SC-003**: The `bootstrap_constitution` prompt can be rendered and applied to a file in a single conversation turn.
- **SC-004**: 100% of tactical script executions are logged for debuggability.

## Assumptions

- **Environment**: Assumes a Unix-like environment where bash scripts can run.
- **Script Availability**: Assumes the project was initialized with `spec-kit` and contains the standard `.specify` scripts.
- **User Permission**: The user has granted permission for the AI to run shell commands via MCP.
