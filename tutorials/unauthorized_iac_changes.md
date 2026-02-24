---
title: "Detecting unauthorized Terraform changes"
description: "Learn how to use Kosli to detect unauthorized Terraform infrastructure changes — changes made outside your approved CI process."
---

By the end of this tutorial, you will have set up Kosli to track authorized Terraform changes and detect when an unauthorized change slips through.

<Info>
This tutorial focuses on detecting changes made by bypassing the approved Terraform process (e.g. a developer running `terraform apply` directly from their machine). Detecting <Tooltip tip="Drift occurs when infrastructure is changed directly via cloud APIs, consoles, or CLI tools without going through Terraform at all, causing the actual state to diverge from the desired state defined in your Terraform config.">infrastructure drift</Tooltip> is a separate concern covered by [Terraform drift detection](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift).
</Info>

## Prerequisites

* [Install Terraform](https://developer.hashicorp.com/terraform/install).
* [Install Snyk CLI](https://docs.snyk.io/snyk-cli/getting-started-with-the-snyk-cli#install-the-snyk-cli-and-authenticate-your-machine) (optional — needed for the security scan step).
* [Create a Kosli account](https://app.kosli.com/) if you do not have one.
* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).

## Setup

```shell
export KOSLI_ORG=<your-personal-kosli-org-name>
export KOSLI_API_TOKEN=<your-api-token>
```

Clone the tutorial repository:

```shell
git clone https://github.com/kosli-dev/iac-changes-tutorial.git
cd iac-changes-tutorial
```

## Create a Kosli flow

Create a Kosli flow to represent the approved process for Terraform changes. Using <Tooltip tip="Creates a flow with no required attestations, useful for getting started without defining compliance requirements upfront.">--use-empty-template</Tooltip> keeps things simple for this tutorial:

```shell
kosli create flow tf-tutorial --use-empty-template
```

## Make and track an authorized change

<Info>
In production, an authorized change goes through CI. In this tutorial, you run those commands locally to simulate the process.
</Info>

Begin a trail to represent a single authorized change:

```shell
kosli begin trail authorized-1 --flow=tf-tutorial
```

Optionally, scan your Terraform config for security issues and attest the <Tooltip tip="Static Analysis Results Interchange Format — a standard JSON format for reporting security findings from static analysis tools.">SARIF</Tooltip> output to Kosli:

```shell
snyk iac test main.tf --sarif-file-output=sarif.json
kosli attest snyk --name=security --flow=tf-tutorial --trail=authorized-1 --scan-results=sarif.json
```

Create a Terraform plan, save it to a file, and attest it to Kosli:

```shell
terraform init
terraform plan -out=tf.plan
kosli attest generic --name=tf-plan --flow=tf-tutorial --trail=authorized-1 --attachments=tf.plan
```

Apply the plan and attest the resulting <Tooltip tip="A JSON file Terraform uses to map your configuration to real-world infrastructure. Its SHA256 fingerprint uniquely identifies the current infrastructure state.">state file</Tooltip> as an artifact. Kosli calculates a fingerprint from the state file contents — this fingerprint is how it later detects unauthorized changes:

<Info>
This tutorial uses a local state file for simplicity. In production, the state file is typically stored in cloud storage (e.g. AWS S3) and you would download it after the authorized change. Note that `--build-url` and `--commit-url` are set to placeholder URLs here — in CI these are set automatically.
</Info>

```shell
terraform apply -auto-approve tf.plan
kosli attest artifact terraform.tfstate --name=state-file --artifact-type=file --flow=tf-tutorial --trail=authorized-1 \
   --build-url=https://example.com --commit-url=https://example.com --commit=HEAD
```

## Monitor the state file

To detect unauthorized changes, Kosli monitors the state file for changes by tracking it in an environment. Create a `server` environment:

```shell
kosli create env terraform-state --type=server
```

Report the current state file to the environment:

<Info>
In production, configure environment reporting to run periodically or on state file changes. See [reporting AWS environments](/tutorials/report_aws_envs) if you use S3 as your Terraform backend.
</Info>

```shell
kosli snapshot path terraform-state --name=tf-state --path=terraform.tfstate
```

Check the latest snapshot:

```shell
kosli get snapshot terraform-state
```

You should see:

```plaintext
COMMIT   ARTIFACT                                                                       FLOW         COMPLIANCE     RUNNING_SINCE  REPLICAS
d881b2f  Name: tf-state                                                                 tf-tutorial  NON-COMPLIANT  28 minutes ago   1
         Fingerprint: a57667a7b921b91d438631afa1a1fe35300b4da909a19d2b61196580f30f1d0c
```

The `FLOW` column shows `tf-tutorial` — Kosli has provenance for this change. In the Kosli UI under **Environments > terraform-state**, the artifact shows as compliant.

<Frame><img src="/images/authorized-iac-change.png" alt="Environment shows an authorized change" /></Frame>

## Introduce an unauthorized change

Simulate an unauthorized change by modifying line 6 of `main.tf` — change `random_pet_result` to `random_pet_name` — then apply directly without going through the approved process:

```shell
terraform apply --auto-approve
```

Report the updated state file to Kosli:

<Info>
In production this step is not needed — environment reporting runs automatically on change or on a schedule.
</Info>

```shell
kosli snapshot path terraform-state --name=tf-state --path=terraform.tfstate
```

Check the snapshot again:

```shell
kosli get snapshot terraform-state
```

You should see:

```plaintext
COMMIT  ARTIFACT                                                                       FLOW  COMPLIANCE     RUNNING_SINCE   REPLICAS
N/A     Name: tf-state                                                                 N/A   NON-COMPLIANT  8 minutes ago  1
        Fingerprint: edd93dcde27718ed493222ceb218275655555f3f3bfefa95628c599e678ac325
```

The `FLOW` is now `N/A` — Kosli has no provenance for this state file fingerprint. It was not attested through any known flow, which means the change was unauthorized. The environment page reflects this:

<Frame><img src="/images/unauthorized-iac-change.png" alt="Environment shows an unauthorized change" /></Frame>

## What you've accomplished

You have used Kosli to track authorized Terraform changes and detect an unauthorized one. By fingerprinting the Terraform state file and comparing it against attested artifacts, Kosli can tell whether a running infrastructure state came from an approved process or not.

From here you can:
* Set up alerts and automated responses when unauthorized changes are detected using [Kosli actions](/integrations/actions)
* See how to report S3-backed state files automatically in the [Report AWS environments](/tutorials/report_aws_envs) tutorial
