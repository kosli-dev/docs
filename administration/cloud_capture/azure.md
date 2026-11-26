---
title: "Cloud Capture on Azure"
sidebarTitle: "Azure"
description: "Set up Cloud Capture for your Azure subscriptions, choose which resource groups it snapshots, and review the access it uses."
tag: "BETA"
---

<Warning>
Cloud Capture is still in active development. Its capabilities and configuration format may change, and onboarding is done together with Kosli's Customer Success team.
</Warning>

Cloud Capture snapshots the running container-based web apps in Azure App Service, in the subscriptions you register. Azure support is in early access, so the Azure page appears in your Cloud Capture settings only once Kosli has enabled it for your organization.

## Set up

Nothing is deployed in Azure. Cloud Capture reads a subscription as a Kosli application registered in Microsoft Entra, which you consent to in your tenant and then grant read access on each subscription.

<Steps>
  <Step title="Consent to the Kosli application">
    In your organization's **Settings**, go to **Cloud Capture**, open **Azure** and select **Register account**. Follow the **Consent in Azure** link as a Global Administrator of your tenant. Consenting creates the application's service principal in your tenant; it has no access until you grant it some in the next step.
  </Step>
  <Step title="Grant access and tag the subscription">
    The registration form shows three Azure CLI commands with your values filled in. Run them as an owner of the subscription:

    ```bash
    az role assignment create --assignee "<kosli-application-id>" --role Reader --scope "/subscriptions/<subscription-id>"
    az role assignment create --assignee "<kosli-application-id>" --role AcrPull --scope "/subscriptions/<subscription-id>"
    az tag update --resource-id "/subscriptions/<subscription-id>" --operation Merge --tags kosli-external-id="<your-external-id>"
    ```

    `Reader` lets Cloud Capture list the App Service sites and read tags, and `AcrPull` lets it fingerprint their container images. The `kosli-external-id` tag is how Cloud Capture checks the subscription is yours to read: it refuses to list a subscription whose tag does not carry your organization's external ID.
  </Step>
  <Step title="Register the subscription">
    Accounts can only be registered while Cloud Capture is enabled. When you have consented to the application, granted it access and tagged the subscription, enter the **Tenant ID** and **Subscription ID** in the same registration form and save it. Register each subscription you want scanned.

    Azure has no regions to choose: Cloud Capture scans the whole subscription and reports each resource group that holds running container-based web apps into its own environment.

    Cloud Capture scans every five minutes unless you [choose another frequency](/administration/cloud_capture/getting_started#scan-frequency), and picks up a registered subscription the next time it runs - you should see environments and snapshots appearing within a few minutes.
  </Step>
</Steps>

## Excluding resources

Exclude resources by tagging the resource group that holds them. In your organization's **Settings**, go to **Cloud Capture**, open **Azure** and add the tag to the **Skip tags** panel in the Azure defaults. Cloud Capture skips every resource group that carries one of the tags, with all of the web apps in it; tags on an individual web app are not read.

Key and value must both match the resource group's tag exactly. Through the API, the tags are the `azure` list of `skip_tags`; see [Using the API](/administration/cloud_capture/getting_started#using-the-api).

## Permissions and security

For the model that is common to every cloud, see [Cloud Capture security](/administration/cloud_capture/security).

Nothing is deployed in your Azure tenant. Kosli registers one multi-tenant application in Microsoft Entra, and Cloud Capture reads your subscription as that application. The application's credentials are Kosli's own and never leave Kosli. Access is granted in three steps, each of which you control:

1. **Consent.** A Global Administrator of your tenant consents to the Kosli application, which creates its service principal in your tenant. Consent alone grants no access to any subscription.
2. **Role assignments.** You assign the application two built-in roles on each subscription you want scanned:

   | Role | What Cloud Capture uses it for |
   |---|---|
   | `Reader` | Listing the App Service sites in the subscription, and reading resource group tags and the subscription's own tags |
   | `AcrPull` | Fingerprinting the container images of your web apps from your container registries |

3. **A tag on the subscription.** You tag the subscription `kosli-external-id` with your organization's external ID. Cloud Capture refuses to list a subscription whose tag does not match the external ID of the organization it is working for.

The registration form in the Kosli UI shows the consent link and the three Azure CLI commands with your values filled in; see [Set up](#set-up).

To withdraw access, remove the role assignments or the tag from the subscription, or delete the application's service principal from your tenant, and remove the subscription from your registered accounts in Kosli.

### Tenant isolation

* The Kosli application's credentials are held by Kosli and are not readable by the part of Cloud
  Capture that plans work, only by the workers that carry it out.
* Before a worker lists anything in a subscription, it reads the subscription's `kosli-external-id`
  tag and compares it with the external ID of the organization the job is for. Only someone with
  write access to your subscription can set that tag, so another Kosli tenant that registered your
  subscription ID would be refused.
* The application has access only to the subscriptions on which you assigned it a role.
