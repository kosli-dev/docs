---
title: GitHub sign-in
description: "Sign in to Kosli with a GitHub account, and allow Kosli's sign-in traffic through a GitHub IP allow list."
icon: "github"
---

Kosli supports signing in with a GitHub account. If your organization uses an identity provider,
[single sign-on](/administration/authentication/single_sign_on) is the alternative, and
[Magic Link](/administration/authentication/magic_link) works without one.

## Before you begin

Your GitHub account must have a verified email address, otherwise sign-in fails. Check the status of
your email addresses at [github.com/settings/emails](https://github.com/settings/emails).

## Sign in with GitHub

<Steps>
  <Step title="Open Kosli">
    Open the Kosli web app for your region:

    - EU: [app.kosli.com](https://app.kosli.com)
    - US: [app.us.kosli.com](https://app.us.kosli.com)
  </Step>
  <Step title="Choose GitHub">
    Select **Continue with GitHub** on the sign-in page. GitHub asks you to authorize Kosli the
    first time you sign in.
  </Step>
  <Step title="Return to Kosli">
    Once GitHub confirms the authorization, you are signed in to Kosli.
  </Step>
</Steps>

## GitHub IP allow lists

If your GitHub organization or enterprise restricts access with an
[IP allow list](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization),
GitHub sign-in to Kosli fails until Kosli's sign-in traffic is allowed.

Kosli uses [Descope](https://www.descope.com/) as its identity provider. After you authorize Kosli in
GitHub, Descope calls GitHub from a fixed set of IP addresses to complete the sign-in. GitHub rejects
those calls unless the addresses are on your allow list.

Add the addresses for the Kosli instance you sign in to. Only one set is needed.

### app.kosli.com (EU)

- `3.72.207.40`
- `3.74.59.88`
- `3.121.31.67`

### app.us.kosli.com (US)

- `35.170.24.133`
- `3.212.215.29`
- `52.44.167.251`

<Info>
These are Descope's **Project Static IPs**. Descope publishes the current list at
[Public static IPs](https://docs.descope.com/how-to-deploy-to-production/public-static-ips). If sign-in
stops working after you have added the addresses above, check that page for changes.
</Info>
