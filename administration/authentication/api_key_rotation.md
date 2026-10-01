---
title: API key rotation
description: Reference for how Kosli API key rotation works, including grace periods and the rotation API.
icon: "arrows-rotate"
---

Rotating API keys regularly limits the blast radius of a leaked credential. Kosli supports **zero-downtime rotation** for service account API keys: a new key is issued immediately while the old key remains valid for a configurable grace period.

## How rotation works

When you rotate a service account API key, Kosli:

1. Generates a new API key and returns its value once.
2. Sets the new key's expiry to the **rotated key's current expiry** unless you pass `--expires-at` (CLI) or `expires_at` (API), bounded by the server-side **maximum lifetime of 365 days from creation**.
3. Keeps the old key valid for a configurable grace period (default: **24 hours**).
4. Automatically revokes the old key when the grace period expires.

Choose a grace period that fits your deployment cadence — long enough to roll the new key out to every consumer, short enough to limit exposure.

<Warning>
Rotation on its own does not extend the credential. If the rotated key was already close to its expiry, the new key expires at the same moment unless you pass an explicit `--expires-at` (up to the 365-day cap).
</Warning>

## Expiry warnings

Kosli warns you before an API key expires, so you can rotate it in time. Keys with no expiry never trigger a warning.

### When warnings are sent

A key gets at most two warnings:

| Warning | Sent when |
|---|---|
| First notice | 14 days or less are left before the key expires |
| Last call | 3 days or less are left, and the key still has the same expiry date |

Rotating a key resets its warnings. With a new expiry date, the countdown starts again for that date. With the same date, the next daily check warns you again.

A key created with less than 14 days to live gets only the last call. All keys expiring for the same recipient are grouped in one message, which lists each key, its expiry date, and when it was last used.

### Who receives them

By default, recipients depend on the kind of key:

- **Service account keys** go to the organization's admins. The member who created the key also gets a message about their own keys, as long as they are still a member. An admin who created a key gets only the admin message.
- **Personal keys** go to the key's owner only. The organization is not informed.

### Send warnings somewhere else

An admin can replace the default recipients for service account keys with one or more destinations: email addresses, a Slack webhook, or a webhook URL. When destinations are set, only those receive the warnings. Admins and key creators are not copied.

Personal keys are not affected. Their owner is always warned directly.

<Steps>
  <Step title="Open the Notifications settings">
    Go to **Settings → Notifications** in the organization. This tab is visible to admins of shared organizations.
  </Step>
  <Step title="Set the destinations">
    Under **API key expiry warnings**, click **Set destinations**, add one row per destination, and click **Save**.
  </Step>
  <Step title="Restore the defaults when needed">
    Click **Restore default recipients** to go back to admins and key creators.
  </Step>
</Steps>

The page also shows when the last warning was sent and whether the latest delivery failed.

The API offers the same settings under `/api/v2/notification-config/{org}/api_key_expiry`:

- [Get notification configuration](/api-reference/notification-config/get-notification-configuration) returns the current destinations. Any member can read them.
- [Create or update notification configuration](/api-reference/notification-config/create-or-update-notification-configuration) replaces the destinations. Admins only.
- [Delete notification configuration](/api-reference/notification-config/delete-notification-configuration) removes them and restores the default recipients. Admins only.

## Where next

- [Rotating API keys (tutorial)](/tutorials/rotating_api_keys) — step-by-step walkthrough in the web app and via the API.
- [Service accounts](/administration/authentication/service_accounts) — service account lifecycle.
- [Rotate an API key (API reference)](/api-reference/service-accounts/rotate-an-api-key-for-a-service-account)
- [Revoke an API key (API reference)](/api-reference/service-accounts/revoke-an-api-key-for-a-service-account)
- [List API keys (API reference)](/api-reference/service-accounts/list-api-keys-for-a-service-account)
- [Notification configuration (API reference)](/api-reference/notification-config/get-notification-configuration)
