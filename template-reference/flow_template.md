---
title: Flow Template
description: "Reference for the YAML template file used to define compliance controls for a Kosli flow."
---

A flow template defines what attestations are required for a trail and its artifacts to be compliant. You pass the template file when creating or updating a flow with [`kosli create flow --template-file`](/client_reference/kosli_create_flow).

## Specification

<ParamField path="version" type="integer" required>
  The version of the specification schema. Currently only `1` is supported.
</ParamField>

<ParamField path="trail" type="object">
  The trail specification. Defines what must be attested at the trail level and what artifacts are expected.

  <Expandable title="trail properties">
    <ParamField path="trail.attestations" type="array">
      Attestations required at the trail level for it to be compliant.

      <Expandable title="attestation properties">
        <ParamField path="trail.attestations[].name" type="string" required>
          A unique name for the attestation within this template.
        </ParamField>

        <ParamField path="trail.attestations[].type" type="string" required>
          The attestation type. One of: `generic`, `jira`, `junit`, `pull_request`, `snyk`, `sonar`, `*` (matches any type).
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField path="trail.artifacts" type="array">
      Artifacts expected to be produced in the trail. Each artifact can have its own attestation requirements.

      <Expandable title="artifact properties">
        <ParamField path="trail.artifacts[].name" type="string" required>
          A reference name for the artifact (e.g. `frontend-app`, `backend`).
        </ParamField>

        <ParamField path="trail.artifacts[].attestations" type="array">
          Attestations required for this artifact to be compliant.

          <Expandable title="attestation properties">
            <ParamField path="trail.artifacts[].attestations[].name" type="string" required>
              A unique name for the attestation within this artifact.
            </ParamField>

            <ParamField path="trail.artifacts[].attestations[].type" type="string" required>
              The attestation type. One of: `generic`, `jira`, `junit`, `pull_request`, `snyk`, `sonar`, or `custom:<custom-type-name>` for [custom attestation types](/client_reference/kosli_create_attestation-type).
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

## Example

Add the `$schema` comment to get editor validation and autocomplete:

```yaml
# yaml-language-server: $schema=https://kosli.mintlify.app/schemas/flow-template.json
version: 1
trail:
  attestations:
  - name: jira-ticket
    type: jira
  - name: risk-level-assessment
    type: generic
  artifacts:
  - name: backend
    attestations:
    - name: unit-tests
      type: junit
    - name: security-scan
      type: snyk
  - name: frontend
    attestations:
    - name: manual-ui-test
      type: generic
    - name: coverage-metrics
      type: custom:coverage-metrics
```

## Using the template

Pass the template file when creating or updating a flow:

```shell
kosli create flow my-flow --template-file ./flow-template.yml
```

Once the flow exists, start a trail with [`kosli begin trail`](/client_reference/kosli_begin_trail) and record attestations using the [`kosli attest`](/client_reference/kosli_attest_generic) commands. Kosli evaluates trail compliance against the template automatically.

<Info>
  Trail-level attestations apply to the entire trail. Artifact-level attestations apply to a specific artifact produced within the trail.
</Info>

## Editor validation

A [JSON Schema](https://kosli.mintlify.app/schemas/flow-template.json) is available for the flow template format. Add the following comment to the top of your template file to enable inline validation and autocomplete in VS Code (requires the [YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)) and other schema-aware editors:

```yaml
# yaml-language-server: $schema=https://kosli.mintlify.app/schemas/flow-template.json
```
