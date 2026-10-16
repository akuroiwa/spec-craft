# Strategic Hub (Obsidian)

The Strategic Hub is the heart of the Spec-Craft workflow. It leverages Obsidian to maintain a high-level creative roadmap that guides all implementation efforts.

## Strategy vs Tactics Analogy
Understanding the difference between strategy and tactics is key to the Spec-Craft philosophy:

- **Strategy (Obsidian)**:
  - **Focus**: "What" and "Why".
  - **Content**: Expands and details the Spec-Kit Constitution process, housing storyboards, domain models, geometric principles, and long-term milestones.
  - **Permanence**: Acts as the project's persistent architectural record.
- **Tactics (spec-kit)**:
  - **Focus**: "How".
  - **Process**: Short-term iterative SDD cycles via the Shorter Path (Specify → Plan → Tasks → Implement → Converge).
  - **Action**: Creating modular code files, generating SVG scenes, building CAD models, and continuously converging codebase reality with specification intent.

## The Bridge
Spec-Craft acts as the bridge, allowing AI agents to read the strategy in [Obsidian](https://obsidian.md/) and translate it into tactical tasks in [spec-kit](https://github.com/github/spec-kit).

## Operational Transparency
Spec-Craft prioritizes security and reliability. Instead of executing sensitive tactical tasks in hidden background processes, AI agents:
1. **Discover**: Read command definitions (TOML) to understand the required steps.
2. **Propose**: Suggest the exact shell command to the user.
3. **Confirm**: Execute only after the user provides confirmation in their terminal.

This interactive approach ensures that secure events, such as SSH password prompts, are handled safely by the human creator.
