---
title: "Getting started with Cloud Capture"
sidebarTitle: "Getting started"
description: "Learn how to configure Cloud Capture for your organization"
tag: "BETA"
---

<Warning>
Cloud Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Cloud Capture is a managed service that runs on Kosli's infrastructure and connects to your cloud platform to observe the resources deployed there. To get set up with Cloud Capture you need to grant permissions to Kosli's cloud account and enable Cloud Capture within your Kosli org.

## Overview

Getting started with Cloud Capture involves two steps.

<Steps>
  <Step title="Prepare your environment">
    Create an IAM role in your cloud accounts specifically for Cloud Capture.
  </Step>
  <Step title="Enable Cloud Capture">
    Enable Cloud Capture for your Kosli org, and the regular snapshots will appear in Kosli.
  </Step>
</Steps>

<Tabs>
<Tab title="AWS">

### Prepare your environment

In order for Cloud Capture to reach into your AWS cloud, to discover your ECS clusters and Lambdas, you need to grant permission to Kosli to do so. This requires the creation of an IAM role that Kosli can assume; the role will exist within your AWS account.

To simplify this process, Kosli has created a CloudFormation template that contains a role with the minimum set of permissions needed by Cloud Capture.  The role can be assumed by Kosli and is protected by an external Id; each organization within Kosli has its own external Id.  The CloudFormation template can be downloaded from the Settings page for your organization within the Kosli UI.

If you would rather create the role yourself, see [Cloud Capture Security](/administration/cloud_capture/security) for the trust policy and the full set of permissions the role needs.

The CloudFormation template can be deployed within an AWS account, or can be attached to an AWS Organizational Unit (OU) as a StackSet; this latter option ensures the correct IAM permissions are rolled out to all AWS accounts within the OU.

When used, the CloudFormation template will send your AWS account id to Kosli, so that we are automatically notified that your account is ready to be included in Cloud Capture.  Similarly, if you delete the CloudFormation stack we will be notified and know that the account is no longer to be included.

### Enable Cloud Capture

When you have created the IAM role, using the CloudFormation template, you can activate Cloud Capture within the Kosli user-interface.  Cloud Capture runs on a five-minute schedule, and once you have enabled it, Cloud Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

### Excluding resources

If there are resources you do not wish to include within a Cloud Capture snapshot, for example an ECS cluster that you consider to be out of scope, you can add a tag to it indicating that the item should be skipped.  Adding a tag with the name `kosli.capture` and the value `false` will ensure that Cloud Capture skips over that resource.
</Tab>
<Tab title="GCP">

<Warning>
GCP support is coming soon
</Warning>

### Prepare your environment

In order for Cloud Capture to reach into your GCP project, to discover your Kubernetes clusters, you need to grant permission to Kosli to do so.  This requires a service account in your project that Cloud Capture can impersonate through workload identity federation; the service account, and the workload identity pool that guards it, exist within your own project.

To simplify this process, Kosli has created a Terraform configuration that creates that service account, a custom role holding the minimum set of permissions needed by Cloud Capture, and a workload identity pool that accepts only the Kosli-side role created for your organization.  The Terraform can be downloaded from the Settings page for your organization within the Kosli UI.

If you would rather create the role yourself, see [Cloud Capture Security](/administration/cloud_capture/security) for the trust policy and the full set of permissions the role needs.

GCP has no equivalent of the CloudFormation "phone-home" feature, so the Terraform configuration emits the two values Kosli needs — the workload identity provider and the service account email — as outputs. Share them with Kosli once the deployment completes; you can read them at any time with `gcloud infra-manager deployments describe`. See [Cloud Capture Security](/administration/cloud_capture/security) for the deployment command.

### Enable Cloud Capture

When you have created the role and added the account details to Kosli, you can activate Cloud Capture within the Kosli user-interface.  Cloud Capture runs on a five-minute schedule, and once you have enabled it, Cloud Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

### Excluding resources

Support for excluding resources is coming soon.
</Tab>
</Tabs>

