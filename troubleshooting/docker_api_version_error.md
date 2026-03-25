---
title: "Docker API version error in GitHub Actions"
description: 'How to fix the "client version 1.47 is too new" error when running the Kosli CLI in GitHub Action workflows.'
---

## Error

```
Error response from daemon: client version 1.47 is too new. Maximum supported API version is 1.45
```

## Solution

Set the `DOCKER_API_VERSION` environment variable in your workflow:

```yaml
env:
  DOCKER_API_VERSION: "1.45"
```

## Context

The latest Kosli CLI defaults to Docker API version 1.47, but GitHub Action workflows currently support a maximum of 1.45.
