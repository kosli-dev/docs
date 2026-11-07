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

Service accounts have the same role model as users: **Admin**, **Member**, **Snapshotter**, or **Reader**. The role determines what the service account can do in the organization. Pick the least-privileged role that fits the workload.

See [Roles in Kosli](/administration/managing_users/roles_in_kosli) for the full permissions matrix. As a starting point:

- **Member** — CI/CD systems that report attestations, manage flows, and create resources.
- **Snapshotter** — runtime reporters that record environment snapshots and create and tag environments (for example, CLI callers using `--auto-environment`).
- **Reader** — read-only systems such as dashboards or query tooling.
- **Admin** — rarely needed; reserve for automation that manages users, roles, or organization-wide settings (for example, Terraform-driven org bootstrap).

## Manage service accounts with the CLI

You can create and manage service accounts and their API keys with the Kosli CLI instead of the UI. These commands assume that `--api-token` and `--org` are [set](/getting_started/install#assigning-flags-via-environment-variables), and the API token belongs to a user or service account allowed to manage service accounts.

Create a service account with `--privilege` set to `admin`, `member`, `snapshotter`, or `reader`:

```shell
kosli create service-account ci-github-actions \
    --privilege member \
    --description "CI pipeline in GitHub Actions"
```

API keys are created separately. The key value is shown only once, so store it in your secret store straight away. Without `--expires-at`, the key gets the maximum allowed lifetime.

```shell
kosli create api-key \
    --service-account ci-github-actions \
    --description "key for CI" \
    --expires-at <YYYY-MM-DD>
```

To inspect, change, or remove service accounts:

```shell
kosli list service-accounts
kosli get service-account ci-github-actions
kosli update service-account ci-github-actions --privilege reader
kosli delete service-account ci-github-actions --assume-yes
```

To list a service account's API keys, or revoke one:

```shell
kosli list api-keys --service-account ci-github-actions
kosli delete api-key <key-id> --service-account ci-github-actions --assume-yes
```

`kosli list api-keys` shows each active key's metadata, including its ID, but never the key value. `kosli delete api-key` revokes the key immediately and also deletes every key that was created with it.

`kosli update service-account` changes only the flags you pass. `kosli delete service-account` permanently deletes the service account and its API keys. It asks for confirmation, so pass `--assume-yes` in CI or other non-interactive shells.

See the reference pages for all flags: [`kosli create service-account`](/client_reference/kosli_create_service-account), [`kosli list service-accounts`](/client_reference/kosli_list_service-accounts), [`kosli get service-account`](/client_reference/kosli_get_service-account), [`kosli update service-account`](/client_reference/kosli_update_service-account), [`kosli delete service-account`](/client_reference/kosli_delete_service-account), [`kosli create api-key`](/client_reference/kosli_create_api-key), [`kosli list api-keys`](/client_reference/kosli_list_api-keys), and [`kosli delete api-key`](/client_reference/kosli_delete_api-key).

## Manage service accounts with Terraform

The Kosli Terraform provider manages service accounts with the [`kosli_service_account`](/terraform-reference/resources/service_account) resource and their API keys with the [`kosli_service_account_api_key`](/terraform-reference/resources/service_account_api_key) resource:

```terraform
resource "kosli_service_account" "ci" {
  name        = "ci-github-actions"
  description = "CI pipeline in GitHub Actions"
  privilege   = "member"
}

resource "kosli_service_account_api_key" "ci_key" {
  service_account_name = kosli_service_account.ci.name
  description          = "key for CI"
}

output "ci_api_key" {
  value     = kosli_service_account_api_key.ci_key.key
  sensitive = true
}
```

The raw `key` is returned only when Terraform creates the key, and is stored in Terraform state as a sensitive value, so protect your state. API keys are immutable: changing `description`, `expires_at`, or `service_account_name` revokes the key and creates a new one. To read an existing service account without managing it, use the [`kosli_service_account` data source](/terraform-reference/data-sources/service_account).

## Rotate or revoke keys

For zero-downtime rotation and the API-driven flow, see:

- [API key rotation (reference)](/administration/authentication/api_key_rotation)
- [Rotating API keys (tutorial)](/tutorials/rotating_api_keys)
