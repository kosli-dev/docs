---
title: "Report AWS Bedrock AgentCore environments to Kosli"
description: "How to build an agent container image in CI, attest it to Kosli, and report the AgentCore runtimes running it as a Kosli environment."
---

<Warning>
**This page describes a proposed feature.** `kosli snapshot agentcore` does not
exist yet, and there is no `agentcore` environment type on the Kosli server.
Every Kosli command on this page is marked as proposed where it is not yet
available. The AWS commands are real and work today.
</Warning>

AWS Bedrock AgentCore runs your agent as a managed runtime. To hold an agent to
the same standard as the rest of your services, you need to know which build is
serving traffic and be able to trace it back to the commit and the pipeline that
produced it.

This guide covers the two halves of that:

- **Attest the agent image before you release it**, so the evidence exists while
  you can still act on it.
- **Report the running AgentCore runtimes to Kosli** as an environment snapshot,
  so you can see what is actually serving.

How you structure the first half decides whether Kosli can gate a release or only
record it, so start there.

## Prerequisites

* Have access to AWS, with AgentCore runtimes deployed from container images.
* [Create an AgentCore Kosli environment](/getting_started/environments#create-an-environment) named `agentcore-env-tutorial`. *(Proposed: the `agentcore` environment type is not yet available.)*
* [Get a Kosli API token](/getting_started/authenticating_to_kosli).
* [Install Kosli CLI](/getting_started/install).

Reporting reads AgentCore and ECR. This read-only policy is sufficient for the
whole chain:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:List*",
        "bedrock-agentcore:Get*",
        "ecr:BatchGetImage",
        "ecr:DescribeImages"
      ],
      "Resource": "*"
    }
  ]
}
```

The ECR permissions are not optional. AgentCore returns the image reference
exactly as it was supplied, which is usually a tag, and Kosli has to resolve
that tag to a digest before it means anything. See
[How Kosli fingerprints an agent](#how-kosli-fingerprints-an-agent).

<Tip>
This policy uses wildcards to keep it readable. For production, AWS recommends
scoping to specific runtime ARNs rather than `"Resource": "*"`. See
[Security best practices for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html).
</Tip>

## Separate the build from the release

The AgentCore CLI's `agentcore deploy` builds your container image **inside your
AWS account**: it provisions a CodeBuild project, builds from source there, and
creates or updates the runtime in the same operation.

The problem is not that AWS did the building. You can attest an image you did not
build - `kosli attest artifact` with `--artifact-type oci` reads the digest from
the registry - so running it after `agentcore deploy` does produce an artifact in
Kosli whose fingerprint matches the snapshot.

The problem is **when** the artifact becomes known. Because the build and the
runtime update are one operation, there is no point at which the image exists and
the runtime has not already been pointed at it. Anything you attest afterwards
describes something that is already serving traffic:

- A Kosli policy on that artifact reports a violation instead of preventing one.
- Vulnerability scans, approvals, and test evidence all land post-release.
- Until you attest, the snapshot shows a running artifact Kosli has never seen,
  which reads as a compliance gap that later resolves itself.

Splitting build from release fixes all of that, and it's the pattern AWS itself
publishes for CI/CD: their
[GitHub Actions reference pipeline](https://aws.amazon.com/blogs/machine-learning/deploy-ai-agents-on-amazon-bedrock-agentcore-using-github-actions/)
builds and pushes the image to ECR from the Dockerfile, scans it with Amazon
Inspector, and only then creates the AgentCore runtime from that image. It does
not use `agentcore deploy`. Attesting to Kosli goes in the same slot as the scan.

<Note>
If you are staying on `agentcore deploy` for now, attesting the ECR image
afterwards is still worth doing. You get a complete audit trail of what is
running and where it came from. What you do not get is the ability to stop a bad
build from reaching production, because by the time you can attest it, it is
already live.
</Note>

<Steps>
<Step title="Build for ARM64">
AgentCore runtimes are `aarch64`. If your CI runners are `x86_64`, cross-build
with buildx:

```shell
docker buildx build \
    --platform linux/arm64 \
    --tag <your-account>.dkr.ecr.<region>.amazonaws.com/<repo>:<tag> \
    --push .
```

Pushing here rather than in a separate step gives you the digest buildx
calculated, which is what you want to attest.

ARM64 is a hard requirement, not a preference. AgentCore Runtime runs on AWS
Graviton, and an image built for another architecture fails at deploy time.
</Step>

<Step title="Attest the image to Kosli">
Report the artifact with the digest that will be running:

```shell
kosli attest artifact <your-account>.dkr.ecr.<region>.amazonaws.com/<repo>:<tag> \
    --artifact-type oci \
    --name agent \
    --flow <your-flow-name> \
    --trail <your-trail-name> \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

Add whatever else your pipeline proves about this build with
[`kosli attest`](/client_reference/kosli_attest_generic) - test results, scan
results, approvals. That evidence is what makes the running agent auditable
later.

This is the step that has to happen before the release, not after it. Gate the
next step on it if you want the build blocked rather than merely recorded.
</Step>

<Step title="Point AgentCore at the pre-built image">
`CreateAgentRuntime` accepts a container image directly, so AgentCore does not
have to build anything. Reference the image **by digest** rather than by tag:

```shell
aws bedrock-agentcore-control create-agent-runtime \
    --agent-runtime-name <your-runtime-name> \
    --role-arn <your-execution-role-arn> \
    --network-configuration '{"networkMode":"PUBLIC"}' \
    --agent-runtime-artifact '{
      "containerConfiguration": {
        "containerUri": "<your-account>.dkr.ecr.<region>.amazonaws.com/<repo>@sha256:<digest>"
      }
    }'
```

`containerUri` accepts either `:tag` or `@sha256:digest`. Using the digest is
worth the small inconvenience: it names exactly the image you attested, and it
cannot be repointed at different content later. Use `update-agent-runtime` with
the same artifact shape to roll out a new build, which creates a new runtime
version.

<Note>
`--agent-runtime-artifact` is a tagged union: set either
`containerConfiguration` or `codeConfiguration`, never both. AWS documents
deploying a pre-built ECR image as a supported pattern, including
`AgentRuntimeArtifact.fromEcrRepository` and `fromImageUri` in the CDK. Kosli
has not yet run reporting against a runtime deployed this way end to end, so
treat the invocation above as a starting point rather than a tested recipe.
</Note>
</Step>
</Steps>

Now the digest running in AgentCore is a digest your CI produced and attested,
and the environment snapshot below can be matched against it.

## Report using Kosli CLI

<Warning>
Proposed. This command does not exist yet.
</Warning>

Export your AWS credentials:

```shell
export AWS_REGION=yourAWSRegion
export AWS_ACCESS_KEY_ID=yourAWSAccessKeyID
export AWS_SECRET_ACCESS_KEY=yourAWSSecretAccessKey
```

Report every AgentCore runtime in the region:

```shell
kosli snapshot agentcore agentcore-env-tutorial \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

One Kosli environment covers all AgentCore runtimes in one AWS account and
region, and each runtime appears as one artifact in the snapshot. This matches
how [`kosli snapshot ecs`](/client_reference/kosli_snapshot_ecs) and
[`kosli snapshot lambda`](/client_reference/kosli_snapshot_lambda) work, and it
means one snapshot diff shows you every agent that moved.

Filter with the same flags as the ECS reporter when you want a narrower
environment:

```shell
# include runtimes matching a list of names
kosli snapshot agentcore agentcore-env-tutorial --runtimes runtime1,runtime2 ...

# include runtimes matching a pattern
kosli snapshot agentcore agentcore-env-tutorial --runtimes-regex "prod-*" ...

# exclude runtimes matching a pattern
kosli snapshot agentcore agentcore-env-tutorial --exclude-regex "dev-*" ...
```

All filtering is case-sensitive. Include and exclude flags are mutually
exclusive.

## How Kosli fingerprints an agent

Kosli records the **image digest**, not the URI AgentCore hands back.

AgentCore returns the image reference exactly as it was supplied. If it was
supplied as a tag, that is what you get back:

```json
{
  "agentRuntimeArtifact": {
    "containerConfiguration": {
      "containerUri": "<account>.dkr.ecr.<region>.amazonaws.com/<repo>:66fe54aab857..."
    }
  }
}
```

That trailing 64-character hex string sits in the tag position, after the `:`,
not the digest position, which would be `@sha256:`. Build tooling often uses a
content hash as a tag, which makes it look immutable when it is not: the same
tag can be repointed at different content. The actual digest of that image is a
different value.

So Kosli resolves the tag through ECR to get the real digest, the same way the
ECS reporter does. That is why `ecr:BatchGetImage` and `ecr:DescribeImages` are
in the policy above, and it is why the digest in your snapshot will not match
the hex string in `containerUri`. It is not meant to.

If you pin by digest as recommended above, the reference is already immutable
and unambiguous. Kosli still verifies it through ECR, but there is nothing left
to resolve.

Kosli reads the version that is actually **live** rather than the newest one.
AgentCore creates a new runtime version on every image update and keeps the old
ones, and endpoints decide which version serves traffic. The `DEFAULT` endpoint
follows the newest version, but a named endpoint does not: you can have
`DEFAULT` on version 4 while a `PROD` endpoint still serves version 2. Reading
the newest version would report an image that nothing is running.

## Report using Terraform module

Planned for a future iteration. There is no AgentCore support in the
[Kosli reporter Terraform module](https://registry.terraform.io/modules/kosli-dev/kosli-reporter/aws/latest)
yet. Until then, run the CLI from your own scheduled job or pipeline.

## Limitations

**CodeZip builds are not supported.** AgentCore runtimes deployed from an S3
code bundle describe their artifact by location, not by content:

```json
{
  "agentRuntimeArtifact": {
    "codeConfiguration": {
      "code": { "s3": { "bucket": "...", "prefix": "....zip" } }
    }
  }
}
```

AWS Lambda deploys the same way and hands you a `CodeSha256` computed by the
service. AgentCore has no equivalent, and nothing in the response is guaranteed
to change when the code changes:

- The `s3` block does define an optional `versionId`, but it is **supplied by
  whoever deploys**, not computed by AgentCore. It defaults to the latest
  version of the object, and it is absent from the response when the deployer
  did not set it, so a reporter cannot depend on it being there.
- The `prefix` is sometimes a content hash, but only because some deployment
  tools happen to name the object that way. Others use a stable path that never
  changes.

Either way, Kosli would be recording where the code lives rather than what the
code is.

Rather than record a fingerprint that may be silently wrong, Kosli reports
container-based runtimes only. If you deploy agents from code bundles today,
moving to container builds is also what puts you on the CI-build-and-attest path
described above.

**Agent configuration is not tracked.** A snapshot covers the image that is
running. Prompts, tool availability, and model choice are not part of the
fingerprint.

## What you've accomplished

You have an agent image built and attested in your own CI, and a Kosli
environment showing which AgentCore runtimes are serving which build. When an
agent changes, Kosli records it, and you can trace the running digest back to
the commit that produced it.

From here you can:
* Query your environment with [`kosli list snapshots`](/client_reference/kosli_list_snapshots) and [`kosli get snapshot`](/client_reference/kosli_get_snapshot)
* [Compare snapshots to see what changed](/client_reference/kosli_diff_snapshots)
* Trace a running artifact back to its git commit with the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
* Report your other AWS workloads with the [Report AWS environments](/tutorials/report_aws_envs) guide
