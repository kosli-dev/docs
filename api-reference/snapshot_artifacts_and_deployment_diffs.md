---
title: "Snapshot artifacts and deployment diffs"
description: "How Kosli decides what an artifact replaced in an environment, what deployment_diff in the get snapshot response means, and when it is null."
---

This page explains the `deployment_diff` object that the [get snapshot](/api-reference/snapshots/get-snapshot) endpoint returns for every artifact in an environment snapshot: how Kosli picks the artifact it compares against, why there is one answer per flow, and when the value is `null`. The field descriptions themselves are in the endpoint's response schema; this page covers the semantics behind them.

## Two kinds of diff

Kosli answers two different "what changed" questions about an environment. They are easy to confuse because both are called a diff.

| Question | Use |
|---|---|
| What is in snapshot B that was not in snapshot A, and vice versa? | [`kosli diff snapshots`](/client_reference/kosli_diff_snapshots), which compares two whole snapshots as sets of artifacts. |
| For this one running artifact, what was running in its place before it, and what changed between them? | `deployment_diff` on the artifact, in the [get snapshot](/api-reference/snapshots/get-snapshot) response. |

The first is a set difference between two points in time. The second is a pointer from a running artifact back to its predecessor, and it is the one to read for lead-time and change reporting. The rest of this page is about the second.

## How a snapshot records change

Kosli creates a new snapshot only when the reported set of running artifacts differs from the latest snapshot. An artifact is identified by its **fingerprint** (its SHA-256 digest), not its name. When a fingerprint appears that was not in the previous snapshot, Kosli records a **started** event for it; when one disappears, an **exited** event. The name is recorded alongside, but it carries no identity: `web:cbe481c` and `web:236898f` are two different artifacts because their fingerprints differ, and two containers with different names but the same digest are the same artifact.

`deployment_diff` is computed from these started events, not from snapshot numbering.

## What "previous" means

`deployment_diff` hangs off the **current** artifact and points **backwards**. Within a flow, the previous artifact is the one that:

1. was also reported into the **same flow**,
2. has a **different fingerprint**, and
3. **started running in this environment most recently before** the current artifact started.

If the current artifact was reported with a `template_reference_name`, the match is further restricted to artifacts with the same `template_reference_name`. This is what keeps a multi-service environment honest: the `web` container is compared against the previous `web` container, not against whatever else deployed around the same time.

Three consequences follow:

- **It is not the artifact in the previous snapshot.** Snapshots are created whenever anything in the environment changes, including other services. The match is driven by start events, so a deploy of another service does not make an artifact's `deployment_diff` go stale or disappear.
- **It is not matched on name.** `previous_artifact_name` is reported separately because the predecessor may have run under a different name, which is normal when the tag carries the commit.
- **It is anchored to when the current artifact started**, not to when you make the request. Every artifact in the latest snapshot still carries the diff describing what it replaced when it started, and the value is stable for as long as the artifact keeps running.

## One answer per flow

An artifact can be reported into several flows: a build flow, a promotion flow, a scanning flow. Each entry in `artifacts[].flows[]` carries its **own** `deployment_diff`, computed independently using only artifacts reported into that flow.

The public `cyber-dojo` organization shows this. Its `web` image is reported into four flows, and the latest `aws-prod` snapshot returns four different answers for the same running image:

| Flow | Previous fingerprint | `diff_url` compares |
|---|---|---|
| `web-ci` | `36ad0020` | `cyber-dojo/web` `cbe481c...236898f` |
| `production-promotion` | `36ad0020` | `cyber-dojo/aws-prod-co-promotion` `7494758...7494758` |
| `snyk-aws-beta-per-artifact` | `36ad0020` | `cyber-dojo/snyk-scanning` `ed3c81d...30111f1` |
| `snyk-aws-prod-per-artifact` | `29c69c2f` | `cyber-dojo/snyk-scanning` `00c4797...30111f1` |

Two separate things are happening:

- **Different flows can pick a different previous artifact.** Three flows agree the predecessor was `36ad0020`. `snyk-aws-prod-per-artifact` picks `29c69c2f` because `36ad0020` was never reported into that flow, so the search skipped further back to the last image that was.
- **Even when they agree on the artifact, they disagree on the commit.** `git_commit` is recorded per flow, and each flow here tracks a different repository. The same image is commit `236898f` of `cyber-dojo/web` to the build flow and commit `30111f1` of the scanning repository to the Snyk flows. `previous_git_commit` and `diff_url` describe **that flow's repository**, not the image in the abstract.

To answer "what source code changed", read the entry for the flow that **builds** the artifact. The other entries answer a real question, but a different one, and can be degenerate: the promotion flow compares `7494758` against itself because the promotion repository did not move between the two promotions.

### The top-level field is `flows[0]`

`deployment_diff` appears twice in each artifact:

- `artifacts[].deployment_diff`, at the top level, and
- `artifacts[].flows[].deployment_diff`, one per flow.

The top-level field is a verbatim copy of `flows[0].deployment_diff`, kept for convenience and backwards compatibility. It is not an aggregate and does not pick the most relevant flow; it reflects stored order.

<Warning>
If your artifacts are reported into more than one flow, read `flows[]` and select the flow you mean by `flow_name`. Do not build on the top-level copy.
</Warning>

For a single-flow artifact the two are identical and the top-level field is all you need.

## When it is `null`

`deployment_diff` is always present in the response. When there is nothing to compare against, the value is `null`. That happens when:

- **The artifact has no provenance.** Something is running that was never reported to a flow, so there is no history to search.
- **Nothing from this flow has run here before.** The first deploy of a service into an environment has nothing to diff against.
- **No start event can be resolved** for the current artifact before this snapshot, an edge case in older data.

When it is not `null`, every sub-field is present. `previous_trail_name` and `previous_template_reference_name` can individually be `null` for artifacts reported before trails and templates existed. `diff_url` can be an empty string (see below). The remaining fields always have a value.

## Three caveats

- **`previous_running` is about this snapshot, not history.** `false` means the predecessor is gone, the normal steady state after a deploy completes. `true` means both versions are present in this snapshot at once: a rolling deploy caught mid-flight, a canary, or a partially drained service.
- **`previous_artifact_compliance_state` is evaluated when you make the request**, not frozen at snapshot time. If someone attests evidence against the older artifact tomorrow, this field can change for a snapshot taken today. Compliance is a live judgment about an artifact, not a historical record of the deploy.
- **`diff_url` can be `""`.** It is built by matching the commit URL against GitHub, GitLab, Bitbucket, and Azure DevOps. Any other git host produces an empty string rather than a broken link. `previous_git_commit` and the artifact's own `git_commit` are still there, so you can build the link yourself.

## See it yourself

`cyber-dojo` is a public organization, so no API token is needed:

```shell
BASE="https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod"

# the deployment diff for the web service, from the flow that builds it
curl -s "$BASE/-1" | jq '.artifacts[] | select(.name | contains("/web:")) | .flows[] | select(.flow_name == "web-ci") | .deployment_diff'

# one line per artifact: name and the top-level diff_url
curl -s "$BASE/-1" | jq -r '.artifacts[] | "\(.name)  ->  \(.deployment_diff.diff_url // "no diff")"'
```

`-1` is the latest snapshot. The other snapshot expressions (`#N`, `~N`, `@{...}`) are listed on the [get snapshot](/api-reference/snapshots/get-snapshot) page. For a private organization, authenticate with your [API token](/administration/authentication/api_authentication_methods).

## Related

- [get snapshot](/api-reference/snapshots/get-snapshot) — the response schema, including every `deployment_diff` field.
- [`kosli get snapshot`](/client_reference/kosli_get_snapshot) and [`kosli diff snapshots`](/client_reference/kosli_diff_snapshots) — the CLI equivalents.
- [Querying Kosli](/tutorials/querying_kosli) and [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) — tutorials that walk through snapshot diffs.
- [Environments](/getting_started/environments) — creating environments and reporting snapshots.
