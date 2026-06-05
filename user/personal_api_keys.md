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

{/* TODO: expand with rotation guidance for personal keys and link to audit-log visibility */}
