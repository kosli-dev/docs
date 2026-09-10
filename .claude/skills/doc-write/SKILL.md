---
name: doc-write
description: Create, write, or update documentation pages in a Mintlify-based docs site. Use when the user wants to write docs, create a new page, document a feature, add a guide or tutorial, or update existing documentation. Do NOT use for reviewing or auditing — use doc-review for that. Triggers on "write docs for X", "create a new page", "document this feature", "add a tutorial", "draft a how-to guide".
---

# Doc write

Author Mintlify pages for the Kosli docs site following Diátaxis and this repo's CLAUDE.md.

## Before writing

1. **Read CLAUDE.md** — components, writing style, link format, frontmatter, and the don'ts. Follow it exactly.
2. **Read `config/navigation.json`** for the navigation tree. Navigation lives there, not in `docs.json` — `docs.json` only holds a `$ref` to it.
3. **Search for existing content** with Grep and Glob. Updating a page beats adding one; a thin new page next to an existing one splits the topic.
4. **Check open issues** — `gh issue list --state open --label content` — the gap may already be tracked, with context on what the reader needs.
5. **Read 2-3 pages in the destination group** to match voice, structure, and component usage.

## Generated pages

**Deterministically regenerated — an edit here is deleted on the next release.** Fix the source instead:

| Path | Fix it in |
|---|---|
| `client_reference/kosli*.md` | **`kosli-dev/cli`** → `cmd/kosli/<command>.go` (e.g. `kosli_attest_sonar.md` ← `attestSonar.go`) |
| `helm/k8s_reporter/*.mdx` | **`kosli-dev/cli`** → `charts/k8s-reporter/mintlify/<page>.md.gotmpl` or `values.yaml` |
| `schemas/` | **`kosli-dev/server`** → the Pydantic models, then `scripts/update_schemas.py` |
| The `kosli *` groups in `config/navigation.json` | This repo → `scripts/update-cli-nav.py` |
| Live-docs sections in `client_reference/` | This repo → `scripts/add_livedocs.py`, `scripts/live_docs_*_data.py` |

Run `scripts/dev_live_docs.sh` to regenerate locally; it restores `client_reference/` on exit.

In the CLI's Go long descriptions, **`^` means backtick** (`^--jq^`, `^jq^`) and `kosli docs` substitutes it. Write `^`, not a literal backtick, when editing those strings.

**Agent-synced from upstream — an edit survives but will drift.** `terraform-reference/` (from `kosli-dev/terraform-provider-kosli`) and `github-action-reference/setup_cli_action.md` (from `kosli-dev/setup-cli-action`'s `README.md` and `action.yml`) are maintained by the `.mintlify/workflows/` agents. Edit the page when it is wrong, but check it against upstream first — if upstream disagrees, the next sync undoes you.

**Hand-authored despite the directory:** `client_reference/overview.md` and `client_reference/output_and_verbosity.md`. Regeneration only removes `kosli*.md`. Edit these freely.

To document a command's *usage*, write a how-to that links to the generated reference rather than restating its flags — a restated flag list goes stale silently.

## Classify the doc type

| Type | Purpose | User need | Structure |
|------|---------|-----------|-----------|
| **Tutorial** | Learning-oriented | "Teach me X" | Guided steps with a known outcome |
| **How-to guide** | Task-oriented | "How do I do X?" | Goal-focused steps, assumes knowledge |
| **Reference** | Information-oriented | "What is X?" | Complete, accurate, terse |
| **Explanation** | Understanding-oriented | "Why does X work this way?" | Context, background, trade-offs |

Tutorials teach through doing; how-to guides solve one problem for someone who already knows the basics. If the type is genuinely ambiguous, ask.

## Decide where the page goes

Tabs are named after subjects, not document types, so **placement follows the reader's job, not the classification above.** One subject draws all four Diátaxis needs, and they belong in the same tab, sorted by page form inside it.

Pick the tab whose membership test the page satisfies. If a page fails every test, the structure is wrong, not the page — raise it rather than forcing a fit.

| Tab | Membership test — the reader… |
|---|---|
| **Discover Kosli** | …has not started yet: orientation, first run, learning, getting unstuck |
| **Platform administration** | …is configuring Kosli itself for an organization |
| **Risks & controls** | …is deciding what must be true, or proving it was |
| **Environments and runtime** | …is reporting, or interpreting, what is actually running |
| **Record evidence** | …is instrumenting a pipeline to produce evidence |
| **Reference** | …knows what they want and needs exact syntax or values |
| **Changelog** | …wants to know what shipped |

Reference wins on content shape, not on subject. A reference page about an integration belongs in Reference — a GitHub Action reference page was once authored into `integrations/` and had to be moved in a follow-up commit.

Two tests can both look plausible. When they do, ask which reader is holding the page: someone standing Kosli up for the first time is in Discover Kosli even if the task is administrative; someone hardening an existing org is in Platform administration even if it is their first week.

Read the pages already in your chosen group before writing, and follow the convention they set rather than creating a parallel group beside them.

## Navigation rules

- **Creating a page and adding it to `config/navigation.json` are one task.** A page absent from navigation does not exist on the site.
- Add it to an existing group. Only create a group when you are adding three or more sibling pages — a group wrapping a single page adds a click and gives nothing back.
- Keep pages within three levels of their tab.
- **Sentence case for group labels**, matching CLAUDE.md's heading rule: "Naming conventions", not "Naming Conventions".

## When moving, renaming, or deleting a page

1. Add a `config/redirects.json` entry from the old path to the new one. The old URL is in bookmarks, in CLI error output, and in changelog entries.
2. Grep the repo for the old path and update every link.
3. If a heading is being renamed, grep for its anchor first. Some anchors are referenced from outside this repo — the CLI prints `faq/faq.md#boolean-flags` in an error message. Keep the heading, or update the source that links to it.

## Writing

1. Classify the doc type and pick the destination from the table above.
2. Outline against the doc type.
3. Write the file. Root-relative links only (`/getting_started/install`). Frontmatter `title` and `description` are required.
4. Add the navigation entry.
5. Add redirects if anything moved.
6. Verify: does the change contradict a generated reference page, a schema, or a changelog entry? Grep and fix what it contradicts.

## Changelog

The changelog is for product changes, not doc changes — a new page describing an existing feature does not get an entry. When documenting a feature that *did* ship, check whether `changelog/index.mdx` already covers it, and make the entry and the page agree. Changelog entries are written by `.mintlify/workflows/update-changelog.md` from release tags; if an entry is wrong, fix the entry too.

Follow the existing `<Update>` format exactly and ask which `tags` value applies (`"CLI"`, `"Platform"`, `"Terraform Provider"`, `"GitHub Action"`) before writing one.

## Report

- File path created or updated.
- Navigation entry added, and which tab and group — say why that placement.
- Redirects added, if any.
- Pages that should now cross-link to this one.
