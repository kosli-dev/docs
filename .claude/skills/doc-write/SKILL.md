---
name: doc-write
description: Create, write, or update documentation pages in a Mintlify-based docs site. Use when the user wants to write docs, create a new page, document a feature, add a guide or tutorial, or update existing documentation. Do NOT use for reviewing or auditing — use doc-review for that. Triggers on "write docs for X", "create a new page", "document this feature", "add a tutorial", "draft a how-to guide".
---

# Doc Write

Author Mintlify docs pages following the Diátaxis framework and the project's CLAUDE.md.

## Before writing

1. **Read the project's CLAUDE.md** — it defines all site-specific conventions (components, writing style, link format, frontmatter, don'ts). Follow it exactly. If no CLAUDE.md exists, read 3-4 existing pages to infer conventions.
2. **Read `docs.json`** to understand navigation structure.
3. **Read 2-3 similar pages** to match the site's voice, structure, and component usage.
4. **Search for existing content** using Grep and Glob — you may need to update rather than create.

## Classify the doc type (Diátaxis)

Every page must fit one of these four types. Classify before writing:

| Type | Purpose | User need | Structure |
|------|---------|-----------|-----------|
| **Tutorial** | Learning-oriented | "Teach me X" | Step-by-step guided learning experience with expected outcomes |
| **How-to guide** | Task-oriented | "How do I do X?" | Goal-focused steps, assumes knowledge, handles variations |
| **Reference** | Information-oriented | "What is X?" | Complete, accurate, terse technical description |
| **Explanation** | Understanding-oriented | "Why does X work this way?" | Context, background, trade-offs, alternatives |

A common mistake is mixing tutorials with how-to guides — tutorials teach through doing, how-to guides solve specific problems. If the doc type is ambiguous, ask the user.

## Writing process

1. **Classify** the doc type and confirm with the user if uncertain.
2. **Outline** the page structure based on the doc type.
3. **Write** the MDX file following the project's CLAUDE.md conventions.
4. **Place** the file in the correct directory and update `config/navigation.json` (or `docs.json` navigation, whichever the project uses).

## Output

Write files directly to disk using Write/Edit tools. Then report:
- File path of the created/updated page.
- Navigation entry added (path in `config/navigation.json` or `docs.json`).
- Related pages that should cross-link to this one.
