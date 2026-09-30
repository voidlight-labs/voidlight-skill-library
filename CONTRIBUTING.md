# Contributing to Voidlight Plugin Library

This repository hosts multiple independent agent plugins under `plugins/`. Each plugin is self-contained: its manifests, skills, agents, docs, installers, and benchmarks live inside its folder.

## Adding a new plugin

1. Create `plugins/<plugin-name>/` where `<plugin-name>` matches the manifest `name` exactly (lower-case, hyphenated).
2. Author `.zcode-plugin/plugin.json` (required for ZCode) and `.claude-plugin/plugin.json` (optional, for Claude Code). Keep both manifests in sync.
3. Add the plugin to the root `marketplace.json` with matching `name`, `version`, `description`, and a relative `source` path.
4. Add a row to the plugin table in the root `README.md`.

## Editing an existing plugin

Work inside the plugin's folder. Increment the plugin manifest's semantic version and keep skill frontmatter `metadata.version` in sync with the manifest. Skill anatomy rules (sections, rules count, examples, benchmark scenarios) are documented in the plugin's own `CONTRIBUTING.md` and `SKILL_TEMPLATE.md`.

## Validation checklist

Before opening a PR, verify:

- Both manifests (if present) are valid JSON with matching `name` and `version`.
- Plugin folder name equals manifest `name`.
- Root `marketplace.json` has an entry for the plugin with a correct relative `source`.
- Skill files have valid YAML frontmatter (`name` + `description` top-level; `version`, `author`, `applyTo`, `tags` under `metadata`).
- Plugin benchmark (if the plugin ships one) still runs: `cd plugins/<name>/benchmark && pip install -r requirements.txt && python benchmark.py`.

## License

MIT, same as the repository.
