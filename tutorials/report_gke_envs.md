---
title: "Report GKE environments to Kosli"
description: "Learn how to report running pods across your GKE clusters to Kosli — using Cloud Asset Inventory instead of connecting to any cluster control plane."
---

By the end of this tutorial, you will have reported a snapshot of your GKE pods to Kosli, making the running artifacts across your clusters visible and trackable.

`kosli snapshot gke` reads GKE pods from Google [Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/asset-inventory-overview) instead of the Kubernetes API server. It needs no kubeconfig, no Kubernetes RBAC, and no network path to any cluster control plane — traffic only goes to `cloudasset.googleapis.com`. A single invocation can cover every cluster in a project, folder, or organization.

<Note>
`kosli snapshot gke` is in beta. The reported payload matches [`kosli snapshot k8s`](/client_reference/kosli_snapshot_k8s) (container image digests, creation timestamps, and owners of Running and Failed pods), so both commands report into the same K8S environment type.
</Note>

There are two ways to do this:

- **Kosli CLI** — quick to run, suitable for testing only
- **<Tooltip tip="A Cloud Run Job that runs the Kosli CLI image on a Cloud Scheduler cron, reading GKE pods from Cloud Asset Inventory and reporting them to Kosli automatically.">Scheduled Cloud Run Job</Tooltip>** — runs the reporter inside GCP on a schedule for continuous, production-grade reporting

Follow the section that matches your needs.

## Prerequisites

* Have access to a Google Cloud project (or folder / organization) with one or more GKE clusters.
* Enable the Cloud Asset API on the project that owns the credentials you will use:

  ```shell
  gcloud services enable cloudasset.googleapis.com --project=<your-gcp-project>
  ```

* [Create a Kubernetes Kosli environment](/getting_started/environments#create-an-environment) named `gke-tutorial`.
* [Get a Kosli API token](/getting_started/authenticating_to_kosli).

<Note>
Cloud Asset Inventory is eventually consistent, so a snapshot can lag behind very recent pod changes.
</Note>

## Report using Kosli CLI

This approach is suitable for testing only.

[Install Kosli CLI](/getting_started/install) if you have not done so, then authenticate to GCP with Application Default Credentials:

```shell
gcloud auth application-default login
```

Run the snapshot command:

```shell
kosli snapshot gke gke-tutorial \
    --project <your-gcp-project> \
    --api-token <your-api-token-here> \
    --org <your-kosli-org-name>
```

This reports the pods of every GKE cluster in the project. Use `--folder` or `--organization` instead of `--project` to widen the scope, and combine `--clusters` / `--clusters-regex` and `--locations` to narrow it. Namespace filtering uses the same `--namespaces` / `--namespaces-regex` / `--exclude-namespaces` / `--exclude-namespaces-regex` flags as `kosli snapshot k8s`.

<Warning>
One invocation reports every matching pod to a single Kosli environment and does not record which cluster each pod runs in. Pods that share a namespace and name across clusters (for example `StatefulSet` pods such as `web-0`) cannot be told apart afterwards. To keep clusters apart, snapshot each one with `--clusters` to its own environment.
</Warning>

Run `kosli snapshot gke --help` for the full flag reference.

## Report using a scheduled Cloud Run Job

For production, run the reporter inside GCP as a Cloud Run Job triggered by Cloud Scheduler.

<Steps>
<Step title="Create a service account for the reporter">

```shell
gcloud iam service-accounts create kosli-gke-reporter \
    --display-name="Kosli GKE reporter" \
    --project=<your-gcp-project>
```

</Step>

<Step title="Grant the reporter Cloud Asset Inventory access">

Create a custom role with the minimum permissions the reporter needs, and grant it on the scope you want to snapshot (project, folder, or organization):

```shell
gcloud iam roles create kosliGkeReporter \
    --project=<your-gcp-project> \
    --title="Kosli GKE reporter" \
    --permissions=cloudasset.assets.listContainerPod,serviceusage.services.use

gcloud projects add-iam-policy-binding <your-gcp-project> \
    --member="serviceAccount:kosli-gke-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="projects/<your-gcp-project>/roles/kosliGkeReporter"
```

For a folder- or organization-wide snapshot, bind the same role at that level with `gcloud resource-manager folders add-iam-policy-binding` or `gcloud organizations add-iam-policy-binding`.

<Note>
`roles/cloudasset.viewer` also works, but it grants `listResource` for every asset type, including `k8s.io/Secret`. The custom role above restricts the reporter to listing GKE pods.
</Note>

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
    --member="serviceAccount:kosli-gke-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor" \
    --project=<your-gcp-project>
```

</Step>

<Step title="Deploy the reporter as a Cloud Run Job">

```shell
gcloud run jobs deploy kosli-gke-reporter \
    --image=ghcr.io/kosli-dev/cli:latest \
    --region=<your-gcp-region> \
    --project=<your-gcp-project> \
    --service-account=kosli-gke-reporter@<your-gcp-project>.iam.gserviceaccount.com \
    --set-env-vars=KOSLI_ORG=<your-kosli-org-name>,KOSLI_HOST=https://app.kosli.com \
    --set-secrets=KOSLI_API_TOKEN=kosli-api-token:latest \
    --args=snapshot,gke,gke-tutorial,--project,<your-gcp-project>
```

<Tip>
Pin the CLI image to a specific version (for example `ghcr.io/kosli-dev/cli:v2.18.0`) so the reporter behavior does not change unexpectedly when a new release is published.
</Tip>

<Note>
Cloud Run Jobs are created with `deletionProtection=true` by default. You will need to disable it (`gcloud run jobs update kosli-gke-reporter --no-deletion-protection --region=<your-gcp-region>`) before you can delete or replace the Job later.
</Note>

</Step>

<Step title="Schedule the reporter with Cloud Scheduler">

Create a Cloud Scheduler job that triggers the Cloud Run Job every five minutes, and grant its service account permission to invoke the Job:

```shell
gcloud scheduler jobs create http kosli-gke-reporter-schedule \
    --location=<your-gcp-region> \
    --schedule="*/5 * * * *" \
    --uri="https://run.googleapis.com/v2/projects/<your-gcp-project>/locations/<your-gcp-region>/jobs/kosli-gke-reporter:run" \
    --http-method=POST \
    --oauth-service-account-email=kosli-gke-reporter@<your-gcp-project>.iam.gserviceaccount.com \
    --project=<your-gcp-project>

gcloud run jobs add-iam-policy-binding kosli-gke-reporter \
    --region=<your-gcp-region> \
    --member="serviceAccount:kosli-gke-reporter@<your-gcp-project>.iam.gserviceaccount.com" \
    --role="roles/run.invoker" \
    --project=<your-gcp-project>
```

</Step>

<Step title="Verify the reporter">

In the GCP console, open **Cloud Run** -> **Jobs** -> **kosli-gke-reporter** and check the execution logs for a recent successful run. Then confirm that a fresh snapshot has appeared for the `gke-tutorial` environment in the Kosli UI.

</Step>
</Steps>

## What you've accomplished

You have reported a snapshot of your GKE pods to Kosli, without opening any cluster control plane to the reporter. Kosli now tracks the running artifacts in that environment and will record changes as they happen.

From here you can:
* Query your environment with [`kosli list snapshots`](/client_reference/kosli_list_snapshots) and [`kosli get snapshot`](/client_reference/kosli_get_snapshot)
* [Compare snapshots to see what changed](/client_reference/kosli_diff_snapshots)
* Trace a running artifact back to its git commit with the [From commit to production](/tutorials/following_a_git_commit_to_runtime_environments) tutorial
