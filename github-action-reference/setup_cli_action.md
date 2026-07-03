---
title: GitHub Action
description: Reference for the setup-kosli-cli GitHub Action that installs the Kosli CLI on GitHub Actions runners.
icon: github
---

The [`kosli-dev/setup-cli-action`](https://github.com/kosli-dev/setup-cli-action) GitHub Action (`setup-kosli-cli`) installs the [Kosli CLI](/client_reference) on GitHub Actions runners. After the action runs, every CLI command is available in later steps of the job.

The action runs on `ubuntu-latest`, `windows-latest`, and `macos-latest` runners.

<Note>
This page documents the action itself. For a broader guide to using Kosli in GitHub Actions, including the command flags that are defaulted from GitHub CI variables, see [CI/CD](/integrations/ci_cd).
</Note>

## Usage

Install the latest release of the Kosli CLI:

```yaml
steps:
  - uses: kosli-dev/setup-cli-action@v5
```

Install a specific version:

```yaml
steps:
  - name: Setup Kosli CLI
    uses: kosli-dev/setup-cli-action@v5
    with:
      version: 2.11.43
```

## Inputs

| Input | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `version` | No | `latest` | Version of the Kosli CLI to install. See [Version selection](#version-selection). |
| `github-token` | No | `${{ github.token }}` | Token used to authenticate the GitHub API calls that resolve `latest` or a major/minor pin. You normally do not need to set this. |

## Outputs

| Output | Description |
| :--- | :--- |
| `version` | The resolved Kosli CLI version that was installed. When `version` is `latest` or a major/minor pin, this is the concrete semver that was selected (e.g. `2.12.0`). |

Reference the resolved version in later steps:

```yaml
steps:
  - name: Setup Kosli CLI
    id: setup
    uses: kosli-dev/setup-cli-action@v5

  - name: Print installed version
    run: echo "Installed Kosli CLI ${{ steps.setup.outputs.version }}"
```

## Version selection

The `version` input accepts:

- **A full semver**, e.g. `2.11.43` — installed as-is.
- **A major pin**, e.g. `"2"` — resolves to the newest stable `2.x` release, and never `3.0.0`.
- **A major.minor pin**, e.g. `"2.11"` — resolves to the newest stable `2.11.z` patch.
- **`latest`** — resolves to the newest stable release of [`kosli-dev/cli`](https://github.com/kosli-dev/cli). This is the default.

Major and minor pins resolve at runtime and never select a pre-release or a higher major.

<Warning>
Quote partial versions. In YAML, `version: 2.10` is parsed as the number `2.1`, which is not what you mean. Always quote a major or minor pin: `version: "2"`, `version: "2.10"`.
</Warning>

Track a major version and pick up every update within it without ever jumping to the next (breaking) major:

```yaml
steps:
  - name: Setup Kosli CLI
    uses: kosli-dev/setup-cli-action@v5
    with:
      version: "2"   # newest stable 2.x, never 3.x
```

## Example job

Secrets in GitHub Actions are not automatically exported as environment variables, so set the API token explicitly. All CLI flags can be set as environment variables by adding the `KOSLI_` prefix and capitalizing them.

```yaml
jobs:
  build-image:
    runs-on: ubuntu-latest
    env:
      KOSLI_API_TOKEN: ${{ secrets.KOSLI_API_TOKEN }}
      KOSLI_ORG: my-org
      KOSLI_FLOW: my-flow
      KOSLI_TRAIL: ${{ github.sha }}
      IMAGE_NAME: my-registry/my-image:latest
    steps:
      - name: Build and push Docker image
        id: build
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: ${{ env.IMAGE_NAME }}

      - name: Setup Kosli CLI
        uses: kosli-dev/setup-cli-action@v5

      - name: Attest image provenance
        run: kosli attest artifact "${IMAGE_NAME}" --artifact-type=oci
```

For a complete example of a GitHub workflow using Kosli, see the Kosli CLI's [own workflow](https://github.com/kosli-dev/cli/blob/main/.github/workflows/docker.yml).

## References

- Action source: [`kosli-dev/setup-cli-action`](https://github.com/kosli-dev/setup-cli-action)
- Marketplace listing: [setup-kosli-cli](https://github.com/marketplace/actions/setup-kosli-cli)
- [CI/CD integration guide](/integrations/ci_cd)
- [Kosli CLI reference](/client_reference)
