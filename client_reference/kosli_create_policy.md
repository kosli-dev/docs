---
title: "kosli create policy"
description: "Create or update a Kosli policy."
---
## Synopsis

```shell
kosli create policy POLICY-NAME POLICY-FILE-PATH [flags]
```

Updating policy content creates a new version of the policy.

## Flags
| Flag | Description |
| :--- | :--- |
|        --comment string  |  [optional] comment about the change made in a policy file when updating a policy.  |
|        --description string  |  [optional] policy description.  |
|    -D, --dry-run  |  [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors.  |
|    -h, --help  |  help for policy  |
|        --type string  |  [defaulted] the type of policy. One of: [env] (default "env")  |

## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag /faq/#boolean-flags (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. 'http://proxy-server-ip:proxy-port'  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
	<Accordion title="create a Kosli policy">

	
	```shell
	kosli create policy yourPolicyName yourPolicyFile.yml 
		--description yourPolicyDescription 
		--type env 
	
	```
	
	</Accordion>
	<Accordion title="update a Kosli policy">

	
	```shell
	kosli create policy yourPolicyName yourPolicyFile.yml 
		--description yourPolicyDescription 
		--type env 
		--comment yourChangeComment 
	```
	
	
	</Accordion>
</AccordionGroup>
