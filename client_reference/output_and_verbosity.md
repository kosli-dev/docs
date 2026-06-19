---
title: "Output and verbosity"
description: "How the Kosli CLI writes output, what warnings mean, and how to control verbosity."
---

This page explains where the Kosli CLI writes its output, what `[warning]` messages mean, and how to control verbosity in scripts and CI/CD pipelines.

## Where output goes

The CLI splits its output across two streams:

- **stdout** — Command results: created object IDs, JSON, tables, and any value intended to be piped or captured.
- **stderr** — Warnings, debug lines, and the "new version available" update notice.

The **exit code** is the authoritative success or failure signal. A non-zero exit code means the command failed; zero means it succeeded, regardless of what appeared on stderr.

## Warning messages

Warnings are written in the form `[warning] <message>` and indicate a non-fatal condition that the CLI worked around. Examples:

```text
[warning] failed to get git repo info. <details>
[warning] Repo URL will not be reported, <details>
[warning] failed to remove evidence file <path>: <details>
```

Warnings:

- Are always written to **stderr**.
- **Never** affect the exit code.
- Are not errors — the command completed successfully.

If you see a warning in a pipeline that you have already validated end-to-end, it is safe to suppress it (see below). If a warning is new or unexpected, read the message and address the underlying cause.

## Verbosity controls

| Flag | Effect |
|---|---|
| _(default)_ | Errors and `[warning]` lines to stderr. Results to stdout. |
| `-q`, `--quiet` | Suppresses `[warning]` lines. Errors still print. |
| `--debug` | Adds `[debug]` lines to stderr. Overrides `--quiet`. |
| `--debug=false` | Explicit-off form. Useful when a parent process or env var has enabled debug and you want to disable it for one command. |

When both `--quiet` and `--debug` are set, `--debug` wins and a debug notice is printed explaining the override.

Both flags have equivalent environment variables, following the standard `KOSLI_` prefix:

- `KOSLI_QUIET=true`
- `KOSLI_DEBUG=true`

## Warnings in CI/CD pipelines

CI systems including Jenkins, Azure DevOps, Bitbucket Pipelines, and GitHub Actions multiplex stdout and stderr into a single build log. Some render stderr lines in red or with error-level styling. This makes non-fatal `[warning]` lines look alarming to pipeline reviewers even though they have no effect on the build.

Once you have validated a workflow end-to-end, add `--quiet` (or set `KOSLI_QUIET=true`) to the Kosli CLI invocations to keep build logs clean:

```shell
kosli attest generic --quiet ...
```

<Warning>
Avoid redirecting all of stderr to `/dev/null` (for example, `kosli ... 2>/dev/null`). That hides genuine error messages and makes failures much harder to diagnose. Prefer `--quiet`, which suppresses only `[warning]` lines and keeps real errors visible.
</Warning>

If you are capturing CLI output in a shell subshell and seeing debug or warning lines mixed into the captured value, see [CLI in subshell captures stderr](/troubleshooting/subshell_stderr).

## See also

- [kosli root command and global flags](/client_reference/kosli)
- [CLI in subshell captures stderr](/troubleshooting/subshell_stderr)
