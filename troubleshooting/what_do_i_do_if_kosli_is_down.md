---
title: "What do I do if Kosli is down?"
description: "This page shows you how to bypass Kosli attestations if Kosli is down so your CI pipelines keep running, and how to re-enable them when it recovers."
---

## Status of Kosli services <iframe src="https://status.app.kosli.com/badge" width="250" height="30" scrolling="no"/>


<script src="https://uptime.betterstack.com/widgets/announcement.js" data-id="212616" async="async" type="text/javascript"></script>

You can also check the current status of Kosli services by running `kosli status` in the CLI.

## Turning Kosli CLI calls on and off instantly

If the `KOSLI_DRY_RUN` environment variable is set to `true` then all Kosli CLI commands will:
* Not communicate with Kosli at all
* Print the payload they would have sent
* Exit with a zero status code

We recommend creating an Org-level KOSLI_DRY_RUN variable in your CI system and, in all CI workflows,
ensuring there is an environment variable set from it.

For example, in a [Github Action workflow](https://github.com/cyber-dojo/differ/blob/main/.github/workflows/main.yml):

```yaml
name: Main
...
env:
  KOSLI_DRY_RUN: ${{ vars.KOSLI_DRY_RUN }}           # true iff Kosli is down
```

## Turning Kosli API calls on and off instantly

If you are using the Kosli API in your workflows (e.g. using `curl`), we recommend using the same Org-level `KOSLI_DRY_RUN`
environment variable and guarding the `curl` call with a simple if statement. For example:

```shell
#!/usr/bin/env bash

kosli_curl()
{
  local URL="${1}"
  local JSON_PAYLOAD="${2}"

  if [ "${KOSLI_DRY_RUN:-}" == "true" ]; then
    echo KOSLI_DRY_RUN is set to true. This is the payload that would have been sent
    echo "${JSON_PAYLOAD}" | jq .
  else
    curl ... --data="${JSON_PAYLOAD}" "${URL}"
  fi
}
```
