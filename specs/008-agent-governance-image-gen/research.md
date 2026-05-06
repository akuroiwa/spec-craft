# Research: Agent Governance & Generative Workflows

## Decisions

### 1. Extension Registry Reference
- **Decision**: Update the `agent_extension_guide` prompt to explicitly link to `https://geminicli.com/extensions/`.
- **Rationale**: Provides a single source of truth for the user and keeps the AI's guidance synchronized with the official community repository.
- **Alternatives**: Inlining the entire directory (rejected due to maintenance overhead).

### 2. Proactive Capability Detection
- **Decision**: Implement a `CapabilityChecker` class that scans the MCP server's internal tool/prompt registry and checks `.specify/extensions.yml`.
- **Rationale**: Allows the AI to "know what it can do" before attempting a task, preventing runtime errors and improving UX.
- **Alternatives**: Try-except based execution (rejected as it is less helpful to the user).

### 3. Generative Workflow Sequence
- **Decision**: Define a three-step sequence in the `generative_workflow_guide`: 
    1. **Strategic Spec**: Analyze Obsidian roadmap.
    2. **Tactics Verification**: Check for required extensions.
    3. **Implementation**: Trigger the specific generative tool (e.g., `trigger_svg_build` or an external extension command).
- **Rationale**: Ensures the SDD philosophy is maintained even for non-code assets.

## Best Practices
- **Installation Instructions**: Always provide the exact shell command for installation (e.g., `gemini-cli extension install <name>`).
- **Capability Mapping**: Map high-level intents (e.g., "draw a hero") to specific tool patterns (e.g., `nanobanana.gen`).
- **Domain Specialization**: Tailor guides for Manga (Image), Music (Audio), and Engineering (CAD/3D).
