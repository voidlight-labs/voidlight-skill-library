# Voidlight Skill Library

![Version](https://img.shields.io/badge/version-2.1.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> Universal AI skill specifications enforcing production-grade coding standards across all major AI coding agents.

## Overview

The Voidlight Skill Library is a collection of `.md` skill files that AI agents load to enforce strict coding standards. Each skill targets a specific language or framework, providing a complete rulebook for generating production-grade code.

## Architecture Principle: 2-Layer Pragmatic Clean Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DOMAIN LAYER (Inbound)                    │
│                     Pure Native Only                        │
│                                                              │
│  domain/entity          → Domain entities, value objects    │
│  domain/usecase         → Use cases, application services   │
│  domain/port            → Repository interfaces             │
│  domain/exception       → Domain-specific exceptions        │
│  domain/event           → Domain events                    │
│  domain/service         → Domain services (pure logic)     │
│                                                              │
│  RULES:                                                      │
│  • Compiles with ONLY the language standard library          │
│  • ZERO framework imports                                    │
│  • ZERO external library imports                             │
│  • Pure functions for business logic                         │
│  • Entities are self-validating, never anemic                │
│  • Exceptions are domain-specific, not framework-specific   │
└─────────────────────────────────────────────────────────────┘
                              │
                              │
┌─────────────────────────────────────────────────────────────┐
│              INFRASTRUCTURE LAYER (Outbound)                 │
│              Frameworks and Libraries Allowed               │
│                                                              │
│  infrastructure/persistence  → DB adapters, ORM             │
│  infrastructure/rest         → REST controllers, routes     │
│  infrastructure/external     → HTTP clients, third-party    │
│  infrastructure/config       → Framework config, DI         │
│                                                              │
│  RULES:                                                      │
│  • Implements domain ports                                   │
│  • Contains ALL framework code                               │
│  • Handles all I/O operations                                │
│  • Never puts business logic here                            │
└─────────────────────────────────────────────────────────────┘
```

## Available Skills

| Skill | Apply To | Frameworks |
|---|---|---|
| `java-craft` | `**/*.java` | Spring Boot, Quarkus |
| `python-craft` | `**/*.py` | FastAPI |
| `rust-craft` | `**/*.rs` | Axum, Actix |
| `typescript-craft` | `**/*.ts` | Backend TypeScript: Express, Fastify |
| `nuxt-craft` | `**/*.{vue,ts}` | Nuxt 3, Vue 3 |
| `nextjs-craft` | `**/*.{tsx,ts}` | Next.js App Router |

## Quick Install

One-liner install for any supported agent:

```bash
curl -sL https://raw.githubusercontent.com/voidlight-labs/voidlight-skill-library/main/install.sh | bash -s -- python-craft
```

Or with Python (cross-platform, including Windows):

```bash
python -c "$(curl -sL https://raw.githubusercontent.com/voidlight-labs/voidlight-skill-library/main/install.py)" python-craft
```

### Install all skills

```bash
curl -sL ... | bash -s -- --all
```

### Per-agent quick install

| Agent | Command | Install Target |
|---|---|---|
| **OpenCode** | `bash install.sh python-craft` | `~/.agents/skills/python-craft/SKILL.md` |
| **Kimi Code CLI** | `bash install.sh python-craft` | `~/.kimi-code/skills/python-craft/SKILL.md` |
| **Gemini CLI** | `bash install.sh --agent gemini python-craft` | `~/.gemini/GEMINI.md` (append) |
| **Claude** (project) | `bash install.sh --agent claude python-craft` | `CLAUDE.md` (project root) |
| **GitHub Copilot** | `bash install.sh --agent codex python-craft` | `.github/copilot-instructions.md` |

For detailed install options, see [docs/INSTALL.md](docs/INSTALL.md).

## Quick Start

Copy the skill file for your language/framework into your AI agent's skill directory, or use the install script above.

## Benchmark

30 test scenarios in `benchmark/` (5 per skill).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — Copyright Voidlight

---

**Born from the void, Guided by the light.**
