# Research: Project Foundation

## Decisions

### 1. FastMCP and GitPython Integration
- **Decision**: Use a dedicated `WorkspaceDetector` class to wrap GitPython logic for identifying project roots and status.
- **Rationale**: Keeps MCP tool logic clean and decouples repository state management from the server interface.
- **Alternatives**: Direct shell calls to `git` (rejected due to overhead and parsing complexity).

### 2. Package Structure (CLI + MCP)
- **Decision**: Use `src/spec_craft/main.py` as the unified entry point. Use `argparse` or `click` for CLI, and provide a subcommand to start the MCP server.
- **Rationale**: Common pattern for modern Python tools. Simplifies installation and usage.
- **Alternatives**: Separate entry points (too complex for initial phase).

### 3. Verification of "Editable" Mode
- **Decision**: Use `pip install -e .` followed by `spec-craft --version` in a temporary virtual environment for CI/CD or manual validation.
- **Rationale**: Standard way to verify package metadata and entry point availability.

## Best Practices
- **PEP 621**: Use `[project]` table in `pyproject.toml`.
- **FastMCP**: Use Pydantic models for tool inputs to ensure type safety.
- **GitPython**: Always use `Repo(search_parent_directories=True)` for robustness.
