---
title: "kosli tag"
description: "Tag a resource in Kosli with key-value pairs.  "
---

## Synopsis

```shell
kosli tag RESOURCE-TYPE [RESOURCE-ID] [flags]
```

Tag a resource in Kosli with key-value pairs.  
use --set to add or update tags, and --unset to remove tags.

Valid resource types are: flow, flows, env, environment, environments, control, controls, repo, repos.

Repos are identified by their name. If multiple repos share the same name
across VCS providers, use --provider to disambiguate, or tag the repo
unambiguously by its internal ID with --repo-id (see: kosli get repo).
Note: in dry-run mode the repo name is not resolved to its internal ID
(no request is made to Kosli), so the previewed request URL contains the
name as-is, whereas a real run sends the resolved ID.


## Flags
| Flag | Description |
| :--- | :--- |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-h`, `--help`  |  help for tag  |
|        `--provider` string  |  [optional] The VCS provider of the repo (e.g. github, gitlab). Only valid when tagging repos; required when multiple repos share the same name across providers.  |
|        `--repo-id` string  |  [optional] The repo's internal ID (see: kosli get repo). Only valid when tagging repos; replaces the RESOURCE-ID argument and identifies the repo unambiguously.  |
|    `-s`, `--set` stringToString  |  [optional] The key-value pairs to tag the resource with. The format is: key=value  |
|    `-u`, `--unset` strings  |  [optional] The list of tag keys to remove from the resource.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    `-a`, `--api-token` string  |  The Kosli API token.  |
|    `-c`, `--config-file` string  |  [optional] The Kosli config file path. (default "kosli")  |
|        `--debug`  |  [optional] Print debug logs to stdout.  |
|    `-H`, `--host` string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        `--http-proxy` string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port`  |
|    `-r`, `--max-api-retries` int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        `--org` string  |  The Kosli organization.  |
|    `-q`, `--quiet`  |  [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins.  |


## Live Examples in different CI systems

<Tabs>
	<Tab title="GitHub">
	View an example of the `kosli tag` command in GitHub.

	In [this YAML file](https://github.com/cyber-dojo/aws-prod-co-promotion/blob/d7e31ce0207b766140ae689f38625da4374acf87/.github/workflows/promote_one.yml#L73)
	</Tab>
	<Tab title="GitLab">
	View an example of the `kosli tag` command in GitLab.

	In [this YAML file](https://gitlab.com/cyber-dojo/creator/-/blob/42876c4da26ee74e4bbfe14c2949cc7cb2d3345e/.gitlab/workflows/main.yml#L55)
	</Tab>
</Tabs>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="add/update tags to a flow">
```shell
kosli tag flow yourFlowName 
	--set key1=value1 
	--set key2=value2 

```
</Accordion>
<Accordion title="tag an environment">
```shell
kosli tag env yourEnvironmentName 
	--set key1=value1 
	--set key2=value2 

```
</Accordion>
<Accordion title="add/update tags to an environment">
```shell
kosli tag env yourEnvironmentName 
	--set key1=value1 
	--set key2=value2 

```
</Accordion>
<Accordion title="remove tags from an environment">
```shell
kosli tag env yourEnvironmentName 
	--unset key1=value1 

```
</Accordion>
<Accordion title="tag a control">
```shell
kosli tag control yourControlIdentifier 
	--set key1=value1 

```
</Accordion>
<Accordion title="tag a repo">
```shell
kosli tag repo yourOrg/yourRepoName 
	--set key1=value1 

```
</Accordion>
<Accordion title="tag a repo whose name exists across multiple VCS providers">
```shell
kosli tag repo yourOrg/yourRepoName 
	--provider github 
	--set key1=value1 

```
</Accordion>
<Accordion title="tag a repo by its internal ID (see: kosli get repo)">
```shell
kosli tag repo --repo-id yourRepoID 
	--set key1=value1 
```
</Accordion>
</AccordionGroup>

