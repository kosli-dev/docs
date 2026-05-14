---
title: "kosli assert pullrequest azure"
beta: false
deprecated: false
description: "Assert an Azure DevOps pull request for a git commit exists.  "
---

## Synopsis

```shell
kosli assert pullrequest azure [flags]
```

Assert an Azure DevOps pull request for a git commit exists.  
The command exits with non-zero exit code 
if no pull requests were found for the commit.

## Flags
| Flag | Description |
| :--- | :--- |
|        `--azure-org-url` string  |  Azure organization url. E.g. `https://dev.azure.com/myOrg` (defaulted if you are running in Azure Devops pipelines: [docs](/integrations/ci_cd) ).  |
|        `--azure-token` string  |  Azure Personal Access token.  |
|        `--commit` string  |  Git commit for which to find pull request evidence. (defaulted in some CIs: [docs](/integrations/ci_cd) ). (default "HEAD")  |
|    `-D`, `--dry-run`  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    `-h`, `--help`  |  help for azure  |
|        `--project` string  |  Azure project.(defaulted if you are running in Azure Devops pipelines: [docs](/integrations/ci_cd) ).  |
|        `--repository` string  |  Git repository. (defaulted in some CIs: [docs](/integrations/ci_cd) ).  |


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


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

```shell
kosli assert pullrequest azure \
	--azure-token yourAzureToken \
	--azure-org-url yourAzureOrgUrl \
	--commit yourGitCommit \
	--project yourAzureDevopsProject \
	--repository yourAzureDevOpsGitRepository
```

