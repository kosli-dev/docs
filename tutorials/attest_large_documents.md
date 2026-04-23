---
title: "Attesting large documents (SBOMs, SARIF, vulnerability reports)"
description: "How to attest large security and compliance reports in Kosli using summary attestations and the Evidence Vault"
---

In this tutorial, we will attest a large security report to Kosli using a lightweight summary for compliance evaluation, with the full document preserved in the Evidence Vault for audit purposes.
By the end, you will have a Kosli attestation that captures the key facts from your report — vulnerability counts, severity levels, pass/fail status — and links to the full file for audit access.

This two-part approach keeps attestation payloads focused on what compliance rules need to evaluate, while ensuring the raw evidence remains available.

## Prerequisites

* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).
* A Kosli flow and trail to attest to — follow the [Getting started guide](/getting_started/flows) if you need one.
* A report file to attest (e.g. an SBOM in JSON format, or a SARIF vulnerability report).

## Step 1: Create a summary attestation type

Define a custom attestation type that captures the key facts from your report. In this example we use a vulnerability report distilled into a summary JSON file:

```json
{
  "critical": 0,
  "high": 2,
  "medium": 14,
  "low": 37
}
```

Create an attestation type that enforces a zero-critical-findings rule:

```shell
kosli create attestation-type vulnerability-summary \
  --description "Summary of vulnerability scan findings" \
  --jq '.critical == 0'
```

You should see: `attestation-type vulnerability-summary was created`.

You can verify it with:

```shell
kosli get attestation-type vulnerability-summary
```

## Step 2: Distill your report into a summary

Use `jq` (or any other tool) to extract the fields you care about from your full report and write them to a summary file.

For example, if your tool produces a SARIF file, you might count findings by severity and write the result to `vuln-summary.json`.

The exact transformation will depend on your tool's output format. The goal is a small JSON object that your attestation type's rules can evaluate.

## Step 3: Attest the summary and attach the full report

Use `--attachments` to upload the full report to the Evidence Vault alongside the summary attestation:

```shell
kosli attest custom \
  --type vulnerability-summary \
  --name security-scan \
  --flow <your-flow-name> \
  --trail <your-trail-name> \
  --attestation-data vuln-summary.json \
  --attachments full-report.sarif
```

Kosli will:

* Evaluate the jq rule against `vuln-summary.json` to determine compliance.
* Store `full-report.sarif` in the Evidence Vault, linked to this attestation.

## Step 4: Verify the attestation

```shell
kosli get attestation <attestation-name> \
  --flow <your-flow-name> \
  --trail <your-trail-name>
```

The attestation record will show the compliance status and include a link to the attached file in the Evidence Vault.

## What you've accomplished

You have attested a security report to Kosli using a lightweight summary for compliance evaluation, with the full document preserved in the Evidence Vault for audit purposes.

From here you can:
* Read the [`kosli create attestation-type`](/client_reference/kosli_create_attestation-type) reference for all available options.
* Read the [`kosli attest custom`](/client_reference/kosli_attest_custom) reference for attesting to artifacts.
* Review [naming conventions for attestation types](/implementation_guide/phase_2/plan_organizational_structure/naming_conventions/attestation_types).
