---
title: "Kosli Capture Managed Service"
sidebarTitle: "Kosli Capture"
description: "Learn how the Kosli Capture Managed Service snapshots your cloud environments from Kosli's infrastructure, with no software to install."
tag: "BETA"
---

<Warning>
Kosli Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Kosli Capture is a managed service that runs on Kosli's infrastructure and connects to your cloud platform to observe the resources deployed there. You grant Kosli Capture a set of permissions, and it uses them to run a `kosli snapshot` every few minutes against the infrastructure you have allowed it to scan.

Kosli also supports reporting from your own cloud accounts by running the Kosli CLI on a schedule. Kosli Capture inverts this, with Kosli running the regular [snapshots](/getting_started/environments) so there is no software for you to install.

To set it up for your organization, see [Getting started with Kosli Capture](/administration/kosli_capture/getting_started).

## Overview

Kosli Capture connects to your cloud accounts using permissions that you manage.  You configure Kosli Capture by activating it for different services, and Kosli Capture uses the permissions to regularly reach into your estate and record snapshots, sending the data into your Kosli organization.  Kosli Capture uses details about your infrastructure, such as the name of an ECS cluster, to build environments within Kosli.

<Frame>
<img src="/images/administration/kosli-capture-overview.png" alt="Diagram showing Kosli Capture, inside Kosli, sending queries to and receiving snapshots from three customer cloud accounts, then passing the data to the Kosli API and database" />
</Frame>

## Security

The security of your cloud infrastructure is the primary driver behind the internal architecture of
Kosli Capture. You grant a read-only IAM role in your account, protected by an external ID that acts
as a shared secret between Kosli and you. On Kosli's side, each Kosli Capture job runs under a role
scoped to your organization alone, so a worker running for another customer cannot reach your cloud
account. Kosli Capture holds no customer data; snapshots go straight to Kosli through the same ingest
path as your existing pipelines. See [Kosli Capture Security](/administration/kosli_capture/security)
for the isolation model and the full list of permissions.

## Hands-off operation

Kosli Capture has been designed to operate with no on-going support from you.  Once the initial security permissions have been created, Kosli Capture will continue to operate in a headless mode. As your cloud infrastructure changes over time, Kosli Capture will continue to find resources without you needing to do anything; your application teams do not need to take any action in order to onboard their products and services into Kosli.

## Finding resources

Kosli Capture finds all supported resources within your AWS accounts, and determines which Kosli environment should hold the snapshots. Kosli Capture will create physical environments for you inside Kosli.

Kosli Capture can [filter out resources based on AWS tags](/administration/kosli_capture/getting_started#excluding-resources).

As your cloud environment evolves, such as the addition of new AWS ECS clusters or the retirement of existing Lambdas, Kosli Capture automatically detects the changes. Because Kosli Capture creates physical environments as needed, when your infrastructure changes, Kosli will keep up. No changes to the configuration created during the initial setup are required.

## Multiple AWS accounts

Kosli Capture can operate across multiple AWS regions and accounts, allowing you to snapshot development, QA, pre-production, and production workloads with the same process.

## Operation

When Kosli Capture runs against one of your cloud accounts, it starts by gaining temporary credentials for the role you have created. It then uses these credentials to find resources to snapshot, such as finding all of your AWS ECS clusters.  For each resource it identifies, Kosli Capture generates a snapshot within Kosli.

<Frame>
<img src="/images/administration/kosli-capture-4-steps.png" alt="Diagram of the four steps Kosli Capture follows in a customer AWS account: assume the IAM role using the external ID, receive temporary STS credentials, find the ECS clusters, then snapshot the clusters" />
</Frame>

