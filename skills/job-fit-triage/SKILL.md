---
name: job-fit-triage
description: Assess whether a job is worth applying to by comparing the posting, company context, candidate evidence, constraints, and application cost. Use when the user shares a job description, role link, target company, or list of openings and asks whether to apply, prioritize roles, identify fit gaps, or decide how to position themselves.
---

# Job Fit Triage

## Workflow

1. Extract the role facts: title, level, location, work model, compensation if available, core responsibilities, required qualifications, preferred qualifications, domain, and hiring signals.
2. Extract candidate facts only from provided material. Separate verified evidence from assumptions and missing data.
3. Score fit across four dimensions: role alignment, evidence strength, constraints, and strategic value.
4. Identify blockers, fixable gaps, and narrative angles.
5. Recommend one action: apply now, apply after targeted edits, network first, park, or skip.

## Evidence Rules

- Do not invent experience, credentials, employers, dates, metrics, compensation, work authorization, or referrals.
- If the posting is unavailable or incomplete, state what is missing and grade only the known facts.
- Treat weak matches as useful information, not as a reason to inflate the candidate profile.
- Prefer concrete proof: shipped projects, quantified outcomes, tools used, domains served, leadership scope, writing samples, and public artifacts.

## Output

Return:

- Fit verdict with one-sentence rationale.
- Score table for role alignment, evidence strength, constraints, and strategic value.
- Best evidence to foreground.
- Gaps to close before applying.
- Suggested next step.

Use short, direct language. The user needs a decision, not encouragement.
