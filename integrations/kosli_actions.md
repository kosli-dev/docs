---
title: Kosli Actions
description: Automate if-this-then-that workflows with Kosli Actions.
---

<Note>
You need the Admin or Member role to create, update, and delete Actions.

Learn more about roles in Kosli in [Roles in Kosli](/administration/managing_users/roles_in_kosli/).
</Note>

Actions enable you to automate the execution of if-this-do-that workflows based on Kosli events. You can configure actions to either receive a Slack notification or a JSON payload on a custom webhook when certain Kosli events happen.

You can configure actions to be triggered by one or more of the following events occurring in one or more environments. The first column is the name shown in the Kosli UI. The second column is the value to use in the [API](/api-reference/actions/create-or-update-environment-action) and in the [Terraform provider](/terraform-reference/resources/action).

| Trigger (UI) | API value | Fires when |
|---|---|---|
| Artifact Start | `ON_STARTED_ARTIFACT` | An artifact starts running in the environment. |
| Artifact Stop | `ON_EXITED_ARTIFACT` | An artifact stops running in the environment. |
| Artifact changed | `ON_SCALED_ARTIFACT` | An artifact that is already running becomes compliant or non-compliant, or new provenance is recorded for it (for example, an attestation arrives after the artifact was deployed). It does **not** fire for new deployments; use Artifact Start for that. |
| Artifact allow-listing | `ON_ALLOWED_ARTIFACT` | An artifact is added to the allow-list in the environment. |
| Environment becomes compliant | `ON_COMPLIANT_ENV` | The environment changes from <Badge color="red">Non-Compliant</Badge> to <Badge color="green">Compliant</Badge>. |
| Environment becomes non-compliant | `ON_NON_COMPLIANT_ENV` | The environment changes from <Badge color="green">Compliant</Badge> to <Badge color="red">Non-Compliant</Badge>. |

<Note>
`ON_SCALED_ARTIFACT` keeps its historical name for API compatibility. Kosli no longer records instance scaling events, so this trigger never fires because of a change in replica count.
</Note>


## Slack Notifications

To receive Kosli notifications in Slack, you have two options. You can either use the Kosli Slack App or set up Slack Incoming Webhooks. Both approaches allow you to configure Kosli notifications in Slack, offering flexibility based on your preferences.

<Card title="Kosli Slack App (recommended)" icon="slack">
    Subscribe to Kosli notifications using the [Kosli Slack App](/integrations/slack/). This method is recommended for a seamless integration.
    Use the app to create notification settings by running the `/kosli subscribe` slash command.
</Card>
<Card title="Slack Incoming Webhooks" icon="webhook">
    - Create a [Slack incoming webhook](https://api.slack.com/messaging/webhooks#create_a_webhook).
    - Use this webhook to [create a notification settings in the Kosli UI](/integrations/kosli_actions/#manage-actions-in-the-ui).
</Card>

## Custom Webhook Notifications

Custom webhook notifications empower you to implement automation workflows for "if-this-then-that" scenarios. Whenever an event that matches your specified notification settings occurs, a JSON payload, as outlined below, is transmitted to your designated custom webhook:

```json
{
    "version": "1.0",
    "timestamp": "1692616493",
    "org": "cyber-dojo",
    "environment": "aws-prod",
    "event_type": "STARTED_ARTIFACT",
    "description": "1 instance started running (from 0 to 1)",
    "snapshot":  {
           "index": "1035",
           "status": "compliant",
           "html_url": "https://app.kosli.com/cyber-dojo/environments/aws-prod/snapshots/1035",
           "api_url": "https://app.kosli.com/api/v2/snapshots/cyber-dojo/aws-prod/1035"
     },
    "artifact": {
        "name": "runner",
        "fingerprint": "719defb995c86ad7c406ad74258fe98b9ebd71dfa80cd786870c967cb6c1f08d",
        "provenance": {
            "flow": "runner",
            "status": "compliant",
            "commit": "1ac157003dd6fb9ec764daa47726b7bfed65c312",
            "commit_url": "https://github.com/cyber-dojo/runner/commit/1ac157003dd6fb9ec764daa47726b7bfed65c312",
            "html_url": "https://app.kosli.com/cyber-dojo/runner/719defb995c86ad7c406ad74258fe98b9ebd71dfa80cd786870c967cb6c1f08d",
            "api_url": "https://app.kosli.com/api/v2/artifacts/cyber-dojo/runner/fingerprint/719defb995c86ad7c406ad74258fe98b9ebd71dfa80cd786870c967cb6c1f08d",
            "build_url": "https://github.com/cyber-dojo/runner/actions/runs/5891969166"
        }
    }
}
```

`event_type` is the trigger's API value without the `ON_` prefix: `STARTED_ARTIFACT`, `EXITED_ARTIFACT`, `SCALED_ARTIFACT`, `ALLOWED_ARTIFACT`, `COMPLIANT_ENV`, or `NON_COMPLIANT_ENV`. For `SCALED_ARTIFACT`, the `description` field says which change occurred: the artifact became compliant, became non-compliant, or had new provenance recorded.

## Email

Provide a comma-separated list of recipient email addresses. Notifications are sent from `noreply@kosli.com`.


# Manage Actions in the UI

You can manage Actions for your organization in the Kosli UI from the `Actions` section in the left navigation menu. The Actions sections enables you to:
- **Create Notifications:** Create a new notifications settings.
- **Delete Notifications:** Remove existing notification settings that are no longer needed.
- **Update Notifications:** Modify notification settings as needed.
