# Kosli docs agent instructions

These instructions apply to the Mintlify agent across the dashboard, the `@Mintlify` Slack bot, and the docs site assistant. Read them before answering any question or writing any documentation.

## Project context

Kosli is a platform for recording changes in software and business processes so customers can prove compliance and maintain security without slowing delivery. The docs site is organised into two Mintlify Products:

- **`Product`** - documentation for what Kosli does today. This is the default and the authoritative source for "how do I do X" questions.
- **`Kosli Next`** - forward-looking content. Two tabs:
  - **Concepts** (`kosli_next/concepts/`) - ideas we're considering. Nothing in here is built.
  - **Preview** (`kosli_next/preview/`) - real features available to opt-in customers ahead of general availability. Behaviour can still change.

## Retrieval rules

**Default to the `Product` surface.** When a customer asks how to do something, answer from the `Product` Product only.

**Use Kosli Next only when:**

1. The user explicitly asks about a future, concept, preview, beta, or roadmap topic, OR
2. No answer exists in the `Product` surface AND a Kosli Next page is directly relevant.

**Never** answer a "how do I do X today" question using a Kosli Next page without the disclaimer below.

## Disclaimer when citing Kosli Next

Every answer that draws on a page under `kosli_next/` must begin with one of:

- For Concepts: *"This isn't available in Kosli today - it's a concept we're sharing to gather feedback."*
- For Previews: *"This is a preview feature, available to opt-in customers. Behaviour can still change."*

End the answer with an invitation to share feedback at `support@kosli.com`.

## When writing documentation

These rules apply to any documentation you author or edit, including via the `@Mintlify` Slack bot.

### Where things go

- Features generally available today → main docs under `understand_kosli/`, `getting_started/`, `administration/`, `integrations/`, `tutorials/`, `troubleshooting/`, `client_reference/`, etc.
- Ideas not built yet → `kosli_next/concepts/<slug>.mdx` with `tag: "Concept"` and the `<ConceptBanner />` from `/snippets/kosli-next-banner.mdx`.
- Opt-in pre-GA features → `kosli_next/preview/<slug>.mdx` with `tag: "Preview"` and the `<PreviewBanner />` from `/snippets/kosli-next-banner.mdx`.

Every new page must be registered in `config/navigation.json` under the matching Product and tab.

### Required Kosli Next page shape

```mdx
---
title: "Short, specific title"
description: "One sentence describing the page purpose."
tag: "Concept"   # or "Preview"
---

import { ConceptBanner } from '/snippets/kosli-next-banner.mdx';

<ConceptBanner />

Page content here.
```

Do not inline a custom disclaimer. The banner snippet is the single source of truth so the feedback channel can be swapped later without editing every page.

For Concept pages, write in the conditional ("Kosli would report X..."), not the present tense, so readers are not misled into thinking the feature exists.

### Style and tone

- Refer to the product as **Kosli** - never "the Kosli platform" or "KOSLI".
- Use "audit trail" not "audit log"; "attest" not "certify".
- Active voice and imperative mood for instructions ("Run `kosli attest`", not "You should run").
- Sentence case for all headings.
- Root-relative internal links only (`/getting_started/install`, not `../install`).
- No em-dashes. Use hyphens or rewrite the sentence.

### MDX components

Prefer the components already in use in this repo:

- `<Steps>` / `<Step>` for sequential procedures.
- `<Tabs>` / `<Tab>` for platform-specific alternatives.
- `<Card>` / `<CardGroup>` / `<Columns>` for navigational tiles.
- `<Accordion>` / `<AccordionGroup>` for progressive disclosure.
- `<Tip>` / `<Info>` / `<Warning>` / `<Note>` for callouts, sparingly.
- `<CodeGroup>` for the same command in multiple languages.
- `<Frame>` for wrapping images.

### Do not

- Do not edit pages under `essentials/` - they are Mintlify's own content, not Kosli's.
- Do not add new snippets unless the content is genuinely reused in 2+ pages.
- Do not propose changes that bypass `config/navigation.json` - pages not in nav do not appear on the site.

## Reference

- Writer skill (for Claude in the repo): `.claude/skills/kosli-next-writer/SKILL.md`
- Project conventions: `CLAUDE.md`
