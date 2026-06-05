---
title: API authentication methods
description: How to authenticate to the Kosli API using bearer tokens or HTTP basic auth.
icon: "shield-halved"
---

The Kosli API supports two authentication methods:

| Method | Status | When to use |
|--------|--------|-------------|
| [Bearer token](#bearer-token) | **Recommended** | All new integrations. Works for service account and personal API keys. |
| [HTTP basic auth](#http-basic-auth) | Legacy | Fallback for tools that cannot send an `Authorization: Bearer` header. |

<Tip>
If you are integrating Kosli for the first time, use bearer tokens. Basic auth remains supported for backwards compatibility but is not the recommended path.
</Tip>

## Bearer token

Bearer tokens work with both [service account](/administration/authentication/service_accounts) and [personal](/user/personal_api_keys) API keys.

### In the CLI

Pass the token to any `kosli` command using one of:

- The `--api-token` flag.
- The `KOSLI_API_TOKEN` environment variable.
- A config file passed via `--config-file` — see [Assigning flags via config files](/getting_started/install#assigning-flags-via-config-files).

### In API requests

Send the token in the `Authorization` header:

```shell
curl -H "Authorization: Bearer <<your-api-key>>" \
  https://app.kosli.com/api/v2/environments/<<your-org-name>>
```

## HTTP basic auth

<Note>
HTTP basic auth is a legacy method kept for backwards compatibility with tools that cannot send an `Authorization: Bearer` header. For all new integrations, use bearer tokens instead.
</Note>

Kosli accepts HTTP basic auth as an alternative to bearer tokens. The API key is sent as the **username**; the password is ignored.

```shell
curl -u "<<your-api-key>>:" \
  https://app.kosli.com/api/v2/environments/<<your-org-name>>
```

<Warning>
The trailing colon (`:`) is required. Without it, `curl` treats the whole string as a username with no password and **prompts interactively** for one — at which point the API key may already be visible in the prompt or shell history (especially when the key comes from an environment variable). The value after the colon can be anything, including empty; Kosli ignores it.
</Warning>

Equivalently, set the `Authorization` header directly with the base64-encoded `<<your-api-key>>:` string:

```shell
curl -H "Authorization: Basic $(printf '%s:' "<<your-api-key>>" | base64)" \
  https://app.kosli.com/api/v2/environments/<<your-org-name>>
```
