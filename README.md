# Voidlight Plugin Library

A library of agent plugins by Voidlight. Each folder under `plugins/` is an installable agent plugin (compatible with Claude Code and ZCode). The root `marketplace.json` is the catalog: install the whole library as a plugin marketplace, or consume plugins individually.

## Plugins

| Plugin | Path | What |
|---|---|---|
| [strict-hexagonal](plugins/strict-hexagonal/) | `plugins/strict-hexagonal/` | Language-craft skills enforcing strict 2-layer hexagonal architecture (Java, Python, Rust, TypeScript, Nuxt, Next.js), a Markdown-to-VDL converter, and the prd-craft/craft-router process skills. |

## Repository layout

```
voidlight-plugin-library/
├── marketplace.json              # Root plugin catalog (ZCode native format)
├── plugins/
│   └── strict-hexagonal/         # One self-contained plugin per folder
│       ├── .zcode-plugin/plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── skills/               # SKILL.md per skill
│       ├── agents/               # Subagent persona definitions
│       ├── benchmark/            # Benchmark runner + scenarios
│       ├── docs/                 # Plugin docs (INSTALL.md)
│       ├── install.sh / install.py
│       └── README.md / CONTRIBUTING.md
```

## Installing

### Via plugin marketplace (recommended)

1. In ZCode, open **Plugin Marketplace → Add → Add Plugin Marketplace** and point it at this repository (or your local clone).
2. Install the plugin you want from the market list.

### Via install scripts

Each plugin ships its own installers. From the plugin folder:

```bash
cd plugins/strict-hexagonal
./install.sh            # POSIX (Linux/macOS/WSL)
python install.py       # Cross-platform fallback (Windows, restricted shells)
```

See [plugins/strict-hexagonal/docs/INSTALL.md](plugins/strict-hexagonal/docs/INSTALL.md) for agent targets and options.

## Adding a plugin

1. Create `plugins/<plugin-name>/` with a `.zcode-plugin/plugin.json` (and optionally `.claude-plugin/plugin.json`). The folder name must match the manifest `name`.
2. Add an entry to the root `marketplace.json`.
3. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Versioning

Each plugin versions independently; the plugin manifest `version` is the single source of truth. See the plugin's own README for its version history.
