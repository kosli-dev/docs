---
title: "Path/Image name is a single whitespace character"
description: "How to fix the whitespace path error when using multi-line Kosli CLI commands."
---

## Error

```
Error: failed to calculate artifact fingerprint: stat  : no such file or directory. The directory path is ' '.
```

## Solution

Check your multi-line command for extraneous whitespace after line-continuation backslashes (`\`). Remove any spaces or tabs after the `\` on each line.

## Context

When using multi-line commands, whitespace added after a line-continuation backslash is interpreted as the artifact path or image name argument.
