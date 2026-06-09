---
name: job-search-workflow-automation
description: Orchestrate a disciplined job-search workflow across sourcing, triage, application preparation, tracking, follow-ups, and weekly review without submitting applications or sending outreach without user approval. Use when the user wants to automate job hunting, run a daily or weekly search routine, process a batch of roles, maintain an application pipeline, or coordinate resume, outreach, interview, and offer skills.
---

# Job Search Workflow Automation

## Boundary

Automate organization and preparation, not representation. Do not submit applications, send messages, answer screening questions, create accounts, use credentials, work around platform limits, scrape against site rules, or claim user approval that was not given. Keep the user as final reviewer and actor for submissions and outreach.

## Workflow

1. Establish the user's target profile: roles, seniority, locations, work model, compensation, domains, must-haves, deal-breakers, and available source materials.
2. Create or update a local pipeline table when the user wants tracking. Suggested columns: company, role, URL, source, status, priority, fit verdict, next action, owner, deadline, last contact, notes.
3. Collect candidate roles only from user-provided links, files, approved searches, or explicitly allowed sources.
4. De-duplicate roles by company, title, location, and posting URL.
5. Triage each role with `job-fit-triage`; mark apply, network first, watch, or skip.
6. For apply-ready roles, prepare materials by invoking the right downstream skill: `evidence-resume-tailoring`, `no-slop-resume-writer`, `ats-readability-check`, or `job-outreach-drafting`.
7. For network-first roles or event/community paths, prepare relationship-building messages with `professional-networking-outreach`.
8. Queue follow-ups and reminders after user-confirmed applications, interviews, recruiter conversations, or networking interactions.
9. Produce a daily or weekly review: new roles found, roles skipped, materials ready for review, pending user approvals, stale follow-ups, and next highest-leverage actions.

## Automation Modes

- Intake mode: build preferences, evidence inventory, and pipeline schema.
- Batch triage mode: process a list of postings and produce ranked next actions.
- Preparation mode: draft resumes, outreach, and interview prep packets for approved roles.
- Follow-up mode: find stale applications or conversations and draft user-approved messages.
- Review mode: summarize progress, bottlenecks, and decisions for the next cycle.

## Safety Rules

- Require explicit user confirmation before any external action.
- Treat job-board terms, robots restrictions, rate limits, and account rules as hard boundaries.
- Do not mass-message recruiters or create generic outreach campaigns.
- Do not invent candidate facts, eligibility, salary expectations, work authorization, referrals, or availability.
- Store sensitive job-search data only where the user chooses; warn if plain-text files may contain personal or compensation details.

## Output

Return:

- Current pipeline summary.
- Top roles with fit verdict and rationale.
- Prepared artifacts ready for user review.
- Decisions needed from the user.
- Next scheduled or manual workflow step.
