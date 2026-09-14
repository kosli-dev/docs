---
title: "Querying Kosli"
description: "This tutorial shows you how to use Kosli's query commands to search for artifacts, inspect their history, and browse runtime environment snapshots."
---

`get`, `list`, `log`, and `diff` commands let you query everything Kosli knows about your artifacts and environments directly from your terminal.
By the end of this tutorial, you will have searched for an artifact by commit SHA, inspected its full history, browsed environment snapshots, and compared two snapshots to see what changed.

We will query **cyber-dojo**, an open-source project whose Kosli data is public.

## Prerequisites

* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/authenticating_to_kosli).

## Setup

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=<your-api-token>
```

Any valid Kosli API token can read cyber-dojo, because it is a public organization. If you don't have a token yet, the read-only cyber-dojo token shown in the [CLI reference live examples](/client_reference/kosli_list_flows#live-example) works for this tutorial.

## Search by commit SHA

If you have a git commit SHA, `kosli search` will find any artifact built from it:

```shell
kosli search 99d7b74
```

```
Search result resolved to commit 99d7b74f39e311d492902ad48dbe97da63f2c687
Name:              244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74
Fingerprint:       a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424
Has provenance:    true
Flow:              creator-ci
Git commit:        99d7b74f39e311d492902ad48dbe97da63f2c687
Commit URL:        https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687
Build URL:         https://github.com/cyber-dojo/creator/actions/runs/34443243072
Artifact URL:      https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424
Compliance state:  COMPLIANT
Running in:        [ aws-beta, aws-prod ]
Exited from:       [  ]
History:
    Commit 99d7b74                                Thu, 10 Sep 2026 07:58:56 CEST
    Artifact created                              Thu, 10 Sep 2026 08:01:20 CEST
    Started running in aws-beta#8339 environment  Thu, 10 Sep 2026 08:06:24 CEST
    Started running in aws-prod#5349 environment  Thu, 10 Sep 2026 08:55:58 CEST

[... further artifacts for this commit ...]
```

One commit can produce several artifacts, and `kosli search` prints each one as its own block. Here the same commit also produced Terraform state artifacts in other flows; those blocks are trimmed from the output above.

## List flows and artifacts

The search result tells us this artifact belongs to the `creator-ci` flow. If you don't know which flows exist in your org, you can list them all:

```shell
kosli list flows
```

```
NAME                    DESCRIPTION                         VISIBILITY  TAGS
creator-ci              UX for Group/Kata creation          private     [ci=github], [repo_url=https://github.com/cyber-dojo/creator], [kind=build], [env=aws-beta]
custom-start-points-ci  Custom exercises choices            private     [ci=github], [repo_url=https://github.com/cyber-dojo/custom-start-points], [kind=build], [env=aws-beta]
dashboard-ci            UX for a group practice dashboard   private     [ci=github], [repo_url=https://github.com/cyber-dojo/dashboard], [kind=build], [env=aws-beta]
differ-ci               Diff files from two traffic-lights  private     [ci=github], [repo_url=https://github.com/cyber-dojo/differ], [kind=build], [env=aws-beta]
[...]
web-ci                  UX for practicing TDD               private     [ci=github], [repo_url=https://github.com/cyber-dojo/web], [kind=build], [env=aws-beta]
```

The `VISIBILITY` column is a legacy per-flow field and does not affect who can read a flow. Access is determined by the organization's visibility. cyber-dojo is a public organization, so any valid Kosli API token can read every flow listed here.

Once you know the flow name, you can list the artifacts reported to it:

```shell
kosli list artifacts --flow creator-ci
```

```
COMMIT   ARTIFACT                                                                       STATE      CREATED_AT
99d7b74  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74          COMPLIANT  Thu, 10 Sep 2026 08:01:20 CEST
         Fingerprint: a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424

abdc613  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:abdc613          COMPLIANT  Mon, 07 Sep 2026 12:56:13 CEST
         Fingerprint: ba988cfdac64da22bc8268442c467504fe8df565e65c2f3c4344ce00c83e561a

b1e77bf  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:b1e77bf          COMPLIANT  Thu, 03 Sep 2026 16:53:05 CEST
         Fingerprint: 3e2248d4cd5715c23ef4b322291cc34b48c741f5ea299f8681349529b0829d56
[...]
```

By default, the last 15 artifacts are shown. Use <Tooltip tip="Limit results per page, e.g. -n 5 to show only 5 artifacts.">-n</Tooltip> to change how many are shown, <Tooltip tip="Select a page of results, e.g. --page 2 to see the next page.">--page</Tooltip> to paginate, and <Tooltip tip="Change the output format, e.g. --output json to get JSON instead of a table.">--output</Tooltip> to change the format.

## Get an artifact

The artifact list gives you commit SHAs and fingerprints. Use either to fetch the full history of a specific artifact — the syntax is <Tooltip tip="Use flow:sha to identify by commit SHA (e.g. creator-ci:99d7b74), or flow@fingerprint to identify by fingerprint (e.g. creator-ci@a39fa32...).">flow:sha or flow@fingerprint</Tooltip>:

```shell
kosli get artifact creator-ci:99d7b74
```

```
Name:                     244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74
Flow:                     creator-ci
Trail:                    99d7b74f39e311d492902ad48dbe97da63f2c687
Name in template:         creator
Fingerprint:              a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424
Created on:               Thu, 10 Sep 2026 08:01:20 CEST • 4 days ago
Git commit:               99d7b74f39e311d492902ad48dbe97da63f2c687
Commit URL:               https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687
Build URL:                https://github.com/cyber-dojo/creator/actions/runs/34443243072
Artifact URL:             https://app.kosli.com/cyber-dojo/flows/creator-ci/artifacts/a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424
State:                    COMPLIANT
Running in environments:  aws-beta#8339, aws-prod#5349
History:
    creator reported                                                Thu, 10 Sep 2026 08:01:20 CEST
    Attestation creator.provenance-facts (custom:provenance-facts)  Thu, 10 Sep 2026 08:01:22 CEST
    Attestation creator.provenance-decision (decision)              Thu, 10 Sep 2026 08:01:28 CEST
    Attestation creator.sbom-facts (custom:sbom-facts)              Thu, 10 Sep 2026 08:01:31 CEST
    Attestation creator.sbom-decision (decision)                    Thu, 10 Sep 2026 08:01:44 CEST
    Attestation creator.snyk-container-scan (decision)              Thu, 10 Sep 2026 08:03:10 CEST
    Attestation creator.unit-test (junit)                           Thu, 10 Sep 2026 08:03:52 CEST
    Attestation creator.unit-test-coverage (generic)                Thu, 10 Sep 2026 08:03:54 CEST
    Deployment of creator in aws-beta#8339                          Thu, 10 Sep 2026 08:06:24 CEST
    Deployment of creator in aws-prod#5349                          Thu, 10 Sep 2026 08:55:58 CEST
```


## Browse environment snapshots

The artifact history shows it was deployed to `aws-beta` and `aws-prod`. To explore those environments, start by listing what Kosli knows about them:

```shell
kosli list environments
```

```
NAME                                TYPE     LAST REPORT                LAST MODIFIED              TAGS                                POLICIES
aws-beta                            ECS      2026-09-14T11:27:23+02:00  2026-09-14T11:27:23+02:00  [url=https://beta.cyber-dojo.org/]  [provenance pull-request snyk-scan-aws-beta trail-compliance-aws-beta]
aws-beta-terraform-drift-detection  server   2026-09-14T11:25:08+02:00  2026-09-14T11:25:08+02:00                                      [provenance]
aws-prod                            ECS      2026-09-14T11:26:58+02:00  2026-09-14T11:26:58+02:00  [url=https://cyber-dojo.org/]       [production-promotion provenance pull-request snyk-scan-aws-prod trail-compliance-aws-prod]
aws-prod-terraform-drift-detection  server   2026-09-14T11:23:32+02:00  2026-09-14T11:23:32+02:00                                      [provenance]
production                          logical                             2026-09-14T09:04:58+02:00                                      []
staging                             logical                             2026-09-14T09:05:24+02:00                                      []
```

To browse the history of changes in an environment:

```shell
kosli list snapshots aws-beta
```

```
SNAPSHOT  FROM                            TO                              DURATION        COMPLIANT
8372      Mon, 14 Sep 2026 09:05:24 CEST  now                             2 hours         true
8371      Mon, 14 Sep 2026 09:04:24 CEST  Mon, 14 Sep 2026 09:05:24 CEST  about a minute  true
8370      Mon, 14 Sep 2026 09:01:23 CEST  Mon, 14 Sep 2026 09:04:24 CEST  3 minutes       true
8369      Mon, 14 Sep 2026 09:00:24 CEST  Mon, 14 Sep 2026 09:01:23 CEST  59 seconds      true
...
```

To see what was running in a specific snapshot, for example `#8339`, where the `creator` artifact above started running:

```shell
kosli get snapshot aws-beta#8339
```

```
COMMIT   ARTIFACT                                                                                                                                      FLOW        COMPLIANCE  RUNNING_SINCE  REPLICAS
99d7b74  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424  creator-ci  COMPLIANT   4 days ago     1
         Fingerprint: a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424

06dc33a  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/differ:06dc33a@sha256:dbd68f81c38a9bdbccac20e2ca5c23c6377a7093b0c7e5730156431eb06d64cf   differ-ci   COMPLIANT   5 days ago     1
         Fingerprint: dbd68f81c38a9bdbccac20e2ca5c23c6377a7093b0c7e5730156431eb06d64cf
[...]
```

You can also reference snapshots relatively — `aws-beta~1` means one behind the current snapshot, `aws-beta~19` means 19 behind.

## Compare snapshots

Now that you can see individual snapshots, you can also diff two of them to find out exactly what changed between any two points in time. Comparing snapshot `#8339` with the one before it shows the `creator` deployment:

```shell
kosli diff snapshots aws-beta#8339 aws-beta#8338
```

```
Only present in aws-beta#8339

     Name:         244531986313.dkr.ecr.eu-central-1.amazonaws.com/creator:99d7b74@sha256:a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424
     Fingerprint:  a39fa3230549d3c6cb1732cc929c4e21041a09a21b2bb692cd37c9afe5fcd424
     Flow:         creator-ci
     Commit URL:   https://github.com/cyber-dojo/creator/commit/99d7b74f39e311d492902ad48dbe97da63f2c687
     Started:      Thu, 10 Sep 2026 08:06:01 CEST • 4 days ago
     Instances:    1
```

Relative references work here too. `kosli diff snapshots aws-beta aws-beta~1` compares the two most recent snapshots. If the same artifacts are running in both, the command prints nothing.

You can also diff two different environments to see what's running in one but not the other:

```shell
kosli diff snapshots aws-beta~3 aws-prod
```

## Don't parse the raw CLI output

The human-readable output you see above (tables, `COMPLIANT`/`NON-COMPLIANT` labels, history lines, etc.) is intended for people, not scripts. The exact wording, casing, and field labels may change between CLI versions to improve clarity or to stay aligned with the UI, and parsing this text in scripts or CI gates will silently break when it does.

If you need to act on Kosli data programmatically — for example, to fail a pipeline when an artifact is non-compliant — use one of the stable interfaces instead:

* **Exit codes.** Commands like `kosli assert` exit non-zero when the assertion fails, so you can branch on `$?` directly without parsing any output.
* **Structured output.** Pass `--output json` to any `get`, `list`, `search`, or `diff` command and read the documented JSON fields (e.g. `compliant`) rather than grepping the text rendering.

As a rule of thumb: if you're tempted to `grep COMPLIANT` or `grep NON-COMPLIANT` in a script, switch to the exit-code check or JSON field - it will keep working across CLI upgrades.

## What you've accomplished

You have searched for an artifact by commit SHA, inspected a flow's artifact list, fetched an artifact's full history, browsed environment snapshots, and diffed two snapshots to see exactly what changed.

From here you can:
* Learn more about [`kosli search`](/client_reference/kosli_search), [`kosli get artifact`](/client_reference/kosli_get_artifact), and [`kosli diff snapshots`](/client_reference/kosli_diff_snapshots) in the CLI reference
* See a real end-to-end example in the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
