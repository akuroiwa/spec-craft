# Data Model: Obsidian Hub & Agent Management

## Entities

### Storyboard
A strategic roadmap parsed from Obsidian.
- `file_path`: Path (Absolute path to the .md file)
- `metadata`: Dictionary (Parsed YAML frontmatter)
- `sections`: List of Section objects (Headers and their content)

### Section
A part of a Storyboard.
- `title`: String (Header name)
- `level`: Integer (Header level, e.g., 1 for #)
- `content`: String (Text under the header)

### ExtensionInfo
Information about an agent extension.
- `name`: String (e.g., "nano-banana")
- `is_installed`: Boolean
- `install_command`: String (Command to install if missing)

### DomainPrompt
Encapsulated domain knowledge.
- `domain`: String (e.g., "manga", "cad")
- `content`: String (The prompt text)

## Relationships
- A `Storyboard` consists of multiple `Section`s.
- `spec-craft` uses `ExtensionInfo` to suggest environment updates.
- `spec-craft` provides `DomainPrompt`s to the LLM via MCP.
