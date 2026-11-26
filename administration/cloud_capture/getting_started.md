---
title: "Cloud Capture settings"
sidebarTitle: "Settings"
description: "Choose how often Cloud Capture scans, how it names the environments it reports into, and whether it runs as a dry run."
tag: "BETA"
---

<Warning>
Cloud Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

These settings belong to your Kosli organization, so they apply to every cloud account Cloud Capture scans for you. Find them in your organization's **Settings**, under **Cloud Capture**.

To connect a cloud account, and to choose which of its resources are captured, see the page for your cloud: [AWS](/administration/cloud_capture/aws), [Azure](/administration/cloud_capture/azure), or [Google Cloud](/administration/cloud_capture/google_cloud). Skip tags, and the S3 opt-in tags on AWS, are set for each cloud and are described on those pages.

## Scan frequency

Cloud Capture scans your registered accounts every five minutes unless you choose otherwise. The frequency is a setting of your Kosli organization, so it applies to every account and region Cloud Capture scans for you.

To change it, open your organization's **Settings**, go to **Cloud Capture**, and under **Scan frequency** pick an interval from the list: every 5, 10, 15, or 30 minutes, or every 1, 2, 6, 12, or 24 hours. Select **Save**, and the next scan runs at the new interval; nothing restarts and no snapshots are lost. Like the other Cloud Capture settings, the frequency can only be changed while Cloud Capture is enabled.

Each scan reports what is running in every environment Cloud Capture manages for you, and Kosli records a new snapshot when that differs from the last one. The interval is therefore how long a change can go unnoticed: a deployment that lands and is rolled back inside one interval may never be seen. Five minutes suits most teams; an estate that changes rarely can scan hourly.

Through the API, the frequency is `scan_interval_minutes` on the settings resource described in [Using the API](#using-the-api): any whole number of minutes from 5 to 1440 (a day), not only the presets the settings page offers, with 5 the value when it is left out. An interval set this way that is not one of the presets is shown on the settings page as its own option, so saving another setting there keeps it. The PUT replaces every setting, so read the current configuration first and send the other settings back unchanged.

## Environment names

Cloud Capture names each environment it reports into from a template. The default template is `{account_id}-{region}-{service}-{resource}`, so an ECS cluster named `app` in account `123456789012` and region `eu-central-1` reports into `123456789012-eu-central-1-ecs-app`. If a name matches an environment that already exists in your organization, Cloud Capture reports into that environment. This lets you name environments so you can tell accounts apart, or send snapshots into environments you already have.

To change the template, open your organization's **Settings**, go to **Cloud Capture**, and under **Environment names** select **Edit**. As you type, the page previews the names the template gives example resources. Select **Save** to store it, or **Use the default** and then **Save** to go back to the default template. Like the other Cloud Capture settings, the template can only be changed while Cloud Capture is enabled. Resources are named with the new template from the next scan.

A template is text with any of these placeholders:

| Placeholder | Value |
|-------------|-------|
| `{cloud}` | The cloud provider: `aws`, `azure`, or `gcp`. |
| `{account_id}` | The cloud account ID: an AWS account ID, an Azure subscription ID, or a Google Cloud project ID. |
| `{account_name}` | The name you gave the account, for example `staging`. Empty for an account with no name. See [Account names](#account-names). |
| `{account}` | The account's name where it has one, and its account ID where it does not. |
| `{region}` | The region, for example `eu-central-1`. Empty on Azure, which is scanned a subscription at a time. |
| `{service}` | The service: `ecs`, `lambda`, or `s3` on AWS, `apps` on Azure, `cloud-run` or `gke` on Google Cloud. |
| `{resource}` | The resource's own name: the ECS cluster, S3 bucket, Azure resource group, or GKE cluster. |
| `{tag:Key}` | The value of the resource's tag `Key`. For example, `aws-{tag:Env}` names a cluster tagged `Env=prod` as `aws-prod`. |

How a template is rendered:

- The text between placeholders can only hold letters, digits, `.`, `_`, and `-`, and a template must start with a letter, a digit, or a placeholder. Placeholder names are case-sensitive and take no formatting.
- A region's Lambda functions are captured together as one resource, and so are a region's Cloud Run services and jobs, so `{resource}` and every `{tag:Key}` are empty for them. An empty placeholder removes the separator before it: with the default template, a region's Lambda functions report into `123456789012-eu-central-1-lambda`.
- `{account_name}` is empty for an account with no name, and that account is still captured. When the empty placeholder starts the template, it removes the separator after it instead, so `{account_name}-{service}-{resource}` names a cluster `app` in an unnamed account `ecs-app`. With `{account}-{resource}`, a cluster named `payments` reports into `staging-payments` in an account named `staging`, and into `222222222222-payments` in account `222222222222` with no name.
- Tag keys are case-sensitive, as AWS stores them, so `{tag:env}` does not read a tag named `Env`. A key may contain colons and spaces, as in `{tag:aws:cloudformation:stack-name}`.
- A resource that does not carry a tag the template names is not captured, and the scan reports it as failed. So is a resource whose rendered name Kosli does not accept, for example because a tag value contains a space. A tag that is present with an empty value renders empty.

<Warning>
Give every resource its own name. A template that renders the same name for two resources sends both into one environment, and that environment then switches between the two resources on every scan. This happens with `aws-prod` on an account with two ECS clusters, with a template that has no `{region}` on an account scanned in two regions, and with a template that has no `{account_id}` or `{account}` when two accounts hold a cluster of the same name. A template that uses `{account_name}` without `{account_id}` sends same-named clusters in every unnamed account into one environment, so use `{account}` unless every account has a name. Account names do not have to be unique, so two accounts with the same name collide in the same way under `{account_name}` and `{account}`. It also happens when a `{tag:Key}` placeholder is the only part that would tell resources apart: tag placeholders are empty for Lambda functions, so `aws-{tag:Env}` sends every region's Lambda functions into `aws`. Run a [dry run](#dry-run) to check the names before you rely on them.
</Warning>

Through the API, the template is `environment_name_template` on the settings resource described in [Using the API](#using-the-api). Leaving it out, or sending `null`, uses the default template. A template that breaks the rules above is refused with a `400` response.

### Account names

You can give each registered account a name, such as `staging` or `prod-us`, to use in environment names through `{account_name}` and `{account}`. Naming accounts is optional, so you can name a few and leave the rest.

To name an account, open your organization's **Settings** and go to **Cloud Capture**. In the **Registered accounts** table, open the actions menu in the account's row, select **Edit**, and enter the name in **Account name**. You can also enter it when you select **Register account**. A name starts with a letter or digit and holds only letters, digits, `.`, `_`, and `-`. Clear the field and save to remove the name. A named account's row shows its name, with its account ID beneath it.

Through the API, the name is `account_name` on the account's registration, at `/api/v2/cloud-capture/<your-org>/accounts/aws/<account-id>`. The PUT replaces the whole registration, so read it with a GET first and send its `role_arn`, `regions`, `services`, and `dry_run` back with the name. A PUT without `account_name` removes the name.

## Dry run

A dry run shows what Cloud Capture would do without changing anything in your organization. Every scan that is a dry run searches the registered accounts and reports what it found, but records no snapshots and creates no environments.

To turn it on for the whole organization, open **Settings**, go to **Cloud Capture**, and switch on **Dry run**. To dry run a single account, switch on **Dry run** in that account's row of the **Registered accounts** table. While the organization-wide dry run is on, every account is a dry run. Like the other Cloud Capture settings, dry run can only be changed while Cloud Capture is enabled.

After a dry run, open the actions menu in the account's row and select **Show latest results**. The results list what the scan found in each region and service, the environment each resource would report into, which of those environments would be created, and why any resource failed. Switch dry run off to start recording snapshots.

Through the API, the organization-wide switch is `dry_run` on the settings resource described in [Using the API](#using-the-api).

## Using the API

Every setting on this page is a field of one settings resource, along with the skip tags and S3 opt-in tags described on each cloud's page. The settings PUT replaces every setting, not only the one you are changing, so start from what is stored: read the current configuration, take the `enabled`, `default_regions`, `scan_interval_minutes`, `skip_tags`, `opt_in_tags`, `dry_run`, and `environment_name_template` values from its `settings` object, change the ones you want, and send those fields back. A field you leave out is reset: `dry_run` to `false`, `environment_name_template` to the [default template](#environment-names), and `skip_tags` and `opt_in_tags` to none, which stops your S3 buckets being captured. The response leaves out `environment_name_template` while your organization uses the default, so leave it out of the PUT in that case too. Sending the example below as it stands would set your default regions, scan interval, skip tags, S3 opt-in tags, and dry run to the values shown, and your environment names to the default.

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

`skip_tags` holds one list of tags for each cloud: `aws`, `azure`, and `gcp`.
