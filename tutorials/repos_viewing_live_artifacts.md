---
title: "Viewing live artifacts from a repository"
description: "Learn how to see which artifacts from a repository are currently running across your environments in Kosli."
---

Kosli provides a live view of all artifacts from a given repository that are currently running across your environments. By the end of this tutorial, you will have queried the live status of a repository's artifacts and understood the information returned.

## Prerequisites

- [Install Kosli CLI](/getting_started/install) (v2.11.35 or higher).
- [Get a Kosli API token](/getting_started/service-accounts).
- Have at least one [environment](/getting_started/environments) actively reporting snapshots.
- Have [attested artifacts](/getting_started/artifacts) linked to a repository that are currently deployed.

## Setup

```shell
export KOSLI_ORG=<your-org>
export KOSLI_API_TOKEN=<your-api-token>
```

## Query live artifacts via the API

Use the Kosli API to get all currently running artifacts from a repository:

```shell
curl -H "Authorization: Bearer ${KOSLI_API_TOKEN}" \
    "https://app.kosli.com/api/v2/repos/${KOSLI_ORG}/live-artifacts/my-org%2Fmy-repo"
```

<Note>
  URL-encode the repo name if it contains a slash. For example, `my-org/my-repo` becomes `my-org%2Fmy-repo`.
</Note>

The response includes:

- **environments** -- which environments currently have running artifacts from this repo
- **artifacts** -- the artifacts running in those environments
- **live_artifacts** -- a flattened view with compliance status, fingerprint, commit SHA, and start timestamp for each running artifact

If multiple repos share the same name across VCS providers, add the `provider` query parameter:

```shell
curl -H "Authorization: Bearer ${KOSLI_API_TOKEN}" \
    "https://app.kosli.com/api/v2/repos/${KOSLI_ORG}/live-artifacts/my-org%2Fmy-repo?provider=github"
```

## View live artifacts in the Kosli app

In the [Kosli app](https://app.kosli.com):

1. Navigate to **Repositories** in the sidebar.
2. Select your repository.
3. The overview shows currently running artifacts across all environments, including their compliance state.

## Trace a running artifact back to source

When you find an artifact running in an environment, use `kosli search` with its commit SHA or fingerprint to get its full provenance:

```shell
kosli search <commit-sha>
```

This shows the artifact's build origin, attestations, and full deployment history.

## What you've accomplished

You have queried the live status of artifacts from a repository across all environments and traced running artifacts back to their source.

From here you can:

- [Create a repository in Kosli](/tutorials/repos_creating_a_repo)
- [Track builds from a repository](/tutorials/repos_tracking_builds)
- Learn more about [querying Kosli](/tutorials/querying_kosli)
