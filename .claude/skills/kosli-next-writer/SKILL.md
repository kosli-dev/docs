---
name: kosli-next-writer
description: Use when writing or editing docs for Kosli Next - the docs surface for forward-looking concepts and preview features. Triggers on mentions of "Kosli Next", "concept docs", "preview feature docs", or any work on files under `kosli_next/`. Covers where files go, required front matter and banners, navigation updates, and tone.
---

# Writing for Kosli Next

Kosli Next is a separate Mintlify Product (alongside "Product") for content that is **not currently available in Kosli**. Use it for concepts (ideas we're considering) and preview features (opt-in pre-GA features).

If the content describes something shippable today, it does NOT belong in Kosli Next - it goes in the main "Product" surface under `understand_kosli/`, `getting_started/`, etc.

## Decision flow

1. **Is the feature available to all customers today?** → Main docs. Stop reading this skill.
2. **Is it an idea or direction we want feedback on, but nothing is built yet?** → Kosli Next → Concepts.
3. **Is it real, usable, but opt-in / pre-GA?** → Kosli Next → Preview.

## File locations

| Content type | Directory |
|---|---|
| Concept page | `kosli_next/concepts/<slug>.mdx` |
| Preview page | `kosli_next/preview/<slug>.mdx` |

Use lowercase, underscore-separated slugs to match the rest of the repo (`kosli_next/concepts/my_concept.mdx`).

## Required page template

Every Kosli Next page starts with this shape:

```mdx
---
title: "Short, specific title"
description: "One sentence describing the page purpose."
tag: "Concept"   # or "Preview"
---

import { ConceptBanner } from '/snippets/kosli-next-banner.mdx';
{/* or: import { PreviewBanner } from '/snippets/kosli-next-banner.mdx'; */}

<ConceptBanner />
{/* or: <PreviewBanner /> */}

Page content goes here.
```

The banner snippet (`snippets/kosli-next-banner.mdx`) is the single source of truth for the disclaimer + feedback CTA. Do NOT inline a custom disclaimer.

## Navigation update (required)

Add the new page path to `config/navigation.json` under the matching tab in the **Kosli Next** product:

- Concept pages → `products[1].tabs[0].groups[0].pages`
- Preview pages → `products[1].tabs[1].groups[0].pages`

A page that isn't in `config/navigation.json` won't appear in the sidebar. This is a core repo rule.

## Tone

Standard Kosli writing rules from the project `CLAUDE.md` still apply:

- Sentence case for headings.
- Active voice and imperative mood.
- "Kosli" - not "the Kosli platform" or "KOSLI".
- Root-relative internal links (`/kosli_next/concepts/foo`, not `../foo`).
- No em-dashes. Use hyphens or rewrite the sentence.

Two Kosli Next-specific additions:

- **Be honest about status.** Don't write a Concept page in the present tense as if it works ("Kosli reports X..."). Write in the conditional ("Kosli would report X...") so readers aren't misled into thinking the feature exists.
- **Invite feedback.** End each page with a short prompt: "Tell us what you think - email support@kosli.com." (The banner says this too; an end-of-page nudge is fine.)

## Form

Diátaxis is NOT enforced inside Kosli Next. Pick whichever shape best explains the idea:

- A short PR/FAQ-style explainer (problem → proposed approach → open questions) is often a good fit for Concepts.
- A how-to + reference combination tends to fit Previews.

## Verification

Before opening a PR:

1. Run `mint dev` and confirm the page appears under the right tab in the Kosli Next product switcher.
2. Confirm the banner renders.
3. Run `mint broken-links`.

