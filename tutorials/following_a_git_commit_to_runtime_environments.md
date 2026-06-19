---
title: From commit to production
description: "In this 5 minute tutorial you'll learn how Kosli tracks \"life after git\" and shows you events from CI pipelines (eg, building the docker image, running the unit tests, deploying, etc) and runtime environments (eg, the blue-green rollover, instance scaling, etc)"
---

We will follow an actual git commit from a CI pipeline all the way into production runtime environments.
By the end, you will have queried Kosli to see an artifact's history — from creation in CI through running in production to eventual shutdown — without any access to the production environment.

We will use **cyber-dojo**, an open-source microservice platform whose Kosli data is public.
The commit we follow fixed a misconfiguration: `runner` should run with three replicas but was accidentally running with one after a migration from GKE to ECS.

<Info>
[cyber-dojo](https://cyber-dojo.org) is a web platform where teams practice TDD. It has a dozen microservices, each with its own GitHub Actions CI pipeline producing a Docker image, running in two AWS environments: `aws-beta` and `aws-prod`.
</Info>

## Prerequisites

* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/authenticating_to_kosli).

## Setup

Set your environment variables to use the public `cyber-dojo` Kosli organization:

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
NAME                        DESCRIPTION                                               VISIBILITY  TAGS
creator-ci                  UX for Group/Kata creation                                private     [ci=github], [repo_url=https://github.com/cyber-dojo/creator], [kind=build], [env=aws-beta]
custom-start-points-ci      Custom exercises choices                                  private     [env=aws-beta], [ci=github], [repo_url=https://github.com/cyber-dojo/custom-start-points], [kind=build]
dashboard-ci                UX for a group practice dashboard                         private     [ci=github], [repo_url=https://github.com/cyber-dojo/dashboard], [kind=build], [env=aws-beta]
differ-ci                   Diff files from two traffic-lights                        private     [env=aws-beta], [ci=github], [repo_url=https://github.com/cyber-dojo/differ], [kind=build]
differ-ci-tf                Terraform human-readable plan and state file fingerprint  private
docker-base-ci              Build cyber-dojo/docker-base image                        private
exercises-start-points-ci   Exercises choices                                         private     [ci=github], [repo_url=https://github.com/cyber-dojo/exercises-start-points], [kind=build], [env=aws-beta]
languages-start-points-ci   Language+TestFramework choices                            private     [ci=github], [repo_url=https://github.com/cyber-dojo/languages-start-points], [kind=build], [env=aws-beta]
nginx-ci                    Reverse proxy                                             private     [kind=build], [env=aws-beta], [ci=github], [repo_url=https://github.com/cyber-dojo/nginx]
production-promotion        Promotes sets of Artifacts from aws-beta to aws-prod      private     [ci=github], [repo_url=https://github.com/cyber-dojo/aws-prod-co-promotion], [kind=release], [env=aws-prod]
production-server-access    Flow to track production server access                    private
runner-ci                   Test runner                                               private     [ci=github], [repo_url=https://github.com/cyber-dojo/runner], [kind=build], [env=aws-beta]

...some output elided...
```

## Follow the artifact

The commit that fixed the replica count was [16d9990](https://github.com/cyber-dojo/runner/commit/16d9990ad23a40eecaf087abac2a58a2d2a4b3f4) in the `runner` repository. Fetch its history from Kosli with `kosli search`, which accepts a git commit (full or short-form) or an artifact fingerprint:

```shell
kosli search 16d9990
```

You will see:

```plaintext
Search result resolved to commit 16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
Name:              cyberdojo/runner:16d9990
Fingerprint:       9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625
Has provenance:    true
Flow:              runner-archived-at-1709658802
Git commit:        16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
Commit URL:        https://github.com/cyber-dojo/runner/commit/16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
Build URL:         https://github.com/cyber-dojo/runner/actions/runs/2902808452
Artifact URL:      https://app.kosli.com/cyber-dojo/flows/runner-archived-at-1709658802/artifacts/9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625
Compliance state:  COMPLIANT
Running in:        [  ]
Exited from:       [ aws-beta, aws-prod ]
History:
    Artifact created                               Mon, 22 Aug 2022 11:35:00 CEST
    Started running in aws-beta#84 environment     Mon, 22 Aug 2022 11:38:28 CEST
    Started running in aws-prod#65 environment     Mon, 22 Aug 2022 11:39:22 CEST
    No longer running in aws-beta#119 environment  Wed, 24 Aug 2022 18:05:42 CEST
    No longer running in aws-prod#96 environment   Wed, 24 Aug 2022 18:12:28 CEST
```

<Info>
When this commit was made, the runner repository reported to a flow simply named `runner`. cyber-dojo's flows have since been reorganized (today the repository reports to `runner-ci`, as the flow list above shows) and the original flows archived. Archiving a flow currently renames it by appending `-archived-at-<timestamp>`, which is why the historical evidence displays the longer name.
</Info>

The **History** shows the artifact's lifecycle: created by CI, running in both environments, and eventually replaced by a newer version. `Has provenance: true` means the artifact was reported to Kosli by a CI pipeline, so its build history is known. The compliance state `COMPLIANT` means all required evidence was provided before deployment.

The same information is available in the [Kosli web interface](https://app.kosli.com/cyber-dojo/flows/runner-archived-at-1709658802/artifacts/9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625).

## Inspect the environment snapshot

The History shows the artifact started running in snapshot `aws-prod#65`. Query that snapshot to see everything running in production at that moment:

```shell
kosli get snapshot aws-prod#65
```

The output will be:

```plaintext
COMMIT   ARTIFACT                                                                              FLOW                                           COMPLIANCE  RUNNING_SINCE  REPLICAS
16d9990  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/runner:16d9990                  runner-archived-at-1709658802                  COMPLIANT   2022-08-22     3
         Fingerprint: 9af401c4350b21e3f1df17d6ad808da43d9646e75b6da902cc7c492bcfb9c625

7c45272  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/shas:7c45272                    shas-archived-at-1705491385                    COMPLIANT   2022-08-22  1
         Fingerprint: 76c442c04283c4ca1af22d882750eb960cf53c0aa041bbdb2db9df2f2c1282be

...some output elided...

85d83c6  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/runner:85d83c6                  runner-archived-at-1709658802                  COMPLIANT   2022-08-20  1
         Fingerprint: eeb0cfc9ee7f69fbd9531d5b8c1e8d22a8de119e2a422344a714a868e9a8bfec

1a2b170  Name: 274425519734.dkr.ecr.eu-central-1.amazonaws.com/differ:1a2b170                  differ-archived-at-1707630536                  COMPLIANT   2022-08-20  1
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
     Flow:         runner-archived-at-1709658802
     Commit URL:   https://github.com/cyber-dojo/runner/commit/16d9990ad23a40eecaf087abac2a58a2d2a4b3f4
     Started:      Mon, 22 Aug 2022 11:39:17 CEST • 2022-08-22
     Instances:    3
```

This confirms that `runner:16d9990` is the only new artifact in snapshot 65 — exactly the commit that fixed the replica count.

## What you've accomplished

You have traced a git commit from its creation in CI through deployment and into production, querying its compliance state, runtime replicas, and the exact moment it appeared in the environment — all without any direct access to `aws-prod`.

From here you can:
* Explore more of cyber-dojo's data at [app.kosli.com/cyber-dojo](https://app.kosli.com/cyber-dojo)
* Learn how to report your own environments with [`kosli snapshot`](/client_reference/kosli_snapshot_k8s)
* Set up your own flows and trails with the [Getting started guide](/getting_started/flows)
