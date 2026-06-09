# Structure Notes

This repo follows the portable Agent Skills baseline and adapts conventions from active public skill catalogs without vendoring their content.

## References Checked

- `openai/skills`: official catalog shape with a `skills/` directory, install guidance, and per-skill discoverability through `SKILL.md`.
- `togethercomputer/skills`: compact README table, per-skill `agents/openai.yaml`, and optional `references/` or `scripts/` only when they materially help.
- `mxyhi/ok-skills`: simple clone-and-copy installation model for `SKILL.md` compatible agents.
- `opensite-ai/opensite-skills`: repository-level structure validation and explicit metadata checks.
- `agentskills.io/specification`: exact `SKILL.md` casing, required `name` and `description` fields, optional resource directories, and progressive disclosure.

## Choices Applied Here

- Keep installable skills under `skills/<skill-name>/`.
- Require exact-case `SKILL.md` and matching folder/frontmatter names.
- Include `agents/openai.yaml` for every skill because Codex surfaces can use it.
- Keep main skill files lean; add one-level `references/`, `scripts/`, or `assets/` only when a skill genuinely needs them.
- Maintain a small manifest so the README and validation script have a source of truth.
- Use a standard-library validator instead of adding package management solely for checks.
- Block generator signatures and filler claims in public files.
- Avoid exact-name duplicates with public GitHub skills. Rename generic concepts to job-search-specific names when a public skill already uses the obvious name.
- Keep automation skills scoped to user-approved preparation and tracking when public examples already cover application-submission systems.
- Keep networking skills scoped to user-reviewed relationship building when public examples already cover platform autopilot behavior.
