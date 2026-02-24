---
title: "Attesting Snyk scans"
description: "In this tutorial, we will see how you can run and attest different types of Snyk scans to Kosli. We will run the scans on the Kosli CLI git repo"
---

In this tutorial, we will run Snyk scans against the Kosli CLI git repo and attest the results to a Kosli trail.
By the end, you will have a Kosli trail with attested Snyk scan results that you can view in the Kosli app.

## Prerequisites

To follow the steps in this tutorial, you need to:
* [Setup Snyk on your machine](https://docs.snyk.io/snyk-cli/getting-started-with-the-snyk-cli#install-the-snyk-cli-and-authenticate-your-machine).
* [Install Helm](https://helm.sh/docs/intro/install/) if you want to try Snyk IaC attestations, otherwise skip.
* [Install Docker](https://docs.docker.com/engine/install/) if you want to try Snyk container attestations, otherwise skip.
* [Create a Kosli account](https://app.kosli.com/) (Skip if you already have one).
* [Install Kosli CLI](/getting_started/install).
* [Get a Kosli API token](/getting_started/service-accounts).

## Setup

Set the `KOSLI_ORG` environment variable to your personal org name and `KOSLI_API_TOKEN` to your token:
```shell
export KOSLI_ORG=<your-personal-kosli-org-name>
export KOSLI_API_TOKEN=<your-api-token>
```

Clone the Kosli CLI git repo:
```shell
git clone https://github.com/kosli-dev/cli.git
cd cli
```

## Create a Flow and Trail

We will start by creating a flow in Kosli to contain trails and artifacts for this tutorial:

```shell
kosli create flow snyk-demo --use-empty-template
```

You should see: `flow snyk-demo was created`.

Then start a trail to bind our Snyk attestations to:

```shell
kosli begin trail test-1 --flow snyk-demo
```

You should see: `trail 'test-1' was begun`.

## Attest Snyk scans

We can now run Snyk scans and attest them to the trail. After each attestation, you can verify the result by navigating to **https://app.kosli.com/`your-personal-org-name`/flows/snyk-demo/trails/test-1** in the Kosli app.

### Open Source scan

[Snyk Open Source](https://docs.snyk.io/scan-using-snyk/snyk-open-source) finds vulnerabilities in the open-source libraries used by your application:

```shell
snyk test --sarif-file-output=os.json

kosli attest snyk --flow snyk-demo --trail test-1 --name open-source-scan --scan-results os.json --commit HEAD
```

You should see: `snyk attestation 'open-source-scan' is reported to trail: test-1`.

### Code scan

[Snyk Code](https://docs.snyk.io/scan-using-snyk/snyk-code) scans your source code for security issues:

```shell
snyk code test --sarif-file-output=code.json

kosli attest snyk --flow snyk-demo --trail test-1 --name code-scan --scan-results code.json --commit HEAD
```

You should see: `snyk attestation 'code-scan' is reported to trail: test-1`.

### Container scan

[Snyk Container](https://docs.snyk.io/scan-using-snyk/snyk-container) scans container images for security issues:

```shell
docker pull ghcr.io/kosli-dev/cli:v2.8.3
snyk container test ghcr.io/kosli-dev/cli:v2.8.3 --file=Dockerfile --sarif-file-output=container.json

kosli attest snyk --flow snyk-demo --trail test-1 --name container-scan --scan-results container.json --commit HEAD
```

You should see: `snyk attestation 'container-scan' is reported to trail: test-1`.

### IaC scan

[Snyk IaC](https://docs.snyk.io/scan-using-snyk/snyk-iac) scans IaC configuration files (Terraform, Kubernetes, Helm) for security issues:

```shell
helm template ./charts/k8s-reporter --output-dir helm \
  --set kosliApiToken.secretName=secret \
  --set reporterConfig.kosliEnvironmentName=foo \
  --set reporterConfig.kosliOrg=bar

snyk iac test helm --sarif-file-output=helm.json

kosli attest snyk --flow snyk-demo --trail test-1 --name helm-scan --scan-results helm.json --commit HEAD
```

You should see: `snyk attestation 'helm-scan' is reported to trail: test-1`.

## What you've accomplished

You have run four types of Snyk scans and attested each result to a Kosli trail. The trail now holds a tamper-proof record of your scan findings, linked to a specific git commit.

From here you can:
- Explore the trail in the [Kosli app](https://app.kosli.com)
- Attest scans to an artifact in a trail — see [`kosli attest snyk`](/client_reference/kosli_attest_snyk) for details
- Add Snyk attestations to your CI pipeline using the [GitHub Actions integration](/integrations/actions)
