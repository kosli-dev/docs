---
title: Roles in Kosli
description: Understand the roles in Kosli and their permissions to manage access for users and service accounts within your organization.
---
Kosli uses a single role model that applies to both **users** and **[service accounts](/administration/authentication/service_accounts)**. Understanding these roles is essential for assigning the appropriate level of access to your team members and to the automated systems that talk to Kosli on their behalf.

<Note>
Roles apply to service accounts the same way they apply to users. Wherever this page mentions a "user", read it as "user or service account" unless explicitly stated otherwise. The only role-related capability that is user-only is being invited to or removed from the organization.
</Note>

## Overview

| Role | Description | Best for |
|------|-------------|----------|
| **Admin** | Full control over the organization | Organization owners, security leads, platform engineering leads |
| **Member** | Can create and modify resources | Developers, platform engineers, CI/CD systems |
| **Snapshotter** | Can create snapshots, environments, and manage its own service accounts | Environment and operations teams |
| **Reader** | Read-only access to view data | Auditors, compliance officers, stakeholders, reporting systems |

## Permissions Matrix

| Capability | Admin | Member | Snapshotter | Reader |
|------------|:-----:|:------:|:-----------:|:------:|
| **User Management** | | | |
| Invite and remove users | ✅ | ❌ | ❌ | ❌ |
| Change user roles | ✅ | ❌ | ❌ | ❌ |
| **Organization Settings** | | | |
| Modify organization settings | ✅ | ❌ | ❌ | ❌ |
| Configure integrations (Slack, LaunchDarkly) | ✅ | ✅ | ❌ | ❌ |
| **Service Accounts** | | | |
| Create and manage service accounts | ✅ | ✅ | ✅ | ❌ |
| Generate service account API keys | ✅ (any) | ✅ (own only) | ✅ (own only) | ❌ |
| **Resource Management** | | | |
| Create flows | ✅ | ✅ | ❌ | ❌ |
| Update/delete flows | ✅ | ✅ | ❌ | ❌ |
| Create environments (and re-create) | ✅ | ✅ | ✅ | ❌ |
| Update environments (PATCH, archive, rename, attach/detach policies) | ✅ | ✅ | ❌ | ❌ |
| Delete environments | ✅ | ❌ | ❌ | ❌ |
| Create/update policies | ✅ | ✅ | ❌ | ❌ |
| Delete policies | ❌ | ❌ | ❌ | ❌ |
| Create attestation types | ✅ | ✅ | ❌ | ❌ |
| Update/delete attestation types | ✅ | ✅ | ❌ | ❌ |
| **Attestations & Snapshots** | | | |
| Report attestations | ✅ | ✅ | ❌ | ❌ |
| Report environment snapshots | ✅ | ✅ | ✅ | ❌ |
| Create and manage approvals | ✅ | ✅ | ❌ | ❌ |
| **Actions** | | | |
| Create, update, and delete actions | ✅ | ✅ | ❌ | ❌ |
| View actions | ✅ | ✅ | ✅ | ✅ |
| **Data Access** | | | |
| View trails and artifacts | ✅ | ✅ | ✅ | ✅ |
| View attestations | ✅ | ✅ | ✅ | ✅ |
| View snapshots | ✅ | ✅ | ✅ | ✅ |
| Query and search data | ✅ | ✅ | ✅ | ✅ |
| Export and generate reports | ✅ | ✅ | ✅ | ✅ |
| View flow/policy configurations | ✅ | ✅ | ✅ | ✅ |

---

## Role details

The following sections provide more details about each Kosli user role, including their permissions and when to assign them.

  <Accordion title="Admin" icon="shield-check">

  Administrators have full control over the organization and its resources.

  ### Permissions

  Admins can perform all actions in Kosli, including:

  - **User Management**: Invite, remove, and change roles of organization members (Admin only)
  - **Organization Settings**: Modify organization-wide settings and configurations (Admin only)
  - **Service Accounts**: Create and manage service accounts and their API keys
  - **Integrations**: Configure integrations with external systems (Slack, LaunchDarkly, etc.)
  - **Resource Management**: Create, update, and delete flows, environments, policies, and attestation types
  - **Attestations & Snapshots**: Report attestations, environment snapshots, and manage approvals
  - **Actions**: Create, update, and delete actions for automated workflows and notifications
  - **Data Access**: View all trails, artifacts, attestations, and snapshots

  ### When to assign

  Assign the Admin role to:
  - Organization owners or senior leaders responsible for overall Kosli implementation
  - Security engineers who need to manage user access and compliance processes
  - Platform engineering leads who need to configure integrations and manage organization settings

  <Warning>
  Limit the number of Admins to maintain security and control over your organization. Most users should be Members or Readers.
  </Warning>

  </Accordion>
  <Accordion title="Member" icon="user-check">

  Members can create and modify resources, manage service accounts, and configure integrations, but cannot manage users or organization-wide settings.

  ### Permissions

  Members can:

  - **Service Accounts**: Create and manage service accounts and their API keys
  - **Integrations**: Configure integrations with external systems (Slack, LaunchDarkly, etc.)
  - **Resource Management**: Create, update, and delete flows, environments, policies, and attestation types
  - **Attestations & Snapshots**: Report attestations, environment snapshots, and manage approvals
  - **Actions**: Create, update, and delete actions for automated workflows and notifications
  - **Data Access**: View all trails, artifacts, attestations, and snapshots

  Members cannot:
  - Manage users or change user roles
  - Modify organization-wide settings

  ### When to assign

  Assign the Member role to:
  - Platform engineers who need to implement Kosli across teams and manage service accounts
  - Application developers who need to report attestations and manage flows
  - Team leads who need to configure integrations and create service accounts for their teams
  - CI/CD systems that need to report attestations and snapshots (via service accounts)

 </Accordion>
  <Accordion title="Snapshotter" icon="camera">


  Snapshotters can create environments, report environment snapshots, and manage their own service accounts, but cannot modify other resources, manage users, configure integrations, or change organization-wide settings.

  ### Permissions

  Snapshotters can:

  - **Service Accounts**: Create service accounts. They can manage the API keys of service accounts they created themselves — API keys on other service accounts can only be managed by the account's creator or an org Admin.
  - **Environments**: Create new environments (needed so CLI flows like `--auto-environment` work with a snapshotter token).
  - **Snapshots**: Report environment snapshots.
  - **View Data**: Access trails, artifacts, attestations, and snapshots.
  - **Query Information**: Search and filter data across flows and environments.
  - **Generate Reports**: Export and analyze compliance data.
  - **View Configurations**: See flow definitions, policies, attestation types, and actions (but cannot modify them).

  Snapshotters cannot:
  - Use the dedicated update paths on an environment (PATCH, archive, rename, attach/detach policies).
  - Create, update, or delete flows, policies, attestation types, or other resources.
  - Report attestations.
  - Manage approvals.
  - Create or manage actions.
  - Configure integrations.
  - Invite users or change settings.

  <Warning>
  Because the environment create endpoint (`PUT /api/v2/environments/{org}`) is idempotent — a re-PUT of an existing environment updates it — a snapshotter token can modify an existing environment's description, scaling, policies, and included environments by re-PUTting a full payload. Only the dedicated update paths (PATCH, archive, rename, policy attach/detach) are blocked. Keep this in mind when scoping snapshotter tokens for environments you don't want them to change.
  </Warning>

  ### When to assign

  Assign the Snapshotter role to:
  - Environment teams who need to manage runtime environments and report snapshots
  - Systems that only need to report environment state without modifying build pipelines

  ---

  </Accordion>
  <Accordion title="Reader" icon="eye">

  Readers have read-only access to view data in Kosli without the ability to create or modify resources.

  ### Permissions

  Readers can:

  - **View Data**: Access trails, artifacts, attestations, and snapshots
  - **Query Information**: Search and filter data across flows and environments
  - **Generate Reports**: Export and analyze compliance data
  - **View Configurations**: See flow definitions, policies, attestation types, and actions (but cannot modify them)

  Readers cannot:
  - Create, update, or delete any resources
  - Report attestations or snapshots
  - Manage approvals
  - Create or manage actions
  - Create or manage service accounts
  - Configure integrations
  - Invite users or change settings

  ### When to assign

  Assign the Reader role to:
  - Auditors who need visibility into compliance data
  - Compliance officers reviewing attestation and deployment history
  - Stakeholders and executives who want to monitor software delivery
  - Reporting and monitoring systems that query Kosli data for dashboards
  </Accordion>


## Assigning roles

To assign or change a user's role:

1. Log in to Kosli as an Admin
2. Navigate to your organization from the left navigation menu
3. Go to `Settings` > `Members`
4. Find the user you want to modify
5. Select their new role from the dropdown menu

<Note>
Role changes take effect immediately. Users will see their updated permissions the next time they interact with Kosli.
</Note>

---

## Best practices

### Follow the principle of least privilege

Assign users the minimum role required to perform their job functions. Start with Reader access and increase permissions as needed.

### Use service accounts for automation

For CI/CD pipelines and automated systems, create service accounts with the Member role rather than using personal API keys. This provides better auditability and security.

### Regular access reviews

Periodically review user roles and remove access for team members who no longer need it. This is especially important when people change roles or leave the organization.

### Separate concerns

- **Admins**: Focus on governance, security, and organization-wide configuration
- **Members**: Handle day-to-day operations and resource management
- **Snapshotters**: Manage environments and policies without affecting build flows
- **Readers**: Provide visibility without risk of accidental changes

---

## See also

- [Mapping users to roles](/administration/managing_users/mapping_users_to_roles) — recommended Kosli roles for common organizational roles.
- [Service accounts](/administration/authentication/service_accounts) — assigning roles to machine users.
