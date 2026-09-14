---
title: "Kosli Capture Managed Service"
sidebarTitle: "Kosli Capture"
description: "Learn how the Kosli Capture Managed Service snapshots your cloud environments from Kosli's infrastructure, with no software to install."
tag: "ALPHA"
---

<Warning>
Kosli Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Kosli Capture is a managed service that runs on Kosli's infrastructure and connects to your cloud platform to observe the resources deployed there. You grant Kosli Capture a set of permissions, and it uses them to run a `kosli snapshot` every few minutes against the infrastructure you have allowed it to scan.

Kosli also supports reporting from your own cloud accounts by running the Kosli CLI on a schedule. Kosli Capture inverts this, with Kosli running the regular [snapshots](/getting_started/environments) so there is no software for you to install.

## Overview

Kosli Capture connects to your cloud accounts using permissions that you manage.  You configure Kosli Capture by providing a few details describing what you want to be in scope, and Kosli Capture uses the permissions to regularly reach into your estate and record snapshots, sending the data into your Kosli organization.  Kosli Capture is architected to be driven by your tagging scheme; it examines the tags on your infrastructure and uses them to determine how to structure the snapshots, and how to build the environments within Kosli.

There are several benefits to this this architecture:

* the only infrastructure you need to manage is an IAM role; you do not need to install or execute any additional software in your cloud estate;
* Kosli Capture leverages your existing tagging scheme, so as your infrastructure evolves, Kosli Capture will automatically discover the snapshots it needs to take.

## Security

The security of your cloud infrastructure is the primary driver behind the internal architecture of the Kosli Capture managed service.  Kosli Capture runs as a shared, autoscaled service, but each job runs under a role that is scoped to one customer

* A Kosli Capture worker picks up a job for your organization and assumes a Kosli-side role that exists only for your organization. Only that role is permitted to call AssumeRole into A's account with A's ExternalId.
* When the job finishes, those credentials are discarded. A worker holding credentials for your cloud account has no path to anyone else's account.
* The trust policy's ExternalId lives in Parameter Store and is readable only by the Kosli-side role for your organization. The shared task role cannot read any customer's ExternalId. Separation is enforced by IAM, not by application code.

Kosli Catpure does not hold any customer data, it is near-stateless with the only thing it keeps is your configuration data.  Snapshots taken by Kosli Catpure are immediately sent to Kosli through the same ingest path as your existing pipelines.

## Hands-off operation

Kosli Capture has been designed to operate with no on-going support from you.  Once the initial security permissions have been created, Kosli capture will continue to operate in a headless mode.  Monitoring, maintenance and rotation of API keys is all handed automatically.  As your cloud infrastructure changes over time, Kosli capture will continue to find resources according to your tagging scheme without you needing to do anything; your application teams do not need to take any action in order to onboard their products and services into Kosli.

## Setup

Getting started with Kosli Capture involves three stages:

<Steps>
  <Step title="Prepare your environment">
    Create an IAM role in your AWS account specifically for Kosli Capture. Kosli provides a CloudFormation template to simplify this process. The template requires a shared secret, which Kosli provides to you during onboarding.
  </Step>
  <Step title="Write the configuration document">
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

## Multiple AWS accounts

Kosli Capture can operate across multiple AWS regions and accounts, allowing you to snapshot development, QA, pre-production, and production workloads with the same configuration document.

## IAM permissions

For Kosli Capture to snapshot your environment, you must grant a set of read-only permissions. Kosli's CloudFormation template lists these. The permissions are typically "Describe" or "List" permissions.  The [Kosli Capture Security](./kosli_capture_security) page provides a deep-diver into the structure of the permissions needed.

The IAM role created in your environment includes a trust policy that allows Kosli Capture to assume the role. The trust policy limits access to the AWS account in which Kosli Capture is running. Furthermore, the trust policy includes an external ID that acts as a shared secret between Kosli and you, so that only access from Kosli Capture is permitted.

The external ID (shared secret) is securely stored with Kosli Capture. Kosli's internal IAM permissions ensure that the secret can only be accessed by the specific instance of Kosli Capture worker that is operating for you.
