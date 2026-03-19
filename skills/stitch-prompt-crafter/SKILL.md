---
name: stitch-prompt-crafter
description: Convert a PRD into practical Korean prompts for Google Stitch, including first-generation prompts, revision prompts, and prototype-linking prompts. Use this when a user already has a PRD and wants to generate or refine UI screens in Stitch.
---

# Stitch Prompt Crafter

Use this skill after a PRD already exists.

## Workflow

1. Read the PRD.
2. Extract user, problem, core features, and screen count.
3. Produce:
   - an initial generation prompt
   - a simplification prompt
   - a tone-adjustment prompt
   - a Prototypes linking prompt

## Rules

- Keep prompts in Korean by default.
- Prefer concrete layout language over abstract branding language.
- Mention screen names explicitly when multiple screens are needed.
- For revision prompts, target one issue at a time.

Read `references/examples.md` for prompt patterns.
