---
title: "Getting Started with Kosli Capture"
sidebarTitle: "Getting started"
description: "Learn how to configure Kosli Capture for your organization"
tag: "ALPHA"
---

<Warning>
Kosli Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Kosli Capture is a managed service that runs on Kosli's infrastructure and connects to your cloud platform to observe the resources deployed there. To get set up with Kosli Capture you need to grant permissions to Kosli's cloud account and provide configuration details for how your tags should map to environments within Kosli.

## Overview

Getting started with Kosli Capture involves two stages:

<Steps>
  <Step title="Prepare your environment">
    Create an IAM role in your AWS account specifically for Kosli Capture. Kosli provides a CloudFormation template to simplify this process. The template requires a shared secret, which Kosli provides to you.
  </Step>
  <Step title="Enable Kosli Capture">
    Enable Kosli Capture for your Kosli org, and the regular snapshots appear in Kosli.
  </Step>
</Steps>

## Prepare your environment

In order for Kosli Capture to reach into your cloud, to discover your ECS clusters and Lambdas, you need to grant permission to Kosli to do so.  Within AWS this requires the creation of an IAM role that Kosli can assume; the role will exist within your AWS account.

To simplify this process, Kosli has created a CloudFormation template that contains a role with the minimum set of permissions needed by Kosli Capture.  The role can be assumed by Kosli and is protected by an external Id; each organization within Kosli has its own external Id.

The CloudFormation template can be deployed within an AWS account, or can be attached to an AWS Organizational Unit (OU) as a StackSet; this latter option ensures the correct IAM permissions are rolled out to all AWS accounts within the OU.

When used, the CloudFormation template will send your AWS account id to Kosli, so that we are automatically notified that your account is ready to be included in Kosli Capture.  Similarly, if you delete the CloudFormation stack we will be notified and know that the account is no longer to be included.

## Enable Kosli Capture

When you have created the IAM role, using the CloudFormation template, you can activate Kosli Capture within the Kosli user-interface.  Kosli Capture runs on a five-minute schedule, and once you have enabled it, Kosli Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

## Excluding resources

If there are resources you do not wish to include within a Kosli Capture Managed snapshot, for example an ECS cluster that you consider to be out of scope, you can add an AWS tag to it indicating that the item should be skipped.  Adding a tag with the name `kosli.capture` and the value `false` will ensure that Kosli Capture skips over that resource.
