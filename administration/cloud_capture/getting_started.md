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

Getting started with Cloud Capture involves two steps. Each step has instructions for AWS, Azure and Google Cloud. Azure and Google Cloud are in early access, so their pages appear in your settings only once Kosli has enabled them for your organization.

<Steps>
  <Step title="Prepare your environment">
    <Tabs>
      <Tab title="AWS">
        In order for Cloud Capture to reach into your AWS cloud, to discover your ECS clusters, Lambdas and S3 buckets, you need to grant permission to Kosli to do so. This requires the creation of an IAM role that Kosli can assume; the role will exist within your AWS account.

        To simplify this process, Kosli has created a CloudFormation template that contains a role with the minimum set of permissions needed by Cloud Capture.  The role can be assumed by Kosli and is protected by an external Id; each organization within Kosli has its own external Id.  The CloudFormation template can be downloaded from the Settings page for your organization within the Kosli UI.

        If you would rather create the role yourself, see [Cloud Capture Security](/administration/cloud_capture/security) for the trust policy and the full set of permissions the role needs.

        The CloudFormation template can be deployed within an AWS account, or can be attached to an AWS Organizational Unit (OU) as a StackSet; this latter option ensures the correct IAM permissions are rolled out to all AWS accounts within the OU.

        The template's **S3 buckets** parameter is empty by default, and the role can then read no object in any bucket. Leave it empty unless you want S3 buckets snapshotted; see [Capturing S3 buckets](#capturing-s3-buckets).
      </Tab>
      <Tab title="Azure">
        Nothing is deployed in Azure. Cloud Capture reads a subscription as a Kosli application registered in Microsoft Entra, which you consent to in your tenant and then grant read access on each subscription.

        <Steps>
          <Step title="Consent to the Kosli application">
            In your organization's **Settings**, go to **Cloud Capture**, open **Azure** and select **Register account**. Follow the **Consent in Azure** link as a Global Administrator of your tenant. Consenting creates the application's service principal in your tenant; it has no access until you grant it some in the next step.
          </Step>
          <Step title="Grant access and tag the subscription">
            The registration form shows three Azure CLI commands with your values filled in. Run them as an owner of the subscription:

            ```bash
            az role assignment create --assignee "<kosli-application-id>" --role Reader --scope "/subscriptions/<subscription-id>"
            az role assignment create --assignee "<kosli-application-id>" --role AcrPull --scope "/subscriptions/<subscription-id>"
            az tag update --resource-id "/subscriptions/<subscription-id>" --operation Merge --tags kosli-external-id="<your-external-id>"
            ```

            `Reader` lets Cloud Capture list the App Service sites and read tags, and `AcrPull` lets it fingerprint their container images. The `kosli-external-id` tag is how Cloud Capture checks the subscription is yours to read: it refuses to list a subscription whose tag does not carry your organization's external ID.
          </Step>
        </Steps>
      </Tab>
      <Tab title="Google Cloud">
        In order for Cloud Capture to reach into your Google Cloud project, to discover your Cloud Run services and jobs and your Google Kubernetes Engine (GKE) clusters, you need to grant permission to Kosli to do so.  This requires a service account in your project that Cloud Capture can impersonate through workload identity federation; the service account, and the workload identity pool that guards it, exist within your own project.

        To simplify this process, Kosli has created a Terraform configuration that creates that service account, the read-only roles Cloud Capture needs, and a workload identity pool that accepts only the Kosli-side role created for your organization.

        If you would rather create these resources yourself, see [Cloud Capture Security](/administration/cloud_capture/security) for the service account, workload identity pool and roles that Cloud Capture needs.

        <Steps>
          <Step title="Download the Terraform configuration">
            Infrastructure Manager reads a configuration from a local directory, so download the published file into an empty directory:

            ```bash
            mkdir kosli-capture && cd kosli-capture
            curl --fail --remote-name \
                https://kosli-cloud-capture-templates.s3.eu-central-1.amazonaws.com/gcp/v0.2.0/main.tf
            ```

            You also need two values from Kosli: the Kosli AWS account ID, and the name of the Kosli-side IAM role for your organization. The configuration isn't pre-filled with them. In your organization's **Settings**, go to **Cloud Capture**, open **Google Cloud** and select **Register account**; the first step of the form shows both.
          </Step>
          <Step title="Deploy with Infrastructure Manager">
            Deploy the configuration once in each project that holds Cloud Run services or jobs, or GKE clusters, you want Cloud Capture to snapshot. Run the following from the directory containing the configuration:

            ```bash
            gcloud infra-manager deployments apply \
                projects/<your-gcp-project>/locations/<your-gcp-region>/deployments/kosli-capture \
                --service-account=projects/<your-gcp-project>/serviceAccounts/<deployer>@<your-gcp-project>.iam.gserviceaccount.com \
                --local-source=. \
                --input-values=project_id=<your-gcp-project>,kosli_aws_account_id=<value from Kosli>,kosli_role_name=<value from Kosli>
            ```

            Infrastructure Manager runs Terraform as the service account you name, so that service account needs permission to enable APIs and to create workload identity pools, service accounts, custom roles and project IAM bindings.
          </Step>
          <Step title="Read the two outputs">
            Kosli needs two values to connect to your project. The configuration emits both as Terraform outputs:

            - `kosli_capture_provider`: the full resource name of the workload identity provider
            - `kosli_capture_service_account`: the email of the service account Cloud Capture impersonates

            You enter both when you register the project. You can read them at any time from the deployment's latest revision:

            ```bash
            gcloud infra-manager revisions describe \
                "$(gcloud infra-manager deployments describe \
                    projects/<your-gcp-project>/locations/<your-gcp-region>/deployments/kosli-capture \
                    --format='value(latestRevision)')" \
                --format='yaml(applyResults.outputs)'
            ```
          </Step>
        </Steps>
      </Tab>
    </Tabs>
  </Step>
  <Step title="Enable Cloud Capture">
    <Tabs>
      <Tab title="AWS">
        When you have created the IAM role, using the CloudFormation template, you can activate Cloud Capture within the Kosli user-interface.

        To check environment names, or to exclude resources, before any snapshots are recorded, switch on [Dry run](#dry-run) and add [skip tags](#excluding-resources) now, before you register accounts.

        Kosli is not notified when you create or delete the stack, so you then register each account yourself. Accounts can only be registered while Cloud Capture is enabled. Open your organization's **Settings**, go to **Cloud Capture**, open **AWS**, select **Register account**, and enter the ARN of the role the stack created. Choose the services to scan in the account: ECS and Lambda are selected for a new account, and S3 is not, because it needs the extra steps in [Capturing S3 buckets](#capturing-s3-buckets). If you deploy the template as a StackSet, register every account in the OU, including accounts that join it later. If you delete a stack, also remove its account from the **Registered accounts** table; until you do, scans of that account fail because the role no longer exists.

        Cloud Capture scans every five minutes unless you [choose another frequency](#scan-frequency), and picks up a registered account the next time it runs - you should see environments and snapshots appearing within a few minutes.
      </Tab>
      <Tab title="Azure">
        Accounts can only be registered while Cloud Capture is enabled. When you have consented to the application, granted it access and tagged the subscription, enter the **Tenant ID** and **Subscription ID** in the same registration form and save it. Register each subscription you want scanned.

        Azure has no regions to choose: Cloud Capture scans the whole subscription and reports each resource group that holds running container-based web apps into its own environment.

        Cloud Capture scans every five minutes unless you [choose another frequency](#scan-frequency), and picks up a registered subscription the next time it runs - you should see environments and snapshots appearing within a few minutes.
      </Tab>
      <Tab title="Google Cloud">
        Accounts can only be registered while Cloud Capture is enabled. When you have deployed the configuration, continue the registration form: enter the project ID, the workload identity provider name and the service account email, and choose the regions and services to scan. Cloud Run is selected for a new project. GKE is not selected, so select it if you want clusters snapshotted.

        Cloud Capture never connects to a GKE cluster. It lists the project's clusters and reads their pods from Google's Cloud Asset Inventory, so a private cluster is snapshotted like any other and nothing is installed in it. Cloud Asset Inventory can be a few minutes behind a cluster, so a pod that lives for less time than that may never be seen.

        Cloud Capture scans every five minutes unless you [choose another frequency](#scan-frequency), and picks up a registered project the next time it runs - you should see environments and snapshots appearing within a few minutes.
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Excluding resources

<Tabs>
<Tab title="AWS">

If there are resources you do not want Cloud Capture to snapshot, such as a test cluster or a service a vendor runs in your account, exclude them by tag. You choose the tags: in your organization's **Settings**, go to **Cloud Capture**, open **AWS** and edit the AWS defaults. The **Skip tags** panel there takes any number of key and value pairs, and Cloud Capture skips every resource that carries one of them.

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
- The tag is read on the resource Cloud Capture snapshots. An ECS cluster is skipped with everything in it, its services and tasks included; tags on a service or a task definition are not read. A Lambda function is skipped on its own, and the region's Lambda environment in Kosli is made up of the functions that remain. An S3 bucket is only ever snapshotted when it carries an [S3 opt-in tag](#capturing-s3-buckets); a bucket that carries an opt-in tag and a skip tag is skipped.
- The change takes effect on the next scan. A Kosli environment that was already being captured keeps its last snapshot and receives no new ones; nothing is deleted. Remove the skip tag from the resource, and the next run picks it up again.
- Skip tags, like the other Cloud Capture settings, can only be changed while Cloud Capture is enabled.
- The IAM role created by the CloudFormation template already grants the permissions needed to read tags, `ecs:DescribeClusters` and `lambda:ListTags`, so no change to the role is needed.

Skip tags can also be set through the API, as part of the organization's Cloud Capture settings. The settings PUT replaces every setting, not only the one you are changing, so start from what is stored: read the current configuration, take the `enabled`, `default_regions`, `scan_interval_minutes`, `skip_tags`, `opt_in_tags`, `dry_run` and `environment_name_template` values from its `settings` object, add your tags to `skip_tags`, and send those fields back. A field you leave out is reset: `dry_run` to `false`, `environment_name_template` to the [default template](#environment-names), and `skip_tags` and `opt_in_tags` to none, which stops your S3 buckets being captured. The response leaves out `environment_name_template` while your organization uses the default, so leave it out of the PUT in that case too. Sending the example below as it stands would also set your default regions, scan interval, S3 opt-in tags and dry run to the values shown, and your environment names to the default.

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
    "opt_in_tags": {"aws": [{"key": "kosli-capture-s3", "value": "true"}]},
    "dry_run": false
  }'
```
</Tab>
<Tab title="Azure">

Exclude resources by tagging the resource group that holds them. In your organization's **Settings**, go to **Cloud Capture**, open **Azure** and add the tag to the **Skip tags** panel in the Azure defaults. Cloud Capture skips every resource group that carries one of the tags, with all of the web apps in it; tags on an individual web app are not read.

Key and value must both match the resource group's tag exactly. Through the API, the tags are the `azure` list of `skip_tags`.
</Tab>
<Tab title="Google Cloud">

Exclude resources by label. In your organization's **Settings**, go to **Cloud Capture**, open **Google Cloud** and add the label to the **Skip tags** panel in the Google Cloud defaults. Key and value must both match the resource's label exactly.

- A Cloud Run service or job is skipped on its own, and the region's Cloud Run environment in Kosli is made up of the services and jobs that remain.
- A GKE cluster is skipped with everything in it. The label is read on the cluster; labels on workloads inside it are not read.

Through the API, the labels are the `gcp` list of `skip_tags`.
</Tab>
</Tabs>

## Capturing S3 buckets

Cloud Capture reports the content of an S3 bucket as one artifact, whose fingerprint is calculated from the SHA256 checksums S3 stores for the bucket's objects. No object is downloaded, with one exception: a `.kosli_ignore` file at the root of the bucket, if there is one, which lists keys to leave out.

S3 is opt-in, bucket by bucket. An account usually holds many buckets you would not want reported, such as CloudTrail and load balancer access logs, and a snapshot makes one request to AWS for every object in the bucket on every scan, which AWS bills to your account. So a bucket is snapshotted only when all of the following are true.

<Steps>
  <Step title="Name the buckets in the CloudFormation stack">
    Deploy version `v0.2.0` or later of the CloudFormation template, or update your existing stack to it, and list the buckets in its **S3 buckets** parameter (`S3BucketNames`): a comma-separated list of bucket names in lowercase, with no spaces. A name may use `*` and `?` as wildcards, for example `acme-releases-*`.

    This is the permission. The role can list and read objects in the buckets you name and in no others. See [Cloud Capture Security](/administration/cloud_capture/security) for exactly what it grants.
  </Step>
  <Step title="Choose an S3 opt-in tag">
    In your organization's **Settings**, go to **Cloud Capture**, open **AWS** and edit the AWS defaults. In the **S3 opt-in tags** panel, beneath **Skip tags**, add a key and a value, for example `kosli-capture-s3` and `true`, and save.

    Until you set an opt-in tag, no bucket is captured.
  </Step>
  <Step title="Tag each bucket you want captured">
    ```bash
    aws s3api put-bucket-tagging \
      --bucket acme-releases \
      --tagging 'TagSet=[{Key=kosli-capture-s3,Value=true}]'
    ```

    `put-bucket-tagging` replaces all of a bucket's tags, so include the tags the bucket already carries. Key and value must both match the opt-in tag exactly; tags are case-sensitive.
  </Step>
  <Step title="Select S3 on the account">
    In the **Registered accounts** table, edit the account and select **s3** among its services.
  </Step>
</Steps>

What to expect:

- **Each bucket is its own environment**, of type S3, named by your [environment name template](#environment-names) with the bucket name as `{resource}`.
- **Each bucket reports exactly one artifact, named after the bucket.** A bucket holding several objects is fingerprinted as a directory, and a bucket holding a single object is fingerprinted as that file. Either way the artifact carries the bucket's name, not the object's.
- **An empty bucket is captured, not failed.** It reports one artifact, named after the bucket, with the fingerprint of an empty directory: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Every empty bucket therefore shares that fingerprint.
- **A bucket needs both the tag and the permission.** A bucket that carries the opt-in tag but is not named in the stack fails its snapshot on every scan, with an access denied error. A bucket that is named in the stack but not tagged is left alone.
- **Skipping wins.** A bucket that carries an opt-in tag and a [skip tag](#excluding-resources) is not captured.
- **Only objects with a SHA256 checksum are fingerprinted.** S3 stores a full-object SHA256 checksum only when the upload asks for one, for example with `aws s3api put-object --checksum-algorithm SHA256`. An object without one, or one uploaded in several parts, is left out of the fingerprint, as if the bucket did not hold it. The fingerprint therefore matches an artifact you attested from the bucket's whole content only once every object carries the checksum, and a bucket where no object does is reported as an empty bucket.
- **Buckets encrypted with a KMS key are not supported.** The role is granted no KMS permission, so a bucket whose objects use SSE-KMS fails its snapshot. S3's default encryption, SSE-S3, needs nothing more.
- **Large buckets cost more and can time out.** A snapshot is one request per object, on every scan. At the default five minute frequency, a bucket of 100,000 objects is about 29 million requests a day. A bucket of more than roughly 100,000 objects may not finish in the time a snapshot is given, and then fails. Consider a longer [scan frequency](#scan-frequency) if you capture large buckets; it applies to everything Cloud Capture scans for you.
- **A newly tagged bucket is picked up on a later scan**, once AWS reports the tag. Removing the tag, or the opt-in tag from your settings, stops new snapshots; the environment keeps its last snapshot and nothing is deleted.

Through the API, the tags are `opt_in_tags` on the same settings resource as the [skip tags](#excluding-resources), with the same shape. The settings PUT replaces every setting, so a PUT that leaves `opt_in_tags` out removes them, and your buckets stop being captured.

## Scan frequency

Cloud Capture scans your registered accounts every five minutes unless you choose otherwise. The frequency is a setting of your Kosli organization, so it applies to every account and region Cloud Capture scans for you.

To change it, open your organization's **Settings**, go to **Cloud Capture**, and under **Scan frequency** pick an interval from the list: every 5, 10, 15 or 30 minutes, or every 1, 2, 6, 12 or 24 hours. Select **Save**, and the next scan runs at the new interval; nothing restarts and no snapshots are lost. Like the other Cloud Capture settings, the frequency can only be changed while Cloud Capture is enabled.

Each scan reports what is running in every environment Cloud Capture manages for you, and Kosli records a new snapshot when that differs from the last one. The interval is therefore how long a change can go unnoticed: a deployment that lands and is rolled back inside one interval may never be seen. Five minutes suits most teams; an estate that changes rarely can scan hourly.

Through the API, the frequency is `scan_interval_minutes` on the same settings resource as the skip tags above: any whole number of minutes from 5 to 1440 (a day), not only the presets the settings page offers, with 5 the value when it is left out. An interval set this way that is not one of the presets is shown on the settings page as its own option, so saving another setting there keeps it. The PUT replaces every setting, so read the current configuration first and send the other settings back unchanged.

## Environment names

Cloud Capture names each environment it reports into from a template. The default template is `{account_id}-{region}-{service}-{resource}`, so an ECS cluster named `app` in account `123456789012` and region `eu-central-1` reports into `123456789012-eu-central-1-ecs-app`. If a name matches an environment that already exists in your organization, Cloud Capture reports into that environment. This lets you name environments so you can tell accounts apart, or send snapshots into environments you already have.

To change the template, open your organization's **Settings**, go to **Cloud Capture**, and under **Environment names** select **Edit**. As you type, the page previews the names the template gives example resources. Select **Save** to store it, or **Use the default** and then **Save** to go back to the default template. Like the other Cloud Capture settings, the template can only be changed while Cloud Capture is enabled. Resources are named with the new template from the next scan.

A template is text with any of these placeholders:

| Placeholder | Value |
|-------------|-------|
| `{cloud}` | The cloud provider: `aws`, `azure` or `gcp`. |
| `{account_id}` | The cloud account ID: an AWS account ID, an Azure subscription ID or a Google Cloud project ID. |
| `{account_name}` | The name you gave the account, for example `staging`. Empty for an account with no name. See [Account names](#account-names). |
| `{account}` | The account's name where it has one, and its account ID where it does not. |
| `{region}` | The region, for example `eu-central-1`. Empty on Azure, which is scanned a subscription at a time. |
| `{service}` | The service: `ecs`, `lambda` or `s3` on AWS, `apps` on Azure, `cloud-run` or `gke` on Google Cloud. |
| `{resource}` | The resource's own name: the ECS cluster, S3 bucket, Azure resource group or GKE cluster. |
| `{tag:Key}` | The value of the resource's tag `Key`. For example, `aws-{tag:Env}` names a cluster tagged `Env=prod` as `aws-prod`. |

How a template is rendered:

- The text between placeholders can only hold letters, digits, `.`, `_` and `-`, and a template must start with a letter, a digit or a placeholder. Placeholder names are case-sensitive and take no formatting.
- A region's Lambda functions are captured together as one resource, and so are a region's Cloud Run services and jobs, so `{resource}` and every `{tag:Key}` are empty for them. An empty placeholder removes the separator before it: with the default template, a region's Lambda functions report into `123456789012-eu-central-1-lambda`.
- `{account_name}` is empty for an account with no name, and that account is still captured. When the empty placeholder starts the template, it removes the separator after it instead, so `{account_name}-{service}-{resource}` names a cluster `app` in an unnamed account `ecs-app`. With `{account}-{resource}`, a cluster named `payments` reports into `staging-payments` in an account named `staging`, and into `222222222222-payments` in account `222222222222` with no name.
- Tag keys are case-sensitive, as AWS stores them, so `{tag:env}` does not read a tag named `Env`. A key may contain colons and spaces, as in `{tag:aws:cloudformation:stack-name}`.
- A resource that does not carry a tag the template names is not captured, and the scan reports it as failed. So is a resource whose rendered name Kosli does not accept, for example because a tag value contains a space. A tag that is present with an empty value renders empty.

<Warning>
Give every resource its own name. A template that renders the same name for two resources sends both into one environment, and that environment then switches between the two resources on every scan. This happens with `aws-prod` on an account with two ECS clusters, with a template that has no `{region}` on an account scanned in two regions, and with a template that has no `{account_id}` or `{account}` when two accounts hold a cluster of the same name. A template that uses `{account_name}` without `{account_id}` sends same-named clusters in every unnamed account into one environment, so use `{account}` unless every account has a name. Account names do not have to be unique, so two accounts with the same name collide in the same way under `{account_name}` and `{account}`. It also happens when a `{tag:Key}` placeholder is the only part that would tell resources apart: tag placeholders are empty for Lambda functions, so `aws-{tag:Env}` sends every region's Lambda functions into `aws`. Run a [dry run](#dry-run) to check the names before you rely on them.
</Warning>

Through the API, the template is `environment_name_template` on the same settings resource as the skip tags above. Leaving it out, or sending `null`, uses the default template. A template that breaks the rules above is refused with a `400` response.

### Account names

You can give each registered account a name, such as `staging` or `prod-us`, to use in environment names through `{account_name}` and `{account}`. Naming accounts is optional, so you can name a few and leave the rest.

To name an account, open your organization's **Settings** and go to **Cloud Capture**. In the **Registered accounts** table, open the actions menu in the account's row, select **Edit**, and enter the name in **Account name**. You can also enter it when you select **Register account**. A name starts with a letter or digit and holds only letters, digits, `.`, `_` and `-`. Clear the field and save to remove the name. A named account's row shows its name, with its account ID beneath it.

Through the API, the name is `account_name` on the account's registration, at `/api/v2/cloud-capture/<your-org>/accounts/aws/<account-id>`. The PUT replaces the whole registration, so read it with a GET first and send its `role_arn`, `regions`, `services` and `dry_run` back with the name. A PUT without `account_name` removes the name.

## Dry run

A dry run shows what Cloud Capture would do without changing anything in your organization. Every scan that is a dry run searches the registered accounts and reports what it found, but records no snapshots and creates no environments.

To turn it on for the whole organization, open **Settings**, go to **Cloud Capture**, and switch on **Dry run**. To dry run a single account, switch on **Dry run** in that account's row of the **Registered accounts** table. While the organization-wide dry run is on, every account is a dry run. Like the other Cloud Capture settings, dry run can only be changed while Cloud Capture is enabled.

After a dry run, open the actions menu in the account's row and select **Show latest results**. The results list what the scan found in each region and service, the environment each resource would report into, which of those environments would be created, and why any resource failed. Switch dry run off to start recording snapshots.

Through the API, the organization-wide switch is `dry_run` on the same settings resource as the skip tags above.
