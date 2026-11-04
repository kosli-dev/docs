---
title: Personal API keys
description: Create and manage personal API keys tied to your Kosli user account.
icon: "key"
---

A personal API key authenticates as **you**. It inherits your permissions across every organization you belong to.

<Warning>
For CI/CD pipelines and any other automation, use a [service account](/administration/authentication/service_accounts) instead. Service account keys are scoped to a single organization, have an explicit role, and produce cleaner audit trails.
</Warning>

## Create a personal API key

<Steps>
  <Step title="Open your profile">
    From the user menu in the top-right corner of the Kosli app, click **Profile**:

    - EU: [app.kosli.com/settings/profile](https://app.kosli.com/settings/profile)
    - US: [app.us.kosli.com/settings/profile](https://app.us.kosli.com/settings/profile)
  </Step>
  <Step title="Add an API key">
    In the **API keys** section, click **Add API key**. Choose a Time-To-Live (TTL), add a descriptive label, and click **Add**.
  </Step>
  <Step title="Copy the key immediately">
    Kosli stores only a cryptographic hash of the token. The original value is shown once and cannot be retrieved later.
  </Step>
</Steps>

## Use the key

The same usage applies as for service account keys — see [Authenticating to Kosli](/getting_started/authenticating_to_kosli#use-the-token).

## Rotate a key

To replace a personal API key without downtime, regenerate it. Kosli issues a new key and keeps the old one valid for a grace period, as described in [API key rotation](/administration/authentication/api_key_rotation).

1. Open **Profile**, and in the **API keys** section open the menu of the key you want to replace.
2. Click **Regenerate**.
3. Choose when the new key expires and how many hours the current key stays valid (24 by default), then click **Regenerate**.
4. Copy the new key immediately and update everything that uses the old one.

## Delete a key

To delete a personal API key, open **Profile → API keys**, open the key's menu, and click **Delete**. The key stops working immediately.

## Manage keys from the CLI

The `kosli` API key commands manage your own personal keys when you pass `--personal` instead of `--service-account`. Personal keys belong to you, not to an organization, so `--org` is not needed. You can't combine `--personal` with `--service-account`.

```shell
# list your personal API keys
kosli list api-keys --personal --api-token "$KOSLI_API_TOKEN"

# create a new personal API key
kosli create api-key --personal --description "my laptop" --api-token "$KOSLI_API_TOKEN"

# rotate a key, keeping the old one valid for 48 hours
kosli rotate api-key <key-id> --personal --grace-period-hours 48 --api-token "$KOSLI_API_TOKEN"

# delete a key
kosli delete api-key <key-id> --personal --api-token "$KOSLI_API_TOKEN"
```

When `--api-token` is itself a personal API key, these limits apply:

- A key you create with it expires no later than that key, and is deleted along with it.
- You can only rotate or delete that key and the keys created with it.

To get a key that outlives the one you are using, create it from your **Profile** page. See [`kosli create api-key`](/client_reference/kosli_create_api-key), [`kosli rotate api-key`](/client_reference/kosli_rotate_api-key), [`kosli list api-keys`](/client_reference/kosli_list_api-keys), [`kosli get api-key`](/client_reference/kosli_get_api-key), and [`kosli delete api-key`](/client_reference/kosli_delete_api-key) for every flag.

Service accounts can't manage personal API keys. Use the service account key commands for them.
