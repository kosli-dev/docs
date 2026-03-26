---
title: FAQ
description: "Frequently asked questions"
---

<AccordionGroup>

<Accordion title="Where can I find API documentation?">
Kosli API documentation is available for logged-in Kosli users at [app.kosli.com/api/v2/doc](https://app.kosli.com/api/v2/doc/).
You can also find the link at [app.kosli.com](https://app.kosli.com) after clicking your avatar (top-right corner of the page).
</Accordion>

<Accordion title="Do I have to provide all the flags all the time?">
A number of flags won't change their values often (or at all) between commands, like `--org` or `--api-token`. Some will differ between e.g. workflows, like `--flow`. You can define them as environment variables to avoid unnecessary redundancy. Check [Environment variables](/getting_started/install#assigning-flags-via-environment-variables) to learn more.
</Accordion>

<Accordion title="What is dry run and how to use it?">
You can use dry run to disable writing to `app.kosli.com` — e.g. if you're just trying things out, or troubleshooting (dry run will print the payload the CLI would send in a non dry run mode).

There are three ways to enable a dry run:
1. Use the `--dry-run` flag (no value needed) to enable it per command
2. Set the `KOSLI_DRY_RUN` environment variable to `true` to enable it globally (e.g. in your terminal or CI)
3. Set the `KOSLI_API_TOKEN` environment variable to `DRY_RUN` to enable it globally (e.g. in your terminal or CI)
</Accordion>

<Accordion title="What is the --config-file flag?">
A config file is an alternative to using Kosli flags or environment variables. Usually you'd use a config file for values that rarely change — like api token or org — but you can represent all Kosli flags in a config file. The key for each value is the same as the flag name, capitalized, so `--api-token` becomes `API-TOKEN`, and `--org` becomes `ORG`, etc.

You can use JSON, YAML, or TOML format:

<CodeGroup>
```json kosli-conf.json
{
  "ORG": "my-org",
  "API-TOKEN": "123456abcdef"
}
```

```yaml kosli-conf.yaml
ORG: "my-org"
API-TOKEN: "123456abcdef"
```

```toml kosli-conf.toml
ORG = "my-org"
API-TOKEN = "123456abcdef"
```
</CodeGroup>

When calling a Kosli command you can skip the file extension. For example, to list environments with `org` and `api-token` in the configuration file:

```shell
kosli list environments --config-file kosli-conf
```

`--config-file` defaults to `kosli`, so if you name your file `kosli.<yaml|toml|json>` and the file is in the same location as where you run Kosli commands from, you can skip the `--config-file` altogether.
</Accordion>

<Accordion title="Reporting the same artifact and evidence multiple times">
If an artifact or evidence is reported multiple times there are a few corner cases:

**Template** — When an artifact is reported, the template for the flow is stored together with the artifact. If the template has changed between reports, the last template is considered the template for that artifact.

**Evidence** — If a given named evidence is reported multiple times, the compliance status of the last reported version is considered the compliance state of that evidence. If an artifact is reported multiple times with different git-commits, the last reported version of the named commit-evidence is considered the compliance state.

**Evidence outside the template** — If an artifact has evidence (commit or artifact evidence) that is not part of the template, the state of the extra evidence will affect the overall compliance of the artifact.
</Accordion>

<Accordion title="How to set compliant status of generic evidence">
The `--compliant` flag is a [boolean flag](#boolean-flags).
To report generic evidence as non-compliant use `--compliant=false`:

```shell
kosli report evidence artifact generic server:1.0 \
  --artifact-type docker \
  --name test \
  --description "generic test evidence" \
  --compliant=false \
  --flow server
```

`--compliant` is set to `true` by default, so to report as compliant simply skip the flag altogether.
</Accordion>

<Accordion title="Why can't I delete or archive a policy?">
It's not possible to delete a policy in Kosli. This is by design, because there can be snapshots that were previously evaluated using the policy. Deleting it would compromise the integrity of those historical evaluations.

Archiving policies isn't available yet. If this is something you'd find useful, we'd love to hear about your use case — reach out to us at support@kosli.com.
</Accordion>

</AccordionGroup>

## Boolean flags

Flags with values can usually be specified with an `=` or with a **space** as a separator.
For example, `--artifact-type=file` or `--artifact-type file`.
However, an explicitly specified boolean flag value **must** use an `=`.
For example, if you try this:
```
kosli attest generic Dockerfile --artifact-type file  --compliant true ...
```
You will get an error stating:
```
Error: accepts at most 1 arg(s), received 2
```
Here, `--artifact-type file` is parsed as if it was `--artifact-type=file`, leaving:
```
kosli attest generic Dockerfile --compliant true ...
```
Then `--compliant` is parsed as if *implicitly* defaulting to `--compliant=true`, leaving:
```
kosli attest generic Dockerfile true ...
```
The parser then sees `Dockerfile` and `true` as the two
arguments to `kosli attest generic`.
