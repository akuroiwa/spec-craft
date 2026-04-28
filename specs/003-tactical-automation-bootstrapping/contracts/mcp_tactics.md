# MCP Contract: Tactical Automation & Strategic Setup

## Tools

### `execute_tactical_script`
- **Purpose**: Run a spec-kit script from `.specify/scripts/bash/`.
- **Input**: 
    - `script_name`: String (e.g., "check-prerequisites.sh")
    - `arguments`: List of strings
- **Output**: JSON containing `stdout`, `stderr`, and `exit_code`.

## Prompts

### `bootstrap_constitution`
- **Role**: Provides a curated list of SDD rules for new projects.
- **Rules included**:
    - Git Commit Procedure (Section VIII - TBD)
    - Branch Lifecycle (Section VI)
    - In-Code Prompt Principles (Section VII)

### `agent_extension_guide`
- **Role**: Shows where to install extensions for specific agents.
- **Input**: `agent_name` (optional)
- **Output**: Agent-specific directory information.
