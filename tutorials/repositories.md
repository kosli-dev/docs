---
title: Working with repositories
description: Learn how repositories are captured in Kosli and how to view builds, deployments, and live artifacts from the Kosli app.
---

Repositories in Kosli give you a repo-centric view of your software supply chain. Instead of navigating across flows, trails, and environments separately, you can start from a repository and see everything that matters: what was built, where it was deployed, and what is running right now.

This is useful when you need to:

- **Answer audit questions quickly** — "What version of this repo is running in production?" or "How often do we deploy this service?"
- **Track DORA-style metrics per repo** — build frequency, deployment frequency, and lead time for changes, broken down by environment.
- **Verify compliance at a glance** — see which commits are currently running across all environments and whether their artifacts are compliant.
- **Investigate incidents** — trace a running artifact back to its source commit, build, and full attestation history.

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

You should also be able to see the repository in the [Kosli app](https://app.kosli.com) by navigating to **Repositories** in the sidebar. Your newly captured repository appears in the list, and you can search by name to find it.

## Tracking builds

A build is recorded in Kosli the first time you attest an artifact. Subsequent attestations for that artifact fingerprint do not create additional build records.

Tracking builds per repository helps you understand your team's development cadence. You can see how frequently new artifacts are produced and spot changes in build activity over time — for example, a sudden drop may indicate a blocked pipeline, while a spike could signal a release push.

### View build metrics in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Build** tab. This view shows:

- **Build frequency chart** — a visualization of how often builds occur over a configurable time period (last 7, 14, 28, or 90 days).
- **Builds list** — a paginated list of individual builds within the selected period, including commit details and timestamps.

Use the time period selector to adjust the range and analyze build trends.

## Tracking deployments

Kosli detects deployments automatically when an artifact appears in an [environment snapshot](/getting_started/environments). If the artifact was attested with repository metadata, the deployment is linked back to the source repository. For details on reporting snapshots, see [reporting Kubernetes environments](/tutorials/report_k8s_envs) or [reporting AWS environments](/tutorials/report_aws_envs).

Tracking deployments per repository gives you visibility into how changes flow from build to production. You can measure deployment frequency and lead time for changes — two of the four DORA metrics — broken down by environment.

### View deployment metrics in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Release** tab. This tab has two sub-views:

**Metrics** — shows per-environment charts for:
- **Deployment frequency** — how often deployments happen over a configurable time period.
- **Lead time for changes** — how long it takes from build to deployment.

**Deployments** — shows a paginated list of individual deployments with:
- Which environment received the artifact.
- The commit and artifact details.
- Time period and environment filtering to compare deployment patterns across staging, production, etc.

## Viewing live artifacts

The live artifacts view gives you an at-a-glance picture of what is currently running from a repository across all your environments. This allows you to see the compliance of the artifacts and the commit that each artifact was built from.

This is particularly useful for:
- **Incident response** — quickly identify which version of a service is running in production.
- **Drift detection** — spot when different environments are running different commits from the same repo.
- **Compliance audits** — verify that all running artifacts are compliant without checking each environment individually.

### View live status in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Run** tab. This view shows a table with:

- **Commit** — the source commit for each group of running artifacts, including the commit SHA, author, message, and timestamp.
- **Environment** — the environments where artifacts from that commit are running, with links to the relevant environment snapshot.
- **Artifact** — the individual artifacts running in each environment, with their compliance status (compliant or non-compliant) and fingerprint.

Use the environment filter to narrow the view to specific environments.

## What you've accomplished

You have learned how Kosli automatically captures repositories from attestations and how to use the Kosli app to monitor builds, deployments, and live artifacts for a repository.

From here you can:

- Learn more about [environments](/getting_started/environments)
- Learn more about [attestations](/getting_started/attestations)
- [Query Kosli](/tutorials/querying_kosli) for detailed artifact provenance
