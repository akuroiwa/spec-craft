# Research: Release Engineering & CI/CD

## Decisions

### 1. GitHub Actions with `uv`
- **Decision**: Use `astral-sh/setup-uv` action in the CI workflows.
- **Rationale**: Official action provided by the creators of `uv`. It handles caching and installation efficiently.
- **Alternatives**: Manual `pip install uv` (rejected as it is slower and less integrated).

### 2. Trusted Publishing (PyPI)
- **Decision**: Use OIDC (OpenID Connect) for publishing to PyPI.
- **Rationale**: Most secure method; eliminates the need for long-lived API tokens or secrets in GitHub.
- **Alternatives**: Standard API Token secrets (rejected in favor of the more secure OIDC).

### 3. Package Resource Inclusion
- **Decision**: Use `[tool.setuptools.package-data]` in `pyproject.toml` and a `MANIFEST.in` file to guarantee inclusion of `static/`, `extension/`, and `templates/`.
- **Rationale**: `setuptools` (backend used in `pyproject.toml`) requires explicit declaration for non-package-module data files.
- **Alternatives**: Relying solely on `include-package-data = true` (rejected as it can be inconsistent without a MANIFEST).

## Best Practices
- **CI Matrix**: Test against Python 3.10, 3.11, and 3.12 to ensure broad compatibility.
- **Node.js Setup**: Use `actions/setup-node` in the test workflow to ensure `npx @jscad/cli` can run for integration tests.
- **Dry Run**: Include a `uv build` step in the test workflow to verify packaging integrity before actual release.
