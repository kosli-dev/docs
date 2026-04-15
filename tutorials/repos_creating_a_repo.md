---
title: "Creating a repository in Kosli"
description: "Learn how repositories are captured in Kosli and how to verify your repo appears after attesting artifacts."
---

Repositories in Kosli are automatically captured when attestations include repository metadata. This happens automatically when you use Kosli CLI v2.11.35 or higher inside a CI pipeline. By the end of this tutorial, you will have verified that Kosli captures your repository and learned how to list and inspect repos.

## Prerequisites

- [Install Kosli CLI](/getting_started/install) (v2.11.35 or higher).
- [Get a Kosli API token](/getting_started/service-accounts).
- Have a [Flow](/getting_started/flows) and [Trail](/getting_started/trails) already created.

## Setup

```shell
export KOSLI_ORG=<your-org>
export KOSLI_API_TOKEN=<your-api-token>
```

## How repos are created

You do not create repos manually. Kosli captures repository information from attestations that include repo metadata. In CI environments, the CLI automatically populates these fields from environment variables (e.g. `GITHUB_REPOSITORY` in GitHub Actions).

You can also provide repo metadata explicitly using these flags on `kosli attest` and `kosli begin trail` commands:

| Flag | Description |
|---|---|
| `--repository` | Name of the git repo as registered in Kosli (e.g. `my-org/my-repo`) |
| `--repo-provider` | VCS provider: `github`, `gitlab`, `bitbucket`, or `azure-devops` |
| `--repo-url` | URL of the repository |
| `--repo-id` | Unique identifier of the repository in the VCS provider |

## Attest an artifact with repo metadata

If you are running outside of CI, provide the repo flags explicitly:

```shell
kosli attest artifact my-app:latest \
    --name my-app \
    --flow my-flow \
    --trail my-trail \
    --artifact-type oci \
    --repository my-org/my-repo \
    --repo-provider github \
    --repo-url https://github.com/my-org/my-repo \
    --commit $(git rev-parse HEAD)
```

## List repos

After attesting, verify that Kosli captured your repository:

```shell
kosli list repos
```

You can also filter by VCS provider:

```shell
kosli list repos --provider github
```

## Get repo details

Inspect a specific repo:

```shell
kosli get repo my-org/my-repo
```

## What you've accomplished

You have learned how Kosli automatically captures repositories from attestations and how to list and inspect them.

From here you can:

- [Track builds from a repository](/tutorials/repos_tracking_builds)
- [Track deployments from a repository](/tutorials/repos_tracking_deployments)
- [View live artifacts from a repository](/tutorials/repos_viewing_live_artifacts)
