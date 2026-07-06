# Voidlight Skill Library Benchmark

This directory contains benchmark scenarios for evaluating AI agent compliance with Voidlight Skill Library rules.

## Overview

The benchmark tests whether AI-generated code follows 2-layer pragmatic clean architecture, strict typing, explicit naming, and single responsibility principles.

## Scenario Structure

Each skill has 5 benchmark scenarios:

| Difficulty | Count | Description |
|---|---|---|
| Easy | 2 | Basic entity + repository + use case. Tests fundamental 2-layer compliance. |
| Medium | 2 | Multi-entity with relationships, domain events, or error handling. |
| Hard | 1 | Complex business logic with multiple use cases and edge cases. |

**Total: 30 scenarios (5 per skill x 6 skills)**

## Running the Benchmark

```bash
cd benchmark
pip install -r requirements.txt
python benchmark.py              # All skills
python benchmark.py --skill python-craft   # Specific skill
python benchmark.py --format json         # JSON output
python benchmark.py --format csv          # CSV output
```

## Scoring Methodology

Each scenario is scored against:
1. SRP Enforcement — Function/class length, single responsibility
2. Explicit Naming — Descriptive function/variable names
3. Type Safety — Type annotations, no escape hatches
4. 2-Layer Architecture — Domain pure native, infrastructure has framework
5. Inbound Purity — No framework imports in domain layer

The scoring rubric from each skill applies (0-100 scale).

## Skills Covered

| Skill | Scenarios | Directory |
|---|---|---|
| java-craft | 5 | `benchmark/scenarios/java/` |
| python-craft | 5 | `benchmark/scenarios/python/` |
| rust-craft | 5 | `benchmark/scenarios/rust/` |
| typescript-craft | 5 | `benchmark/scenarios/typescript/` |
| nuxt-craft | 5 | `benchmark/scenarios/nuxt/` |
| nextjs-craft | 5 | `benchmark/scenarios/nextjs/` |

## Adding New Scenarios

Create a file in `benchmark/scenarios/{skill}/` following this format:

```
scenario-{NN}-{difficulty}.md
```

### Scenario Format

```markdown
# Scenario: {Name}

## Difficulty
Easy | Medium | Hard

## Description
{What the model is asked to implement}

## Prompt
{Exact prompt to give the model}

## Expected Output
- File: {path}
- Must contain: {list}
- Must not contain: {list}

## Scoring Criteria
- [ ] {Criterion} ({points} points)
```

For questions, see [CONTRIBUTING.md](../CONTRIBUTING.md).
