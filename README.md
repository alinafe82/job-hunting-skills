# Job Hunting Skills

Installable agent skills for a disciplined job search: role triage, resume tailoring, outreach, interview preparation, offer negotiation, workflow automation, and skill review.

The repo is intentionally small. Each skill has a required `SKILL.md` file and Codex UI metadata in `agents/openai.yaml`. Shared checks live in `scripts/`.

## Skills

| Skill | Use when |
| --- | --- |
| `job-fit-triage` | Deciding whether a role is worth applying to, prioritizing openings, or identifying evidence gaps. |
| `job-search-workflow-automation` | Orchestrating sourcing, triage, preparation, tracking, and follow-ups with user approval gates. |
| `professional-networking-outreach` | Planning LinkedIn, Meetup, event, alumni, and community networking without spam. |
| `evidence-resume-tailoring` | Adapting a resume to a specific role using verified candidate evidence. |
| `job-outreach-drafting` | Writing concise role-specific recruiter, referral, hiring manager, or follow-up messages. |
| `interview-evidence-pack` | Preparing targeted interview packets, question banks, and evidence-backed stories. |
| `offer-ask-planner` | Planning compensation, scope, title, start-date, or competing-offer discussions. |
| `no-slop-resume-writer` | Writing a factual resume draft from real candidate evidence without filler. |
| `ats-readability-check` | Checking truthful resume parseability, relevance, and human-review credibility. |
| `job-skill-grading` | Reviewing a job-hunting skill for trigger clarity, usefulness, safety, and publish readiness. |

## Install

Install one skill by copying its folder into your Codex skills directory:

```sh
mkdir -p ~/.codex/skills
cp -R skills/job-fit-triage ~/.codex/skills/
```

Install all skills:

```sh
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

Restart Codex after installing skills.

## Validate

Run the local checks before publishing changes:

```sh
python3 scripts/validate_skills.py
```

The validator checks skill folder names, `SKILL.md` frontmatter, `agents/openai.yaml`, manifest drift, and public-text quality rules.

Automation skills in this repo prepare and organize work. They do not submit applications, send outreach, use credentials, or work around job-board rules without explicit user action.

## Structure Notes

See [docs/structure-notes.md](docs/structure-notes.md) for the public repositories and specifications used to shape this repo.
