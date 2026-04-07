---
name: "Update API reference"
on:
  cron: "0 9 * * 1"
context:
  - repo: "kosli-dev/server"
notify:
  slack:
    channels:
      - docs
---

# Agent Instructions

Check kosli-dev/server for **new tags/releases** published since the last time `api-reference/openapi.json` was updated (check the most recent commit touching that file for context). Only document changes that are part of a tagged release — do not include unreleased work on `main`.

If no new tags exist since the last update, do not open a PR.

For each new release, review the diff for changes to API endpoints, parameters, response shapes, or error codes. If API changes were introduced, update `api-reference/openapi.json` in this repository to reflect those changes. This is the OpenAPI 3.1.0 specification that powers the API Reference section of the docs site.

Specifically:
- Add new endpoints, parameters, or response fields as defined in the server code.
- Update descriptions, type information, and examples where affected.
- If a parameter or endpoint was removed, mark it as **deprecated** rather than deleting it, unless the code explicitly removes it with no deprecation period.
- Preserve the existing `servers` field in the spec — do not modify the server URLs.
- Preserve the existing `security` and `securitySchemes` configuration.

If new endpoint tags (groups) are introduced, add corresponding entries to the API Reference navigation in `config/navigation.json`, maintaining alphabetical group order.

## Important

- If no API changes were introduced, do nothing.
- Do not include private repository file paths, directory structures, code snippets, or any other internal implementation details in PR titles, descriptions, or commit messages. The PR body should only describe the user-facing change in terms of the API behavior.
- Do not modify any files other than `api-reference/openapi.json` and `config/navigation.json`.
