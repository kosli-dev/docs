---
title: Automated user provisioning
description: "Learn about configuring automated user provisioning (SCIM) with Kosli."
---

Kosli supports SCIM provisioning and deprovisioning of users. This feature allows users to be added to Kosli by assigning them to the Kosli application within your Identity Provider (IdP). This page explains how to get started.

## Benefits

User provisioning within your IdP simplifies the process of granting access to Kosli; you no longer need to explicitly invite people one-by-one. Your existing processes and procedures for onboarding team members can now be leveraged to give access to the Kosli platform.

User deprovisioning within your IdP means that when your people no longer need access to Kosli, for example because they have changed roles or left your organization, their access to Kosli is revoked automatically.

## Prerequisites

Before configuring SCIM, make sure that:

- **[Single sign-on](/administration/authentication/single_sign_on) is already configured.** SCIM builds on your
  existing SSO connection, and IdP groups are mapped to Kosli roles in the SSO part of the same wizard.
- **SCIM is enabled for your Kosli organizations.** Tell your Kosli Customer Success representative which
  organizations you want SCIM for, so that the matching roles can be created — see
  [Roles for new and existing users](#roles-for-new-and-existing-users) below.
- **You have a link to the setup wizard.** Your Customer Success representative provides one with instructions
  for your IdP, which you can pass on to the team that will do the work.
- **That team can administer your IdP.** They need permissions to create or modify application registrations,
  and to manage the groups you map to Kosli roles.

## Setup

The team that manages your IdP configures the connection between your IdP and Kosli's auth provider. Because
different IdPs need different configuration, the wizard gives step-by-step instructions specific to yours.

<Note>
Adding SCIM does not normally require any change to your existing SSO connection. The exception is Okta over
OIDC: Okta's SCIM integration only works with a SAML connection, so an Okta OIDC connection has to be recreated
using SAML before SCIM can be enabled. If you are not sure which your IdP uses, ask your Kosli Customer Success
representative.
</Note>

On the first screen, select the **SCIM Configuration** box to get started:

<Frame>
  <img src="/images/administration/scim-setup-wizard.png" alt="Start page for the SSO and SCIM setup suite wizard" />
</Frame>

The setup wizard then has a step-by-step guide, with screenshots, showing how to set up and configure the application.

When that is all done, and you have added your users to the relevant groups inside your IdP and triggered a provisioning cycle, any changes to your users within the IdP will be reflected within Kosli.

## Timeliness

Once changes within your IdP have been synced, they are typically reflected in Kosli within five minutes.

## Existing Kosli users

People who already have access to Kosli via SSO keep that access. Enabling SCIM does not, by itself, change
anyone's roles or organization memberships — nothing in Kosli moves until your IdP sends a change.

From then on, your IdP drives membership. Once a user has been provisioned through SCIM, the groups they belong
to in your IdP determine their organizations and roles in Kosli, replacing whatever they had before.

That makes the first sync worth planning. A full or forced sync in your IdP — however it is labeled there —
provisions every assigned user at once, not only the ones you have just changed, so make sure your groups and
[role mappings](#map-your-idp-groups-to-kosli-roles) are correct before you trigger one.

## Roles for new and existing users

Kosli supports role assignment through your IdP, so that users' [roles within Kosli](/administration/managing_users/roles_in_kosli) can be managed by your onboarding and IT teams, without requiring admin access to Kosli.

You will need to tell us which of your Kosli organizations you wish to have SCIM enabled for; we will then create the necessary roles within our auth provider. Each organization will have four roles, with the names `kosli-<org-name>-<role>`, to correspond to the available roles in Kosli (admin, member, snapshotter, reader).

Within your IdP you will need to create a group for each of these roles. You will then add your users to the groups corresponding to the organizations/roles you wish them to have in Kosli. If a member receives two different roles for the same organization, the highest-privilege role will be assigned.

### Map your IdP groups to Kosli roles

Within the **SSO Configuration** wizard (not the SCIM wizard this time), go to the **Group Attribute Mapping** tab and follow the instructions. Ensure you correctly map each of your IdP groups to the corresponding role.

<Frame>
  <img src="/images/administration/scim-group-role-mapping.png" alt="Section in the SSO Setup Suite Wizard showing how to configure mapping of IdP groups to Kosli roles" />
</Frame>

When you have finished the group mapping, you can click through to the **Testing** page and save the configuration.

<Note>
Once a user has been provisioned through SCIM, your IdP is authoritative for that user: their roles can no
longer be changed in Kosli, so every later role change has to be made through their IdP group membership.
</Note>
