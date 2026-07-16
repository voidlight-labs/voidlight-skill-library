---
name: markdown-to-vdl
version: 1.0.0
description: >
  Instruction skill for converting structured Markdown documents into valid
  VDL (Voidlight Definition Language) syntax. Enforces entity inference,
  relationship extraction, evidence block construction, and post-conversion
  validation.
applyTo: "**/*.md"
tags: [vdl, markdown, converter, knowledge-graph, voidlight]
author: Voidlight
---

## Identity

This skill guides agents in transforming hierarchical Markdown documents into
valid `.vdl` files. The Markdown source uses heading levels, lists, blockquotes,
and frontmatter to encode a knowledge graph. The agent maps these structural
elements to VDL entities, properties, relationships, and evidence blocks.

Scope: any `*.md` file that encodes doctrines, laws, frameworks, concepts, or
axioms. The agent produces one `.vdl` file per Markdown document. After
conversion, the agent must run `vdl validate` and fix any reported errors
before considering the task complete.

## Mandatory Rules

### Rule 1: Document Structure Mapping

1. **YAML frontmatter** (if present) maps to top-level module annotations.
2. **H1 (`# Title`)** maps to the document title and optional pillar/category.
3. **H2 (`## Title`)** maps to an entity declaration: `type "id" { ... }`.
4. **H3 (`### Title`)** maps to entity properties or relationship sections.
5. **Bullet lists** under H3 map to relationship arrays or annotation values.
6. **Blockquotes** (`> ...`) map to revelation evidence sources and text.
7. **Paragraphs** under an "Argument" or "Synthesis" section map to synthesis
   arguments.
8. **Code blocks or indented analogies** map to `analogy` evidence items.

### Rule 2: Entity Type Inference

Infer the VDL entity type from the H2 heading semantics:

| Markdown Cue | VDL Type |
|--------------|----------|
| Axiom, Postulate, First Principle, Core Truth | `axiom` |
| Framework, System, Architecture, Constitution, Methodology | `framework` |
| Law, Rule, Mandate, Commandment | `law` |
| Principle, Guideline, Tenet, Doctrine | `principle` |
| Concept, Idea, Pattern, Practice, Ritual, Protocol | `concept` |
| Artifact, Output, Deliverable, Work Product | `artifact` |
| Pillar, Foundation, Column, Root | `pillar` |
| Document, Paper, Record, File | `document` |
| Project, Initiative, Program, Effort | `project` |
| Release, Version, Milestone, Drop | `release` |
| Persona, Role, Actor, User Type | `persona` |
| Collection, Group, Set, Bundle | `collection` |

If the heading is ambiguous, default to `concept` and flag the choice to the
user. Never invent entity types outside the VDL grammar (axiom, framework, law, principle, concept, artifact, pillar, document, project, release, persona, collection).

### Rule 3: Entity ID Generation

1. Derive the entity ID from the H2 heading text.
2. Convert to lowercase ASCII.
3. Replace spaces and hyphens with underscores.
4. Remove all punctuation except dots (used for namespacing).
5. Collapse consecutive underscores.
6. Prepend a namespace if the document uses one (e.g., `soul.law.i`).
7. IDs must be unique within the generated `.vdl` file.
8. IDs must match the VDL identifier pattern:
   `^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*$`.

### Rule 4: Property Extraction

Extract the following entity properties from Markdown content:

| VDL Property | Markdown Source |
|--------------|-----------------|
| `version "X.Y"` | Frontmatter `version:` or H3 "Version". Default `"1.0"`. |
| `title "..."` | H2 heading text, preserved in title case. |
| `description "..."` | First paragraph after the H2, or frontmatter `description:`. |
| `previous "..."` | H3 "Previous Version" or frontmatter `previous:`. Omit if absent. |

### Rule 5: Relationship Mapping

Map H3 section headings to relationship arrays. The array contents are the
bullet-list items or comma-separated IDs.

| H3 Heading Cue | VDL Relationship |
|----------------|------------------|
| Requires, Depends On, Prerequisites | `requires [ ... ]` |
| Based On, Builds Upon, Grounded In | `based_on [ ... ]` |
| Derives From, Descended From, Follows | `derives_from [ ... ]` |
| Enables, Unlocks, Makes Possible | `enables [ ... ]` |
| References, See Also, Related | `references [ ... ]` |
| Implements, Fulfills, Realizes | `implements [ ... ]` |
| Inspired By, Influenced By, Drawn From | `inspired_by [ ... ]` |
| Evolved From, Grew Out Of, Matured From | `evolved_from [ ... ]` |
| Contradicts, Opposes, Refutes | `contradicts [ ... ]` |

Each item must be a quoted string ID. Validate that referenced IDs exist in the
same document; if external, flag them with a comment.

### Rule 6: Evidence Block Construction

Every entity except `artifact` must have an evidence block. The evidence block starts with the keyword `evidence {` and
contains one or more evidence items.

| Markdown Source | VDL Evidence Item |
|-----------------|-------------------|
| Blockquote with optional translator | `revelation { source "..." text "..." [translator "..."] }` |
| Argument paragraph citing multiple sources | `synthesis { sources [ "...", "..." ] argument "..." }` |
| Analogy section with domain label | `analogy { domain "..." mapping "..." }` |

If the Markdown blockquote attributes a translator, include the optional `translator` field.

If no evidence section exists in the Markdown, the agent **must** generate a
minimal placeholder `revelation` and warn the user.

### Rule 7: Annotation Mapping

Convert YAML frontmatter keys to module-level annotations generically. Any frontmatter key maps to `@key("value")` placed at the top of the `.vdl` file. Common mappings include:

| Frontmatter Key | VDL Annotation |
|-----------------|----------------|
| `author:` | `@author("...")` |
| `date:` or `created:` | `@created("...")` |
| `status:` (draft, canonical, deprecated) | `@status("...")` |
| `pillar:` or `category:` | `@pillar("...")` |

Unknown frontmatter keys must still be emitted as annotations in the order they appear in the frontmatter.

### Rule 8: Validation Gate

1. After emitting the `.vdl` file, the agent **must** run:
   ```bash
   vdl validate <output.vdl>
   ```
2. If validation fails, the agent **must** interpret the error and fix the
   generated file. Common fixes:
   - **Missing evidence** → add a `revelation` block.
   - **Invalid version** → ensure `version "X.Y"`.
   - **Unresolved reference** → ensure the `target_id` exists or add a stub
     entity.
   - **Circular dependency** → refactor `requires` or `derives_from` chains.
   - **Synthesis with <2 sources** → add another source or convert to `revelation` or `analogy`.
3. Only mark the conversion complete when `vdl validate` exits with code 0.

### Rule 9: Type Constraint Pre-Validation

Before emitting VDL, the agent must enforce these structural rules to prevent validation failures:

1. `axiom` entities must have **zero** `requires` relationships.
2. `framework` entities must have **at least one** `based_on` relationship.
3. `law` and `principle` entities must have **at least one** `derives_from` relationship.
4. `artifact` entities must have at least one relationship (of any type) to a `law` or `principle`.
5. `synthesis` evidence must contain **at least two** sources in its `sources` array.
6. If the Markdown source violates a type constraint, the agent must either:
   - Add the missing relationship/evidence using contextual inference, or
   - Flag the issue to the user and refuse to emit invalid VDL.

## Examples

### Example 1: Minimal Law Conversion

**Markdown Input:**

```markdown
---
author: Khayren
created: 2024-03-15
status: canonical
pillar: soul
---

# The Seven Laws

## Autonomy Is Mandatory

**Version:** 5.0

Every node must retain sovereign control over its own processing.

### Derives From

- voidlight_constitution

### Evidence

> **Source:** Quran 2:30
> "And when your Lord said to the angels, 'Indeed, I will make upon the earth a successive authority.'"
```

**VDL Output:**

```vdl
@author("Khayren")
@created("2024-03-15")
@status("canonical")
@pillar("soul")

law "autonomy_is_mandatory" {
    version "5.0"
    title "Autonomy Is Mandatory"
    description "Every node must retain sovereign control over its own processing."

    derives_from [ "voidlight_constitution" ]

    evidence {
        revelation {
            source "Quran 2:30"
            text "And when your Lord said to the angels, 'Indeed, I will make upon the earth a successive authority.'"
        }
    }
}
```

### Example 2: Framework with Multiple Relationships and Evidence Types

**Markdown Input:**

```markdown
## Divine Alignment

**Version:** 2.0

A methodology for aligning human nodes with divine purpose.

### Based On

- voidlight_constitution

### Enables

- daily_practice
- node_assessment
- alignment_ritual

### References

- soul.law.i
- soul.law.iv

### Evidence

> **Source:** Quran 91:7-10
> "And the soul and He who proportioned it..."

**Synthesis:** This framework synthesizes the Quranic model of soul
purification (tazkiyah) with modern systems thinking (Quran 91:7-10) and the
divine capacity for human responsibility (Quran 2:286). Just as the soul has
innate capacity for both corruption and purification, a human node has
capacity for both misalignment and alignment.

**Analogy — Astronomy:** Just as a telescope must be precisely aligned with
celestial coordinates to capture clear images of distant stars, a human node
must be aligned with divine coordinates to receive clear signal from the
Creator.
```

**VDL Output:**

```vdl
framework "divine_alignment" {
    version "2.0"
    title "Divine Alignment"
    description "A methodology for aligning human nodes with divine purpose."

    based_on [ "voidlight_constitution" ]

    enables [
        "daily_practice",
        "node_assessment",
        "alignment_ritual"
    ]

    references [
        "soul.law.i",
        "soul.law.iv"
    ]

    evidence {
        revelation {
            source "Quran 91:7-10"
            text "And the soul and He who proportioned it..."
        }

        synthesis {
            sources [ "Quran 91:7-10", "Quran 2:286" ]
            argument "This framework synthesizes the Quranic model of soul purification (tazkiyah) with modern systems thinking (Quran 91:7-10) and the divine capacity for human responsibility (Quran 2:286). Just as the soul has innate capacity for both corruption and purification, a human node has capacity for both misalignment and alignment."
        }

        analogy {
            domain "Astronomy"
            mapping "Just as a telescope must be precisely aligned with celestial coordinates to capture clear images of distant stars, a human node must be aligned with divine coordinates to receive clear signal from the Creator."
        }
    }
}
```

## Notes

- This skill produces **instruction-level guidance** for agents. It does not
  provide a native executable or parser. The agent performs the conversion
  using its reasoning capabilities guided by the rules above.
- Always prefer explicit structure in Markdown (frontmatter, clear H2/H3
  hierarchy, labeled lists) over heuristic guessing.
- When in doubt, ask the user for clarification rather than emitting invalid
  VDL.
