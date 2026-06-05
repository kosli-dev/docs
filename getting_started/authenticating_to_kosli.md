---
title: Authenticating to Kosli
description: How to get an API token for the Kosli CLI and API, and where to manage credentials.
icon: "key"
---

Most interactions with Kosli — from the CLI, the API, or CI/CD pipelines — require an API token. This page covers the quickest path to getting one and points to the deeper documentation for each topic.

## Pick a credential type

| Use case | Credential | Where to manage it |
|----------|------------|--------------------|
| CI/CD, runtime reporters, automation | **Service account API key** (recommended) | [Service accounts](/administration/authentication/service_accounts) |
| Interactive scripts tied to your user | **Personal API key** | [Personal API keys](/user/personal_api_keys) |

<Tip>
For anything automated, use a service account. Personal API keys inherit your user's permissions across every organization you belong to, which is rarely what you want for a pipeline.
</Tip>

## Quick start: get a token

<Steps>
  <Step title="Sign in to Kosli">
    Open the Kosli web app and sign in:

    - EU: [app.kosli.com](https://app.kosli.com)
    - US: [app.us.kosli.com](https://app.us.kosli.com)
  </Step>
  <Step title="Create a key">
    - **For CI/CD**, follow [Service accounts](/administration/authentication/service_accounts) to create a service account and generate its first API key.
    - **For your own scripts**, follow [Personal API keys](/user/personal_api_keys) to generate a key tied to your user.
  </Step>
  <Step title="Copy the key immediately">
    Kosli stores only a hash of the token, so the original is shown once and cannot be retrieved later. Paste it straight into your secret store.
  </Step>
</Steps>

## Use the token

Pass the token as a bearer token when calling the API directly:

```shell
curl -H "Authorization: Bearer <<your-api-key>>" \
  https://app.kosli.com/api/v2/environments/<<your-org-name>>
```

For CLI usage, basic auth, and full examples, see [API authentication methods](/administration/authentication/api_authentication_methods).

## See also

- [Service accounts](/administration/authentication/service_accounts) — admin lifecycle for machine credentials.
- [API key rotation](/administration/authentication/api_key_rotation) — how rotation works, with a [step-by-step tutorial](/tutorials/rotating_api_keys).
- [Roles in Kosli](/administration/managing_users/roles_in_kosli) — what users and service accounts can do at each role.
