# Quickstart: Releasing Spec-Craft

## 1. Local Verification
Before pushing, ensure all tests pass locally:
```bash
uv run pytest
uv build
```

## 2. Pushing Changes
Push your branch and merge into `main` to trigger the CI tests.

## 3. Creating a Release
To publish to PyPI:
1. Update `version` in `pyproject.toml`.
2. Commit and tag:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
3. GitHub Actions will automatically publish to PyPI.
