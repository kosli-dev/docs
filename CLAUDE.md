# CLAUDE.md

This file governs repo-specific conventions for Claude Code. Skills and system prompts govern their own domains and take precedence for their scope.

## Core rules

These are non-negotiable — follow them regardless of other instructions:

1. Never commit directly to `main` — always work on a branch and open a PR.
2. Never create a page file without also adding it to `navigation` in `docs.json`.
3. Never use relative links — always use root-relative paths (e.g., `/getting_started/install`).
4. Commit messages and PR titles must follow [Conventional Commits](https://www.conventionalcommits.org/): `type: short description` (lowercase, no period). Common types: `feat`, `fix`, `docs`, `style`, `chore`.
5. Run `mint broken-links` before committing navigation or link changes.

## Project Overview

Kosli documentation site built with [Mintlify](https://mintlify.com/docs). Content is authored in Markdown (`.md`) and MDX (`.mdx`) files. Configuration lives in `docs.json`.

## Development Commands

```bash
npm i -g mint          # Install Mintlify CLI (one-time)
mint dev               # Start local dev server at http://localhost:3000
mint dev --port 3333   # Start on custom port
mint update            # Update Mintlify CLI
mint broken-links      # Validate all internal links
mint a11y              # Check color contrast and accessibility
```

Requires Node.js v19+.

## Architecture

- **`docs.json`** — Central config: navigation structure, theme, API settings, logos, footer. All page routing is defined here under `navigation.products[].tabs[].groups`.
- **Content directories** — `understand_kosli/`, `getting_started/`, `administration/`, `integrations/`, `implementation_guide/`, `client_reference/`, `api-reference/`
- **`snippets/`** — Reusable MDX content fragments
- **`style.css`** — Custom CSS overrides applied on top of the Mintlify theme
- **`api-reference/openapi.json`** — OpenAPI spec for Kosli API endpoints
- **`essentials/`** — Mintlify's own getting-started guide, kept as a reference. Do not edit or link to these pages in Kosli navigation.

## Content Conventions

Every page requires YAML front matter:

```yaml
---
title: Short, specific title
description: One sentence describing the page purpose.
---
```

- **MUST** Use root-relative paths for internal links: `/understand_kosli/what_is_kosli` ✓ — `../what_is_kosli` ✗
- **MUST** Adding a new page: create the file AND add its path to `navigation` in `docs.json`. Both steps are required.
- **SHOULD** Follow the [Diátaxis](https://diataxis.fr/) framework when choosing page form:
  - **Tutorial** — teaches by doing (e.g., "Get familiar with Kosli")
  - **How-to guide** — step-by-step for a specific goal (e.g., "Report AWS environments")
  - **Reference** — factual, lookup-oriented (e.g., CLI reference pages)
  - **Explanation** — concepts and background (e.g., "What is Kosli?")
- **MAY** Add an `icon` field to front matter using [Font Awesome](https://fontawesome.com/icons) names.

### MDX Components

| Component | Use for |
|---|---|
| `<Steps>` / `<Step>` | Sequential procedures |
| `<Tabs>` / `<Tab>` | Platform-specific or alternative content |
| `<Card>` / `<CardGroup>` | Navigational links, feature highlights |
| `<Accordion>` / `<AccordionGroup>` | Progressive disclosure, FAQs |
| `<Tip>` / `<Info>` / `<Warning>` / `<Note>` | Callouts — use sparingly |
| `<CodeGroup>` | Same command in multiple languages/tools |
| `<Frame>` | Wrapping images |

### Writing style

- Use active voice and imperative mood for instructions ("Run `kosli attest`", not "You should run").
- Refer to the product as **Kosli** — not "the Kosli platform" or "KOSLI".
- Use "audit trail" not "audit log"; "attest" not "certify".
- Sentence case for all headings.

## Don'ts

- Don't use relative links — they break when pages move.
- Don't create a page without updating `docs.json` navigation — it won't appear in the site.
- Don't edit files in `essentials/` — they are Mintlify's content, not Kosli's.
- Don't add content to `snippets/` unless it is genuinely reused in 2+ pages.
- Don't commit image files without placing them in an appropriate subdirectory.
- Don't push to `main` directly — always use a PR.

## Skills

When available, prefer skills over ad-hoc approaches:

- **PR creation** — use the `pr-creator` skill if available.
- **Changelog entries** — use the `changelog-creator` skill if available. Follow the existing `<Update>` format in `changelog/index.mdx` exactly:
  ```mdx
  <Update label="Month Year" description="vX.X.X" tags={["Product Name"]}>

  ## New features / Bug fixes / Changes

  - ...

  [View on GitHub](https://github.com/kosli-dev/...)

  </Update>
  ```
  Always prompt the user for the `tags` value (e.g., `"Terraform Provider"`, `"CLI"`) before generating an entry.

## Deployment

Automatic via Mintlify GitHub app on push to `main`. No manual deployment steps.
