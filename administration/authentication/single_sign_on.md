---
title: "Single Sign On"
description: "Learn about configuring Single Sign On with Kosli"
icon: "right-to-bracket"
---

Kosli supports signing-in using your identity provider, via Single Sign On (SSO).

## Enabling Single Sign On

When you are ready for your organization to access Kosli using Single Sign On, your IT team will need to configure a new SSO connection. It's done through a self-service setup wizard to make this as straightforward as possible.

Your Kosli Customer Success representative will provide you with a custom direct link to your personalized SSO setup wizard.

## Step by step

Before you begin, you will need access to your Identity Provider (IdP) — such as Azure Entra ID, Okta, or Google Workspace — with permissions to create or modify application registrations and SSO configurations.

<Steps>
  <Step title="Review current status">
    Open the link provided by Kosli. The wizard will display the current state of your SSO connection. If no connection exists yet, you'll see an option to add one.

    <Frame>
      <img src="/images/administration/add-sso.png" alt="The SSO setup wizard welcome screen, showing an SSO Configuration card with an Add button, and grayed-out SSO Mapping and SSO Testing options under Advanced." />
    </Frame>
  </Step>
  <Step title="Select your identity provider">
    Click **+ Add**, then select your IdP from the list (e.g. Okta, Azure Entra ID, Keycloak, Auth0). Select **OIDC** if there is a choice, unless you are using Okta and plan to use SCIM provisioning — in this case, select **SAML**.

    <Frame>
      <img src="/images/administration/select-idp.png" alt="The Identity Provider (IdP) Selection step of the wizard, with a search box and cards for OKTA, Azure Entra ID, Keycloak, and Auth0." />
    </Frame>
  </Step>
  <Step title="Configure the connection">
    The wizard will guide you through the setup process with screenshots specific to your IdP. You'll be asked to copy and paste values between your IdP and the wizard, including:

    - **Client ID** from your IdP's application registration
    - **Client Secret** from your IdP's application registration

    <Frame>
      <img src="/images/administration/sso-setup-suite.png" alt="Step 2 of 6 of the wizard, Identity Provider Information and User Attribute Mapping, with Client ID and Client Secret fields and a screenshot showing where to find those values in Okta." />
    </Frame>
  </Step>
  <Step title="Notify Kosli">
    Once you have completed the SSO configuration in the wizard, please let your Kosli Customer Success representative know. We will then switch your email domain to use SSO and confirm when the migration is complete.
  </Step>
</Steps>
