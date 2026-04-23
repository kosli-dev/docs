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
    type: jira
  artifacts:
  - name: backend
    attestations:
    - name: unit-tests
      type: junit
    - name: security-scan
      type: snyk
```

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
    kosli attest jira \
        --flow backend-ci \
        --trail $(git rev-parse HEAD) \
        --name jira-ticket
        ...
    ```
  </Step>
  <Step title="Attest unit tests to the backend artifact">
  Some attestations are attached to a specific artifact, like the unit tests for the `backend` artifact. Often, evidence like unit tests are created _before_ the artifact is built. To attach the evidence to the artifact before its creation, use `backend` (the artifact's `name` from the template), as well as `unit-tests` (the attestation's `name` from the template).

  ```shell
  kosli attest junit \
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
  kosli attest snyk \
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
kosli attest generic \
    --name security-scan \
    --flow backend-ci \
    --trail $(git rev-parse HEAD) \
    --user-data scan-metadata.json
```

Use **`--attachments`** when you want to archive files for audit purposes — such as test reports,
scan output, or policy files — in the Evidence Vault for later retrieval. Provide multiple paths
as a comma-separated list.

```shell
kosli attest generic \
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

<Warning>
The total request payload — including all data and attachments — is limited to **10 MB** per attestation.
This applies to `--user-data`, `--attachments`, and `--attestation-data` combined. If you need to
attach larger files, store them externally and use `--external-url` to link to them.
</Warning>

## Attestation types

Currently, we support the following types of evidence:

<AccordionGroup>
  <Accordion title="Pull requests" icon="code-pull-request">

    If you use GitHub, Bitbucket, Gitlab or Azure DevOps you can use Kosli to verify if a given git commit comes from a pull/merge request.

    <Warning>
    Currently, the status of the PR does NOT impact the compliance status of the attestation.
    </Warning>

    If there is no pull request for the commit, the attestation will be reported as `non-compliant`. You can choose to short-circuit execution in case pull request is missing by using the `--assert` flag.

    See the CLI reference for the following commands for more details and examples:

    - [attest Github PR ](/client_reference/kosli_attest_pullrequest_github/)
    - [attest Bitbucket PR ](/client_reference/kosli_attest_pullrequest_bitbucket/)
    - [attest Gitlab PR ](/client_reference/kosli_attest_pullrequest_gitlab/)
    - [attest Azure Devops PR ](/client_reference/kosli_attest_pullrequest_azure/)
  </Accordion>
  <Accordion title="JUnit test results" icon="file-check">

    If you produce your test results in JUnit format, you can attest the test results to Kosli. Kosli will analyze the JUnit results and determine the compliance status based on whether any tests have failed and/or errored or not.

    See [attest JUnit results to an artifact or a trail](/client_reference/kosli_attest_junit/) for usage details and examples.
  </Accordion>
  <Accordion title="Snyk security scans" icon="barcode-read">

    You can report results of a Snyk security scan to Kosli and it will analyze the Snyk scan results and determine the compliance status based on whether vulnerabilities were found or not.

    See [attest Snyk results to an artifact or a trail](/client_reference/kosli_attest_snyk/) for usage details and examples.
  </Accordion>
  <Accordion title="Jira issues" icon="clipboard-list-check">

    You can use the Jira attestation to verify that a git commit or branch contains a reference to a Jira issue and that an issue with the same reference does exist in Jira.

    If Jira reference is found in a commit message, that reference will be reported as evidence. If the reference is not found in the commit message, Kosli CLI will check if it's a part of a branch name.

    Kosli CLI will also verify and report if the detected issue reference is found and accessible on Jira (reported as compliant) or not (reported as non compliant).

    See [attest Jira issue to an artifact or a trail](/client_reference/kosli_attest_jira/) for usage details and examples.

  </Accordion>
  <Accordion title="SonarQube scan results" icon="bug">

    You can report the results of a SonarQube Server or SonarQube Cloud scan to Kosli. Kosli will use the status of the scan's Quality Gate (passing or failing) to determine the compliance status.

    These scan result can be attested in two ways:
    - Using Kosli's [webhook integration](/integrations/sonar) with Sonar
    - Using [Kosli's CLI](/client_reference/kosli_attest_sonar)
  </Accordion>
  <Accordion title="Custom" icon="puzzle-piece">

    The above attestations are all "fully typed" - each one knows how to interpret its own particular kind of input.
    For example, `kosli attest snyk` interprets the sarif file produced by a snyk container scan to determine the `true/false` value.
    If you're using a tool that does not yet have a corresponding kosli attest command we recommend creating your own custom attestation type.

    A custom attestation type specifies one or more arbitrary evaluation rules.
    These rules can have an optional schema specifying the types of the names used in the rules, whether they are required, whether they have defaults, etc.
    When a custom attestation is made using this type its rules are applied to the provided custom attestation data to determine its `true/false` compliance status.

    For example, suppose you wish to attest coverage metrics captured as part of a unit-test run.
    The coverage metrics are being saved in a file called `unit-test-coverage.json` as follows:
    ```json
    {
      "code": {
        "lines": {
          "missed": 32,
          "total": 1209
        }
      },
      ...
    }
    ```
    You could create a custom attestation type called `coverage-metrics` using a [jq expression](https://jqlang.org/manual/) rule defining a minimum line coverage of 95%:

    ```bash
    kosli create attestation-type coverage-metrics
      --jq=".code.lines.missed / .code.lines.total * 100 <= 5"
    ```

    You could then make your custom attestation with the json file:
    ```bash
    kosli attest custom
      --type=coverage-metrics
      --attestation-data=unit-test-coverage.json
      ...
    ```

    For this attestation, Kosli would:
    - Evaluate the rule `.code.lines.missed / .code.lines.total * 100 <= 5`
    - Using the values from the file `unit-test-coverage.json`
      - `.code.lines.missed` is `32`
      - `.code.lines.total` is `1209`
    - So `32 / 1209 * 100 <= 5` evaluates to `2.64 <= 5` which is `true`


    See:
    * [create custom attestation type](/client_reference/kosli_create_attestation-type) and
    * [report custom attestation to an artifact or a trail](/client_reference/kosli_attest_custom/) for usage details and examples.
  </Accordion>
  <Accordion title="Generic" icon="certificate">

    <Warning>
    Generic attestations are an earlier, much less sophisticated version of custom attestations.
    We recommend using custom attestations instead of generic attestations.
    </Warning>

    See [report generic attestation to an artifact or a trail](/client_reference/kosli_attest_generic/) for usage details and examples.
  </Accordion>
</AccordionGroup>

