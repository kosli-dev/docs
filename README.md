# Kosli Documentation

> [!WARNING]
> This documentation is still a work in progress and is not yet the official Kosli documentation.

Source for [kosli.mintlify.app](https://kosli.mintlify.app), built with [Mintlify](https://mintlify.com).

## Development

Install the Mintlify CLI (requires Node.js v19+):

```bash
npm i -g mint
```

Start a local preview at `http://localhost:3000`:

```bash
mint dev
```

Other useful commands:

```bash
mint broken-links   # Validate all internal links
mint a11y           # Check colour contrast and accessibility
mint update         # Update the CLI
```

## Content

- **`docs.json`** — Navigation, theme, and site configuration. Every new page must be added here.
- **Content directories** — `understand_kosli/`, `getting_started/`, `administration/`, `integrations/`, `implementation_guide/`, `client_reference/`, `terraform-reference/`, `api-reference/`
- **`snippets/`** — Reusable MDX fragments (only for content used in 2+ pages)
- **`changelog/`** — Product changelog

See [`CLAUDE.md`](CLAUDE.md) for full authoring conventions.

## Deployment

Opening a PR automatically creates a Mintlify preview environment. Merging to `main` deploys to production automatically via the Mintlify GitHub app.

## Automation

**`.mintlify/workflows/update-changelog.md`** — A Mintlify agent workflow that runs every Monday at 09:00 UTC. It reviews all PRs merged to [`kosli-dev/cli`](https://github.com/kosli-dev/cli) and [`kosli-dev/terraform-provider-kosli`](https://github.com/kosli-dev/terraform-provider-kosli) since the last changelog entry and writes a new `<Update>` block to `changelog/index.mdx`. Notifications are posted to the `#docs` Slack channel.
