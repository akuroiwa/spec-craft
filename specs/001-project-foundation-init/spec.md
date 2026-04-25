# Feature Specification: Project Foundation - Initialize Python Package and MCP Server Base

**Feature Branch**: `001-init-python-mcp-base`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 1: Project Foundation - Initialize Python Package and MCP Server Base"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Environment Setup (Priority: P1)

As a developer, I want to initialize a standard Python package structure and MCP server base so that I can start building SDD-specific tools.

**Why this priority**: This is the fundamental building block. Without a valid package structure and server base, no other features can be developed or tested.

**Independent Test**: Can be tested by running `pip install -e .` and verifying that the `spec-craft` command is available and the MCP server starts without errors.

**Acceptance Scenarios**:

1. **Given** a new project directory, **When** I run the initialization process, **Then** a standard Python project structure (src/spec_craft, tests, pyproject.toml) is created.
2. **Given** the project structure, **When** I run the `spec-craft` command, **Then** the FastMCP server starts and listens for connections.

---

### User Story 2 - Spec-Kit Integration Config (Priority: P2)

As a developer, I want the tool to automatically detect and prepare the integration with `spec-kit` so that my development workflow follows SDD principles from the start.

**Why this priority**: Ensuring the tool works seamlessly with `spec-kit` is a core requirement for the `spec-craft` philosophy.

**Independent Test**: Can be tested by verifying the existence and contents of `.specify/memory/constitution.md` and checking if `spec-kit` commands recognize the new project.

**Acceptance Scenarios**:

1. **Given** a workspace with `spec-kit` installed, **When** I initialize `spec-craft`, **Then** the `.specify/memory/constitution.md` is identified or prepared for SDD instructions.

---

### Edge Cases

- **Existing Files**: What happens when `pyproject.toml` or other project files already exist? (Assumed: Fail or prompt for backup).
- **Missing Prerequisites**: How does the system handle missing `fastmcp` or `git` dependencies? (Assumed: Clear error message specifying missing requirements).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST create a PEP 621 compliant `pyproject.toml` with dependencies for `fastmcp`, `gitpython`, and `pydantic`.
- **FR-002**: System MUST establish a `src/spec_craft` directory structure with an entry point for the CLI and MCP server.
- **FR-003**: System MUST provide a basic FastMCP server implementation that can be extended with tools and prompts.
- **FR-004**: System MUST include a `WorkspaceDetector` component to identify project roots, Git repositories, and `.specify` directories.
- **FR-005**: System MUST prepare a `ConstitutionManager` base for interacting with `.specify/memory/constitution.md`.

### Key Entities *(include if feature involves data)*

- **Workspace**: Represents the project directory, containing configuration, source code, and Obsidian files.
- **MCP Server Instance**: The running process that provides tools and prompts to the LLM client.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developer can install the package in "editable" mode in under 30 seconds.
- **SC-002**: The `spec-craft` CLI command responds with a version or help message in under 1 second.
- **SC-003**: The MCP server successfully initializes and reports its capabilities (tools/prompts) to a client.
- **SC-004**: 100% of the core package structure adheres to standard Python project layouts.

## Assumptions

- **Python Version**: Assumes Python 3.10 or higher is installed.
- **Spec-Kit Version**: Assumes compatibility with `spec-kit` version 0.8.x.
- **Operating System**: Initial support is focused on Linux/macOS as per user's environment.
- **Git**: Assumes the project is or will be a Git repository.
