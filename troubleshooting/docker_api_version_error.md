---
title: "Docker API version error in GitHub Actions"
description: 'How to fix the "client version is too new" error when running the Kosli CLI with Docker operations.'
---

## Error

```
Error response from daemon: client version 1.47 is too new. Maximum supported API version is 1.45
```

<Info>
**Kosli CLI v2.15.1+:** This error is resolved automatically. The CLI now negotiates the Docker API version with the daemon, so it adapts to whatever Docker Engine version is available. Upgrade to v2.15.1 or later and no workaround is needed.
</Info>

## Solution for CLI versions before v2.15.1

Set the `DOCKER_API_VERSION` environment variable in your workflow:

```yaml
env:
  DOCKER_API_VERSION: "1.45"
```

## Context

Prior to v2.15.1, the Kosli CLI defaulted to a fixed Docker API version (e.g., 1.47), which could be higher than what the Docker daemon on the host supports. This caused Docker operations (`--artifact-type docker`) to fail with a "client version is too new" error.

From v2.15.1 onwards, the CLI automatically negotiates the API version with the Docker daemon, eliminating this issue.
