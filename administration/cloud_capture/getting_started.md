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

When you have created the IAM role, using the CloudFormation template, you can activate Cloud Capture within the Kosli user-interface.  Cloud Capture scans every five minutes unless you [choose another frequency](#scan-frequency), and once you have enabled it, Cloud Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

### Excluding resources

If there are resources you do not want Cloud Capture to snapshot, such as a test cluster or a service a vendor runs in your account, exclude them by tag. You choose the tags: in your organization's **Settings**, under **Cloud Capture**, the **Skip tags** panel takes any number of key and value pairs, and Cloud Capture skips every resource that carries one of them.

1. Tag the resource in AWS, with any key and value you like. For example, to tag an ECS cluster and a Lambda function with `kosli-capture=false`:

   ```bash
   aws ecs tag-resource \
     --resource-arn arn:aws:ecs:eu-west-1:123456789012:cluster/sandbox \
     --tags key=kosli-capture,value=false

   aws lambda tag-resource \
     --resource arn:aws:lambda:eu-west-1:123456789012:function:scratch \
     --tags kosli-capture=false
   ```

2. In the **Skip tags** panel, enter the key `kosli-capture` and the value `false`, select **Add**, then **Save**.

How the tags are matched:

- A resource is skipped when any one of its tags equals any one of the skip tags, key and value both, exactly as AWS stores them. Tags are case-sensitive, so `Env=test` does not match `env=test`. A key on its own does not match: to skip both `env=test` and `env=staging`, add both.
- The tag is read on the resource Cloud Capture snapshots. An ECS cluster is skipped with everything in it, its services and tasks included; tags on a service or a task definition are not read. A Lambda function is skipped on its own, and the region's Lambda environment in Kosli is made up of the functions that remain.
- The change takes effect on the next scan. A Kosli environment that was already being captured keeps its last snapshot and receives no new ones; nothing is deleted. Remove the tag, or the skip tag, and the next run picks the resource up again.
- Skip tags, like the other Cloud Capture settings, can only be changed while Cloud Capture is enabled.
- The IAM role created by the CloudFormation template already grants the permissions needed to read tags, `ecs:DescribeClusters` and `lambda:ListTags`, so no change to the role is needed.

Skip tags can also be set through the API, as part of the organization's Cloud Capture settings. The settings PUT replaces every setting, not only the one you are changing, so start from what is stored: read the current configuration, take the `enabled`, `default_regions`, `scan_interval_minutes` and `skip_tags` values from its `settings` object, add your tags to `skip_tags`, and send those four fields back. Sending the example below as it stands would also set your default regions and scan interval to the values shown.

```bash
curl "https://app.kosli.com/api/v2/cloud-capture/<your-org>" \
  -H "Authorization: Bearer <api-key>"

curl -X PUT "https://app.kosli.com/api/v2/cloud-capture/<your-org>/settings" \
  -H "Authorization: Bearer <api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": true,
    "default_regions": {"aws": ["eu-west-1"]},
    "scan_interval_minutes": 5,
    "skip_tags": {"aws": [{"key": "kosli-capture", "value": "false"}]}
  }'
```
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

When you have created the role and added the account details to Kosli, you can activate Cloud Capture within the Kosli user-interface.  Cloud Capture scans every five minutes unless you [choose another frequency](#scan-frequency), and once you have enabled it, Cloud Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

### Excluding resources

Excluding resources by label is coming with GCP support.
</Tab>
</Tabs>

## Scan frequency

Cloud Capture scans your registered accounts every five minutes unless you choose otherwise. The frequency is a setting of your Kosli organization, so it applies to every account and region Cloud Capture scans for you.

To change it, open your organization's **Settings**, go to **Cloud Capture**, and under **Scan frequency** pick an interval from the list: every 5, 10, 15 or 30 minutes, or every 1, 2, 6, 12 or 24 hours. Select **Save**, and the next scan runs at the new interval; nothing restarts and no snapshots are lost. Like the other Cloud Capture settings, the frequency can only be changed while Cloud Capture is enabled.

Each scan reports what is running in every environment Cloud Capture manages for you, and Kosli records a new snapshot when that differs from the last one. The interval is therefore how long a change can go unnoticed: a deployment that lands and is rolled back inside one interval may never be seen. Five minutes suits most teams; an estate that changes rarely can scan hourly. Scanning more often than every five minutes is available on request through Kosli's Customer Success team.

Through the API, the frequency is `scan_interval_minutes` on the same settings resource as the skip tags above: a whole number of minutes from 5 to 1440 (a day), with 5 the value when it is left out. The PUT replaces every setting, so read the current configuration first and send the other settings back unchanged.

