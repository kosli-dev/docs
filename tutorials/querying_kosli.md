---
title: "Querying Kosli"
description: "This tutorial shows you how to use Kosli's query commands to search for artifacts, inspect their history, and browse runtime environment snapshots."
---

`get`, `list`, `log`, and `diff` commands let you query everything Kosli knows about your artifacts and environments directly from your terminal.
By the end of this tutorial, you will have searched for an artifact by commit SHA, inspected its full history, browsed environment snapshots, and compared two snapshots to see what changed.

We will query **cyber-dojo**, an open-source project whose Kosli data is public.

## Prerequisites

* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).

## Setup

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=<your-api-token>
```

## Search by commit SHA

If you have a git commit SHA, `kosli search` will find any artifact built from it:

```shell
kosli search 0f5c9e1
```

```
Search result resolved to commit 0f5c9e19c4d4f948d19ce4c8495b2a44745cda96
Name:              cyberdojo/web:0f5c9e1
Fingerprint:       62e1d2909cc59193b31bfd120276fcb8ba5e42dd6becd873218a41e4ce022505
Has provenance:    true
Flow:              web
Git commit:        0f5c9e19c4d4f948d19ce4c8495b2a44745cda96
Commit URL:        https://github.com/cyber-dojo/web/commit/0f5c9e19c4d4f948d19ce4c8495b2a44745cda96
Build URL:         https://github.com/cyber-dojo/web/actions/runs/3021563461
Compliance state:  COMPLIANT
History:
    Artifact created                                   Fri, 09 Sep 2022 11:59:50 CEST
    Deployment #59 to aws-beta environment             Fri, 09 Sep 2022 12:01:12 CEST
    Started running in aws-beta#217 environment        Fri, 09 Sep 2022 12:02:42 CEST
    Deployment #60 to aws-prod environment             Fri, 09 Sep 2022 12:06:37 CEST
    Started running in aws-prod#202 environment        Fri, 09 Sep 2022 12:07:28 CEST
    Scaled up from 1 to 3 in aws-prod#203 environment  Fri, 09 Sep 2022 12:08:28 CEST
    No longer running in aws-beta#222 environment      Sat, 10 Sep 2022 08:44:42 CEST
    No longer running in aws-prod#210 environment      Sat, 10 Sep 2022 08:49:28 CEST
```

## List flows and artifacts

The search result tells us this artifact belongs to the `web` flow. If you don't know which flows exist in your org, you can list them all:

```shell
kosli list flows
```

```
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
shas                    UX for git+image shas               public
web                     UX for practicing TDD               public
```

Once you know the flow name, you can list the artifacts reported to it:

```shell
kosli list artifacts --flow creator
```

```
COMMIT   ARTIFACT                                  STATE       CREATED_AT
344430d  Name: cyberdojo/creator:344430d           COMPLIANT   Wed, 14 Sep 2022 10:48:09 CEST
         Fingerprint: 817a72(...)6b5a273399c693

41bfb7b  Name: cyberdojo/creator:41bfb7b           COMPLIANT   Sat, 10 Sep 2022 08:41:15 CEST
         Fingerprint: 8d6fef(...)b84c281f712ef8

aa0a3d3  Name: cyberdojo/creator:aa0a3d3           COMPLIANT   Fri, 09 Sep 2022 11:58:56 CEST
         Fingerprint: 3ede07(...)238845a631e96a
[...]
```

By default, the last 15 artifacts are shown. Use <Tooltip tip="Limit results per page, e.g. -n 5 to show only 5 artifacts.">-n</Tooltip> to change how many are shown, <Tooltip tip="Select a page of results, e.g. --page 2 to see the next page.">--page</Tooltip> to paginate, and <Tooltip tip="Change the output format, e.g. --output json to get JSON instead of a table.">--output</Tooltip> to change the format.

## Get an artifact

The artifact list gives you commit SHAs and fingerprints. Use either to fetch the full history of a specific artifact — the syntax is <Tooltip tip="Use flow:sha to identify by commit SHA (e.g. creator:344430d), or flow@fingerprint to identify by fingerprint (e.g. creator@817a726...).">flow:sha or flow@fingerprint</Tooltip>:

```shell
kosli get artifact creator:344430d
```

```
Name:                     cyberdojo/creator:344430d
Flow:                     creator
Fingerprint:              817a72609041c51cd2a3bbbcbeb048c687677986b5a273399c6938b5e6aa1ded
Created on:               Wed, 14 Sep 2022 10:48:09 CEST • 2 months ago
Git commit:               344430d530d26068aa1f39760a9c094c989382f3
Commit URL:               https://github.com/cyber-dojo/creator/commit/344430d530d26068aa1f39760a9c094c989382f3
Build URL:                https://github.com/cyber-dojo/creator/actions/runs/3051390570
State:                    COMPLIANT
Running in environments:  aws-beta#265, aws-prod#259
History:
    Artifact created                               Wed, 14 Sep 2022 10:48:09 CEST
    branch-coverage evidence received              Wed, 14 Sep 2022 10:49:11 CEST
    Deployment #100 to aws-beta environment        Wed, 14 Sep 2022 10:50:40 CEST
    Deployment #101 to aws-prod environment        Wed, 14 Sep 2022 10:51:43 CEST
    Started running in aws-beta#229 environment    Wed, 14 Sep 2022 10:52:42 CEST
    Started running in aws-prod#217 environment    Wed, 14 Sep 2022 10:53:28 CEST
    ...
```


## Browse environment snapshots

The artifact history shows it was deployed to `aws-beta` and `aws-prod`. To explore those environments, start by listing what Kosli knows about them:

```shell
kosli list environments
```

```
NAME      TYPE  LAST REPORT                LAST MODIFIED
aws-beta  ECS   2022-10-30T14:51:42+01:00  2022-10-30T14:51:42+01:00
aws-prod  ECS   2022-10-30T14:51:28+01:00  2022-10-30T14:51:28+01:00
beta      K8S   2022-06-15T11:39:59+02:00  2022-06-15T11:39:59+02:00
prod      K8S   2022-06-15T11:40:01+02:00  2022-06-15T11:40:01+02:00
```

To browse the history of changes in an environment:

```shell
kosli list snapshots aws-beta
```

```
SNAPSHOT  FROM                            TO                              DURATION
266       Wed, 19 Oct 2022 09:47:42 CEST  now                             11 days
265       Wed, 19 Oct 2022 09:46:42 CEST  Wed, 19 Oct 2022 09:47:42 CEST  59 seconds
264       Wed, 19 Oct 2022 09:45:42 CEST  Wed, 19 Oct 2022 09:46:42 CEST  about a minute
...
```

To see what was running in a specific snapshot:

```shell
kosli get snapshot aws-beta#256
```

```
COMMIT   ARTIFACT                                                                              FLOW      RUNNING_SINCE  REPLICAS
6fe0d30  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/repler:6fe0d30                  N/A       16 days ago    1
         Fingerprint: a0c03099c832e4ce5f23f5e33dac9889c0b7ccd61297fffdaf1c67e7b99e6f8f

d90a3e4  Name: 244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:d90a3e4               N/A       16 days ago    1
         Fingerprint: dd5308fdcda117c1ff3963e192a069ae390c2fe9e10e8abfa2430224265efe98
[...]
```

You can also reference snapshots relatively — `aws-beta~1` means one behind the current snapshot, `aws-beta~19` means 19 behind.

## Compare snapshots

Now that you can see individual snapshots, you can also diff two of them to find out exactly what changed between any two points in time:

```shell
kosli diff snapshots aws-beta aws-beta~1
```

```
Only present in aws-beta (snapshot: aws-beta#266)

     Name:         244531986313.dkr.ecr.eu-central-1.amazonaws.com/dashboard:d90a3e4
     Fingerprint:  dd5308fdcda117c1ff3963e192a069ae390c2fe9e10e8abfa2430224265efe98
     Flow:         dashboard
     Commit URL:   https://github.com/cyber-dojo/dashboard/commit/d90a3e481d57023816f6694ba4252342889405eb
     Started:      Wed, 19 Oct 2022 09:47:33 CEST • 11 days ago
```

You can also diff two different environments to see what's running in one but not the other:

```shell
kosli diff snapshots aws-beta~3 aws-prod
```

## What you've accomplished

You have searched for an artifact by commit SHA, inspected a flow's artifact list, fetched an artifact's full history, browsed environment snapshots, and diffed two snapshots to see exactly what changed.

From here you can:
* Learn more about [`kosli search`](/client_reference/kosli_search), [`kosli get artifact`](/client_reference/kosli_get_artifact), and [`kosli diff snapshots`](/client_reference/kosli_diff_snapshots) in the CLI reference
* See a real end-to-end example in the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
