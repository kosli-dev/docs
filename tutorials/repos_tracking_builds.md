---
title: "Tracking builds from a repository"
description: "Learn how to track builds originating from a repository in Kosli using the CLI and API."
---

Kosli tracks builds associated with your repositories. A build is recorded when you attest an artifact as part of a trail. By the end of this tutorial, you will have filtered builds by repository and inspected build details.

## Prerequisites

- [Install Kosli CLI](/getting_started/install) (v2.11.35 or higher).
- [Get a Kosli API token](/getting_started/service-accounts).
- Have at least one [attested artifact](/getting_started/artifacts) linked to a repository.

## Setup

```shell
export KOSLI_ORG=<your-org>
export KOSLI_API_TOKEN=<your-api-token>
```

## Record a build

Builds are recorded when you attest artifacts on a trail. Begin a trail and attest an artifact:

```shell
kosli begin trail my-trail \
    --flow my-flow \
    --repository my-org/my-repo \
    --repo-provider github
```

```shell
kosli attest artifact my-app:latest \
    --name my-app \
    --flow my-flow \
    --trail my-trail \
    --artifact-type oci \
    --commit $(git rev-parse HEAD)
```

Each attestation contributes to the build record for the trail.

## List builds for a repository

Use the Kosli API to list builds filtered by repository name:

```shell
curl -H "Authorization: Bearer ${KOSLI_API_TOKEN}" \
    "https://app.kosli.com/api/v2/builds/${KOSLI_ORG}?repo_name=my-org/my-repo"
```

{/* TODO: Verify if `kosli list builds` CLI command exists - only API endpoint confirmed */}

## Filter artifacts by repository

List artifacts from a specific repository using the CLI:

```shell
kosli list artifacts --flow my-flow --repo my-org/my-repo
```

## View build details in the Kosli app

Navigate to **Repositories** in the [Kosli app](https://app.kosli.com), select your repository, and open the **Releases** tab to see build history, deployment frequency, and individual run details.

## What you've accomplished

You have recorded builds via attestations and filtered build data by repository.

From here you can:

- [Track deployments from a repository](/tutorials/repos_tracking_deployments)
- [View live artifacts from a repository](/tutorials/repos_viewing_live_artifacts)
- Learn more about [attestations](/getting_started/attestations)
