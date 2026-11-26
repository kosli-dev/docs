---
title: "Cloud Capture on Google Cloud"
sidebarTitle: "Google Cloud"
description: "Set up Cloud Capture for your Google Cloud projects, choose which Cloud Run and GKE resources it snapshots, and review the permissions it uses."
tag: "BETA"
---

<Warning>
Cloud Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Cloud Capture snapshots the Cloud Run services and jobs, and the Google Kubernetes Engine (GKE) clusters, in the projects you register. Google Cloud support is in early access, so the Google Cloud page appears in your Cloud Capture settings only once Kosli has enabled it for your organization.

## Set up

In order for Cloud Capture to reach into your Google Cloud project, to discover your Cloud Run services and jobs and your Google Kubernetes Engine (GKE) clusters, you need to grant permission to Kosli to do so.  This requires a service account in your project that Cloud Capture can impersonate through workload identity federation; the service account, and the workload identity pool that guards it, exist within your own project.

To simplify this process, Kosli has created a Terraform configuration that creates that service account, the read-only roles Cloud Capture needs, and a workload identity pool that accepts only the Kosli-side role created for your organization.

If you would rather create these resources yourself, see [Permissions and security](#permissions-and-security) for the service account, workload identity pool and roles that Cloud Capture needs.

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
  <Step title="Register the project">
    Accounts can only be registered while Cloud Capture is enabled. When you have deployed the configuration, continue the registration form: enter the project ID, the workload identity provider name and the service account email, and choose the regions and services to scan. Cloud Run is selected for a new project. GKE is not selected, so select it if you want clusters snapshotted.

    Cloud Capture never connects to a GKE cluster. It lists the project's clusters and reads their pods from Google's Cloud Asset Inventory, so a private cluster is snapshotted like any other and nothing is installed in it. Cloud Asset Inventory can be a few minutes behind a cluster, so a pod that lives for less time than that may never be seen.

    Cloud Capture scans every five minutes unless you [choose another frequency](/administration/cloud_capture/getting_started#scan-frequency), and picks up a registered project the next time it runs - you should see environments and snapshots appearing within a few minutes.
  </Step>
</Steps>

## Excluding resources

Exclude resources by label. In your organization's **Settings**, go to **Cloud Capture**, open **Google Cloud** and add the label to the **Skip tags** panel in the Google Cloud defaults. Key and value must both match the resource's label exactly.

- A Cloud Run service or job is skipped on its own, and the region's Cloud Run environment in Kosli is made up of the services and jobs that remain.
- A GKE cluster is skipped with everything in it. The label is read on the cluster; labels on workloads inside it are not read.

Through the API, the labels are the `gcp` list of `skip_tags`; see [Using the API](/administration/cloud_capture/getting_started#using-the-api).

## Permissions and security

For the model that is common to every cloud, see [Cloud Capture security](/administration/cloud_capture/security).

Kosli publishes a Terraform configuration, for use with
[Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs), that creates
everything Cloud Capture needs to snapshot Cloud Run and Google Kubernetes Engine (GKE).
Infrastructure Manager runs Terraform as a managed service inside your project, so there is no
state file or Terraform install for you to manage. Deploy the configuration once in each project
you want Cloud Capture to snapshot. The [current version](https://kosli-cloud-capture-templates.s3.eu-central-1.amazonaws.com/gcp/v0.2.0/main.tf),
`v0.2.0`, is published at
`https://kosli-cloud-capture-templates.s3.eu-central-1.amazonaws.com/gcp/v0.2.0/main.tf`, and what
this page describes is taken from it. Everything it creates is yours, in your project.

Cloud Capture runs in AWS and reaches your project through
[Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation). Cloud
Capture exchanges its own short-lived AWS credentials for a short-lived Google token, then
impersonates a service account that you create. No service account key is ever created or shared.

Your workload identity pool makes two checks before it issues a token:

1. It accepts only credentials issued by the Kosli AWS account in which Cloud Capture runs.
2. Within that account, it accepts only the Kosli-side IAM role dedicated to your organization.
   Every Cloud Capture job runs under the role for the organization it is working for. A job for
   another Kosli tenant presents a different role name, so your pool refuses it, even if that
   tenant gave Kosli your provider and service account details instead of their own.

The role name is part of the credential that AWS signs and Google verifies, so the caller cannot
forge it.

For readers familiar with the AWS setup: the account check plays the part of the principal in the
assume-role trust policy, and the role check plays the part of the external ID.

### What the configuration creates

| Resource | Name | What it is for |
|---|---|---|
| Workload identity pool | `kosli-capture` | Exchanges Cloud Capture's AWS credentials for a Google token |
| AWS provider in the pool | `kosli-aws` | Accepts the Kosli AWS account and, within it, only the Kosli-side role for your organization |
| Service account | `kosli-capture@<project>.iam.gserviceaccount.com` | The identity Cloud Capture acts as in the project. Only the Kosli-side role for your organization may impersonate it |
| Enabled APIs | IAM, IAM Credentials, Security Token Service, Cloud Run, Cloud Resource Manager, Cloud Asset | Needed to create the resources above and to make the read calls below. None is disabled if you destroy the deployment |

The configuration takes three inputs, none of which has a default: `project_id`, and the two values
Kosli supplies, `kosli_aws_account_id` and `kosli_role_name`. It emits two outputs,
`kosli_capture_provider` and `kosli_capture_service_account`, which you enter when you register the
project; see [Set up](#set-up).

### Permissions granted to the service account

All of the grants are read-only, and all are on the project.

| Grant | Permissions | What Cloud Capture uses it for |
|---|---|---|
| `roles/run.viewer` | Google's predefined Cloud Run viewer role | Listing a region's Cloud Run services and jobs with their labels, and reading each service's revisions and images |
| Custom role `kosliCaptureRegistry` | `artifactregistry.tags.get` | Resolving an image referenced by tag to its digest. This is a metadata read; no image layer is ever pulled |
| Custom role `kosliCaptureGke` | `container.clusters.list`, `cloudasset.assets.listContainerPod`, `serviceusage.services.use` | Listing the project's GKE clusters with their labels, and reading the project's pods from [Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview), in the same way as [`kosli snapshot gke`](/client_reference/kosli_snapshot_gke). Google requires `serviceusage.services.use` of every Cloud Asset Inventory call |

Worth knowing for a security review of GKE:

- Cloud Capture never calls a cluster's Kubernetes API. No Kubernetes RBAC objects are created
  inside your clusters, nothing is installed in them, and Cloud Capture needs no network access to
  any cluster control plane, so a private cluster is snapshotted like any other.
- The GKE role is custom because Google's predefined roles are wider: `roles/cloudasset.viewer`
  would list every asset type in the project, including Kubernetes Secrets.
- The role cannot be made narrower than every pod in the project, because Cloud Asset Inventory
  filters by neither cluster nor namespace. A pod's record holds its images, commands, arguments,
  labels, annotations, and any environment variables written into the spec in plain text. A value
  taken from a Kubernetes Secret appears as a reference and not as the secret.
- A project inside a VPC Service Controls perimeter that restricts the Cloud Asset, Kubernetes
  Engine or Cloud Run API needs an ingress rule that admits the service account, because Cloud
  Capture calls from outside the perimeter.

If you wish to grant access for Cloud Capture without using our published configuration, create
the resources and grants in the two tables above. The pool must accept only the Kosli AWS account
and, within it, only the Kosli-side role for your organization, and only that role may impersonate
the service account.

### The configuration in full

<Accordion title="main.tf, version v0.2.0">

```hcl
# The Google Cloud resources Kosli Cloud Capture needs in a customer's
# project, for use with Infrastructure Manager; the README beside this
# directory says how to deploy it and why it is shaped as it is.
#
# Cloud Capture runs in AWS and reaches the project through Workload Identity
# Federation: it exchanges its own short-lived AWS credentials for a
# short-lived Google token, then impersonates the service account created
# here. No service account key is ever created, stored or shared. The pool
# makes two checks before it issues a token: the credentials were issued by
# the Kosli AWS account that serves the customer, and within that account by
# the one IAM role Kosli keeps for the customer's organisation. A Cloud
# Capture job for another tenant runs under a different role and is refused.

terraform {
  required_version = ">= 1.5"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 5.0, < 8.0"
    }
  }
}

provider "google" {
  project = var.project_id
}

variable "project_id" {
  type        = string
  description = "The GCP project that holds the Cloud Run services and jobs, and the GKE clusters, Cloud Capture will snapshot."

  validation {
    condition     = can(regex("^[a-z][a-z0-9-]{4,28}[a-z0-9]$", var.project_id))
    error_message = "Must be a project id: 6 to 30 lowercase letters, digits and hyphens, starting with a letter."
  }
}

variable "kosli_aws_account_id" {
  type        = string
  description = <<-EOT
    The AWS account in which Cloud Capture runs, supplied by Kosli. It differs
    per tenant because more than one Kosli account serves tenants. There
    is no default and no value you can derive yourself.
  EOT

  validation {
    condition     = can(regex("^[0-9]{12}$", var.kosli_aws_account_id))
    error_message = "Must be the 12-digit AWS account id issued to you by Kosli."
  }
}

variable "kosli_role_name" {
  type        = string
  description = <<-EOT
    The name of the IAM role, in the Kosli AWS account, that Cloud Capture
    uses when working for your organisation. Supplied by Kosli. Each Kosli
    organisation has its own role, and the workload identity pool accepts
    only this one, so only Cloud Capture jobs run on behalf of your
    organisation can obtain a token from your project. In the AWS setup,
    the external ID plays the same part.
  EOT

  validation {
    condition     = can(regex("^[A-Za-z0-9+=,.@_-]{1,64}$", var.kosli_role_name))
    error_message = "Must be the IAM role name issued to you by Kosli."
  }
}

# The APIs the exchange and the inventory go through. Cloud Run is enabled
# already in a project with services in it; the IAM ones are what creating a
# pool, a service account and the custom roles, and impersonating the account,
# need; Cloud Resource Manager is what granting the project roles below
# needs, and a fresh project does not have it on; Cloud Asset is the
# inventory a GKE snapshot reads the project's pods from, and costs nothing
# to have on. None is disabled on destroy: they may well be in use by
# something else in the project.
#
# The Kubernetes Engine API is not in the list. A project with clusters has
# it on already, and enabling it in a project without them would switch on
# Compute Engine and its other dependencies for nothing.
resource "google_project_service" "needed" {
  for_each = toset([
    "iam.googleapis.com",
    "iamcredentials.googleapis.com",
    "sts.googleapis.com",
    "run.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "cloudasset.googleapis.com",
  ])

  project            = var.project_id
  service            = each.key
  disable_on_destroy = false
}

resource "google_iam_workload_identity_pool" "kosli_capture" {
  project                   = var.project_id
  workload_identity_pool_id = "kosli-capture"
  display_name              = "Cloud Capture"
  description               = <<-EOT
    Read-only access for Cloud Capture SDLC compliance evidence collection.
    Managed by Infrastructure Manager; do not edit in place.
  EOT

  depends_on = [google_project_service.needed]
}

resource "google_iam_workload_identity_pool_provider" "kosli_aws" {
  project                            = var.project_id
  workload_identity_pool_id          = google_iam_workload_identity_pool.kosli_capture.workload_identity_pool_id
  workload_identity_pool_provider_id = "kosli-aws"
  display_name                       = "Cloud Capture (AWS)"

  aws {
    account_id = var.kosli_aws_account_id
  }

  # The role is read out of the assumed-role ARN AWS signed, less its
  # session name, so every session of the role is the one principal. The
  # subject is the role as well, and not the whole ARN: a subject is at most
  # 127 bytes, and the ARN carries the account, the session name and the
  # role's name, which can be 64 characters, so a long role name would put
  # the ARN over the limit and every exchange would fail.
  attribute_mapping = {
    "google.subject"     = "assertion.arn.extract('assumed-role/{role}/')"
    "attribute.account"  = "assertion.account"
    "attribute.aws_role" = "assertion.arn.extract('assumed-role/{role}/')"
  }

  # Two checks before the pool issues a token. The account check accepts only
  # credentials issued by the Kosli AWS account, however the token reaches
  # Google. The role check accepts, within that account, only the Kosli-side
  # role dedicated to your organisation. A Cloud Capture job for another tenant
  # runs under a different role and is refused here. In the AWS setup, these
  # checks correspond to the trust policy principal and the external ID.
  attribute_condition = join(" && ", [
    "attribute.account == \"${var.kosli_aws_account_id}\"",
    "attribute.aws_role == \"${var.kosli_role_name}\"",
  ])
}

resource "google_service_account" "kosli_capture" {
  project      = var.project_id
  account_id   = "kosli-capture"
  display_name = "Cloud Capture"
  description  = "Impersonated by Cloud Capture to snapshot Cloud Run services and jobs, and GKE clusters. Managed by Infrastructure Manager."

  # Ordered after the APIs, as the pool is: creating a service account needs
  # iam.googleapis.com, which a project may not have enabled before this, and
  # the four bindings below follow through their references to the account.
  depends_on = [google_project_service.needed]
}

# Only the Kosli-side role for your organisation may impersonate the service
# account. The pool's attribute condition already refuses every other identity;
# naming the role here as well keeps the binding correct even if that condition
# is later loosened.
resource "google_service_account_iam_member" "kosli_impersonation" {
  service_account_id = google_service_account.kosli_capture.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.kosli_capture.name}/attribute.aws_role/${var.kosli_role_name}"
}

# What the service account may read. Discovery lists the region's Cloud Run
# services and jobs and reads each one's labels from the same listing, and
# the snapshot reads each service's revisions and the images they run: all
# of it is in roles/run.viewer, the predefined read-only role, and none of it
# returns application data. A revision's spec is the widest: it holds the
# container image, the command, and any environment variables written into
# the spec in plain text; a value taken from a Secret is named there rather
# than resolved, so what comes back is the reference and not the secret.
resource "google_project_iam_member" "kosli_capture_run" {
  project = var.project_id
  role    = "roles/run.viewer"
  member  = google_service_account.kosli_capture.member
}

# The snapshot also resolves each image pinned by a tag to its digest, which
# the Kosli CLI (2.57.0 on) reads from the Artifact Registry API: metadata
# about the tag, and never the image. The predefined read-only role would
# also grant downloadArtifacts, which pulls image layers, so a custom role
# grants the one read the lookup makes and nothing that returns a layer.
# The CLI's other lookup, a tag for an image pinned by digest, is behind a
# flag Cloud Capture does not pass, so its permission
# (artifactregistry.dockerimages.get) is not granted either. The CLI falls
# back to reading the manifest when the API call fails; under this grant
# that fallback cannot succeed, and nothing depends on it, since the
# registries it could read are the ones the API lookup reads. Cloud Run
# reports a service's image already pinned by digest, which the CLI takes
# from the name, so what this grant resolves in practice is a job's image.
# Without this grant a snapshot still succeeds, with an empty digest for
# each tag-pinned image the account could not read.
resource "google_project_iam_custom_role" "kosli_capture_registry" {
  project     = var.project_id
  role_id     = "kosliCaptureRegistry"
  title       = "Cloud Capture registry metadata"
  description = "Read-only image tag metadata for Cloud Capture SDLC compliance evidence collection."

  permissions = ["artifactregistry.tags.get"]

  depends_on = [google_project_service.needed]
}

resource "google_project_iam_member" "kosli_capture_registry" {
  project = var.project_id
  role    = google_project_iam_custom_role.kosli_capture_registry.id
  member  = google_service_account.kosli_capture.member
}

# What the service account may read of the project's GKE clusters (beta).
# Cloud Capture never connects to a cluster: it needs no network path to one,
# no kubeconfig and no Kubernetes RBAC. Discovery lists the project's
# clusters, with their labels, through the Kubernetes Engine API; the
# snapshot reads the project's pods from Cloud Asset Inventory, Google's own
# record of what is in the project, and Google requires
# serviceusage.services.use of every call to it.
#
# A custom role because the predefined ones are wider than this:
# roles/cloudasset.viewer lists every asset type in the project, and
# roles/container.clusterViewer more than the one listing. It cannot be
# narrower than every pod in the project, since Cloud Asset Inventory filters
# by neither cluster nor namespace. A pod's record holds its spec and status:
# the images, commands and arguments, its labels and annotations, and any
# environment variables written into the spec in plain text; a value taken
# from a Secret is named there rather than resolved, so what comes back is
# the reference and not the secret. A cluster's listing holds its
# configuration and no credentials.
resource "google_project_iam_custom_role" "kosli_capture_gke" {
  project     = var.project_id
  role_id     = "kosliCaptureGke"
  title       = "Cloud Capture (GKE)"
  description = "Lists GKE clusters, and their pods from Cloud Asset Inventory, for Cloud Capture. Managed by Infrastructure Manager."

  permissions = [
    "container.clusters.list",
    "cloudasset.assets.listContainerPod",
    "serviceusage.services.use",
  ]

  depends_on = [google_project_service.needed]
}

resource "google_project_iam_member" "kosli_capture_gke" {
  project = var.project_id
  role    = google_project_iam_custom_role.kosli_capture_gke.id
  member  = google_service_account.kosli_capture.member
}

# Kosli needs these two values to connect. Infrastructure Manager records them
# on the deployment's latest revision, under applyResults.outputs.
output "kosli_capture_provider" {
  description = "Full resource name of the workload identity provider; give this to Kosli."
  value       = google_iam_workload_identity_pool_provider.kosli_aws.name
}

output "kosli_capture_service_account" {
  description = "Email of the service account Cloud Capture impersonates; give this to Kosli."
  value       = google_service_account.kosli_capture.email
}
```

</Accordion>

### Deploying with Infrastructure Manager

Download the configuration into an empty directory and run the following from it. Infrastructure
Manager runs Terraform as the service account you name, so that service account needs permission to
enable APIs and to create workload identity pools, service accounts, custom roles and project IAM
bindings. The Kosli AWS account ID and role name are shown in the first step of the Google Cloud
registration form in the Kosli UI.

```bash
gcloud infra-manager deployments apply \
    projects/<your-gcp-project>/locations/<your-gcp-region>/deployments/kosli-capture \
    --service-account=projects/<your-gcp-project>/serviceAccounts/<deployer>@<your-gcp-project>.iam.gserviceaccount.com \
    --local-source=. \
    --input-values=project_id=<your-gcp-project>,kosli_aws_account_id=<value from Kosli>,kosli_role_name=<value from Kosli>
```

### Tenant isolation

Each Cloud Capture job for your organization runs under the Kosli-side IAM role dedicated to your
organization. The workload identity pool in your project accepts only that role, so a job running
for a different tenant cannot obtain a token from your project or impersonate your service account.
Separation is enforced by the identity provider, not by application code.
