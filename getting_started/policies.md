---
title: "Environment Policies"
description: "Define and enforce compliance requirements for artifact deployments across different environments."
icon: "scroll"
---

Environment Policies enable you to define and enforce compliance requirements for artifact deployments across
different environments. With Environment Policies, you can:

- Define specific requirements for each environment (e.g, dev, staging, prod)
- Enforce consistent compliance standards across your deployment pipeline
- Prevent non-compliant artifacts from being deployed (via admission controllers)

Policies are written in YAML and are immutable (updating a policy creates a new version). They can be attached to
one or more environments, and an environment can have one or more policies attached to it.

## Create a Policy

You can create a policy via CLI or via the API. Here is a basic policy that requires provenance and specific
attestations:

```yaml prod-policy.yaml
_schema: https://docs.kosli.com/schemas/policy/v1
artifacts: # the rules apply to artifacts in an environment snapshot
  provenance:
    required: true # all artifacts must have provenance
  attestations:
    - name: dependency-scan # all artifacts must have dependency-scan attestation
      type: "*" # any attestation type
    - name: unit-test # all artifacts must have unit-test attestation
      type: junit # must be a 'junit' attestation type
```

You can create and manage policies using the Kosli CLI (global flags like org and api-token are omitted for brevity):

```shell
kosli create policy prod-requirements prod-policy.yaml
```

```shell
kosli get policy prod-requirements
```

See [kosli create policy](/client_reference/kosli_create_policy/) for usage details and examples.

<Note>
Once you create a policy, you will be able to see it in the UI under `policies` in the left navigation menu.
</Note>

## Policy rules

A policy consists of rules which are applied to artifacts in an environment snapshot.

### Provenance

When `provenance` is set to `required: true`, the artifact must be part of a Kosli Flow (i.e., it must have
provenance information).

```yaml
artifacts:
  provenance:
    required: true
```

### Trail compliance

When `trail-compliance` is set to `required: true`, the artifact must be part of a compliant Trail in its Flow.

```yaml
artifacts:
  trail-compliance:
    required: true
```

### Specific attestations

```yaml
artifacts:
  attestations:
    - name: "*" # attestation name can be anything
      type: pull-request
    - name: acceptance-test
      type: "*" # attestation type can be any built-in or existing custom type
    - name: security-scan
      type: snyk
    - name: coverage-metrics
      type: custom:my-coverage-metrics # custom attestation type
```

### Exceptions

You can add exceptions to policy rules using [policy expressions](/policy-reference/environment_policy#policy-expressions).

```yaml
_schema: https://docs.kosli.com/schemas/policy/v1

artifacts:
  provenance:
    required: true
    exceptions:
      # provenance is required except when one of the expressions evaluates to true
      - if: ${{ matches(artifact.name, "^datadog:.*") }}

  trail-compliance:
    required: true
    exceptions:
      - if: ${{ matches(artifact.name, "^datadog:.*") }}

  attestations:
    - if: ${{ flow.tags.risk-level == "high" }} # only required when expression is true
      name: unit-tests
      type: junit
```

For the complete YAML specification — fields, types, defaults, expression language, and constraints — see the [Environment Policy reference](/policy-reference/environment_policy).

## Attaching/Detaching Policies to/from Environments

Once you define your policies, you can attach them to environments via CLI or API:

```shell
kosli attach-policy prod-requirements --environment=aws-production
```

To detach a policy from an environment:

```shell
kosli detach-policy prod-requirements --environment=aws-production
```

Any attachment/detachment operation automatically triggers an evaluation of the latest environment snapshot and
creates a new one with an updated compliance state.

<Note>
If you detach all attached policies from an environment, the environment compliance state will become <Badge color="gray">Unknown</Badge> since there are no longer any defined requirements for artifacts running in it. The environment will continue to
track snapshots, but its compliance cannot be evaluated without policies.
</Note>


## Enforcing policies

Once policies are attached to environments, you can enforce them as deployment gates in your CI/CD pipeline, via the API, or with a Kubernetes admission controller. See [Enforce policies](/getting_started/enforce_policies) for setup instructions.
