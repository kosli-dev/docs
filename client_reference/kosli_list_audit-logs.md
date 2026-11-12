---
title: "kosli list audit-logs"
description: "List audit log events for an org."
---

## Synopsis

```shell
kosli list audit-logs [flags]
```

List audit log events for an org.
Each event records a change to an org member's role: a member being added, changing role, or being removed.
Listing the audit log requires org admin rights.
The list can be filtered by user, event type, role and source. When multiple filters are provided, only events matching all of them are returned.
The results are paginated and ordered from latest to oldest by default; use --page and --page-limit to navigate the pages.

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `--event-type` | string | [optional] Only list events of this type. Valid values are: [added, changed, removed]. |
| `-h`, `--help` | bool | help for audit-logs |
| `-o`, `--output` | string | [defaulted] The format of the output. Valid formats are: [table, json]. (default "table") |
| `--page` | int | [defaulted] The page number of a response. (default 1) |
| `-n`, `--page-limit` | int | [defaulted] The number of elements per page. (default 15) |
| `--role` | stringArray | [optional] Only list events that set this role. Can be repeated to match more than one role. |
| `--search` | string | [optional] Only list events where the affected user's or the acting user's name contains this substring (case-insensitive). |
| `--sort-by` | string | [optional] The column to sort events by. Valid values are: [when, user, role, changed_by, source]. (defaults to when) |
| `--sort-direction` | string | [optional] The direction to sort events in. Valid values are: [asc, desc]. (defaults to desc) |
| `--source` | stringArray | [optional] Only list events from this source (e.g. app, scim, invitation, script). Can be repeated to match more than one source. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. Config is read from this path or the default only, never implicitly from the current directory. (default "$HOME/.kosli.yml") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="list the first page of audit log events for an org">
```shell
kosli list audit-logs 

```
</Accordion>
<Accordion title="list the second page of audit log events (30 per page)">
```shell
kosli list audit-logs 
	--page 2 
	--page-limit 30 

```
</Accordion>
<Accordion title="list audit log events in JSON">
```shell
kosli list audit-logs 
	--output json 

```
</Accordion>
<Accordion title="list the role changes that affected or were made by users whose name contains 'alice'">
```shell
kosli list audit-logs 
	--search alice 
	--event-type changed 

```
</Accordion>
<Accordion title="list the events that made someone an admin or a member through SCIM (--role and --source can be repeated)">
```shell
kosli list audit-logs 
	--role admin 
	--role member 
	--source scim 

```
</Accordion>
<Accordion title="list audit log events sorted by user name in ascending order">
```shell
kosli list audit-logs 
	--sort-by user 
	--sort-direction asc 
```
</Accordion>
</AccordionGroup>

