---
name: doc-review
description: Review documentation for quality, structure, and convention compliance. Use when the user wants to review docs, audit a page or section, check if content is clear, evaluate information architecture, or assess navigation. Do NOT use when the user wants to write or fix docs — use doc-write for that. Triggers on "review the docs", "audit this page", "is this getting-started page clear", "check the implementation guide section".
---

# Doc Review

Evaluate technical docs against the Diátaxis framework, information-architecture best practices, and the project's CLAUDE.md.

## Before reviewing

1. **Read the project's CLAUDE.md** — it defines all site-specific conventions. Use it as your compliance checklist for writing style, components, link format, and frontmatter. If no CLAUDE.md exists, read 3-4 existing pages to infer conventions.
2. **Read `docs.json`** to understand navigation structure.
3. **Determine review scope** — single page, section, or full site. If unclear, ask the user which scope they want.

## Page-level review

1. **Diátaxis classification** — Identify the doc type (tutorial, how-to, reference, explanation). Does the content match? Common issue: tutorials mixed with reference material, or how-to guides that teach instead of solving.
2. **Content quality** — Clear title? Accurate description? Complete for its doc type? Factually correct and current?
3. **Structure** — Logical flow? Appropriate depth?
4. **CLAUDE.md compliance** — Check the page against every rule and convention in the project's CLAUDE.md (frontmatter, components, links, writing style, don'ts).
5. **Link validation** — Internal links resolve to existing files? (Use Glob/Grep to verify.)

## Section-level review

1. Read all pages in the section.
2. Check navigation order — logical progression?
3. Identify gaps — missing pages for common user tasks?
4. Check Diátaxis balance — right mix of doc types?
5. Verify cross-linking between related pages.
6. Assess consistency in voice, structure, and components.

## Site-level review

1. Is the top-level navigation intuitive?
2. Are tutorials, how-to guides, reference, and explanation clearly separated?
3. Can new users find getting-started content quickly? Can experienced users find reference quickly?
4. Structural issues: orphaned pages, deep nesting (>3 levels), overloaded sections, missing landing pages.

## Output format

Categorize findings as:
- **Critical** — Broken functionality, factual errors, missing required content.
- **Improvement** — Clarity issues, structural problems, missing best practices.
- **Suggestion** — Nice-to-have enhancements.

For each: **Location** (file:line or section), **Issue**, **Recommendation**.

End with a summary: findings by category, overall assessment, top 3 priorities.
