---
title: Review membership changes
description: Use the Audit Log page in Kosli to see who was added to or removed from your organization, how their roles changed, and who made each change.
sidebarTitle: Membership changes
icon: "clock-rotate-left"
---

Kosli records every change to your organization's membership: users being added, removed, re-added, or given a different [role](/administration/managing_users/roles_in_kosli). The **Audit Log** page lets you search and filter that history, so you can answer access reviews and audit questions about Kosli itself.

## Prerequisites

- You are an **Admin** of a shared organization. The **Audit Log** page is not available in personal organizations, and other roles cannot open it.

## Open the Audit Log

1. In Kosli, go to **Settings** and select **User Management**.
2. Select **Audit Log**, below **Invitations**.

The table lists changes newest first, 15 per page. Each row has these columns:

| Column | What it shows |
|--------|---------------|
| **When** | The date and time of the change, in your local time. |
| **User** | The user whose membership changed. |
| **Role change** | What changed: **Added as** a role, **Re-added as** a role, a change from one role to another (for example `member → admin`), or **Removed from organization** with the role they had before. |
| **Changed by** | The user who made the change. For changes made by your identity provider through [SCIM](/administration/managing_users/automated_user_provisioning), this shows **External IDP**. |
| **Source** | Where the change came from: `app` (the Kosli web app), `scim` (your identity provider), `invitation` (a user accepting an invitation), or `script` (a change Kosli applied directly, outside the app). |

Select a column header to sort the whole log by that column. Select it again to reverse the order.

## Search and filter the log

- **Search**: type a name in the **Search by member or actor** box. Kosli matches both the user whose membership changed and the user who made the change.
- **Event**: show only **Added**, **Changed**, or **Removed** events. You can pick one event type at a time.
- **Role**: show only changes that resulted in one or more roles: **Admin**, **Member**, **Snapshotter**, **Reader**, or **Revoked** (users who were removed).
- **Source**: show only changes from one or more sources: **App**, **SCIM**, **Invitation**, or **Script**.
- **Timestamp**: set a **From** date, a **To** date, or both to limit the log to a date range. Dates are whole days in your local time.

Active filters appear above the table. Clear them all at once from there.

The page URL includes your search, filters, and sort order. Bookmark or share the URL to come back to the same view.

## List the log with the CLI

You can read the same history with [`kosli list audit-logs`](/client_reference/kosli_list_audit-logs), for example to export it for an access review. Like the page, the command requires org admin rights. It supports the same search, event, role, and source filters, but not a date range.

```shell
kosli list audit-logs \
  --event-type removed \
  --source scim \
  --output json
```
