---
name: "Update changelog"
on:
  cron: "0 9 * * 1"
context:
  - repo: "kosli-dev/cli"
  - repo: "kosli-dev/terraform-provider-kosli"
  - repo: "kosli-dev/server"
notify:
  slack:
    channels:
      - docs
---

# Agent Instructions

Check each repository (kosli-dev/cli, kosli-dev/terraform-provider-kosli, kosli-dev/server) for **new tags/releases** published since the last changelog entry for that product in changelog/index.mdx. Only document changes that are part of a tagged release — do not include unreleased work on `main`.

For each new release tag found, write a changelog entry in changelog/index.mdx. If no new tags exist for a repository since its last changelog entry, skip it. If there are no new tags across any repository, do not open a PR.

This workflow only updates changelog/index.mdx. Do not modify any other files.

Label should be the date the workflow runs, like "March 16, 2026". Description should be the version number of the release, like "v0.3.0".
Tags should be the product(s) affected by the release:
- kosli-dev/cli → `["CLI"]`
- kosli-dev/terraform-provider-kosli → `["Terraform Provider"]`
- kosli-dev/server → `["Platform"]`

The changelog is about changes to the product, not changes to the docs.

Only include updates that affect end users. Do not include internal-only information such as:
- Private repository file paths or directory structures
- Code snippets, internal function names, or implementation details

For each change, describe what changed and what it means for users. Organize entries in this order:
1. New features
2. Updates
3. Bug fixes

If unsure about the structure, review recent changelog updates and follow that style and format.

Be polite and terse. The changelog must be skimmable and quick to read. Include relevant links to docs pages.

PR titles and commit messages **must** follow [Conventional Commits](https://www.conventionalcommits.org/) format: `type: short description` (lowercase, no period). Use `docs:` as the type. Example: `docs: add changelog entry for CLI v2.5.0`.
