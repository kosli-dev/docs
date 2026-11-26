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

Each cloud's page gives the full detail: what you create, the exact permissions, and how the trust condition works.

| Cloud | Identity in your account | Trust condition | Access granted | Details |
|---|---|---|---|---|
| AWS | An IAM role you create | Only Kosli's AWS account can assume the role, and only with the external ID of your organization | Read-only ECS and Lambda inventory, and object reads only in the S3 buckets you name | [AWS](/administration/cloud_capture/aws#permissions-and-security) |
| Azure | A Kosli application you consent to | A `kosli-external-id` tag on the subscription that must match the external ID of your organization | The `Reader` and `AcrPull` roles on each subscription you choose | [Azure](/administration/cloud_capture/azure#permissions-and-security) |
| Google Cloud | A service account you create | A workload identity pool that accepts only Kosli's AWS account and, within it, only the Kosli-side role for your organization | The Cloud Run viewer role and two read-only custom roles | [Google Cloud](/administration/cloud_capture/google_cloud#permissions-and-security) |

## How Kosli isolates tenants

Cloud Capture runs as a shared, autoscaled service, but each job runs under a role that is scoped to
one tenant.

How that scoping is enforced depends on the cloud; see tenant isolation on [AWS](/administration/cloud_capture/aws#tenant-isolation), [Azure](/administration/cloud_capture/azure#tenant-isolation) and [Google Cloud](/administration/cloud_capture/google_cloud#tenant-isolation).

Cloud Capture itself does not hold any tenant data. Snapshots taken by Cloud Capture are
immediately sent to Kosli through the same ingest path as your existing pipelines.

## Changing security permissions

If the role, the service account and workload identity pool, or the role assignments and tag that
Cloud Capture uses are removed or edited within your cloud accounts, scans of that account fail.
Kosli is not notified of the change and does not remove the account for you: the account stays in
your **Registered accounts** table, with its scans shown as failed, until you restore the
permissions or remove the account.
