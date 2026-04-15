---
title: Working with repositories
description: Learn how VCS code repositories are captured in Kosli and how to view builds, deployments, and live artifacts from the Kosli app.
---

Repositories in Kosli refer to your version control (VCS) code repositories — such as those hosted on GitHub, GitLab, Bitbucket, or Azure DevOps. By connecting your code repositories to Kosli, you get a repo-centric view of your software supply chain. Instead of navigating across flows, trails, and environments separately, you can start from a repository and see everything that matters: what was built, where it was deployed, and what is running right now.

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
| `--repository` | Name of the git repo as registered in Kosli (e.g. `my-org/my-repo`). |
| `--repo-provider` | VCS provider: `github`, `gitlab`, `bitbucket`, or `azure-devops`. Must be one of these values if provided. |
| `--repo-url` | URL of the repository. Must be a valid URL with a scheme and host (see URL format details below). |
| `--repo-id` | Unique identifier of the repository in the VCS provider (see choosing a repo ID below). |

All four flags are needed to fully populate repository information in Kosli. In [supported CI systems](/integrations/ci_cd), some of these flags are auto-defaulted from environment variables. In unsupported CI systems (e.g. Jenkins), you must provide all flags explicitly.

### `--repo-url` format

The `--repo-url` flag must be a valid URL with a scheme (`https://`) and a host. The CLI validates this when the flag is provided.

- **HTTPS web URLs** (recommended): `https://github.com/my-org/my-repo` or `https://bitbucket.org/my-workspace/my-repo`
- **HTTPS clone URLs**: `https://bitbucket.org/my-workspace/my-repo.git` — these pass validation and work, but we recommend dropping the `.git` suffix for consistency with how Kosli displays the URL in the app and CLI output.
- **SSH clone URLs**: `git@github.com:my-org/my-repo.git` — these **do not work** because they lack a URL scheme and fail CLI validation.

<Tip>
Use the plain web URL without `.git` (e.g. `https://bitbucket.org/my-workspace/my-repo`). This is the canonical format used across Kosli and matches what appears in the UI and CLI output.
</Tip>

### Choosing a `--repo-id`

The `--repo-id` should be a **stable, unique identifier** for the repository in your VCS provider. Avoid using the repository name, as it can change if the repo is renamed or moved to another provider.

Good choices for `--repo-id`:
- **GitHub**: The numeric repository ID (available via the GitHub API).
- **GitLab**: The `CI_PROJECT_ID` environment variable.
- **Bitbucket**: The `BITBUCKET_REPO_UUID` environment variable (available in Bitbucket Pipelines). If running in Jenkins with a Bitbucket repo, retrieve this value from the Bitbucket API or check a UUID into the repo in a file.
- **Azure DevOps**: The `Build.Repository.ID` predefined variable.

### Using repo flags in unsupported CI systems

If your CI system is not in the [list of supported CI systems](/integrations/ci_cd) (e.g. Jenkins, Bamboo), the CLI cannot auto-default repo metadata from environment variables. You must provide all four flags explicitly — `--repository`, `--repo-provider`, `--repo-url`, and `--repo-id`.

For example, in a Jenkinsfile for a Bitbucket repository:

```shell
kosli attest artifact my-app:latest \
    --name my-app \
    --flow my-flow \
    --trail my-trail \
    --artifact-type oci \
    --repository my-workspace/my-repo \
    --repo-provider bitbucket \
    --repo-url https://bitbucket.org/my-workspace/my-repo \
    --repo-id "${BITBUCKET_REPO_UUID}" \
    --commit $(git rev-parse HEAD)
```

### Attest an artifact with repo metadata

If you are running outside of CI or in an unsupported CI system, provide the repo flags explicitly:

```shell
kosli attest artifact my-app:latest \
    --name my-app \
    --flow my-flow \
    --trail my-trail \
    --artifact-type oci \
    --repository my-org/my-repo \
    --repo-provider github \
    --repo-url https://github.com/my-org/my-repo \
    --repo-id 123456789 \
    --commit $(git rev-parse HEAD)
```

### Verify your repository in Kosli

After attesting, verify that Kosli captured your repository using the CLI:

```shell
kosli list repos
```

You should also be able to see the repository in the [Kosli app](https://app.kosli.com) by navigating to **Repositories** in the sidebar. Your newly captured repository appears in the list, and you can search by name to find it.

<Frame><img src="/images/repos-list.png" alt="Kosli app showing the repositories list with repos from multiple VCS providers" /></Frame>

## Tracking builds

A build is recorded in Kosli the first time you attest an artifact. Subsequent attestations for that artifact fingerprint do not create additional build records.

Tracking builds per repository helps you understand your team's development cadence. You can see how frequently new artifacts are produced and spot changes in build activity over time — for example, a sudden drop may indicate a blocked pipeline, while a spike could signal a release push.

### View build metrics in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Build** tab. This view shows:

- **Build frequency chart** — a visualization of how often builds occur over a configurable time period (last 7, 14, 28, or 90 days).
- **Builds list** — a paginated list of individual builds within the selected period, including commit details and timestamps.

Use the time period selector to adjust the range and analyze build trends.

<Frame><img src="/images/repos-build-frequency.png" alt="Kosli app showing the Build tab with build frequency chart and builds list" /></Frame>

## Tracking deployments

Kosli detects deployments automatically when an artifact appears in an [environment snapshot](/getting_started/environments). If the artifact was attested with repository metadata, the deployment is linked back to the source repository. For details on reporting snapshots, see [reporting Kubernetes environments](/tutorials/report_k8s_envs) or [reporting AWS environments](/tutorials/report_aws_envs).

Tracking deployments per repository gives you visibility into how changes flow from build to production. You can measure deployment frequency and lead time for changes — two of the four DORA metrics — broken down by environment.

### View deployment metrics in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Release** tab. This tab has two sub-views:

**Metrics** — shows per-environment charts for:
- **Deployment frequency** — how often deployments happen over a configurable time period.
- **Lead time for changes** — how long it takes from build to deployment.

<Frame><img src="/images/repos-release-metrics.png" alt="Kosli app showing the Release Metrics view with deployment lead time and deployment frequency charts" /></Frame>

**Deployments** — shows a paginated list of individual deployments with:
- Which environment received the artifact.
- The commit and artifact details.
- Time period and environment filtering to compare deployment patterns across staging, production, etc.

<Frame><img src="/images/repos-release-deployments.png" alt="Kosli app showing the Release Deployments view with a list of deployments per environment" /></Frame>

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

<Frame><img src="/images/repos-run-tab.png" alt="Kosli app showing the Run tab with live artifacts, their commits, environments, and compliance status" /></Frame>

## What you've accomplished

You have learned how Kosli automatically captures repositories from attestations and how to use the Kosli app to monitor builds, deployments, and live artifacts for a repository.

From here you can:

- Learn more about [environments](/getting_started/environments)
- Learn more about [attestations](/getting_started/attestations)
- [Query Kosli](/tutorials/querying_kosli) for detailed artifact provenance
