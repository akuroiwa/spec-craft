# Feature Specification: Workflow Reliability Refinement

**Feature Branch**: `013-workflow-reliability`  
**Created**: 2026-05-12  
**Status**: Draft  
**Input**: User description: "Phase 13: Workflow Reliability Refinement"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Secure Tactical Execution (Priority: P1)

As an AI agent, I want to perform tactical tasks (spec, plan, etc.) by suggesting slash commands or direct scripts to the user instead of executing them in a hidden pipe, so that I can handle interactive events like SSH password prompts.

**Why this priority**: Prevents terminal feedback loops and allows for secure authentication that only the human user can provide.

**Independent Test**: AI proposes a `/speckit.plan` or `bash setup-plan.sh` command; user executes it in their terminal and confirms it works without hanging.

**Acceptance Scenarios**:

1. **Given** a repository with SSH connection, **When** I need to create a feature branch, **Then** I present the command to the user instead of running it internally via a non-interactive pipe.
2. **Given** a tactical script needing user confirmation, **When** proposed to the user, **Then** the user can intervene and provide input.

---

### User Story 2 - Automated Tactical Knowledge (Priority: P2)

As an AI agent, I want to automatically discover and read the `spec-kit` command definitions (TOML files) for the project so that I know exactly how to execute tactical tasks for any supported agent.

**Why this priority**: Eliminates hardcoded implementation details and allows `spec-craft` to adapt to any AI agent's command structure.

**Independent Test**: AI reads `.gemini/commands/*.toml` and correctly describes the steps for `/speckit.tasks`.

**Acceptance Scenarios**:

1. **Given** a `.gemini/commands` directory, **When** a task starts, **Then** I read the relevant TOML and follow its logic to generate the implementation.

---

### User Story 3 - Clean Resource Cleanup (Priority: P3)

As a maintainer, I want redundant or problematic tools like `execute_tactical_script` to be removed so that the toolkit is streamlined and less prone to errors.

**Why this priority**: Simplifies the codebase and prevents the AI from choosing the wrong "hidden" tool for important tasks.

---

### Edge Cases

- **Missing TOML**: What if the agent's command directory doesn't exist? (Requirement: Fallback to suggesting standard shell scripts).
- **Unsupported Agent**: AI must ask the user where commands are stored if not in a standard path.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST remove the `execute_tactical_script` tool from the MCP server.
- **FR-002**: System MUST add a `boot_tactical_knowledge` prompt to guide the AI to read TOML files.
- **FR-003**: System MUST update the `analyze_workspace` tool to include the detected agent command directory.
- **FR-004**: AI MUST prioritize "suggesting commands" over "hidden internal execution" for interactive tactical tasks.

### Key Entities *(include if feature involves data)*

- **Tactical Definition**: The TOML file containing command logic (e.g., `speckit.plan.toml`).
- **Agent Command Path**: Path to the agent-specific definitions (e.g., `.gemini/commands/`).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 0 hidden terminal feedback loops caused by SSH/interactive prompts.
- **SC-002**: AI correctly identifies and reads 100% of the TOML files in the command path.
- **SC-003**: AI suggests the correct `spec-kit` script for at least 5 major tactical commands.

## Assumptions

- **Agent Identity**: Assumes the user is using `gemini-cli` or similar that uses standard command definitions.
- **Access**: AI has read access to the project root and hidden directories like `.gemini/`.
