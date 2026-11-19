# Kosli Documentation
Source for [docs.kosli.com](https://docs.kosli.com), built with [Mintlify](https://mintlify.com).

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
mint a11y           # Check color contrast and accessibility
mint update         # Update the mint CLI tool
```

## Content

- **`docs.json`** — Theme and site configuration. Uses `$ref` to compose from files in `config/`.
- **`config/`** — Split config: `navigation.json` (page routing — every new page must be added here), `redirects.json`, `footer.json`.
- **Content directories** — `understand_kosli/`, `getting_started/`, `administration/`, `user/`, `integrations/`, `tutorials/`, `implementation_guide/`, `labs/`, `troubleshooting/`, `faq/`, and the reference directories `client_reference/`, `helm/`, `policy-reference/`, `terraform-reference/`, `template-reference/`, `github-action-reference/`. Directory names don't decide where a page appears; `config/navigation.json` does.
- **`snippets/`** — Reusable MDX fragments (only for content used in 2+ pages)
- **`changelog/`** — Product changelog.
- **`product-updates.mdx`** — Product updates. Its RSS feed also feeds the What's new menu in the Kosli app: see [Writing a product update](/docs/writing-product-updates.md) before adding an entry.

See [`CLAUDE.md`](CLAUDE.md) for full authoring conventions.

## Deployment

Opening a PR automatically creates a Mintlify preview environment. Merging to `main` deploys to production automatically via the Mintlify GitHub app.

## Automation

Mintlify Autopilot keeps three areas in sync with their upstream repositories. It opens a PR for each update and announces it in the `#pr-reviews` Slack channel.

- **Changelog** (`changelog/index.mdx`): every Monday and Friday at 09:00 UTC, Autopilot writes an `<Update>` entry for each new release tag of [`kosli-dev/cli`](https://github.com/kosli-dev/cli), [`kosli-dev/terraform-provider-kosli`](https://github.com/kosli-dev/terraform-provider-kosli) and `kosli-dev/server`.
- **Terraform reference** (`terraform-reference/`): every Monday and Friday at 09:00 UTC, Autopilot syncs the pages to the latest release tag of [`kosli-dev/terraform-provider-kosli`](https://github.com/kosli-dev/terraform-provider-kosli).
- **GitHub Action reference** (`github-action-reference/setup_cli_action.md`): every Monday at 09:00 UTC, Autopilot syncs the page to the `README.md` and `action.yml` of the latest [`kosli-dev/setup-cli-action`](https://github.com/kosli-dev/setup-cli-action) release.

Autopilot never updates `product-updates.mdx` on its own. The team writes product updates by hand, and Autopilot only edits the page when a teammate asks it to.
