---
name: ats-readability-check
description: Audit a resume for truthful applicant-tracking readability, screening relevance, and low-friction human review without evasion or misrepresentation. Use when the user asks whether a resume will parse cleanly, match a job description, avoid generic generated-sounding prose, pass legitimate resume screens, or improve formatting before applying.
---

# ATS Readability Check

## Boundary

Optimize for accurate parsing, relevance, and credibility. Do not help hide generated authorship, defeat integrity systems, launder false claims, or work around an employer's rules. If the user asks for rule-circumvention, redirect to factual resume quality: clearer evidence, simpler formatting, and stronger role alignment.

## Workflow

1. Parse the resume into sections and identify formatting that may break applicant systems: tables, columns, text boxes, icons, images, headers, footers, unusual bullets, and nonstandard headings.
2. Compare the resume to the target job description when provided. Map requirements to evidence; do not add missing skills.
3. Scan for generic generated-sounding prose, keyword stuffing, unsupported metrics, vague ownership, and inconsistent dates or titles.
4. Recommend edits that improve truthful parseability and human credibility.
5. Return a pass/revise verdict with prioritized fixes.

## Checks

- Parseability: standard headings, chronological clarity, single-column text, consistent date formats, readable contact information.
- Relevance: role-critical requirements appear where supported by evidence.
- Credibility: every claim can be defended in an interview.
- Voice: concise, specific, and natural; no filler or exaggerated claims.
- Risk: missing facts, unverifiable metrics, sensitive personal details, or formatting that may disappear when parsed.

## Output

Return:

- Verdict: pass, revise, or major rewrite.
- Blocking parseability issues.
- Job-description match gaps.
- Prose credibility fixes.
- Clean rewrite examples for the highest-risk lines.
