# Research: Tactical Automation & Constitutional Bootstrapping

## Decisions

### 1. Tactical Command Execution
- **Decision**: Use Python's `subprocess.run` to execute scripts in `.specify/scripts/bash/`.
- **Rationale**: Direct execution is required for automation. Capturing stdout/stderr allows the AI to react to success or failure.
- **Alternatives**: Providing command strings only (rejected as it doesn't fulfill the "automation" goal).

### 2. Constitutional Bootstrap Rules
- **Decision**: Define a standard set of SDD rules (Section VI, VII, Git Commit Procedure) as constants in `src/spec_craft/mcp/prompts.py`.
- **Rationale**: Consistent with the "In-Code Prompt Definition" principle. Makes the rules portable and easy to inject.
- **Alternatives**: Reading from a local template file (rejected to maintain tool self-containment).

### 3. Agent Extension Mapping
- **Decision**: Use a static mapping of popular AI agents to their extension directories based on research findings.
- **Rationale**: Provides immediate value for the most common tools (Copilot, Claude, Gemini, Cursor).
- **Alternatives**: Dynamic discovery (rejected as it is complex and unreliable across different OS/installations).

## Best Practices
- **Security**: Validate script paths to prevent arbitrary code execution outside the `.specify` directory.
- **User UX**: Always summarize the output of executed scripts, especially if they are long or verbose.
- **Atomicity**: Ensure bootstrapping rules are injected as a coherent block to prevent partial configuration.
