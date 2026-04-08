---
title: "Enforce policies"
description: "Block non-compliant artifacts from deploying by enforcing policies in CI/CD pipelines, via the API, or with Kubernetes admission controllers."
icon: "shield-check"
---

Environment policies define what an artifact needs to be compliant. Policy enforcement gates check artifacts against those requirements and block deployments when they fall short.

You can enforce policies:
- As a **CI/CD pipeline step** that fails the build on non-compliance
- Through the **Kosli API** for custom tooling
- Via a **Kubernetes admission controller** that rejects non-compliant pods

All methods use the same assertion: checking an artifact's fingerprint against an environment, specific policies, or a flow template.

## Assertion scopes

`kosli assert artifact` (and its API equivalent) supports four mutually exclusive scopes:

| Scope | CLI flag | When to use |
|-------|----------|-------------|
| Environment | `--environment` | Check all policies attached to the target environment. The most common choice for deployment gates. |
| Specific policies | `--policy` | Check one or more named policies, regardless of environment attachment. Useful for promotion gates between stages. |
| Flow template | `--flow` | Check the artifact against a flow's template requirements. |
| All flows | _(no scope flag)_ | Check against the templates of every flow the artifact appears in. |

See [`kosli assert artifact`](/client_reference/kosli_assert_artifact) for the full flag reference.

## Enforce in CI/CD pipelines

Add `kosli assert artifact` as a step before your deployment step. If the artifact is non-compliant, the command exits with a non-zero status and the pipeline fails.

### Assert against an environment

Check all policies attached to the target environment:

<Tabs>
  <Tab title="GitHub Actions" icon="github">
  ```yaml
  - name: Assert artifact compliance
    env:
      KOSLI_API_TOKEN: ${{ secrets.KOSLI_API_TOKEN }}
      KOSLI_ORG: my-org
    run: |
      kosli assert artifact ${{ env.IMAGE }} \
        --artifact-type oci \
        --environment production
  ```
  </Tab>
  <Tab title="GitLab CI" icon="gitlab">
  ```yaml
  assert-compliance:
    stage: deploy
    script:
      - kosli assert artifact $IMAGE \
          --artifact-type oci \
          --environment production
    variables:
      KOSLI_API_TOKEN: $KOSLI_API_TOKEN
      KOSLI_ORG: my-org
  ```
  </Tab>
</Tabs>

### Assert against specific policies

Check one or more named policies directly. This is useful when gating a promotion between stages or checking policies that are not attached to an environment:

```shell
kosli assert artifact $IMAGE \
  --artifact-type oci \
  --policy has-tests,has-review
```

<Tip>
Use `--dry-run` to test assertions without sending data to Kosli. The CLI prints the compliance result but always exits with code 0.
</Tip>

## Enforce via the API

For custom deployment tooling or non-CI contexts, call the assert endpoint directly:

<Tabs>
  <Tab title="EU" icon="globe">
  ```shell
  curl -s \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    "https://app.kosli.com/api/v2/asserts/my-org/fingerprint/$SHA256?environment_name=production"
  ```
  </Tab>
  <Tab title="US" icon="globe">
  ```shell
  curl -s \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    "https://app.us.kosli.com/api/v2/asserts/my-org/fingerprint/$SHA256?environment_name=production"
  ```
  </Tab>
</Tabs>

The response includes:
- `compliant` — `true` or `false`
- `policy_evaluations` — detailed results per policy (when asserting against an environment)
- `compliance_status` — per-attestation compliance breakdown

To assert against specific policies instead of an environment:

<Tabs>
  <Tab title="EU" icon="globe">
  ```shell
  curl -s \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    "https://app.kosli.com/api/v2/asserts/my-org/fingerprint/$SHA256?policy_name=has-tests&policy_name=has-review"
  ```
  </Tab>
  <Tab title="US" icon="globe">
  ```shell
  curl -s \
    -H "Authorization: Bearer $KOSLI_API_TOKEN" \
    "https://app.us.kosli.com/api/v2/asserts/my-org/fingerprint/$SHA256?policy_name=has-tests&policy_name=has-review"
  ```
  </Tab>
</Tabs>

See the [Assert artifact API reference](/api-reference/asserts/assert-artifact) for the full response schema. You can also try it out directly in the API playground on that page.

## Enforce with a Kubernetes admission controller

A Kubernetes [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) can call the Kosli assert API when a pod is created and reject pods whose images are non-compliant.

The flow is:

<Steps>
  <Step title="Pod creation triggers the webhook">
    Kubernetes calls your admission webhook before scheduling the pod.
  </Step>
  <Step title="Webhook extracts the image fingerprint">
    The webhook reads the container image reference from the pod spec and resolves its SHA256 digest.
  </Step>
  <Step title="Webhook calls the Kosli assert API">
    The webhook sends a request to the [assert endpoint](/api-reference/asserts/assert-artifact) with the fingerprint and the target environment name.
  </Step>
  <Step title="Webhook returns allow or deny">
    If `compliant` is `true`, the pod is admitted. If `false`, the webhook rejects the pod with a message explaining which policy requirements were not met.
  </Step>
</Steps>

<Tip>
The [Kosli K8S Reporter](/helm/k8s_reporter) reports what is running in your Kubernetes environments to Kosli. Pair it with an admission controller to both enforce and monitor compliance.
</Tip>

## What happens on failure

**CLI:** A non-compliant artifact causes `kosli assert artifact` to exit with a non-zero code. CI/CD pipelines treat this as a failed step and stop the deployment. Use `--output json` to get machine-readable compliance details.

**API:** The response body returns `compliant: false` with a `compliance_status` object describing which attestations are missing or non-compliant, and `policy_evaluations` listing per-policy results.
