# Contributing to Voidlight Skill Library

Thank you for your interest in contributing. This document outlines the process for proposing new skills and updating existing ones.

## How to Propose a New Skill

1. **Start from the template**: Copy `SKILL_TEMPLATE.md` and fill in all sections.
2. **Follow the golden template**: Read `skills/python-craft/SKILL.md` as the canonical reference.
3. **Mirror the structure exactly**:
   - 10 Mandatory Rules with 10 sub-rules each
   - 15 Forbidden Patterns
   - 6-step Thinking Protocol
   - 10 Response Rules
   - 8 Context Awareness items
   - Scoring Rubric with 7 categories, 100 points
4. **Include complete 2-layer architecture examples**.
5. **Add 5 benchmark scenarios** (2 Easy, 2 Medium, 1 Hard).

## Validation Requirements

All skills must pass:
- Valid YAML frontmatter
- All 7 required sections present
- Minimum 5 rules
- DOMAIN/INFRASTRUCTURE LAYER in examples
- Domain layer has zero framework imports

## 2-Layer Architecture

- **Domain Layer**: Pure native, zero framework imports
- **Infrastructure Layer**: Framework code allowed, implements domain ports

## License

MIT — see README.md
