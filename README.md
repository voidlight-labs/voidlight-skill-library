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
| `typescript-craft` | `**/*.ts` | Express, Fastify |
| `nuxt-craft` | `**/*.{vue,ts}` | Nuxt 3, Vue 3 |
| `nextjs-craft` | `**/*.{tsx,ts}` | Next.js App Router |

## Quick Start

Copy the skill file for your language/framework into your AI agent's skill directory.

## Benchmark

30 test scenarios in `benchmark/` (5 per skill).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — Copyright Voidlight

---

**Born from the void, Guided by the light.**
