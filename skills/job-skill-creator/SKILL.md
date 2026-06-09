---
name: job-skill-creator
description: Create or revise focused Agent Skills for this job-hunting catalog while preserving portable structure, lean instructions, and local validation. Use when adding a new skill, splitting a broad skill, updating skill metadata, improving `agents/openai.yaml`, or aligning a skill with the repo's public quality rules.
---

# Job Skill Creator

## Workflow

1. Define the concrete job-search task the skill should improve.
2. Decide whether it belongs in an existing skill before adding a new folder.
3. Use the platform's native skill creation workflow when available. For Codex, prefer the installed `skill-creator` initializer and validator over hand-building folders.
4. If adding a skill manually, create `skills/<skill-name>/SKILL.md` and `skills/<skill-name>/agents/openai.yaml`.
5. Keep `SKILL.md` concise: trigger-rich description, workflow, evidence rules, and expected output.
6. Add `references/`, `scripts/`, or `assets/` only when the resource materially improves repeat use.
7. Update `skills/manifest.json` and `README.md`.
8. Run both the repo validator and the skill validator when available.

## Naming

- Use lowercase letters, digits, and single hyphens.
- Match the folder name and frontmatter `name`.
- Prefer short verb-led or noun-led names that a user would naturally mention.
- Do not create overlapping skills unless the trigger boundary is clear.

## Quality Bar

- The description must say what the skill does and when to use it.
- The body must tell another agent how to perform the task, not explain what skills are.
- `agents/openai.yaml` must match the skill's actual purpose and mention `$skill-name` in `default_prompt`.
- The skill must forbid invented candidate facts when job-search outputs depend on evidence.
- Public files must not include generator signatures, filler claims, or unfinished-work markers.
- If a skill needs research, require current sources and source links.

## Validation

Run:

- `python3 scripts/validate_skills.py`
- The platform skill validator, if available, against each changed skill folder.

## Output

When creating or revising a skill, return:

- Files changed.
- Why the trigger boundary is distinct.
- Validation command and result.
