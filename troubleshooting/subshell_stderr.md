---
title: "CLI in subshell captures stderr"
description: "How to handle Kosli CLI debug output being captured in subshell variables in CI workflows."
---

## Error

When capturing Kosli CLI output in a subshell variable in CI, the variable contains debug output mixed with the expected value:

```shell
DIGEST="$(kosli fingerprint "${IMAGE_NAME}" --artifact-type=docker)"

echo "DIGEST=${DIGEST}"
DIGEST=[debug] calculated fingerprint: 2c6079df5829...
2c6079df58292ed10e8074adcb74be549b7f841a1bd8266f06bb5c518643193e
```

## Solution

Explicitly set `--debug=false` when running Kosli CLI commands in a subshell:

```shell
DIGEST="$(kosli fingerprint "${IMAGE_NAME}" --artifact-type=docker --debug=false)"
```

## Context

The Kosli CLI writes debug information to `stderr` and all other output to `stdout`. In a local terminal, a `$(subshell)` captures only `stdout`. However, in many CI workflows (including GitHub and GitLab), `stdout` and `stderr` are multiplexed together, causing debug output to leak into captured variables.
