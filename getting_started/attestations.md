---
title: "Attestations"
description: "Learn how to make attestations to Kosli to prove compliance in your software supply chain."
icon: "receipt"
---

Attestations are how you record the facts you care about in your software supply chain.
They are the evidence that you have performed certain activities, such as running tests, security scans, or ensuring that a certain requirement is met.

Kosli allows you to report different types of attestations about artifacts and trails.
Kosli will process the evidence you provide and conclude whether the evidence proves compliance or otherwise.

Let's take a look at this example to understand how to make attestations to Kosli.

## Example overview

The following compliance template is expecting 4 attestations, each with its own `name`.

```yml
# yaml-language-server: $schema=https://docs.kosli.com/schemas/flow-template.json
version: 1
trail:
  attestations:
  - name: jira-ticket
    type: system:jira
  artifacts:
  - name: backend
    attestations:
    - name: unit-tests
      type: system:junit
    - name: security-scan
      type: system:sarif
```

<Tip>
The `type:` value uses the form `system:<type-name>` to track the latest version of that system type. To pin a specific version, suffix with `@vN` — e.g. `system:sarif@v1`. See [system attestation types](/attestation_types/system/overview#versioning) for more on versioning.
</Tip>

<Tip>
  See the [Flow Template reference](/template-reference/flow_template) for the full specification, available attestation types, and editor validation with JSON Schema.
</Tip>

It expects `jira-ticket` on the trail, the `backend` artifact, with `unit-tests` and `security-scan` attached to it.
When you make an attestation, you have the choice of what `name` to attach it to.

### Steps

The following sections show how to make each of the four attestations defined in the template above.

<Steps>
  <Step title="Attest a Jira ticket to the trail">
    The `jira-ticket` attestation belongs to a single trail and is not linked to a specific artifact. In this example, the id of the trail is the git commit.

    ```shell
    kosli attest system jira \
        --flow backend-ci \
        --trail $(git rev-parse HEAD) \
        --name jira-ticket
        ...
    ```
  </Step>
  <Step title="Attest unit tests to the backend artifact">
  Some attestations are attached to a specific artifact, like the unit tests for the `backend` artifact. Often, evidence like unit tests are created _before_ the artifact is built. To attach the evidence to the artifact before its creation, use `backend` (the artifact's `name` from the template), as well as `unit-tests` (the attestation's `name` from the template).

  ```shell
  kosli attest system junit \
      --name backend.unit-tests \
      --flow backend-ci \
      --trail $(git rev-parse HEAD) \
      ...
  ```

  This attestation belongs to any artifact attested with the matching `name` from the template (in this example `backend`) and a matching git commit.
  </Step>
  <Step title="Attest the backend artifact">
  Once the artifact has been built, it can be attested with the following command.

  ```shell
  kosli attest artifact my_company/backend:latest \
    --artifact-type docker \
      --flow backend-ci \
      --trail $(git rev-parse HEAD) \
      --name backend
      ...
  ```

  In this case the Kosli CLI will calculate the fingerprint of the docker image called `my_company/backend:latest` and attest it as the `backend` artifact `name` in the trail.

  <Info>
  In all attestation commands the Kosli CLI automatically gathers the git commit and other information from the current git repository and the [CI environment](/integrations/ci_cd). This is how the git commit is used to match attestations to artifacts.
  </Info>
  </Step>
  <Step title="Attest a security scan to the backend artifact">
  Often, evidence like snyk reports are created _after_ the artifact is built. In this case, you can attach the evidence to the artifact after its creation. Use `backend` (the artifact's `name` from the template), as well as `security-scan` (the attestation's `name` from the template) to name the attestation.

  The following attestation will only belong to the artifact `my_company/backend:latest` attested above and its fingerprint, in this case calculated by the Kosli CLI.

  ```shell
  kosli attest system sarif \
      --artifact-type docker my_company/backend:latest \
      --name backend.security-scan \
      --flow backend-ci \
      --trail $(git rev-parse HEAD)
      ...
  ```
  </Step>
</Steps>

## Compliance

### Attesting with a template

The four attestations above are all made against a Flow named `backend-ci` and a Trail named after the git commit.
Typically, the Flow and Trail are explicitly setup before making the attestations (e.g. at the start of a CI workflow).

This is done with the `create flow` and `begin trail` commands, either of which can specify the name of the template yaml file above
(e.g. `.kosli.yml`) whose contents define overall compliance. For example:

```shell
kosli create flow backend-ci \
    --template-file .kosli.yml
    ...

kosli begin trail $(git rev-parse HEAD) \
    --flow backend-ci \
    ...
```

An attested `backend` artifact is then compliant if and only if all the template attestations have been made
against it and are themselves compliant:
- `jira-ticket` on its Trail
- `backend.unit-tests` for its junit evidence
- `backend.security-scan` for its snyk evidence

If any of these attestations are missing, or are individually non-compliant then the `backend` artifact is non-compliant.

### Attesting without a template

An attestation can also be made against a Flow and Trail **not** previously explicitly setup.
In this case a Flow and Trail will be automatically setup but there will be no template yaml file defining
overall compliance. The compliance of any attested artifact will depend only on the compliance of the attestations actually made
and never because a specific attestation is missing.


### Attestation immutability

You can set/edit the template yml file for the Flow/Trail at any time.
This will affect compliance evaluations made after the edit.
It will not affect earlier records of compliance evaluations (e.g. in Environment Snapshots).

Attestations are append-only immutable records. You can report the same attestation multiple times, and each report will be recorded.
However, only the latest version of the attestation is considered when evaluating compliance.

## Evidence Vault

Along with attestations data, you can attach additional supporting evidence files. These will be securely stored in Kosli's **Evidence Vault** and can easily be retrieved when needed. Alternatively, you can store the evidence files in your own preferred storage and only attach links to it in the Kosli attestation.

<Note>
For `JUnit` attestations (see below), Kosli automatically stores the JUnit XML results files in the Evidence Vault. You can disable this by setting `--upload-results=false`
</Note>

## Attaching data to attestations

All `kosli attest` commands support flags for attaching additional data. These flags accept file paths but serve different purposes:

| Flag | Available on | Purpose |
|------|-------------|---------|
| `--user-data` | All evidence attest commands | Attach structured JSON metadata that is stored and visible alongside the attestation in the Kosli UI |
| `--attachments` | All evidence attest commands | Upload files or directories to the Evidence Vault as compressed archives for later download |
| `--attestation-data` | `attest custom` only | Provide the JSON payload that the custom type's jq rules evaluate to determine compliance |

### When to use which

Use **`--user-data`** when you want to store additional context — such as build metadata, environment
variables, or tool versions — that is visible alongside the attestation in the Kosli UI.

```shell
kosli attest system generic \
    --name security-scan \
    --flow backend-ci \
    --trail $(git rev-parse HEAD) \
    --user-data scan-metadata.json
```

Use **`--attachments`** when you want to archive files for audit purposes — such as test reports,
scan output, or policy files — in the Evidence Vault for later retrieval. Provide multiple paths
as a comma-separated list.

```shell
kosli attest system generic \
    --name security-scan \
    --flow backend-ci \
    --trail $(git rev-parse HEAD) \
    --attachments scan-report.html,scan-config.yml
```

Use **`--attestation-data`** on `kosli attest custom` to provide the JSON data that the custom
attestation type's jq expression evaluates. This is what determines the compliance status of the
attestation. See the [Custom](#custom) attestation type below for details.

```shell
kosli attest custom \
    --type coverage-metrics \
    --name unit-tests \
    --flow backend-ci \
    --trail $(git rev-parse HEAD) \
    --attestation-data coverage-results.json
```

<Tip>
These flags can be combined. For example, you can use `--attestation-data` for compliance evaluation,
`--user-data` to store extra metadata, and `--attachments` to archive the full report — all on the
same attestation.
</Tip>

## Attestation types

Kosli supports two categories of attestation types: **system types** curated by Kosli, and **custom types** you define yourself. See the [attestation types overview](/attestation_types/overview) for the full comparison.

<AccordionGroup>
  <Accordion title="System types" icon="cube">

    System types are built in to Kosli — Kosli knows the shape of the input, parses it, and renders it in the trail. The current catalogue covers pull requests, JUnit results, SARIF scans, Jira issues, SonarQube analyses, and a generic catch-all.

    Reach a system type with `kosli attest system <type>` (e.g. `kosli attest system sarif`). Compliance is structural — the attestation records the fact. For opinions on the contents (e.g. *fail on any high finding*), express them as a rego policy and use [`kosli evaluate`](/tutorials/evaluate_trails_with_opa).

    See [available system types](/attestation_types/system/catalogue) for the full list, or the [system attestation types overview](/attestation_types/system/overview) for how versioning and templates work.

    The legacy dedicated commands (`kosli attest snyk`, `kosli attest junit`, `kosli attest jira`, `kosli attest sonar`, `kosli attest pullrequest_*`, `kosli attest generic`) are deprecated — teams should migrate to `kosli attest system <type>`.
  </Accordion>
  <Accordion title="Custom types" icon="puzzle-piece">

    Custom types let you define an attestation shape specific to your org. You write a JSON Schema for the data and one or more jq rules that determine compliance; once created, anyone in the org can attest against the type.

    For example, to attest coverage metrics from `unit-test-coverage.json`:

    ```bash
    kosli create attestation-type coverage-metrics \
      --jq=".code.lines.missed / .code.lines.total * 100 <= 5"

    kosli attest custom \
      --type=coverage-metrics \
      --attestation-data=unit-test-coverage.json \
      ...
    ```

    Use a custom type when no system type fits and you want a reusable, validated evidence shape across flows.

    See [custom attestation types](/attestation_types/custom/overview) for the conceptual overview, [`kosli create attestation-type`](/client_reference/kosli_create_attestation-type) to define one, and [`kosli attest custom`](/client_reference/kosli_attest_custom) to report against one.
  </Accordion>
</AccordionGroup>

