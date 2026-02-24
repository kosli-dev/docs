---
title: "Creating custom CTRF attestation type"
description: "In this tutorial, we will create a custom attestation type with schema and evaluation for Common Test Report Format"
---

In this tutorial, we will create a <Tooltip tip="A user-defined attestation type in Kosli that validates reported data against a JSON schema and evaluates it against a jq compliance rule.">custom attestation type</Tooltip> for <Tooltip tip="Common Test Report Format — a standardised JSON schema for test execution reports that works across testing frameworks such as Jest, Pytest, and Mocha." cta="Learn more" href="https://ctrf.io/">CTRF</Tooltip>.
By the end, you will have a reusable `ctrf` attestation type in Kosli that validates test reports and enforces a zero-failures compliance rule.

## Prerequisites

* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).
* A Kosli flow and trail to attest to — follow the [Getting started guide](/getting_started/flows) if you need one.

## Download the CTRF schema

Download the official <Tooltip tip="A JSON schema defines the expected structure and types of a JSON document, used here to validate that reported test results conform to the CTRF specification." cta="Learn more" href="https://json-schema.org/learn">JSON schema</Tooltip> for CTRF to a file named `ctrf-schema.json`:

```shell
curl -o ctrf-schema.json https://ctrf.io/schemas/schema.json
```

## Create the attestation type

Use `kosli create attestation-type` to define the new type with a <Tooltip tip="A jq expression evaluated against the reported data to determine compliance. If it returns true, the attestation passes; if false, it fails." cta="jq docs" href="https://jqlang.github.io/jq/">jq compliance rule</Tooltip> that requires zero failed tests:

```shell
kosli create attestation-type ctrf \
  --description "Attestation for Common Test Report Format (CTRF)" \
  --schema ctrf-schema.json \
  --jq '.results.summary.failed == 0'
```

You should see: `attestation-type ctrf was created`.

You can verify it exists by running:

```shell
kosli get attestation-type ctrf
```

## Report a CTRF attestation

Once your tests have run and produced a CTRF report (e.g. `ctrf-report.json`), report it to Kosli:

```shell
kosli attest custom \
  --type ctrf \
  --name playwright-tests \
  --flow <your-flow-name> \
  --trail <your-trail-name> \
  --attestation-data ctrf-report.json
```

Kosli will validate `ctrf-report.json` against the schema and evaluate the jq rule. If `.results.summary.failed` is 0, the attestation will be marked as compliant.

## What you've accomplished

You have created a reusable `ctrf` custom attestation type and used it to report a test result to Kosli. Any team in your organisation can now use this same type to uniformly enforce a zero-failures quality gate across all projects, regardless of which testing framework they use.

From here you can:
* Read the [`kosli create attestation-type`](/client_reference/kosli_create_attestation-type) reference for all available options
* Read the [`kosli attest custom`](/client_reference/kosli_attest_custom) reference for attesting to artifacts
* Review [naming conventions for attestation types](/implementation_guide/phase_2/plan_organizational_structure/naming_conventions/attestation_types)
