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
    Grant Kosli read-only access to your cloud accounts for Cloud Capture.
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

In order for Cloud Capture to reach into your GCP project, to discover your GKE clusters, you need to grant permission to Kosli to do so.  This requires a service account in your project that Cloud Capture can impersonate through workload identity federation; the service account, and the workload identity pool that guards it, exist within your own project.

To simplify this process, Kosli has created a Terraform configuration that creates that service account, a custom role holding the minimum set of permissions needed by Cloud Capture, and a workload identity pool that accepts only the Kosli-side role created for your organization.

If you would rather create these resources yourself, see [Cloud Capture Security](/administration/cloud_capture/security) for the service account, workload identity pool and custom role that Cloud Capture needs.

<Steps>
  <Step title="Download the Terraform configuration">
    Download the Terraform configuration from the Settings page for your organization within the Kosli UI.

    You also need two values from Kosli: the Kosli AWS account ID, and the name of the Kosli-side IAM role for your organization.

    {/* TODO: Confirm whether the Terraform downloaded from the Settings page comes pre-filled with the Kosli AWS account ID and role name, or where the user obtains them, and say so here. */}
  </Step>
  <Step title="Deploy with Infrastructure Manager">
    Deploy the configuration once in each project that holds GKE clusters you want Cloud Capture to snapshot. Run the following from the directory containing the configuration:

    ```bash
    gcloud infra-manager deployments apply \
        projects/<your-gcp-project>/locations/<your-gcp-region>/deployments/kosli-capture \
        --service-account=projects/<your-gcp-project>/serviceAccounts/<deployer>@<your-gcp-project>.iam.gserviceaccount.com \
        --local-source=. \
        --input-values=project_id=<your-gcp-project>,kosli_aws_account_id=<value from Kosli>,kosli_role_name=<value from Kosli>
    ```

    Infrastructure Manager runs Terraform as the service account you name, so that service account needs permission to enable APIs and to create workload identity pools, service accounts, custom roles and project IAM bindings.
  </Step>
  <Step title="Share the outputs with Kosli">
    Kosli needs two values to connect to your project. The configuration emits both as Terraform outputs:

    - `kosli_capture_provider`: the full resource name of the workload identity provider
    - `kosli_capture_service_account`: the email of the service account Cloud Capture impersonates

    Share them with Kosli after the deployment completes. You can read them at any time with `gcloud infra-manager deployments describe`.

    {/* TODO: Confirm where the user submits these two values (a form in the Kosli UI, or Customer Success) and say so here. */}
  </Step>
</Steps>

### Enable Cloud Capture

When you have deployed the configuration and shared the workload identity provider name and service account email with Kosli, you can activate Cloud Capture within the Kosli user-interface.  Cloud Capture runs on a five-minute schedule, and once you have enabled it, Cloud Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

### Excluding resources

Support for excluding resources is coming soon.
</Tab>
</Tabs>

