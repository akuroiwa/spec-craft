# Research: Workflow Reliability & Tactical Knowledge

## Decisions

### 1. Removing `execute_tactical_script`
- **Decision**: Completely remove the `execute_tactical_script` tool from `src/spec_craft/mcp/server.py`.
- **Rationale**: This tool uses a hidden pipe that blocks interactive prompts (SSH, git confirmations), leading to terminal feedback loops and hangs.
- **Alternatives**: Trying to use PTY (rejected as overly complex and fragile).

### 2. Bootstrapping Tactical Knowledge via TOML
- **Decision**: Add a `boot_tactical_knowledge` prompt that instructs AI to read the command path (e.g., `.gemini/commands/`).
- **Rationale**: Allows the AI to understand the *logic* of the tactical commands and suggest the correct *shell commands* to the user, ensuring a transparent and interactive execution flow.
- **Alternatives**: Hardcoding command paths (rejected as not portable).

### 3. Agent-Aware Workspace Analysis
- **Decision**: Update `analyze_workspace` to return the `agent_command_path` (e.g., `.gemini/commands/`).
- **Rationale**: Provides the AI with the starting point for tactical discovery.

## Best Practices
- **Prompt Clarity**: Use clear "Given/When/Then" scenarios in the new prompt to guide the AI's tactical suggestions.
- **Security**: Always prefer `run_shell_command` with user visibility for potentially destructive tactical operations.
