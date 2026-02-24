---
title: From commit to production
description: "In this 5 minute tutorial you'll learn how Kosli tracks \"life after git\" and shows you events from CI pipelines (eg, building the docker image, running the unit tests, deploying, etc) and runtime environments (eg, the blue-green rollover, instance scaling, etc)"
---

We will follow an actual git commit from a CI pipeline all the way into production runtime environments.
By the end, you will have queried Kosli to see an artifact's full history — from creation through deployment to scaling and shutdown — without any access to the production environment.

We will use **cyber-dojo**, an open-source microservice platform whose Kosli data is public.
The commit we follow fixed a misconfiguration: `runner` should run with three replicas but was accidentally running with one after a migration from GKE to ECS.

<Info>
[cyber-dojo](https://cyber-dojo.org) is a web platform where teams practice TDD. It has a dozen microservices, each with its own GitHub Actions CI pipeline producing a Docker image, running in two AWS environments: `aws-beta` and `aws-prod`.
</Info>

## Prerequisites

* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).

## Setup

Set your environment variables to use the public `cyber-dojo` Kosli organisation:

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=<your-api-token>
```

## List flows

Find out which `cyber-dojo` repositories have a CI pipeline reporting to Kosli:

```shell
kosli list flows
```

You will see:

```plaintext
NAME                    DESCRIPTION                         VISIBILITY
creator                 UX for Group/Kata creation          public
custom-start-points     Custom exercises choices            public
dashboard               UX for a group practice dashboard   public
differ                  Diff files from two traffic-lights  public
exercises-start-points  Exercises choices                   public
languages-start-points  Language+TestFramework choices      public
nginx                   Reverse proxy                       public
repler                  REPL for Python images              public
runner                  Test runner                         public
saver                   Group/Kata model+persistence        public
version-reporter        UX for git+image version-reporter   public
web                     UX for practicing TDD               public
```

## Follow the artifact

The commit that fixed the replica count was [16d9990](https://github.com/cyber-dojo/runner/commit/16d9990ad23a40eecaf087abac2a58a2d2a4b3f4) in the `runner` repository. Fetch its full history from Kosli:

```shell
kosli get artifact runner:16d9990
```

You will see:

```plaintext
Name:         cyberdojo/runner:16d9990
Flow:         runner
Fingerprint:  9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625
Created on:   Mon, 22 Aug 2022 11:35:00 CEST • 15 days ago
Git commit:   16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
Commit URL:   https://github.com/cyber-dojo/runner/commit/16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
Build URL:    https://github.com/cyber-dojo/runner/actions/runs/2902808452
State:        COMPLIANT
History:
    Artifact created                                     Mon, 22 Aug 2022 11:35:00 CEST
    branch-coverage evidence received                    Mon, 22 Aug 2022 11:36:02 CEST
    Deployment #18 to aws-beta environment               Mon, 22 Aug 2022 11:37:17 CEST
    Deployment #19 to aws-prod environment               Mon, 22 Aug 2022 11:38:21 CEST
    Started running in aws-beta#84 environment           Mon, 22 Aug 2022 11:38:28 CEST
    Started running in aws-prod#65 environment           Mon, 22 Aug 2022 11:39:22 CEST
    Scaled down from 3 to 2 in aws-beta#117 environment  Wed, 24 Aug 2022 18:03:42 CEST
    No longer running in aws-beta#119 environment        Wed, 24 Aug 2022 18:05:42 CEST
    Scaled down from 3 to 1 in aws-prod#94 environment   Wed, 24 Aug 2022 18:10:28 CEST
    No longer running in aws-prod#96 environment         Wed, 24 Aug 2022 18:12:28 CEST
```

The **History** shows the artifact's complete lifecycle: created by CI, evidence attested, deployed to both environments, running with the correct 3 replicas, then eventually scaled down and replaced by a newer version. The state `COMPLIANT` means all required evidence was provided before deployment.

The same information is available in the [Kosli web interface](https://app.kosli.com/cyber-dojo/flows/runner/artifacts/9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625).

## Inspect the environment snapshot

The History shows the artifact started running in snapshot `aws-prod#65`. Query that snapshot to see everything running in production at that moment:

```shell
kosli get snapshot aws-prod#65
```

The output will be:

```plaintext
COMMIT   ARTIFACT                                                                         FLOW       RUNNING_SINCE  REPLICAS
16d9990  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/runner:16d9990             runner     11 days ago    3
         Fingerprint: 9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625

7c45272  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/shas:7c45272               shas       11 days ago    1
         Fingerprint: 76c442c04283c4ca1af22d882750eb960cf53c0aa041bbdb2db9df2f2c1282be

...some output elided...

85d83c6  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/runner:85d83c6             runner     13 days ago    1
         Fingerprint: eeb0cfc9ee7f69fbd9531d5b8c1e8d22a8de119e2a422344a714a868e9a8bfec

1a2b170  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/differ:1a2b170             differ     13 days ago    1
         Fingerprint: d8440b94f7f9174c180324ceafd4148360d9d7c916be2b910f132c58b8a943ae
```

You can see `runner:16d9990` is running with 3 replicas — the fix worked. You also notice two versions of `runner` running simultaneously: this is a blue-green deployment in progress. `runner:85d83c6` (the old version, 1 replica) will be stopped in the next snapshot.

## Diff two snapshots

To see exactly what changed between snapshots `aws-prod#64` and `aws-prod#65`:

```shell
kosli diff snapshots aws-prod#64 aws-prod#65
```

The response will be:

```plaintext
Only present in aws-prod#65

     Name:         274425519734.dkr.ecr.eu-central-1.amazonaws.com/runner:16d9990
     Fingerprint:  9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625
     Flow:         runner
     Commit URL:   https://github.com/cyber-dojo/runner/commit/16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
     Started:      Mon, 22 Aug 2022 11:39:17 CEST • 15 days ago
```

This confirms that `runner:16d9990` is the only new artifact in snapshot 65 — exactly the commit that fixed the replica count.

## What you've accomplished

You have traced a git commit from its creation in CI through deployment and into production, querying its compliance state, runtime replicas, and the exact moment it appeared in the environment — all without any direct access to `aws-prod`.

From here you can:
* Explore more of cyber-dojo's data at [app.kosli.com/cyber-dojo](https://app.kosli.com/cyber-dojo)
* Learn how to report your own environments with [`kosli snapshot`](/client_reference/kosli_snapshot_k8s)
* Set up your own flows and trails with the [Getting started guide](/getting_started/flows)
