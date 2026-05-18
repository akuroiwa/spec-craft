# Quickstart: Vision & Sandbox

## 1. Visual Verification (Blender)
1. Generate your Blender script as usual.
2. Trigger the visual feedback render:
   ```bash
   # (AI calls this tool)
   render_blender_svg("build/3d/house.py", "house_wireframe")
   ```
3. Use the resulting SVG to verify proportions.

## 2. Isolated AI Editing (Emacs)
1. Initialize the sandbox:
   ```bash
   # (AI calls this tool)
   setup_emacs_sandbox()
   ```
2. Perform a lint-safe edit:
   ```bash
   # (AI sends Elisp to rename a symbol)
   edit_with_emacs("(query-replace 'old-name 'new-name)")
   ```

## 3. Environment Check
Run `spec-craft check-env` to ensure your system has Emacs 29+ and the required Blender addons.
