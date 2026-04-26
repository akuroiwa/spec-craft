# Research: Obsidian Hub & Storyboard Integration

## Decisions

### 1. YAML Frontmatter Parsing
- **Decision**: Use `PyYAML` to parse the frontmatter block of Obsidian Markdown files.
- **Rationale**: Robust, handles complex YAML structures, and is already a common dependency in the Python ecosystem.
- **Alternatives**: Manual regex-based parsing (rejected as it is error-prone for nested YAML).

### 2. Extension Detection
- **Decision**: Check for the existence of `.specify/extensions.yml` and use `subprocess` to run `gemini-cli extension list` if available.
- **Rationale**: `extensions.yml` provides a static check, while running the command provides a dynamic check of the current environment.
- **Alternatives**: Only checking `extensions.yml` (rejected as it might be out of sync with actual installations).

### 3. Prompt Structuring in FastMCP
- **Decision**: Create a `spec_craft.mcp.prompts` module to house all domain-specific guidance as Python strings or Pydantic models.
- **Rationale**: Keeps the `server.py` clean while fulfilling the "In-Code Prompt Definition" requirement from the constitution.
- **Alternatives**: Inline strings in `server.py` (rejected due to maintainability concerns as the number of domains grows).

## Best Practices
- **Obsidian**: Follow standard Markdown parsing rules. Treat YAML frontmatter as a distinct metadata entity.
- **MCP Prompts**: Use clear, descriptive names for prompts (e.g., `sdd-strategy-tactics`) and provide examples within the prompt text.
- **CAD Logic**: Base the CAD prompt on `jscad` best practices: modularity, parameterization, and geometric primitives.
