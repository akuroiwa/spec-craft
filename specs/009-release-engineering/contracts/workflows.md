# CI/CD Contracts

## GitHub Actions: `test.yml`
- **Triggers**: `push` to `main`, `pull_request` to `main`.
- **Jobs**:
    - `test`:
        - Matrix: `[3.10, 3.11, 3.12]`
        - Steps: `setup-uv`, `setup-node`, `uv sync`, `pytest`.

## GitHub Actions: `publish.yml`
- **Triggers**: `release` (created) or `push` (tags).
- **Environment**: `pypi`.
- **Permissions**: `id-token: write` (for OIDC).
- **Jobs**:
    - `publish`:
        - Steps: `uv build`, `pypa/gh-action-pypi-publish`.
