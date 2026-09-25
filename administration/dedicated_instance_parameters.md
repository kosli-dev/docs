---
title: Dedicated instance parameters
description: "Required parameters for provisioning a Kosli Dedicated instance."
icon: "sliders"
---

A Kosli Dedicated instance is a single-tenant Kosli instance hosted on infrastructure dedicated to your organization. Provisioning one requires a small set of parameters that a member of the Kosli Customer Success team collects from you before deployment.

## Required parameters

### Identity

- **SSO / SCIM setup** — the identity provider and protocol you want to sign in with (SAML or OIDC), and, if applicable, the SCIM directory for automated user provisioning. See [Single sign-on](/administration/authentication/single_sign_on) for the supported providers and the metadata Kosli needs from your IdP.

### Hosting

- **DNS host** — the hostname you want your instance to be reachable at (for example, `<instance>.kosli.com`). Kosli issues a TLS certificate for this hostname.
- **Customer KMS keys** — the ARNs of the AWS KMS keys that encrypt all data at rest. Follow [Customer KMS keys](/administration/customer_kms_keys) to create a primary key and a secondary-region replica (or two single-region keys) in your own AWS account and share the ARNs with Kosli.
- **AWS regions** — the **primary** and **secondary** AWS regions your instance runs in. Both regions must be ones Kosli Dedicated supports; a member of the Kosli Customer Success team will confirm the current options.

### Network access

- **PrivateLink** — whether inbound traffic to the instance should traverse the public internet or a dedicated AWS PrivateLink endpoint. For PrivateLink, provide the AWS account IDs and VPCs that need to reach the instance.
- **ACL** — the list of source IP ranges (CIDR blocks) allowed to reach the instance over the public endpoint. Leave empty to allow all sources, or restrict to your corporate egress ranges and CI providers.

<Note>
A member of the Kosli Customer Success team will walk through these parameters with you and confirm the exact values required before your instance is provisioned.
</Note>
