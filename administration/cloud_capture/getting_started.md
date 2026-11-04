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

Skip tags can also be set through the API, as part of the organization's Cloud Capture settings. The settings PUT replaces every setting, not only the one you are changing, so start from what is stored: read the current configuration, take the `enabled`, `default_regions`, `scan_interval_minutes`, `skip_tags`, `dry_run` and `environment_name_template` values from its `settings` object, add your tags to `skip_tags`, and send those fields back. A field you leave out is reset: `dry_run` to `false`, and `environment_name_template` to the [default template](#environment-names). The response leaves out `environment_name_template` while your organization uses the default, so leave it out of the PUT in that case too. Sending the example below as it stands would also set your default regions, scan interval and dry run to the values shown, and your environment names to the default.

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
    "skip_tags": {"aws": [{"key": "kosli-capture", "value": "false"}]},
    "dry_run": false
  }'
```
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

    You also need two values from Kosli: the Kosli AWS account ID, and the name of the Kosli-side IAM role for your organization. The configuration isn't pre-filled with them. Copy them from the Cloud Capture section of your organization's Settings page in the Kosli UI.
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

    After the deployment completes, register them with Kosli through the Kosli API's cloud accounts endpoint. You can read them at any time from the deployment's latest revision:

    ```bash
    gcloud infra-manager revisions describe \
        "$(gcloud infra-manager deployments describe \
            projects/<your-gcp-project>/locations/<your-gcp-region>/deployments/kosli-capture \
            --format='value(latestRevision)')" \
        --format='yaml(applyResults.outputs)'
    ```

    {/* TODO: Link to the cloud accounts endpoint in the API reference, and show the call, once it is published. */}
  </Step>
</Steps>

### Enable Cloud Capture

When you have deployed the configuration and registered the workload identity provider name and service account email with Kosli, you can activate Cloud Capture within the Kosli user-interface.  Cloud Capture scans every five minutes unless you [choose another frequency](#scan-frequency), and once you have enabled it, Cloud Capture will pick up your environment the next time it runs - you should see environments and snapshots appearing within a few minutes.

### Excluding resources

Excluding resources by label is coming with GCP support.
</Tab>
</Tabs>

## Scan frequency

Cloud Capture scans your registered accounts every five minutes unless you choose otherwise. The frequency is a setting of your Kosli organization, so it applies to every account and region Cloud Capture scans for you.

To change it, open your organization's **Settings**, go to **Cloud Capture**, and under **Scan frequency** pick an interval from the list: every 5, 10, 15 or 30 minutes, or every 1, 2, 6, 12 or 24 hours. Select **Save**, and the next scan runs at the new interval; nothing restarts and no snapshots are lost. Like the other Cloud Capture settings, the frequency can only be changed while Cloud Capture is enabled.

Each scan reports what is running in every environment Cloud Capture manages for you, and Kosli records a new snapshot when that differs from the last one. The interval is therefore how long a change can go unnoticed: a deployment that lands and is rolled back inside one interval may never be seen. Five minutes suits most teams; an estate that changes rarely can scan hourly.

Through the API, the frequency is `scan_interval_minutes` on the same settings resource as the skip tags above: any whole number of minutes from 5 to 1440 (a day), not only the presets the settings page offers, with 5 the value when it is left out. An interval set this way that is not one of the presets is shown on the settings page as its own option, so saving another setting there keeps it. The PUT replaces every setting, so read the current configuration first and send the other settings back unchanged.

## Environment names

Cloud Capture names each environment it reports into from a template. The default template is `{account_id}-{region}-{service}-{resource}`, so an ECS cluster named `app` in account `123456789012` and region `eu-central-1` reports into `123456789012-eu-central-1-ecs-app`. If a name matches an environment that already exists in your organization, Cloud Capture reports into that environment. This lets you name environments so you can tell accounts apart, or send snapshots into environments you already have.

To change the template, open your organization's **Settings**, go to **Cloud Capture**, and under **Environment names** select **Edit**. As you type, the page previews the names the template gives an example ECS cluster and a region's Lambda functions. Select **Save** to store it, or **Use the default** and then **Save** to go back to the default template. Like the other Cloud Capture settings, the template can only be changed while Cloud Capture is enabled. Resources are named with the new template from the next scan.

A template is text with any of these placeholders:

| Placeholder | Value |
|-------------|-------|
| `{cloud}` | The cloud provider, for example `aws`. |
| `{account_id}` | The cloud account ID. |
| `{region}` | The region, for example `eu-central-1`. |
| `{service}` | The service, for example `ecs` or `lambda`. |
| `{resource}` | The resource's own name, such as the ECS cluster name. |
| `{tag:Key}` | The value of the resource's tag `Key`. For example, `aws-{tag:Env}` names a cluster tagged `Env=prod` as `aws-prod`. |

How a template is rendered:

- The text between placeholders can only hold letters, digits, `.`, `_` and `-`, and a template must start with a letter, a digit or a placeholder. Placeholder names are case-sensitive and take no formatting.
- A region's Lambda functions are captured together as one resource, so `{resource}` and every `{tag:Key}` are empty for them. An empty placeholder removes the separator before it: with the default template, a region's Lambda functions report into `123456789012-eu-central-1-lambda`.
- Tag keys are case-sensitive, as AWS stores them, so `{tag:env}` does not read a tag named `Env`. A key may contain colons and spaces, as in `{tag:aws:cloudformation:stack-name}`.
- A resource that does not carry a tag the template names is not captured, and the scan reports it as failed. So is a resource whose rendered name Kosli does not accept, for example because a tag value contains a space. A tag that is present with an empty value renders empty.

<Warning>
Give every resource its own name. A template that renders the same name for two resources sends both into one environment, and that environment then switches between the two resources on every scan. This happens with `aws-prod` on an account with two ECS clusters, with a template that has no `{region}` on an account scanned in two regions, and with a template that has no `{account_id}` when two accounts hold a cluster of the same name. It also happens when a `{tag:Key}` placeholder is the only part that would tell resources apart: tag placeholders are empty for Lambda functions, so `aws-{tag:Env}` sends every region's Lambda functions into `aws`. Run a [dry run](#dry-run) to check the names before you rely on them.
</Warning>

Through the API, the template is `environment_name_template` on the same settings resource as the skip tags above. Leaving it out, or sending `null`, uses the default template. A template that breaks the rules above is refused with a `400` response.

## Dry run

A dry run shows what Cloud Capture would do without changing anything in your organization. Every scan that is a dry run searches the registered accounts and reports what it found, but records no snapshots and creates no environments.

To turn it on for the whole organization, open **Settings**, go to **Cloud Capture**, and switch on **Dry run**. To dry run a single account, switch on **Dry run** in that account's row of the **Registered accounts** table. While the organization-wide dry run is on, every account is a dry run. Like the other Cloud Capture settings, dry run can only be changed while Cloud Capture is enabled.

After a dry run, open the actions menu in the account's row and select **Show latest results**. The results list what the scan found in each region and service, the environment each resource would report into, which of those environments would be created, and why any resource failed. Switch dry run off to start recording snapshots.

Through the API, the organization-wide switch is `dry_run` on the same settings resource as the skip tags above.
