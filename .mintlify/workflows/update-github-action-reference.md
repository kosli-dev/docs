---
name: "Update GitHub Action reference"
on:
  cron: "0 9 * * 1"
context:
  - repo: "kosli-dev/setup-cli-action"
notify:
  slack:
    channels:
      - docs
---

# Agent Instructions

Check kosli-dev/setup-cli-action for **new tags/releases** published since the last time the GitHub Action reference page was updated. The action uses semver GitHub Releases (e.g., `v5.2.1`) with moving major/minor tags (`v5`, `v5.2`). Check the Releases list for new versions. Only consider changes that are part of a published release — do not include unreleased work on `main`.

If no new releases exist since the last update, do not open a PR.

Keep the GitHub Action reference in `integrations/github_action.md` in sync with the action's [`README.md`](https://github.com/kosli-dev/setup-cli-action/blob/main/README.md) and [`action.yml`](https://github.com/kosli-dev/setup-cli-action/blob/main/action.yml), which are the source of truth. Update the page when any of the following change:

1. **Inputs** — an input is added, removed, renamed, or its accepted values or default change (e.g., `version`, `github-token`).
2. **Outputs** — an output is added, removed, or its meaning changes (e.g., `version`).
3. **Version selection behavior** — how `latest`, full semver, and major/minor pins resolve.
4. **Supported runners** — the set of runners the action supports (`ubuntu-latest`, `windows-latest`, `macos-latest`).
5. **Usage** — the recommended major version in the `uses:` examples (e.g., `@v5`) or the example workflows.

Most releases of this action are Dependabot or internal chore bumps. Those do not change the documented interface — if a release does not affect inputs, outputs, behavior, supported runners, or usage, do not open a PR for it.

When updating the page:
- Follow Mintlify formatting conventions. Review the existing `integrations/github_action.md` and other pages in `integrations/` for style reference.
- Use root-relative links (e.g., `/integrations/ci_cd`, `/client_reference`).
- Keep the page a terse reference: inputs/outputs tables, version-selection rules, and usage examples.

Do not modify changelog/index.mdx — that is handled by the "Update changelog" workflow.

Before opening a PR, review all written content against the style rules in `styles/Kosli/`. In particular, `AmericanSpelling.yml` maps British spellings to their American equivalents — use American spelling throughout (e.g., "behavior", "customize", "organize").

PR titles and commit messages must follow the conventional commits format described in CLAUDE.md. Use `docs:` as the type.
