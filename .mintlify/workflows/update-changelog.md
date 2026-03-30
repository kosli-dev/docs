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

Review all PRs merged to the kosli-dev/cli, kosli-dev/terraform-provider-kosli, and kosli-dev/server repositories since the last changelog update component was added.

Write a changelog post under changelog/index.mdx for this week based on what shipped. If no changelogs exists yet for a given repository, only consider changes for the past week.

Make sure to update resources and data sources in `terraform-reference/` to match `kosli-dev/terraform-provider-kosli`. Make sure when copy documentation across to use Mintlify formatting.

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
