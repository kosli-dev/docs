---
title: API key rotation
description: Reference for how Kosli API key rotation works, including grace periods and the rotation API.
icon: "arrows-rotate"
---

Rotating API keys regularly limits the blast radius of a leaked credential. Kosli supports **zero-downtime rotation** for service account API keys: a new key is issued immediately while the old key remains valid for a configurable grace period.

## How rotation works

When you rotate a service account API key, Kosli:

1. Generates a new API key and returns its value once.
2. Keeps the old key valid for a configurable grace period (default: **24 hours**).
3. Automatically revokes the old key when the grace period expires.

Choose a grace period that fits your deployment cadence — long enough to roll the new key out to every consumer, short enough to limit exposure.

## Where next

- [Rotating API keys (tutorial)](/tutorials/rotating_api_keys) — step-by-step walkthrough in the web app and via the API.
- [Service accounts](/administration/authentication/service_accounts) — service account lifecycle.
- [Rotate an API key (API reference)](/api-reference/service-accounts/rotate-an-api-key-for-a-service-account)
- [Revoke an API key (API reference)](/api-reference/service-accounts/revoke-an-api-key-for-a-service-account)
- [List API keys (API reference)](/api-reference/service-accounts/list-api-keys-for-a-service-account)

{/* TODO: expand with rotation guidance for personal API keys once the personal-key rotation flow is finalized */}
