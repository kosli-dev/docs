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

Check each repository for **new tags** published since the last changelog entry for that product in changelog/index.mdx. Only document changes that are part of a tagged release — do not include unreleased work on `main`.

- **kosli-dev/cli** and **kosli-dev/terraform-provider-kosli** use semver GitHub Releases (e.g., `v2.17.5`, `v0.6.3`). Check the Releases list for new versions.
- **kosli-dev/server** does **not** use GitHub Releases. It uses timestamp-based git tags (e.g., `release-2026-04-30-10-56-05`). You must check git **tags** (not Releases) and look at the commits between the last covered tag and the most recent tag to identify user-facing changes. Consolidate all server changes since the last Platform changelog entry into a single entry.

For each new release found, write a changelog entry in changelog/index.mdx. If no new tags exist for a repository since its last changelog entry, skip it. If there are no new tags across any repository, do not open a PR.

This workflow only updates changelog/index.mdx. Do not modify any other files.

Label should be the date the workflow runs, like "March 16, 2026". Description should be the version number of the release for semver repositories (e.g., "v0.3.0"). For kosli-dev/server, leave description empty (`""`) since it has no semver version.
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

PR titles and commit messages must follow the conventional commits format described in CLAUDE.md. Use `docs:` as the type.
