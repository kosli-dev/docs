---
title: Working with repositories
description: Learn how repositories are captured in Kosli and how to view builds, deployments, and live artifacts from the Kosli app.
---

Repositories in Kosli are automatically captured when attestations include repository metadata. Once captured, you can view build history, track deployments, and see live artifacts across your environments — all from the Kosli app.

## Prerequisites

- [Install Kosli CLI](/getting_started/install) (v2.11.35 or higher).
- [Get a Kosli API token](/getting_started/service-accounts).
- Have a [Flow](/getting_started/flows) and [Trail](/getting_started/trails) already created.

## Setup

```shell
export KOSLI_ORG=<your-org>
export KOSLI_API_TOKEN=<your-api-token>
```

## Creating a repository

You do not create repos manually. Kosli captures repository information from attestations that include repo metadata. In CI environments, the CLI automatically populates these fields from environment variables (e.g. `GITHUB_REPOSITORY` in GitHub Actions).

You can also provide repo metadata explicitly using these flags on `kosli attest` and `kosli begin trail` commands:

| Flag | Description |
|---|---|
| `--repository` | Name of the git repo as registered in Kosli (e.g. `my-org/my-repo`) |
| `--repo-provider` | VCS provider: `github`, `gitlab`, `bitbucket`, or `azure-devops` |
| `--repo-url` | URL of the repository |
| `--repo-id` | Unique identifier of the repository in the VCS provider |

### Attest an artifact with repo metadata

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

### Verify your repository in Kosli

After attesting, verify that Kosli captured your repository using the CLI:

```shell
kosli list repos
```

You can also see the repository in the [Kosli app](https://app.kosli.com) by navigating to **Repositories** in the sidebar. Your newly captured repository should appear in the list.

To inspect a specific repo:

```shell
kosli get repo my-org/my-repo
```

## Tracking builds

A build is recorded in Kosli the first time you attest an artifact. Subsequent attestations on the same trail do not create additional build records.

### View build metrics in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Builds** tab. This view shows:

- **Build frequency chart** — a visualization of how often builds occur over a configurable time period (last 7, 14, 28, or 90 days).
- **Builds list** — a paginated list of individual builds within the selected period, including commit details and timestamps.

Use the period selector to adjust the time range and analyze build trends.

## Tracking deployments

Kosli detects deployments automatically when an artifact appears in an [environment snapshot](/getting_started/environments). If the artifact was attested with repository metadata, the deployment is linked back to the source repository.

The typical flow is:

1. Attest an artifact with repo metadata during your CI build.
2. Deploy the artifact to your runtime environment.
3. Report a snapshot of the environment to Kosli (see [reporting Kubernetes environments](/tutorials/report_k8s_envs) or [reporting AWS environments](/tutorials/report_aws_envs)).
4. Kosli records that the artifact from your repo is now running.

### View deployment metrics in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Releases** tab. This view provides:

- **Deployment frequency** — a chart showing how often deployments happen over a configurable time period.
- **Lead time** — metrics showing how long it takes from build to deployment.
- **Deployments list** — a paginated list of individual deployments with details on which environments received artifacts, filtered by time period.
- **Environment filtering** — narrow results to a specific environment to compare deployment patterns across staging, production, etc.

## Viewing live artifacts

Kosli provides a real-time view of all artifacts from a repository that are currently running across your environments.

### View live status in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Run** tab. This view shows:

- **Commits currently running** — artifacts grouped by commit, showing which commit is deployed where.
- **Environment details** — for each commit, the environments where its artifacts are running, including environment type and snapshot information.
- **Compliance status** — whether each running artifact is compliant or non-compliant.
- **Environment filtering** — filter the view by specific environments to focus on what matters.

## What you've accomplished

You have learned how Kosli automatically captures repositories from attestations and how to use the Kosli app to monitor builds, deployments, and live artifacts for a repository.

From here you can:

- Learn more about [environments](/getting_started/environments)
- Learn more about [attestations](/getting_started/attestations)
- [Query Kosli](/tutorials/querying_kosli) for detailed artifact provenance
