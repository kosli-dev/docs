---
title: "Tracking deployments from a repository"
description: "Learn how to track deployments of artifacts from a repository to your runtime environments in Kosli."
---

Kosli tracks deployments by recording environment snapshots and matching running artifacts back to their source repositories. By the end of this tutorial, you will have tracked a deployment from a repository to an environment and queried deployment history.

## Prerequisites

- [Install Kosli CLI](/getting_started/install) (v2.11.35 or higher).
- [Get a Kosli API token](/getting_started/service-accounts).
- Have a [Kosli environment](/getting_started/environments) configured and reporting snapshots.
- Have at least one [attested artifact](/getting_started/artifacts) linked to a repository.

## Setup

```shell
export KOSLI_ORG=<your-org>
export KOSLI_API_TOKEN=<your-api-token>
```

## How deployment tracking works

Kosli detects deployments automatically when an artifact appears in an environment snapshot. If the artifact was attested with repository metadata, the deployment is linked back to the source repository.

The typical flow is:

1. Attest an artifact with repo metadata during your CI build.
2. Deploy the artifact to your runtime environment.
3. Report a snapshot of the environment to Kosli.
4. Kosli records that the artifact from your repo is now running.

## Report an environment snapshot

After deploying your artifact, snapshot the environment:

<Tabs>
<Tab title="Docker">
```shell
kosli snapshot docker my-environment
```
</Tab>
<Tab title="Kubernetes">
```shell
kosli snapshot k8s my-environment
```
</Tab>
<Tab title="ECS">
```shell
kosli snapshot ecs my-environment \
    --cluster my-cluster
```
</Tab>
</Tabs>

## View environment events filtered by repo

Use the environment log to see events for a specific repository:

```shell
kosli log environment my-environment \
    --repo my-org/my-repo
```

This shows when artifacts from your repo started running, scaled, or stopped in the environment.

## Search for a deployment by commit

Use `kosli search` with a commit SHA to trace a specific change through to its deployment:

```shell
kosli search <commit-sha>
```

The output includes the full history of the artifact built from that commit, including which environments it was deployed to and when.

## View deployments in the Kosli app

In the [Kosli app](https://app.kosli.com), navigate to your repository and open the **Deployments** tab to see:

- Which environments received artifacts from this repo
- Deployment frequency over time
- Filtering by environment

## What you've accomplished

You have tracked a deployment from a repository to a runtime environment and queried deployment history by repo.

From here you can:

- [View currently running artifacts from a repository](/tutorials/repos_viewing_live_artifacts)
- Learn more about [environments](/getting_started/environments)
- [Compare environment snapshots](/client_reference/kosli_diff_snapshots)
