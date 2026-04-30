# Quickstart: Phase 4 Assets

## Multilingual SVG Build
1. Create a template in `templates/scene1.svg` with `{{dialogue1}}`.
2. In Obsidian `obsidian/ja/scene1.md`, add:
   ```yaml
   translations:
     dialogue1: "こんにちは、世界！"
   ```
3. Ask the AI: "Build the Japanese version of scene 1."
4. The AI will use `trigger_svg_build` and output to `build/ja/scene1.svg`.

## Parametric CAD Build
1. Define your component in Obsidian.
2. Ask the AI: "Generate the motor mount STL based on my spec."
3. The AI will provide the JSCAD code to `trigger_cad_build` and output to `build/cad/motor_mount.stl`.
