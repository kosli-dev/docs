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

The Cloud Capture managed service uses the public cloud APIs to extract information about your cloud environments.  In order to do this, you need to provide Kosli with an IAM role inside your cloud environment that allows access to these APIs.  The role is created and managed by you. The role must contain the relevant assume-trust policy to allow Kosli to access your account and must contain the correct permissions for Kosli to find and snapshot your resources.

<Tabs>
<Tab title="AWS">
Kosli publishes a CloudFormation template, for use in AWS, showing the permissions needed.  The template is publicly accessible and can be used directly within an `aws cloudformation create-stack` call.

The CloudFormation template we share with you includes a "phone-home" feature that notifies Kosli when a CloudFormation stack has been built from it; this allows us to pick up the AWS AccountId for the account in which you have used the CloudFormation template without you needing to do anything.  This automation is especially useful when you deploy the template as a StackSet within an Organizational Unit.

If you wish to build an IAM role for Cloud Capture without using our published CloudFormation template, the permissions needed are those shown below. The role must contain an Assume Role policy that allows the Kosli account to access the resources, and must include an externalId. Both of these values are supplied by Kosli and cannot be derived; you cannot construct the trust policy without them.

### Assume role

The IAM role defined within the CloudFormation template includes an "assume role" policy granting permission from Kosli.  This appears as:

```yaml
  KosliCaptureAccessRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Ref RoleName
      Description: >-
        Read-only access for Cloud Capture SDLC compliance evidence collection.
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

  # How Capture finds what to snapshot. Discovery lists the ECS
  # clusters in the account and reads each cluster's tags from the
  # same DescribeClusters call.
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

  # lambda:GetFunction returns a pre-signed URL to the deployment
  # package. That is source-code access, so it is denied outright.
  - Sid: NeverDownloadFunctionCode
    Effect: Deny
    Action:
      - lambda:GetFunction
      - lambda:GetLayerVersion
    Resource: "*"
```

</Tab>
<Tab title="GCP">

<Warning>
GCP support is coming soon
</Warning>

Kosli publishes a Terraform configuration, for use with
[Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs), showing the
permissions needed to snapshot Google Kubernetes Engine (GKE) clusters. Infrastructure Manager runs
Terraform as a managed service inside your project, so there is no state file or Terraform install
for you to manage. Deploy the configuration once in each project that holds clusters you want Cloud
Capture to snapshot.

Cloud Capture runs in AWS and reaches your project through
[Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation). Cloud
Capture exchanges its own short-lived AWS credentials for a short-lived Google token, then
impersonates a service account that you create. No service account key is ever created or shared.

The trust has two parts, mirroring the AWS assume-role policy and external ID. The workload identity
pool accepts credentials only from the Kosli AWS account, which is the counterpart of the principal
in the trust policy. Within that account it accepts only the Kosli-side IAM role that is dedicated
to your organization, which is the counterpart of the external ID. Every Cloud Capture job runs
under the role for the organization it is working for, so a job for another Kosli customer presents
a different role name and is refused by your pool, even if that customer gave Kosli your provider
and service account instead of their own. The role name is part of the credential that AWS signs
and Google verifies, so it cannot be forged by the caller.

GCP has no equivalent of the CloudFormation "phone-home" feature, so the configuration emits the
values Kosli needs as Terraform outputs. Share them with Kosli after the deployment completes; you
can read them at any time with `gcloud infra-manager deployments describe`.

If you wish to grant access for Cloud Capture without using our published configuration, the
resources needed are those shown below. The pool must accept only the Kosli AWS account and, within
it, only the Kosli-side role for your organization, and only that role may impersonate the service
account. The specific permissions needed to find and snapshot GKE clusters are in the custom role.

<Note>
Cloud Capture connects to each cluster's Kubernetes API from Kosli's infrastructure, so the
cluster's control plane endpoint must be reachable from outside your VPC. A cluster whose control
plane has a private endpoint only cannot be snapshotted.
</Note>

### Workload identity federation

The Terraform configuration creates a workload identity pool, an AWS provider within it that trusts
the Kosli-side role for your organization, and a service account that only that role may
impersonate. This appears as:

```hcl
variable "project_id" {
  type        = string
  description = "The GCP project that holds the GKE clusters Cloud Capture will snapshot."
}

variable "kosli_aws_account_id" {
  type        = string
  description = <<-EOT
    The AWS account in which Cloud Capture runs, supplied by Kosli. It differs
    per customer because more than one Kosli account serves customers. There
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
    uses when working for your organization. Supplied by Kosli. Each Kosli
    organization has its own role, so this value is the counterpart of the
    AWS external ID: only jobs run on your behalf can obtain a token from
    your project.
  EOT

  validation {
    condition     = can(regex("^[A-Za-z0-9+=,.@_-]{1,64}$", var.kosli_role_name))
    error_message = "Must be the IAM role name issued to you by Kosli."
  }
}

# Cloud Capture runs in AWS. Workload Identity Federation lets it exchange its
# own short-lived AWS credentials for a short-lived Google token, so no service
# account key is ever created, stored or shared.
resource "google_iam_workload_identity_pool" "kosli_capture" {
  project                   = var.project_id
  workload_identity_pool_id = "kosli-capture"
  display_name              = "Cloud Capture"
  description               = <<-EOT
    Read-only access for Cloud Capture SDLC compliance evidence collection.
    Managed by Infrastructure Manager; do not edit in place.
  EOT
}

resource "google_iam_workload_identity_pool_provider" "kosli_aws" {
  project                            = var.project_id
  workload_identity_pool_id          = google_iam_workload_identity_pool.kosli_capture.workload_identity_pool_id
  workload_identity_pool_provider_id = "kosli-aws"
  display_name                       = "Cloud Capture (AWS)"

  aws {
    account_id = var.kosli_aws_account_id
  }

  attribute_mapping = {
    "google.subject"     = "assertion.arn"
    "attribute.account"  = "assertion.account"
    "attribute.aws_role" = "assertion.arn.extract('assumed-role/{role}/')"
  }

  # Two checks, mirroring the AWS trust policy. The account check is the
  # counterpart of the trust policy principal: only credentials issued by the
  # Kosli account are accepted, however the token reaches Google. The role
  # check is the counterpart of the external ID: within that account, only the
  # Kosli-side role dedicated to your organization is accepted. A Cloud Capture
  # job for another customer runs under a different role and is refused here.
  attribute_condition = join(" && ", [
    "attribute.account == \"${var.kosli_aws_account_id}\"",
    "attribute.aws_role == \"${var.kosli_role_name}\"",
  ])
}

resource "google_service_account" "kosli_capture" {
  project      = var.project_id
  account_id   = "kosli-capture"
  display_name = "Cloud Capture"
  description  = "Impersonated by Cloud Capture to snapshot GKE clusters. Managed by Infrastructure Manager."
}

# Only the Kosli-side role for your organization may impersonate the service
# account. The pool's attribute condition already refuses every other identity;
# naming the role here as well keeps the binding correct even if that condition
# is later loosened.
resource "google_service_account_iam_member" "kosli_impersonation" {
  service_account_id = google_service_account.kosli_capture.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.kosli_capture.name}/attribute.aws_role/${var.kosli_role_name}"
}

# Kosli needs these two values to connect. Infrastructure Manager shows them
# with `gcloud infra-manager deployments describe`.
output "kosli_capture_provider" {
  description = "Full resource name of the workload identity provider; give this to Kosli."
  value       = google_iam_workload_identity_pool_provider.kosli_aws.name
}

output "kosli_capture_service_account" {
  description = "Email of the service account Cloud Capture impersonates; give this to Kosli."
  value       = google_service_account.kosli_capture.email
}
```

### GKE permissions

The Terraform configuration grants the service account a custom role containing read-only GKE
permissions. GKE enforces these permissions both on the GKE API and on the Kubernetes API of each
cluster, so no Kubernetes RBAC objects need to be created inside your clusters. The role is:

```hcl
# How Capture finds what to snapshot. Discovery lists the GKE clusters in the
# project and reads each cluster's labels, endpoint and CA certificate from
# the same clusters.get call.
#
# Worth knowing for a security review: GKE checks the container.* permissions
# below when Cloud Capture calls the Kubernetes API, so this role is also the
# Kubernetes RBAC. None of it returns application data. pods.list is the
# widest - a pod spec holds the container image, the command, and any
# environment variables written into the spec itself in plain text. Values
# taken from a Secret or ConfigMap are named there rather than resolved, and
# this role grants no access to Secrets or ConfigMaps, so what comes back is
# the reference and not the secret.
resource "google_project_iam_custom_role" "kosli_capture" {
  project     = var.project_id
  role_id     = "kosliCapture"
  title       = "Cloud Capture"
  description = "Read-only GKE inventory for Cloud Capture SDLC compliance evidence collection."

  permissions = [
    # Discovery
    "container.clusters.get",
    "container.clusters.list",

    # Snapshot: the Kubernetes API calls that kosli snapshot k8s makes
    "container.namespaces.get",
    "container.namespaces.list",
    "container.pods.get",
    "container.pods.list",
  ]
}

resource "google_project_iam_member" "kosli_capture" {
  project = var.project_id
  role    = google_project_iam_custom_role.kosli_capture.id
  member  = google_service_account.kosli_capture.member
}
```

### Deploying with Infrastructure Manager

Run the following from the directory containing the configuration. Infrastructure Manager runs
Terraform as the service account you name, so that service account needs permission to enable APIs
and to create workload identity pools, service accounts, custom roles and project IAM bindings.

```bash
gcloud infra-manager deployments apply \
    projects/<your-gcp-project>/locations/<your-gcp-region>/deployments/kosli-capture \
    --service-account=projects/<your-gcp-project>/serviceAccounts/<deployer>@<your-gcp-project>.iam.gserviceaccount.com \
    --local-source=. \
    --input-values=project_id=<your-gcp-project>,kosli_aws_account_id=<value from Kosli>,kosli_role_name=<value from Kosli>
```

</Tab>
</Tabs>

## How Kosli isolates customers

Cloud Capture runs as a shared, autoscaled service, but each job runs under a role that is scoped to
one customer:

* A Cloud Capture worker picks up a job for your organization and assumes the role in your account
  using your externalId. A worker running for a different customer is unable to read the externalId
  for your cloud account.
* When the job finishes, the temporary credentials for your account are discarded. A worker holding
  credentials for your cloud account has no path to anyone else's account.
* The ExternalId lives in Kosli's Parameter Store and is readable only by the Kosli-side role for your
  organization. The shared task role cannot read any customer's ExternalId. Separation is enforced
  by IAM, not by application code.

The trust policy on the role in your account limits access to the AWS account in which the Cloud
Capture is running. The ExternalId acts as a shared secret between Kosli and you, so that only
Cloud Capture is permitted to assume the role.

Cloud Capture itself does not hold any customer data. Snapshots taken by Cloud Capture are
immediately sent to Kosli through the same ingest path as your existing pipelines.

## Changing security permissions

If the IAM role assumed by Cloud Capture is removed or edited within your cloud accounts, Cloud
Capture will fail to operate correctly. The failure will be detected and the account will be
removed from the list of accounts captured.
