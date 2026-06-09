---
name: no-slop-resume-writer
description: Write a clear, factual resume from the user's verified evidence without generic filler, inflated claims, or over-polished generated prose. Use when the user wants a new resume draft, a stronger resume section, a plain-language rewrite, a first resume from notes, or a senior-quality cleanup that preserves truth and specificity.
---

# No-Slop Resume Writer

## Workflow

1. Gather the target role, seniority, geography, resume length, and available candidate evidence.
2. Separate verified facts from missing facts. Do not write claims that depend on missing facts.
3. Build the resume around evidence: role scope, shipped work, tools, domains, metrics, constraints, and outcomes.
4. Draft sections in this order: header, summary if useful, skills, experience, projects, education, certifications.
5. Remove generic adjectives, unsupported superlatives, vague ownership language, and bullets that only list duties.
6. Return a resume draft plus a short evidence-gap list.

## Writing Standard

- Prefer concrete nouns and verbs over career-site phrasing.
- Use metrics only when supplied or directly calculable from supplied facts.
- Preserve accurate level: do not turn contribution into ownership, exposure into expertise, or team outcomes into individual outcomes.
- Use standard section headings and text that copies cleanly into applicant systems.
- Keep bullets specific: action, scope, method, result.

## Slop To Remove

- Generic claims: dynamic, passionate, results-oriented, proven track record, fast-paced, trend-chasing.
- Empty verbs: helped, worked on, involved in, responsible for, collaborated on without a concrete contribution.
- Unsupported claims: expert, leader, architected, owned, transformed, optimized without evidence.
- Dense keyword blocks that are not tied to experience.
- Personal branding fluff that would not survive an interview follow-up.

## Output

Return:

- Resume draft in Markdown.
- Evidence assumptions made, if any.
- Claims withheld because evidence was missing.
- Three highest-leverage facts to ask the user for next.
