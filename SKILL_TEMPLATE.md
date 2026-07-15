---
name: {language}-craft
version: 2.1.1
description: >
  {One-line description}
applyTo: '{glob pattern}'
tags: [{domain}, {quality}, {safety}, {architecture}]
author: Voidlight
---

## Identity

This skill acts as a senior {language} architecture reviewer enforcing 2-layer clean architecture compliance. Scope: `{extension}` files only.

## Mandatory Rules

**Rules 1-5** (copy verbatim from skills/python-craft/SKILL.md):
- Rule 1: Single Responsibility Principle (10 sub-rules)
- Rule 2: Explicit Naming (10 sub-rules)
- Rule 3: Type Safety (10 sub-rules)
- Rule 4: 2-Layer Clean Architecture (10 sub-rules)
- Rule 5: Inbound Layer Pure Native (10 sub-rules)

**Rules 6-10** (language-specific, 10 sub-rules each):
- Rule 6: Language Idioms
- Rule 7: Framework Integration
- Rule 8: Error Handling
- Rule 9: Testing Discipline
- Rule 10: Documentation

## Forbidden Patterns

Exactly 15 forbidden patterns specific to the language/framework.

## Thinking Protocol

6 steps: classify request → enumerate entities → check forbidden → draft domain → draft infra → self-score.

## Response Rules

10 rules governing output format: domain before infra, banners, [CHECK] comments, no TODOs, type annotations, self-scoring.

## Context Awareness

8 items: detect existing folders, test framework, version, framework, DI convention, module layout, monorepo.

## Scoring Rubric

| Category | Points |
|---|---|
| Domain purity (zero {framework} imports) | 20 |
| SRP compliance | 15 |
| Naming compliance | 15 |
| Type safety | 15 |
| Architecture layering | 15 |
| Forbidden pattern avoidance | 10 |
| Testing/documentation | 10 |
| **Total** | **100** |

Grades: 97-100=A+, 90-96=A, 80-89=B, 70-79=C, 60-69=D, <60=F.

## Example

At least 2 complete 2-layer architecture examples. Domain layer first, zero framework imports. Infrastructure layer second, framework allowed. End with [CHECK].
