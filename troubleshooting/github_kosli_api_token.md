---
title: "GitHub can't see KOSLI_API_TOKEN secret"
description: "How to make the KOSLI_API_TOKEN secret available in GitHub Actions workflows."
---

## Error

Kosli CLI commands fail in GitHub Actions because `KOSLI_API_TOKEN` is not set, even though the secret exists in your repository.

## Solution

Add the secret to your workflow's environment variables explicitly:

```yaml
env:
  KOSLI_API_TOKEN: ${{ secrets.kosli_api_token }}
```

## Context

Secrets in GitHub Actions are not automatically exported as environment variables. You must map them explicitly in each workflow or job.
