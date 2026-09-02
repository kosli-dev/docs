---
title: "Kosli Capture Managed Service"
sidebarTitle: "Kosli Capture"
description: "Learn how the Kosli Capture Managed Service snapshots your cloud environments from Kosli's infrastructure, with no software to install."
tag: "BETA"
---

<Warning>
Kosli Capture is still in beta. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Kosli Capture is a managed service that runs on Kosli's infrastructure and connects to your cloud platform to observe the resources deployed there. You grant Kosli Capture a set of permissions, and it uses them to run a `kosli snapshot` every few minutes against the infrastructure you have allowed it to scan.

Kosli also supports reporting from your own cloud accounts by running the Kosli CLI on a schedule. Kosli Capture inverts this, with Kosli running the regular [snapshots](/getting_started/environments) so there is no software for you to install.

## Current status

Kosli Capture currently supports ECS and Lambda running within AWS. Support for S3 snapshots and for other cloud providers is in active development. A limitation in Amazon's AWS API currently prevents Kosli Capture from snapshotting EKS clusters; support for Kubernetes running on other cloud providers (e.g. Azure) will be added shortly.

## Approach

Getting started with Kosli Capture involves three stages:

<Steps>
  <Step title="Create an IAM role">
    Create an IAM role in your AWS account specifically for Kosli Capture. Kosli provides a CloudFormation template to simplify this process. The template requires a shared secret, which Kosli provides to you during onboarding.
  </Step>
  <Step title="Author a configuration document">
    Working with Kosli's Customer Success team, author a configuration document that shows how your cloud resources should be mapped to Kosli environments. This configuration document is loaded into Kosli.
  </Step>
  <Step title="Enable Kosli Capture">
    Kosli enables Kosli Capture for your Kosli org, and the regular snapshots appear in Kosli.
  </Step>
</Steps>

## Finding resources

Kosli Capture finds all supported resources within your AWS accounts, and examines the tags on those resources to determine which Kosli environment should hold the snapshots. Kosli Capture will create physical environments for you.

Kosli Capture can filter out resources based on your tags.

As your cloud environment evolves, such as the addition of new ECS clusters or the retirement of existing Lambdas, Kosli Capture automatically detects the changes. Because Kosli Capture creates physical environments as needed, when your infrastructure changes, Kosli will keep up. No changes to the configuration created during the initial setup are required.

## Revoking Kosli Capture

To prevent Kosli Capture from snapshotting your infrastructure, revoke the IAM role created in the initial setup. This role is the only mechanism for Kosli Capture to connect to your cloud environment, so revoking it acts as a simple kill-switch.

## Multiple AWS accounts

Kosli Capture can operate across multiple AWS accounts, allowing you to snapshot development, QA, pre-production, and production workloads with the same configuration document.

## IAM permissions

For Kosli Capture to snapshot your environment, you must grant a set of read-only permissions. Kosli's CloudFormation template lists these. The permissions are typically "Describe" or "List" permissions.

The IAM role created in your environment includes a trust policy that allows Kosli Capture to assume the role. The trust policy limits access to the AWS account in which Kosli Capture is running. Furthermore, the trust policy includes an external ID that acts as a shared secret between Kosli and you, so that only access from Kosli Capture is permitted.

The external ID (shared secret) is securely stored with Kosli Capture. Kosli's internal IAM permissions ensure that the secret can only be accessed by the specific instance of Kosli Capture that has been configured for you.

## Kosli Capture runtime details

Within Kosli's AWS accounts, every customer has a dedicated instance of Kosli Capture running. The Kosli Capture instance for a customer is granted access to that customer's external ID and no other customer's external ID. Similarly, the API token needed to access the Kosli API on behalf of a customer is only accessible by the specific instance of Kosli Capture for that customer. By running isolated instances of the managed service per customer, Kosli guarantees that each customer's data remains separate.

## Snapshot frequency

The configuration for the Kosli Capture Managed Service includes a snapshot frequency parameter. Kosli defaults to running a snapshot every five minutes, but you can change the frequency to meet your own requirements.

## Scaling

Kosli Capture runs multiple snapshots in parallel to support customers with large numbers of Kosli environments or AWS accounts.
