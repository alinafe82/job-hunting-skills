---
name: job-skill-creator
description: Create or revise focused Agent Skills for this job-hunting catalog while preserving portable structure, lean instructions, and local validation. Use when adding a new skill, splitting a broad skill, updating skill metadata, improving `agents/openai.yaml`, or aligning a skill with the repo's public quality rules.
---

# Job Skill Creator

## Workflow

1. Define the concrete job-search task the skill should improve.
2. Decide whether it belongs in an existing skill before adding a new folder.
3. If adding a skill, create `skills/<skill-name>/SKILL.md` and `skills/<skill-name>/agents/openai.yaml`.
4. Keep `SKILL.md` concise: trigger-rich description, workflow, evidence rules, and expected output.
5. Add `references/`, `scripts/`, or `assets/` only when the resource materially improves repeat use.
6. Update `skills/manifest.json` and `README.md`.
7. Run `python3 scripts/validate_skills.py`.

## Naming

- Use lowercase letters, digits, and single hyphens.
- Match the folder name and frontmatter `name`.
- Prefer short verb-led or noun-led names that a user would naturally mention.
- Do not create overlapping skills unless the trigger boundary is clear.

## Quality Bar

- The description must say what the skill does and when to use it.
- The body must tell another agent how to perform the task, not explain what skills are.
- The skill must forbid invented candidate facts when job-search outputs depend on evidence.
- Public files must not include generator signatures, filler claims, or unfinished-work markers.
- If a skill needs research, require current sources and source links.

## Output

When creating or revising a skill, return:

- Files changed.
- Why the trigger boundary is distinct.
- Validation command and result.
