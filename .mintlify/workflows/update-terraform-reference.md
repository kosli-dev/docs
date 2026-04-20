---
name: "Update Terraform reference"
on:
  cron: "0 9 * * 1"
context:
  - repo: "kosli-dev/terraform-provider-kosli"
notify:
  slack:
    channels:
      - docs
---

# Agent Instructions

Check kosli-dev/terraform-provider-kosli for **new tags/releases** published since the last Terraform Provider changelog entry in changelog/index.mdx. Only document changes that are part of a tagged release — do not include unreleased work on `main`.

If no new tags exist since the last Terraform Provider changelog entry, do not open a PR.

Update the Terraform reference docs in `terraform-reference/` to match the latest tagged release of kosli-dev/terraform-provider-kosli:

1. **New resources** — if a new resource was added, create a page under `terraform-reference/resources/` and add it to the navigation in `docs.json`.
2. **New data sources** — if a new data source was added, create a page under `terraform-reference/data-sources/` and add it to the navigation in `docs.json`.
3. **Updated resources/data sources** — if attributes were added, removed, or changed on an existing resource or data source, update the corresponding page.

When creating or updating pages:
- Follow Mintlify formatting conventions. Review existing pages in `terraform-reference/` for style reference.
- Use root-relative links (e.g., `/terraform-reference/resources/environment`).
- Include example usage, schema (required/optional/read-only), and import instructions where applicable.

Do not modify changelog/index.mdx — that is handled by the "Update changelog" workflow.

PR titles and commit messages must follow the conventional commits format described in CLAUDE.md. Use `docs:` as the type.
