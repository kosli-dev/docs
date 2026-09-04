---
title: Automated user provisioning
description: "Learn about configuring automated user provisioning (SCIM) with Kosli."
---

Kosli supports SCIM provisioning and deprovisioning of users. This feature allows users to be added to Kosli by assigning them to the Kosli application within your Identity Provider (IdP). This section explains how to get started.

## Benefits

User provisioning within your IdP simplifies the process of granting access to Kosli; you no longer need to explicitly invite people one-by-one. Your existing processes and procedures for onboarding team members can now be leveraged to give access to the Kosli platform.

User deprovisioning within your IdP means that when your people no longer need access to Kosli, for example because they have changed roles or left your organization, they are automatically revoked from Kosli.

## Setup

To get started with SCIM provisioning, the team managing your [single sign-on](/administration/authentication/single_sign_on) and IdP will need to configure the connection between your IdP and Kosli's auth provider. Different IdPs require different configuration, so Kosli's Customer Success team will provide you a link to the setup wizard with step-by-step instructions, which you can pass on to the relevant team.

On the first screen, select the **SCIM Configuration** box to get started (note that you do not need to make any changes to the existing SSO Configuration):

<Frame>
  <img src="/images/administration/scim-setup-wizard.png" alt="Start page for the SSO and SCIM setup suite wizard" />
</Frame>

The setup wizard then has a step-by-step guide, with screenshots, showing how to set up and configure the application.

When that is all done, and you have added your users to the relevant groups inside your IdP and triggered a provisioning cycle, any changes to your users within the IdP will be reflected within Kosli.

## Timeliness

Once changes within your IdP have been synced, they are typically reflected in Kosli within five minutes.

## Existing Kosli users

People who already have access to Kosli via SSO will retain their access, but will be automatically managed by SCIM once they have been provisioned through the IdP.

## Roles for new and existing users

Kosli now allows handling role assignment through your IdP, so that users' [roles within Kosli](/administration/managing_users/roles_in_kosli) can be managed by your onboarding and IT teams, without requiring admin access to Kosli.

You will need to tell us which of your Kosli organizations you wish to have SCIM enabled for; we will then create the necessary roles within our auth provider. Each organization will have four roles, with the names `kosli-<org-name>-<role>`, to correspond to the available roles in Kosli (admin, member, snapshotter, reader).

Within your IdP you will need to create a group for each of these roles. You will then add your users to the groups corresponding to the organizations/roles you wish them to have in Kosli. If a member receives two different roles for the same organization, the highest-privilege role will be assigned.

<Note>
Once a user has been provisioned through SCIM, the IdP is authoritative and will override that user's pre-existing organization memberships/roles within Kosli.
</Note>

Within the **SSO Configuration** wizard (not the SCIM wizard this time), go to the **Group Attribute Mapping** tab and follow the instructions. Ensure you correctly map each of your IdP groups to the corresponding role.

When you have finished the group mapping, you can click through to the **Testing** page and save the configuration.

<Frame>
  <img src="/images/administration/scim-group-role-mapping.png" alt="Section in the SSO Setup Suite Wizard showing how to configure mapping of IdP groups to Kosli roles" />
</Frame>
