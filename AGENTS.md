# Voidlight Skill Library — AGENTS.md

## Repo Type

Documentation/knowledge repo, not a code project. No build system, no CI/CD, no test suite. The only executable code is the benchmark runner.

## Plugin Packaging

The repo ships as a standard agent plugin (`.claude-plugin/plugin.json`, compatible with Claude Code and ZCode). The manifest `version` is the single source of truth — skill frontmatters carry the same version under `metadata.version`. Skill frontmatter uses the canonical top-level fields `name` + `description` only; `version`, `author`, `applyTo`, and `tags` live under `metadata`.

## Directory Map

| Path | What |
|------|------|
| `.claude-plugin/plugin.json` | Plugin manifest (name, version, description, author, license). Single source of truth for version. |
| `skills/{lang}-craft/SKILL.md` | One per language (7 total). Self-contained AI skill specs loaded by agents. |
| `agents/{persona}.md` | 3 persona definitions (architect, smith, surveyor). Subagent identity specs. |
| `benchmark/benchmark.py` | Python script evaluating AI-generated code against skill rules. |
| `benchmark/scenarios/{lang}/scenario-{NN}-{difficulty}.md` | 30 total (5 per skill). Input files for the benchmark. |
| `SKILL_TEMPLATE.md` | Canonical template for creating new skills. |

## Commands

```bash
# Run benchmark (all skills)
cd benchmark && pip install -r requirements.txt && python benchmark.py

# Run single skill
python benchmark.py --skill python-craft

# Output formats
python benchmark.py --format json
python benchmark.py --format csv
```

Benchmark scenarios live in `benchmark/scenarios/{lang}/`. Requires `pyyaml` and `markdown`.

## Skill File Anatomy (must match exactly)

Every `skills/*/SKILL.md` must contain:
- Valid YAML frontmatter (`name`, `version`, `description`, `applyTo`, `tags`, `author`)
- 10 Mandatory Rules with 10 sub-rules each
- 15 Forbidden Patterns
- 6-step Thinking Protocol
- 10 Response Rules
- 8 Context Awareness items
- Scoring Rubric (7 categories, 100 points)
- Minimum 2 complete 2-layer architecture examples

The canonical reference is `skills/python-craft/SKILL.md`. When creating a new skill, start from `SKILL_TEMPLATE.md`.

## Architecture Principle (2-Layer)

Every skill enforces this split:
- **Domain Layer** (`domain/`): Pure standard library only. Zero framework imports.
- **Infrastructure Layer** (`infrastructure/`): Framework code allowed. Implements domain ports.

This is documented in `README.md` and `CONTRIBUTING.md`. Do not repeat it in agent responses — the skill files already define it.

## Validation Rules (from CONTRIBUTING.md)

New skills or edits must pass:
- Valid YAML frontmatter
- All 7 required sections present
- Minimum 5 rules
- `DOMAIN LAYER` / `INFRASTRUCTURE LAYER` banners in examples
- Domain layer examples have zero framework imports
- 5 benchmark scenarios (2 Easy, 2 Medium, 1 Hard)

## What Skills Apply To

| Skill File | `applyTo` | Framework(s) |
|---|---|---|
| `java-craft` | `**/*.java` | Spring Boot, Quarkus |
| `python-craft` | `**/*.py` | FastAPI |
| `rust-craft` | `**/*.rs` | Axum, Actix |
| `typescript-craft` | `**/*.ts` | Backend TypeScript: Express, Fastify |
| `nuxt-craft` | `**/*.{vue,ts}` | Nuxt 3, Vue 3 |
| `nextjs-craft` | `**/*.{tsx,ts}` | Next.js App Router |
| `markdown-to-vdl` | `**/*.md` | VDL (Voidlight Definition Language) |

## Install Script

Two installers are provided for quick deployment to agent environments:

- **`install.sh`** — POSIX shell script. Primary installer for Linux/macOS/WSL.
- **`install.py`** — Python 3 script. Cross-platform fallback (Windows, restricted environments).

### Agent Install Targets

| Agent | Default Path | Format | `--agent` value |
|---|---|---|---|
| OpenCode | `~/.agents/skills/{name}/SKILL.md` | Native | `opencode` |
| Kimi Code CLI | `~/.kimi-code/skills/{name}/SKILL.md` | Native | `kimi` |
| Gemini CLI | `~/.gemini/GEMINI.md` (append) | Native/Compact | `gemini` |
| Claude (project) | `CLAUDE.md` (project root) | Extracted rules | `claude` |
| GitHub Copilot | `.github/copilot-instructions.md` | Extracted rules | `codex` |

Auto-detect priority: OpenCode → Kimi → Gemini → Claude → Codex → stdout paste.

### Security

Both scripts are read-only (no `sudo`, no `rm -rf`, no arbitrary code execution). They download SKILL.md files from `raw.githubusercontent.com` and write them to the detected agent path. Prompt before overwrite unless `--force` is passed.

## Notes

- Version shared across all skills: `2.2.0` (source of truth: `.claude-plugin/plugin.json`). Keep in sync.
- In Next.js or Nuxt projects, use the framework skill instead of `typescript-craft`; the latter is backend-only.
- No CI workflows. No pre-commit hooks.
- The repo does not contain actual application code — only markdown specifications.
- When adding a benchmark scenario, place it in the correct `benchmark/scenarios/{lang}/` directory.
