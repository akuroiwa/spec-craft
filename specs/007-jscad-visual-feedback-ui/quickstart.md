# Quickstart: 3D Preview & Visual Feedback

## Generating Models with Visuals
1. Define your component in Obsidian.
2. Trigger the build via your AI agent: "Build the gear model with SVG feedback."
3. The system generates `build/cad/universal/gear.stl` and `build/cad/universal/gear.svg`.

## Previewing in Browser
1. Run the following command in your project root:
   ```bash
   spec-craft browse
   ```
2. The browser will open `http://localhost:8080`.
3. Use the interactive controls to rotate and zoom the model.

## AI Visual Feedback
1. Provide the generated SVG to the AI agent.
2. Ask: "Does the proportion of the gear teeth look correct in this projection?"
3. The AI analyzes the SVG and suggests JSCAD code adjustments.
