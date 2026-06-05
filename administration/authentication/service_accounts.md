---
title: Service accounts
description: Create and manage service accounts and their API keys for machine-to-machine access to Kosli.
icon: "user-gear"
---

A **service account** is a machine user. Use service accounts for any non-human caller — CI pipelines, runtime reporters, scripts, and other automation — so that credentials and audit trails are tied to a system rather than a person.

<Warning>
Service accounts are only available in shared organizations.
</Warning>

## Create a service account

<Steps>
  <Step title="Open the organization's settings">
    Sign in to Kosli and select the organization where the service account should live.
    Navigate to **Settings → Service accounts**.
  </Step>
  <Step title="Add the service account">
    Click **Add new service account**, give it a descriptive name (e.g. `ci-github-actions`), and click **Add**.
  </Step>
  <Step title="Generate an API key">
    On the new service account, click **Add API key**. Choose a Time-To-Live (TTL), add a label that identifies where the key will be used, and click **Add**.
  </Step>
  <Step title="Copy the key immediately">
    Kosli stores only a cryptographic hash of the token. The original value is shown once and cannot be retrieved later — paste it directly into your secret store.
  </Step>
</Steps>

## Assign a role

Service accounts have the same role model as users: **Admin**, **Member**, **Snapshotter**, or **Reader**. The role determines what the service account can do in the organization.

See [Roles in Kosli](/administration/managing_users/roles_in_kosli) for the full permissions matrix. As a starting point:

- **Member** — CI/CD systems that report attestations, manage flows, and create resources.
- **Snapshotter** — runtime reporters that only record environment snapshots.
- **Reader** — read-only systems such as dashboards or query tooling.
- **Admin** — rarely needed; reserve for automation that manages users, roles, or organization-wide settings (for example, Terraform-driven org bootstrap).

## Rotate or revoke keys

For zero-downtime rotation and the API-driven flow, see:

- [API key rotation (reference)](/administration/authentication/api_key_rotation)
- [Rotating API keys (tutorial)](/tutorials/rotating_api_keys)
