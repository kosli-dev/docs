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
* [Get a Kosli API token](/getting_started/authenticating_to_kosli).

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

If your proxy requires authentication, embed the credentials in the proxy URL:

```shell
kosli list envs --org cyber-dojo --http-proxy http://username:password@proxy-host:8080 --api-token <your-token>
```

## More examples

Once the proxy is running, any Kosli CLI command can be routed through it by adding the `--http-proxy` flag. Here are some common examples:

**Report a Docker image artifact through the proxy:**

```shell
kosli attest artifact my-app:latest \
  --artifact-type docker \
  --flow my-flow \
  --trail $(git rev-parse HEAD) \
  --name my-app \
  --http-proxy http://localhost:8888 \
  --api-token <your-token> \
  --org <your-org>
```

**Snapshot a Kubernetes cluster through the proxy:**

```shell
kosli snapshot k8s my-k8s-env \
  --kubeconfig ~/.kube/config \
  --namespaces production \
  --http-proxy http://localhost:8888 \
  --api-token <your-token> \
  --org <your-org>
```

**Attach a JUnit test attestation through the proxy:**

```shell
kosli attest junit \
  --name unit-tests \
  --flow my-flow \
  --trail $(git rev-parse HEAD) \
  --results-dir ./test-results \
  --http-proxy http://localhost:8888 \
  --api-token <your-token> \
  --org <your-org>
```

**Request an approval through the proxy:**

```shell
kosli request approval my-app:latest \
  --artifact-type docker \
  --flow my-flow \
  --description "Approve release to production" \
  --http-proxy http://localhost:8888 \
  --api-token <your-token> \
  --org <your-org>
```

## Persist the proxy configuration

Rather than passing `--http-proxy` on every command, save it to your Kosli config:

```shell
kosli config --http-proxy=http://localhost:8888
```

All subsequent CLI commands will now route through the proxy automatically.

## Scope of `--http-proxy`

The `--http-proxy` flag only applies to traffic between the CLI and the Kosli API. Commands that integrate with third-party services (GitHub, GitLab, Jira, SonarCloud/SonarQube, Azure, AWS) use separate HTTP clients that are **not** affected by this flag. To proxy that traffic, set the standard `HTTPS_PROXY` / `HTTP_PROXY` / `NO_PROXY` environment variables separately.

The table below shows every external endpoint the CLI may contact and how to proxy each one:

| Destination | Endpoint | Commands | Proxy method |
|---|---|---|---|
| Kosli API | `https://app.kosli.com` (configurable via `--host`) | All commands | `--http-proxy` or `HTTPS_PROXY` |
| GitHub | `https://api.github.com` (configurable via `--github-base-url`) | PR/commit attestations | `HTTPS_PROXY` only |
| GitLab | `https://gitlab.com` (configurable via `--gitlab-base-url`) | PR attestations | `HTTPS_PROXY` only |
| Jira | Configured via `--jira-base-url` | Jira attestations | `HTTPS_PROXY` only |
| SonarCloud/SonarQube | `https://sonarcloud.io` (configurable via `--sonar-server-url`) | Sonar attestations | `HTTPS_PROXY` only |
| Azure DevOps | Configured via `--azure-org-url` | Azure PR attestations | `HTTPS_PROXY` only |
| Azure management APIs | Azure ARM/IMDS endpoints | Azure app snapshots | `HTTPS_PROXY` only |
| AWS APIs | Regional AWS endpoints | ECS / Lambda / S3 snapshots | `HTTPS_PROXY` only |
| Container registries | OCI registries (ECR, GCR, DockerHub, etc.) | Artifact fingerprinting (`--artifact-type oci`) | `HTTPS_PROXY` only |
| Kubernetes API server | In-cluster or via kubeconfig | `snapshot k8s` | kubeconfig `proxy-url` or `HTTPS_PROXY` |

### Corporate proxies requiring Kerberos or NTLM

Go's HTTP client only supports Basic authentication for proxies. If your corporate proxy requires Kerberos or NTLM (common in large enterprises), run a local auth-handling proxy such as [cntlm](https://cntlm.sourceforge.net/) or [px](https://github.com/genotrance/px), then point `HTTPS_PROXY` at `http://127.0.0.1:<local-port>`.

## Kubernetes reporter

The `snapshot k8s` command makes two independent outbound connections:

1. **Kubernetes API server** — uses the kubeconfig for connection and authentication. Configure the proxy via the kubeconfig `proxy-url` field or the `HTTPS_PROXY` environment variable.
2. **Kosli API** — uses the standard Kosli HTTP client, controlled by `--http-proxy`.

These two connections must be configured independently.

## What you've accomplished

You have set up Tinyproxy as an HTTP proxy and configured the Kosli CLI to route all traffic through it. This pattern works with any HTTP proxy — replace `http://localhost:8888` with your organization's proxy URL and run `kosli config --http-proxy=<your-proxy-url>` to apply it globally.
