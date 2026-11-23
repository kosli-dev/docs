---
title: Cloud Capture - Security
sidebarTitle: Security
description: "Learn about the security of Cloud Capture"
tag: "BETA"
---

<Warning>
Cloud Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

## Cloud Capture permissions

The Cloud Capture managed service uses the public cloud APIs to extract information about your cloud environments.  In order to do this, you need to provide Kosli with an identity in your cloud account that Kosli can use to call these APIs.  The identity is created and managed by you. It must be protected by a trust condition that allows only Kosli to use it, and it must hold the read-only permissions Kosli needs to find and snapshot your resources. On Azure the identity is a Kosli application that you consent to and grant access; on AWS and Google Cloud it is a role or service account you create.

<Tabs>
<Tab title="AWS">
Kosli publishes a CloudFormation template, for use in AWS, showing the permissions needed.  The template is publicly accessible and can be used directly within an `aws cloudformation create-stack` call. The current version, `v0.2.0`, is published at `https://kosli-cloud-capture-templates.s3.eu-central-1.amazonaws.com/aws/v0.2.0/kosli-cloud-capture-access-role.yaml`, and the permissions shown on this page are taken from it. A published version is never changed; a change to the permissions is a new version, and reaches a role you have deployed only when you update your stack.

Version `v0.2.0` adds one optional parameter to the earlier template, **S3 buckets** (`S3BucketNames`), for [capturing S3 buckets](/administration/cloud_capture/getting_started#capturing-s3-buckets). Left empty, the default, the role is the same as the one the earlier template created: it can read no object and no object key in any bucket. A role created from the earlier template keeps working for ECS and Lambda.

If you wish to build an IAM role for Cloud Capture without using our published CloudFormation template, the permissions needed are those shown below. The role must contain an Assume Role policy that allows the Kosli account to access the resources, and must include an externalId. Both of these values are supplied by Kosli and cannot be derived; you cannot construct the trust policy without them. Whichever way you create the role, then register the account with the role's ARN, as described in [Getting started](/administration/cloud_capture/getting_started).

### Assume role

The IAM role defined within the CloudFormation template includes an "assume role" policy granting permission from Kosli.  This appears as:

```yaml
  KosliCloudCaptureAccessRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Ref RoleName
      Description: >-
        Read-only access for Kosli Cloud Capture evidence collection.
        Managed by CloudFormation; do not edit in place.
      MaxSessionDuration: 3600
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Sid: AllowKosliToAssumeWithExternalId
            Effect: Allow
            Principal:
              AWS: !Ref TrustedPrincipalArn
            Action: sts:AssumeRole
            Condition:
              StringEquals:
                sts:ExternalId: !Ref ExternalId
```

### All permissions needed

The IAM role defined within the Cloudformation template includes a number of IAM policy statements, granting read-only access to some AWS APIs.  The statements are:

```yaml
Statement:

  # How Cloud Capture finds what to snapshot. Discovery lists the ECS
  # clusters in the account and reads each cluster's tags from the
  # same DescribeClusters call; a cluster carrying the exclusion
  # tag is skipped and everything else is snapshotted. Without
  # ListClusters and DescribeClusters a role created from this
  # template cannot run discovery at all.
  #
  # Worth knowing for a security review: these are inventory calls
  # and none of them returns application data. DescribeTaskDefinition
  # is the widest - a task definition holds the container image, the
  # command, and any environment variables written into the
  # definition itself in plain text. Values injected from Secrets
  # Manager or Parameter Store are named there rather than resolved,
  # so what comes back is the reference and not the secret.
  - Sid: EcsInventory
    Effect: Allow
    Action:
      - ecs:DescribeCapacityProviders
      - ecs:DescribeClusters
      - ecs:DescribeContainerInstances
      - ecs:DescribeServices
      - ecs:DescribeTaskDefinition
      - ecs:DescribeTasks
      - ecs:ListClusters
      - ecs:ListContainerInstances
      - ecs:ListServices
      - ecs:ListTagsForResource
      - ecs:ListTaskDefinitionFamilies
      - ecs:ListTaskDefinitions
      - ecs:ListTasks
    Resource: "*"

  # Lambda is the next snapshot target after ECS. Granted here so
  # that adding it needs no change to a role you have already
  # reviewed and deployed; read-only, like everything above.
  - Sid: LambdaInventory
    Effect: Allow
    Action:
      - lambda:GetFunctionConfiguration
      - lambda:GetPolicy
      - lambda:ListAliases
      - lambda:ListFunctions
      - lambda:ListTags
      - lambda:ListVersionsByFunction
    Resource: "*"

  # Which buckets exist in a region, and bucket-level metadata,
  # for every bucket; no object key and no object. Cloud Capture
  # lists the buckets of a region to confirm the ones the tagging
  # API named (see S3FindBucketsByTag below) are there.
  - Sid: S3BucketMetadataOnly
    Effect: Allow
    Action:
      - s3:GetBucketLocation
      - s3:GetBucketLogging
      - s3:GetBucketPolicyStatus
      - s3:GetBucketPublicAccessBlock
      - s3:GetBucketTagging
      - s3:GetBucketVersioning
      - s3:GetEncryptionConfiguration
      - s3:ListAllMyBuckets
    Resource: "*"

  # How Cloud Capture finds the buckets to snapshot; not granted
  # when S3BucketNames is empty. A bucket is snapshotted only when
  # it carries one of the S3 opt-in tags you set in Kosli, so
  # Cloud Capture asks the Resource Groups Tagging API for the
  # buckets carrying one, in place of reading the tags of every
  # bucket in the account one by one on every scan.
  #
  # Worth knowing for a security review: AWS cannot scope this
  # permission to S3 or to particular resources. It lets the role
  # read the tag keys and values of every taggable resource in
  # the account, whatever its service. Cloud Capture asks for
  # resources of type s3:bucket carrying your opt-in tags, and
  # for nothing else. Tags are metadata, but if yours hold
  # anything you would not show Kosli, leave S3BucketNames empty.
  - !If
    - SnapshotsS3Buckets
    - Sid: S3FindBucketsByTag
      Effect: Allow
      Action:
        - tag:GetResources
      Resource: "*"
    - !Ref AWS::NoValue

  # What an S3 snapshot reads, in the buckets named in
  # S3BucketNames and no others; neither statement exists when
  # that parameter is empty. A snapshot records the fingerprint of
  # a bucket's content: Cloud Capture lists the object keys, then
  # reads the SHA256 checksum S3 stores for each object with a
  # HeadObject request, which returns the object's metadata and no
  # content.
  #
  # Worth knowing for a security review: AWS has no permission for
  # reading an object's checksum alone. HeadObject is authorised by
  # s3:GetObject, the permission that also authorises downloading
  # the object, so this role is able to read the content of every
  # object in the buckets you name. Cloud Capture downloads one
  # object only, and only if it exists: a `.kosli_ignore` file at
  # the root of the bucket, which lists the keys to leave out of
  # the fingerprint. Name only the buckets you want snapshotted.
  #
  # No KMS permission is granted, so objects encrypted with a KMS
  # key (SSE-KMS) cannot be read and their bucket's snapshot
  # fails. Objects under S3's default encryption (SSE-S3) need
  # nothing more than this.
  #
  # The ARNs are built from the list by joining it: for
  # `a,b` the first is arn:aws:s3:::a and arn:aws:s3:::b, and the
  # second arn:aws:s3:::a/* and arn:aws:s3:::b/*.
  - !If
    - SnapshotsS3Buckets
    - Sid: S3ListObjectKeysInNamedBuckets
      Effect: Allow
      Action:
        - s3:ListBucket
      Resource: !Split
        - ","
        - !Join
          - ""
          - - "arn:aws:s3:::"
            - !Join [",arn:aws:s3:::", !Ref S3BucketNames]
    - !Ref AWS::NoValue

  - !If
    - SnapshotsS3Buckets
    - Sid: S3ReadObjectChecksumsInNamedBuckets
      Effect: Allow
      Action:
        - s3:GetObject
      Resource: !Split
        - ","
        - !Join
          - ""
          - - "arn:aws:s3:::"
            - !Join ["/*,arn:aws:s3:::", !Ref S3BucketNames]
            - "/*"
    - !Ref AWS::NoValue

  # The explicit denies below are redundant given the allow-list
  # above, but they are here so that a security reviewer can
  # verify the boundary without having to reason about IAM
  # defaults, and so that any future widening of this policy cannot
  # accidentally grant data-plane access.
  #
  # s3:GetObject is denied everywhere except in the buckets named
  # in S3BucketNames, and everywhere when none is named.
  - !If
    - SnapshotsS3Buckets
    - Sid: NeverReadObjectDataOutsideNamedBuckets
      Effect: Deny
      Action:
        - s3:GetObject
      NotResource: !Split
        - ","
        - !Join
          - ""
          - - "arn:aws:s3:::"
            - !Join ["/*,arn:aws:s3:::", !Ref S3BucketNames]
            - "/*"
    - Sid: NeverReadObjectData
      Effect: Deny
      Action:
        - s3:GetObject
      Resource: "*"

  # Every other way to read an object, its earlier versions, its
  # ACL or its tags is denied in every bucket, named or not: a
  # snapshot needs none of them.
  - Sid: NeverReadObjectVersionsAclsOrTags
    Effect: Deny
    Action:
      - s3:GetObjectAcl
      - s3:GetObjectAttributes
      - s3:GetObjectTagging
      - s3:GetObjectTorrent
      - s3:GetObjectVersion
      - s3:GetObjectVersionAcl
      - s3:GetObjectVersionAttributes
      - s3:GetObjectVersionTagging
      - s3:ListMultipartUploadParts
    Resource: "*"

  # lambda:GetFunction returns a pre-signed URL to the deployment
  # package. That is source-code access, so it is denied outright.
  # GetLayerVersion does the same for a layer's package, and it is
  # also the IAM action behind the GetLayerVersionByArn API call,
  # so both routes to a layer's code are denied here.
  - Sid: NeverDownloadFunctionCode
    Effect: Deny
    Action:
      - lambda:GetFunction
      - lambda:GetLayerVersion
    Resource: "*"
```

### What capturing S3 buckets grants

The S3 statements above exist only when you name buckets in the **S3 buckets** parameter. Three things are worth knowing for a security review:

- **The role can read the content of every object in the buckets you name.** Cloud Capture reads the SHA256 checksum S3 stores for each object with a `HeadObject` request, which returns metadata and no content. AWS has no permission for reading a checksum alone: `HeadObject` is authorized by `s3:GetObject`, the permission that also authorizes a download. Cloud Capture downloads one object only, a `.kosli_ignore` file at the root of a bucket if there is one. Reads of object versions, ACLs, tags and attributes stay denied in every bucket, and `s3:GetObject` stays denied in every bucket you did not name.
- **The role can read the tags of every taggable resource in the account.** Cloud Capture finds the buckets that carry one of your S3 opt-in tags by asking the Resource Groups Tagging API (`tag:GetResources`), which avoids reading the tags of every bucket one by one on every scan. AWS cannot scope that permission to S3 or to particular resources. Cloud Capture asks only for resources of type `s3:bucket` that carry an opt-in tag.
- **No KMS permission is granted.** Objects encrypted with a KMS key (SSE-KMS) cannot be read, and their bucket's snapshot fails.

A name in the parameter may use `*` and `?` as wildcards, as an IAM resource may. A bare `*` names every bucket in the account. Naming a bucket is a permission, not a selection: Cloud Capture snapshots a bucket only when it also carries one of your S3 opt-in tags.

</Tab>
<Tab title="Azure">

Azure support is in early access.

Nothing is deployed in your Azure tenant. Kosli registers one multi-tenant application in Microsoft Entra, and Cloud Capture reads your subscription as that application. The application's credentials are Kosli's own and never leave Kosli. Access is granted in three steps, each of which you control:

1. **Consent.** A Global Administrator of your tenant consents to the Kosli application, which creates its service principal in your tenant. Consent alone grants no access to any subscription.
2. **Role assignments.** You assign the application two built-in roles on each subscription you want scanned:

   | Role | What Cloud Capture uses it for |
   |---|---|
   | `Reader` | Listing the App Service sites in the subscription, and reading resource group tags and the subscription's own tags |
   | `AcrPull` | Fingerprinting the container images of your web apps from your container registries |

3. **A tag on the subscription.** You tag the subscription `kosli-external-id` with your organization's external ID. Cloud Capture refuses to list a subscription whose tag does not match the external ID of the organization it is working for.

The registration form in the Kosli UI shows the consent link and the three Azure CLI commands with your values filled in; see [Getting started](/administration/cloud_capture/getting_started).

To withdraw access, remove the role assignments or the tag from the subscription, or delete the application's service principal from your tenant, and remove the subscription from your registered accounts in Kosli.

</Tab>
<Tab title="Google Cloud">

Google Cloud support is in early access.

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
project; see [Getting started](/administration/cloud_capture/getting_started).

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

</Tab>
</Tabs>

## How Kosli isolates tenants

Cloud Capture runs as a shared, autoscaled service, but each job runs under a role that is scoped to
one tenant.

<Tabs>
<Tab title="AWS">

* A Cloud Capture worker picks up a job for your organization and assumes the role in your account
  using your externalId. A worker running for a different tenant is unable to read the externalId
  for your cloud account.
* When the job finishes, the temporary credentials for your account are discarded. A worker holding
  credentials for your cloud account has no path to anyone else's account.
* The ExternalId lives in Kosli's Parameter Store and is readable only by the Kosli-side role for your
  organization. The shared task role cannot read any tenant's ExternalId. Separation is enforced
  by IAM, not by application code.

The trust policy on the role in your account limits access to the AWS account in which the Cloud
Capture is running. The ExternalId acts as a shared secret between Kosli and you, so that only
Cloud Capture is permitted to assume the role.

</Tab>
<Tab title="Azure">

* The Kosli application's credentials are held by Kosli and are not readable by the part of Cloud
  Capture that plans work, only by the workers that carry it out.
* Before a worker lists anything in a subscription, it reads the subscription's `kosli-external-id`
  tag and compares it with the external ID of the organization the job is for. Only someone with
  write access to your subscription can set that tag, so another Kosli tenant that registered your
  subscription ID would be refused.
* The application has access only to the subscriptions on which you assigned it a role.

</Tab>
<Tab title="Google Cloud">

Each Cloud Capture job for your organization runs under the Kosli-side IAM role dedicated to your
organization. The workload identity pool in your project accepts only that role, so a job running
for a different tenant cannot obtain a token from your project or impersonate your service account.
Separation is enforced by the identity provider, not by application code.

</Tab>
</Tabs>

Cloud Capture itself does not hold any tenant data. Snapshots taken by Cloud Capture are
immediately sent to Kosli through the same ingest path as your existing pipelines.

## Changing security permissions

If the role, the service account and workload identity pool, or the role assignments and tag that
Cloud Capture uses are removed or edited within your cloud accounts, scans of that account fail.
Kosli is not notified of the change and does not remove the account for you: the account stays in
your **Registered accounts** table, with its scans shown as failed, until you restore the
permissions or remove the account.
