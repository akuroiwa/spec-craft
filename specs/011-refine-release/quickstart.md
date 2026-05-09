# Quickstart: Final Refinement & Staging

## 1. Verifying Refined Drivers
```bash
# Verify CAD (STL+SVG)
trigger_cad_build("...", "part", ["stl", "svg"])

# Verify Bonsai (Architectural)
trigger_full_build() # Ensure architecture is listed
```

## 2. Completing Japanese Docs
```bash
cd docs
make gettext
sphinx-intl update -p _build/gettext -l ja
# Finalize .po files
make ja
```

## 3. Uploading to Test PyPI
```bash
uv build
uv run twine upload --repository testpypi dist/*
```
