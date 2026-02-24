---
title: "Using Kosli CLI with an HTTP proxy"
description: "This tutorial shows you how to set up an HTTP proxy and configure the Kosli CLI to route all traffic through it."
---

In enterprises with strict network policies, all egress traffic to external services must go through an HTTP proxy.
By the end of this tutorial, you will have an HTTP proxy running locally and the Kosli CLI configured to use it.

<Info>
If you already have an HTTP proxy running, skip to [Use the HTTP proxy with Kosli CLI](#use-the-http-proxy-with-kosli-cli).
</Info>

## Prerequisites

* [Install Docker](https://docs.docker.com/engine/install/).
* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).

## Start the HTTP proxy

We will use [Tinyproxy](https://tinyproxy.github.io/) running in Docker as our HTTP proxy.

Create a minimal Tinyproxy configuration and start it:

```shell
cat <<EOF > tinyproxy.conf
User nobody
Group nobody
Port 8888
EOF

docker run -p 8888:8888 -v $(PWD)/tinyproxy.conf:/etc/tinyproxy/tinyproxy.conf:ro kalaksi/tinyproxy
```

You should see Tinyproxy log output in the terminal, confirming it is listening on port 8888.

## Use the HTTP proxy with Kosli CLI

In a new terminal, verify the setup by listing environments from the public `cyber-dojo` demo org:

```shell
kosli list envs --org cyber-dojo --http-proxy http://localhost:8888 --api-token <your-token>
```

Your request is routed through the proxy and forwarded to Kosli. You should see output similar to:

```
NAME                         TYPE  LAST REPORT                LAST MODIFIED              TAGS
aws-beta                     ECS   2024-04-18T15:17:54+02:00  2024-04-18T15:17:54+02:00  [url=https://beta.cyber-dojo.org/]
aws-prod                     ECS   2024-04-18T15:17:57+02:00  2024-04-18T15:17:57+02:00  [url=https://cyber-dojo.org/]
terraform-state-differ-beta  S3    2024-04-18T15:18:23+02:00  2024-04-18T15:18:23+02:00
terraform-state-differ-prod  S3    2024-04-18T15:18:17+02:00  2024-04-18T15:18:17+02:00
```

## Persist the proxy configuration

Rather than passing `--http-proxy` on every command, save it to your Kosli config:

```shell
kosli config --http-proxy=http://localhost:8888
```

All subsequent CLI commands will now route through the proxy automatically.

## What you've accomplished

You have set up Tinyproxy as an HTTP proxy and configured the Kosli CLI to route all traffic through it. This pattern works with any HTTP proxy — replace `http://localhost:8888` with your organisation's proxy URL and run `kosli config --http-proxy=<your-proxy-url>` to apply it globally.
