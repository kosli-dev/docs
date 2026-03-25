---
title: "zsh: no such user or named directory"
description: "How to fix the zsh error when using arguments starting with ~ in Kosli CLI commands."
---

## Error

```shell
kosli list snapshots prod ~3..NOW
```
```plaintext
zsh: no such user or named directory: 3..NOW
```

## Solution

Wrap the argument in quotation marks (single or double):

```shell
kosli list snapshots prod '~3..NOW'
```
or
```shell
kosli list snapshots prod "~3..NOW"
```
