---
title: "kosli get attestation"
beta: false
deprecated: false
description: "Get an attestation using its name or id.  "
---

## Synopsis

```shell
kosli get attestation [ATTESTATION-NAME] [flags]
```

Get an attestation using its name or id.  

You can get an attestation from a trail or artifact using its name. The attestation name should be given
WITHOUT dot-notation.  
To get an attestation from a trail, specify the trail name using the `--trail` flag.  
To get an attestation from an artifact, specify the artifact fingerprint using the `--fingerprint` flag.  
These flags cannot be used together. In both cases the flow must also be specified using the `--flow` flag.  
If there are multiple attestations with the same name on the trail or artifact, a list of all will be returned.

You can also get an attestation by its id using the `--attestation-id` flag. This cannot be used with the attestation name,
or any of the `--flow`, `--trail` or `--fingerprint` flags.


## Flags
| Flag | Description |
| :--- | :--- |
|        --attestation-id string  |  [conditional] The unique identifier of the attestation to retrieve. Cannot be used together with ATTESTATION-NAME.  |
|    -F, --fingerprint string  |  [conditional] The fingerprint of the artifact for the attestation. Cannot be used together with --trail or --attestation-id.  |
|    -f, --flow string  |  [conditional] The name of the Kosli flow for the attestation. Required if ATTESTATION-NAME provided. Cannot be used together with --attestation-id.  |
|    -h, --help  |  help for attestation  |
|    -o, --output string  |  [defaulted] The format of the output. Valid formats are: [table, json]. (default "table")  |
|    -t, --trail string  |  [conditional] The name of the Kosli trail for the attestation. Cannot be used together with --fingerprint or --attestation-id.  |


## Flags inherited from parent commands
| Flag | Description |
| :--- | :--- |
|    -a, --api-token string  |  The Kosli API token.  |
|    -c, --config-file string  |  [optional] The Kosli config file path. (default "kosli")  |
|        --debug  |  [optional] Print debug logs to stdout. A boolean flag [docs](/faq/#boolean-flags) (default false)  |
|    -H, --host string  |  [defaulted] The Kosli endpoint. (default "https://app.kosli.com")  |
|        --http-proxy string  |  [optional] The HTTP proxy URL including protocol and port number. e.g. 'http://proxy-server-ip:proxy-port'  |
|    -r, --max-api-retries int  |  [defaulted] How many times should API calls be retried when the API host is not reachable. (default 3)  |
|        --org string  |  The Kosli organization.  |


## Live Example

To view a live example of 'kosli get attestation' you can run the command below (for the [cyber-dojo](https://app.kosli.com/cyber-dojo) demo organization).

```shell
export KOSLI_ORG=cyber-dojo
export KOSLI_API_TOKEN=Pj_XT2deaVA6V1qrTlthuaWsmjVt4eaHQwqnwqjRO3A  # read-only
kosli get attestation snyk-container-scan --flow=differ-ci --fingerprint=0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0 --output=json
```

<Accordion title="View example output">
```json
[
  {
    "schema_version": 2,
    "attestation_type": "snyk",
    "attestation_name": "snyk-container-scan",
    "is_compliant": true,
    "origin_url": "https://github.com/cyber-dojo/differ/actions/runs/14975901658",
    "artifact_fingerprint": "0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0",
    "target_artifacts": [
      "differ"
    ],
    "git_commit_info": {
      "sha1": "5ccc5c141fdd1fbd97905b7fe0af87e5a592bfb6",
      "message": "Dockerfile - Automated base-image update (#317)\n\nCo-authored-by: JonJagger@users.noreply.github.com <{{ github.actor }}>",
      "author": "Jon Jagger <jon@kosli.com>",
      "branch": "main",
      "timestamp": 1747062671.0,
      "url": "https://github.com/cyber-dojo/differ/commit/5ccc5c141fdd1fbd97905b7fe0af87e5a592bfb6"
    },
    "evidence_archive_path": "83acb2bc-2c26-48a7-8b87-90dfcce7/artifact_attestation/05c2fd70-0832-4868-9e56-e268b720/evidence.tgz",
    "evidence_archive_fingerprint": "8b671e582ee8c9550bb76fb8cef8cb5b4b9f5481737e42f44ad272c931bd82ba",
    "user_data": {},
    "created_at": 1747062776.797778,
    "processed_snyk_results": {
      "schema_version": 1,
      "tool": {
        "name": "Snyk Container",
        "version": "1.1296.2"
      },
      "results": [
        {
          "low_count": 0,
          "medium_count": 0,
          "high_count": 0
        },
        {
          "low_count": 0,
          "medium_count": 0,
          "high_count": 0
        }
      ]
    },
    "attestation_id": "f7cd9b3a-2738-47e6-be36-689d511d",
    "html_url": "https://app.kosli.com/cyber-dojo/flows/differ-ci/trails/5ccc5c141fdd1fbd97905b7fe0af87e5a592bfb6?attestation_id=f7cd9b3a-2738-47e6-be36-689d511d",
    "reported_by": "ci-pipelines",
    "has_audit_package": true,
    "_links": {
      "self": {
        "href": "https://app.kosli.com/api/v2/attestations/cyber-dojo/differ-ci/artifact/0cbbe3a6e73e733e8ca4b8813738d68e824badad0508ff20842832b5143b48c0/snyk-container-scan"
      },
      "evidence": {
        "href": "https://app.kosli.com/api/v2/attestations/cyber-dojo/differ-ci/trail/5ccc5c141fdd1fbd97905b7fe0af87e5a592bfb6/attestation/f7cd9b3a-2738-47e6-be36-689d511d/evidence"
      }
    }
  }
]
```
</Accordion>

## Examples Use Cases

These examples all assume that the flags  `--api-token`, `--org`, `--host`, (and `--flow`, `--trail` when required), are [set/provided](/getting_started/install/#assigning-flags-via-environment-variables). 

<AccordionGroup>
<Accordion title="get an attestation by name from a trail (requires the --trail flag)">
```shell
kosli get attestation attestationName 

```
</Accordion>
<Accordion title="get an attestation by name from an artifact">
```shell
kosli get attestation attestationName 
	--fingerprint fingerprint

```
</Accordion>
<Accordion title="get an attestation by its id">
```shell
kosli get attestation --attestation-id attestationID
```
</Accordion>
</AccordionGroup>

