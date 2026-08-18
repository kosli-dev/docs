---
title: "kosli snapshot paths"
description: "Report a snapshot of artifacts running in specific filesystem paths to Kosli.  "
---

## Synopsis

```shell
kosli snapshot paths ENVIRONMENT-NAME [flags]
```

Report a snapshot of artifacts running in specific filesystem paths to Kosli.  
You can report directory or file artifacts in one or more filesystem paths. 
Artifacts names and the paths to include and exclude when fingerprinting them can be 
defined in a paths file which can be provided using `--paths-file`.

Paths files can be in YAML, JSON or TOML formats.
They specify a list of artifacts to fingerprint. For each artifact, the file specifies a base path to look for the artifact in 
and (optionally) a list of paths to exclude. Excluded paths are relative to the artifact path(s) and can be literal paths or
glob patterns.  
The supported glob pattern syntax is documented here: https://pkg.go.dev/path/filepath#Match ,
plus the ability to use recursive globs "**"

To specify paths in a directory artifact that should always be excluded from the SHA256 calculation, you can add a `.kosli_ignore` file to the root of the artifact.
Each line should specify a relative path or path glob to be ignored. You can include comments in this file, using `#`.
The `.kosli_ignore` will be treated as part of the artifact like any other file, unless it is explicitly ignored itself.

This is an example YAML paths spec file:
```yaml
version: 1
artifacts:
  artifact_name_a:
    path: dir1
    exclude: [subdir1, **/log]
```

## Flags
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-D`, `--dry-run` | bool | [optional] Run in dry-run mode. When enabled, no data is sent to Kosli and the CLI exits with 0 exit code regardless of any errors. |
| `-h`, `--help` | bool | help for paths |
| `--paths-file` | string | The path to a paths file in YAML/JSON/TOML format. Cannot be used together with `--path` . |
| `--watch` | bool | [optional] Watch the filesystem for changes and report snapshots of artifacts running in specific filesystem paths to Kosli. |


## Flags inherited from parent commands
| Flag | Type | Description |
| :--- | :--- | :--- |
| `-a`, `--api-token` | string | The Kosli API token. |
| `-A`, `--auto-environment` | bool | [optional] Create the environment (with the type inferred from the snapshot subcommand) if it does not already exist, before reporting the snapshot. |
| `-c`, `--config-file` | string | [optional] The Kosli config file path. (default "kosli") |
| `--debug` | bool | [optional] Print debug logs to stdout. |
| `--environment-description` | string | [optional] The environment description. |
| `--exclude-scaling` | bool | [optional] Exclude scaling events for snapshots. Snapshots with scaling changes will not result in new environment records. (DEPRECATED: this flag is deprecated and will be removed in a future version. Scaling events do not trigger new snapshots.) |
| `-H`, `--host` | string | [defaulted] The Kosli endpoint. (default "https://app.kosli.com") |
| `--http-proxy` | string | [optional] The HTTP proxy URL including protocol and port number. e.g. `http://proxy-server-ip:proxy-port` |
| `--include-scaling` | bool | [optional] Include scaling events for snapshots. Snapshots with scaling changes will result in new environment records. (DEPRECATED: this flag is deprecated and will be removed in a future version. Scaling events do not trigger new snapshots.) |
| `-r`, `--max-api-retries` | int | [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3) |
| `--org` | string | The Kosli organization. |
| `-q`, `--quiet` | bool | [optional] Suppress non-critical warning messages. Errors and normal output are not affected. If both `--quiet` and `--debug` are set, `--debug` wins. |


## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="report one or more artifacts running in a filesystem using a path spec file">
```shell
kosli snapshot paths yourEnvironmentName 
	--paths-file path/to/your/paths/file 
```
</Accordion>
</AccordionGroup>

