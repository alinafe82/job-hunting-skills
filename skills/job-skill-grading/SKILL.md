---
name: job-skill-grading
description: Grade Agent Skills for this job-hunting catalog before they are installed, committed, or published. Use when reviewing a new or changed skill, checking trigger quality, detecting vague instructions, auditing evidence rules, comparing a skill to repository structure standards, or deciding whether a skill is ready to ship.
---

# Job Skill Grading

## Workflow

1. Inspect the skill folder, `SKILL.md`, `agents/openai.yaml`, and any bundled resources.
2. Check routing: name, description, trigger terms, and whether the skill overlaps existing skills.
3. Check execution value: can another agent follow the workflow without extra context?
4. Check evidence discipline: does the skill prevent invented candidate facts, fabricated metrics, or misleading claims?
5. Check structure: exact `SKILL.md` casing, one-level resources, useful metadata, and manifest/README alignment.
6. Run `python3 scripts/validate_skills.py` when reviewing this repo locally.
7. Give a verdict and the smallest set of changes needed.

## Rubric

Score each category from 0 to 3:

- Trigger clarity: the description makes activation obvious.
- Task specificity: the workflow solves a concrete job-search problem.
- Evidence discipline: the skill protects against invented facts.
- Output usefulness: the expected response shape is clear and actionable.
- Structure: files follow the repo and Agent Skills conventions.
- Maintenance cost: the skill does not add unnecessary resources or overlap.

## Verdicts

- Ship: no blocking issues.
- Revise: useful skill with specific fixes required.
- Merge: the content belongs in an existing skill.
- Reject: the skill is too vague, unsafe, duplicative, or costly to maintain.

## Output

Lead with findings:

- Verdict.
- Scores by category.
- Blocking issues with file references.
- Suggested patch scope.
- Validation result if available.
