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

Label should be the date the workflow runs, like "March 16, 2026". Description should be the version number of the release, like "v0.3.0".
Tags should be the product(s) affected by the release, like ["CLI"], ["API"], or ["Terraform Provider"].

The changelog is about changes to the product, not changes to the docs.

Do not include any internal-only information—no private repository file paths, directory structures, code snippets, internal function names, or implementation details. Only include updates that affect end users. Include a description of the change and what it means for users. Organize the changelog with new features first, then updates, then bug fixes. If you're ever unsure about the structure, review recent changelog updates and follow that style and format.

Be polite and terse. The changelog must be skimmable and quick to read. Include relevant links to docs pages.
