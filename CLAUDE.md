# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kosli documentation site built with [Mintlify](https://mintlify.com/docs). Content is authored in Markdown (`.md`) and MDX (`.mdx`) files. Configuration lives in `docs.json`.

## Development Commands

```bash
npm i -g mint          # Install Mintlify CLI (one-time)
mint dev               # Start local dev server at http://localhost:3000
mint dev --port 3333   # Start on custom port
mint update            # Update Mintlify CLI
mint broken-links      # Validate all internal links
```

Requires Node.js v19+.

## Architecture

- **`docs.json`** — Central config: navigation structure, theme, API settings, logos, footer. All page routing is defined here under `navigation.products[].tabs[].groups`.
- **Content directories** — `understand_kosli/`, `getting_started/`, `administration/`, `integrations/`, `implementation_guide/`, `client_reference/`, `api-reference/`
- **`snippets/`** — Reusable MDX content fragments
- **`api-reference/openapi.json`** — OpenAPI spec for Kosli API endpoints
- **`essentials/`** — Mintlify's own docs guide (not Kosli user-facing content)

## Content Conventions

- Every page needs YAML front matter with `title` and `description`. Optional `icon` field uses Font Awesome names.
- Use root-relative paths for internal links (e.g., `/understand_kosli/what_is_kosli`), not relative paths.
- Adding a new page requires both creating the file and adding its path to the `navigation` section in `docs.json`.

### MDX Components

Common components: `<Steps>`, `<Tabs>`/`<Tab>`, `<Card>`/`<CardGroup>`, `<Accordion>`/`<AccordionGroup>`, `<Tip>`, `<Info>`, `<Warning>`, `<Note>`, `<CodeGroup>`, `<Frame>`.

## Deployment

Automatic via Mintlify GitHub app on push to `main`. No manual deployment steps.
