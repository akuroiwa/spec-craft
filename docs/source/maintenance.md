# Documentation Maintenance

Spec-Craft documentation follows a `gettext` workflow to manage multiple languages.

## Updating the English Source
1. Modify the `.md` files in `docs/source/`.
2. Run `cd docs && make html` to verify locally.

## Updating Translations (Japanese)
After changing the English source, you must update the message catalogs:

1. **Extract new strings**:
   ```bash
   cd docs
   make gettext
   ```
2. **Update PO files**:
   ```bash
   sphinx-intl update -p _build/gettext -l ja
   ```
3. **Edit PO files**:
   Translate the strings in `docs/source/locale/ja/LC_MESSAGES/`.
4. **Build the Japanese version**:
   ```bash
   make ja
   ```

## Read the Docs
Pushing to the `main` branch triggers an automatic build on Read the Docs. Ensure `.readthedocs.yaml` and `docs/requirements.txt` are up to date.
