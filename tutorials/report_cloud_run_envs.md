---
title: "Report Cloud Run environments to Kosli"
description: "Learn how to report running artifacts from a Google Cloud Run project and region to Kosli — using the CLI for a quick test or a scheduled Cloud Run Job for production."
---

By the end of this tutorial, you will have reported a snapshot of your Cloud Run environment to Kosli, making its running services and jobs visible and trackable.

`kosli snapshot cloud-run` covers a specific set of GCP deploy methods. See the [`kosli snapshot cloud-run`](/client_reference/kosli_snapshot_cloud-run) reference for the current list of what's supported.

There are two ways to do this:

- **Kosli CLI** — quick to run, suitable for testing only
- **<Tooltip tip="A Cloud Run Job that runs the Kosli CLI image on a Cloud Scheduler cron, reporting the project's Cloud Run services and jobs to Kosli automatically.">Scheduled Cloud Run Job</Tooltip>** — runs the reporter inside GCP on a schedule for continuous, production-grade reporting

Follow the section that matches your needs.

## Prerequisites

* Have access to a Google Cloud project and region with Cloud Run resources.
* [Create a Cloud Run Kosli environment](/getting_started/environments#create-an-environment) named `cloud-run-tutorial`.
* [Get a Kosli API token](/getting_started/service-accounts).

## Report using Kosli CLI

This approach is suitable for testing only.

[Install Kosli CLI](/getting_started/install) if you have not done so, then authenticate to GCP with Application Default Credentials:

```shell
gcloud auth application-default login
```

Run the snapshot command:

```shell
kosli snapshot cloud-run cloud-run-tutorial \
    --project <your-gcp-project> \
    --region <your-gcp-region> \
    --resolve-names \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

`--resolve-names` makes Cloud Run services display their image tags (for example the commit SHA) instead of bare digests by reverse-resolving the deployed digest against Artifact Registry. The forward digest lookup for tag-pinned Jobs runs automatically whether you pass the flag or not.

See [`kosli snapshot cloud-run`](/client_reference/kosli_snapshot_cloud-run) for the full flag reference.

## Report using a scheduled Cloud Run Job

For production, run the reporter inside GCP as a Cloud Run Job triggered by Cloud Scheduler.

<Steps>
<Step title="Create a service account for the reporter">

```shell
gcloud iam service-accounts create kosli-reporter \
    --display-name="Kosli reporter" \
    --project=<your-gcp-project>
```

</Step>

<Step title="Grant the reporter project-level access to Cloud Run">

`roles/run.viewer` is the minimum needed to list services and jobs in the project.

```shell
gcloud projects add-iam-policy-binding <your-gcp-project> \
    --member="serviceAccount:kosli-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="roles/run.viewer"
```

</Step>

<Step title="Store the Kosli API token in Secret Manager">

Create a secret and add your token as the first version:

```shell
gcloud secrets create kosli-api-token \
    --replication-policy=automatic \
    --project=<your-gcp-project>

printf "<your-api-token-here>" | gcloud secrets versions add kosli-api-token \
    --data-file=- \
    --project=<your-gcp-project>
```

Grant the reporter service account read access to that specific secret:

```shell
gcloud secrets add-iam-policy-binding kosli-api-token \
    --member="serviceAccount:kosli-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" \
    --project=<your-gcp-project>
```

</Step>

<Step title="Grant Artifact Registry read access">

Grant `roles/artifactregistry.reader` to the reporter on each Artifact Registry repository that holds your application images. This is what lets the reporter resolve digests and tags so artifact names are useful on Kosli.

```shell
gcloud artifacts repositories add-iam-policy-binding <your-repo> \
    --location=<your-gcp-region> \
    --member="serviceAccount:kosli-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="roles/artifactregistry.reader" \
    --project=<your-gcp-project>
```

Repeat the command for every Artifact Registry repository that holds images deployed to Cloud Run in this project.

<Note>
If you deploy any Cloud Functions 2nd-gen functions in this project, also grant the same role on the Google-managed `gcf-artifacts` repository in the same region. 2nd-gen functions store their backing images there, and the reporter needs read access to resolve them.
</Note>

</Step>

<Step title="Deploy the reporter as a Cloud Run Job">

```shell
gcloud run jobs deploy kosli-reporter \
    --image=ghcr.io/kosli-dev/cli:latest \
    --region=<your-gcp-region> \
    --project=<your-gcp-project> \
    --service-account=kosli-reporter@<your-gcp-project>.iam.gserviceaccount.com \
    --set-env-vars=KOSLI_ORG=<your-kosli-org-name>,KOSLI_HOST=https://app.kosli.com \
    --set-secrets=KOSLI_API_TOKEN=kosli-api-token:latest \
    --args=snapshot,cloud-run,cloud-run-tutorial,--project,<your-gcp-project>,--region,<your-gcp-region>,--resolve-names
```

<Tip>
Pin the CLI image to a specific version (for example `ghcr.io/kosli-dev/cli:v2.18.0`) so the reporter behavior does not change unexpectedly when a new release is published.
</Tip>

<Note>
Cloud Run Jobs are created with `deletionProtection=true` by default. You will need to disable it (`gcloud run jobs update kosli-reporter --no-deletion-protection --region=<your-gcp-region>`) before you can delete or replace the Job later.
</Note>

</Step>

<Step title="Schedule the reporter with Cloud Scheduler">

Create a Cloud Scheduler job that triggers the Cloud Run Job every five minutes, and grant its service account permission to invoke the Job:

```shell
gcloud scheduler jobs create http kosli-reporter-schedule \
    --location=<your-gcp-region> \
    --schedule="*/5 * * * *" \
    --uri="https://run.googleapis.com/v2/projects/<your-gcp-project>/locations/<your-gcp-region>/jobs/kosli-reporter:run" \
    --http-method=POST \
    --oauth-service-account-email=kosli-reporter@<your-gcp-project>.iam.gserviceaccount.com \
    --project=<your-gcp-project>

gcloud run jobs add-iam-policy-binding kosli-reporter \
    --region=<your-gcp-region> \
    --member="serviceAccount:kosli-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="roles/run.invoker" \
    --project=<your-gcp-project>
```

</Step>

<Step title="Verify the reporter">

In the GCP console, open **Cloud Run** -> **Jobs** -> **kosli-reporter** and check the execution logs for a recent successful run. Then confirm that a fresh snapshot has appeared for the `cloud-run-tutorial` environment in the Kosli UI.

</Step>
</Steps>

## What you've accomplished

You have reported a snapshot of your Cloud Run environment to Kosli. Kosli now tracks the running services and jobs in that environment and will record changes as they happen.

From here you can:
* Query your environment with [`kosli list snapshots`](/client_reference/kosli_list_snapshots) and [`kosli get snapshot`](/client_reference/kosli_get_snapshot)
* [Compare snapshots to see what changed](/client_reference/kosli_diff_snapshots)
* Trace a running artifact back to its git commit with the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
