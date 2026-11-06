---
title: FAQ
description: "Frequently asked questions"
---

import WorkingDirConfigNotice from "/snippets/cli-working-dir-config-notice.mdx";

<AccordionGroup>

<Accordion title="Where can I find API documentation?">
See the [API reference](/api-reference/overview) for base URLs, authentication, and every endpoint.
Each Kosli instance also serves interactive Swagger docs: [app.kosli.com/api/v2/doc](https://app.kosli.com/api/v2/doc/) for EU, [app.us.kosli.com/api/v2/doc](https://app.us.kosli.com/api/v2/doc/) for US, and `https://<your-kosli-domain>/api/v2/doc` for Kosli Dedicated.
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

`--config-file` defaults to `$HOME/.kosli.yml`, which is the file [`kosli config`](/client_reference/kosli_config) writes. Any other config file has to be named explicitly, either with `--config-file` on each command or by setting `KOSLI_CONFIG_FILE` in the environment.

<WorkingDirConfigNotice />
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

<Accordion title="Why is my GitHub login failing?">
If you sign in to Kosli with GitHub, you must have a verified email address on your GitHub account — otherwise login will fail.

You can check the status of your email addresses at [github.com/settings/emails](https://github.com/settings/emails).

If your GitHub organization uses an IP allow list, you also need to allow Kosli's sign-in traffic. See [GitHub sign-in](/administration/authentication/github_login#github-ip-allow-lists) for the addresses to add.
</Accordion>

<Accordion title="When do I use kosli assert, and when kosli evaluate?">
Both commands exit non-zero on a failing result, so both can stop a pipeline. They answer different questions:

- **`kosli assert`** checks a verdict Kosli has already worked out from what you recorded. You write no rules: the rules are your flow templates and environment policies. [`kosli assert artifact`](/client_reference/kosli_assert_artifact) asks whether an artifact is compliant, and [`kosli assert snapshot`](/client_reference/kosli_assert_snapshot) asks whether an environment is.
- **`kosli evaluate`** runs a Rego policy over trail data and returns allow or deny. Use it for rules that flow templates and environment policies can't express, such as "every pull request has an approver who isn't its author". The `evaluate` commands are in beta.

| | `kosli assert artifact` / `snapshot` | `kosli evaluate` |
|---|---|---|
| Answers | Is this artifact or environment compliant? | Does this trail data satisfy my policy? |
| Rules come from | Flow templates and environment policies in Kosli | A Rego policy you write |
| Checks | An artifact (by fingerprint) or an environment snapshot | One or more trails, or local JSON with `evaluate input` |
| Records a result | No | Yes, with `kosli evaluate policy --control`, which records a decision |

Use them together when you work with [controls](/tutorials/working_with_controls): `kosli evaluate policy` records a decision against a control where the judgment is made, an environment policy requires that decision, and `kosli assert artifact --environment` enforces it as the gate before deployment. In short, evaluate where you decide, assert where you deploy.

The other `assert` commands are narrower checks: `kosli assert pullrequest` fails if a commit has no pull request, and `kosli assert status` fails if the Kosli server is down.

To learn more, see [Enforce policies](/getting_started/enforce_policies) for `assert`, and [Evaluate trails with OPA policies](/tutorials/evaluate_trails_with_opa) and the [Rego policy reference](/policy-reference/rego_policy) for `evaluate`.
</Accordion>

<Accordion title="Why can't I delete or archive a policy?">
It's not possible to delete a policy in Kosli. This is by design, because there can be snapshots that were previously evaluated using the policy. Deleting it would compromise the integrity of those historical evaluations.

Archiving policies isn't available yet. If this is something you'd find useful, we'd love to hear about your use case — reach out to us at support@kosli.com.
</Accordion>

</AccordionGroup>

## Boolean flags

Flags with values can usually be specified with an `=` or with a **space** as a separator.
For example, `--artifact-type=file` or `--artifact-type file`.
Boolean flags accept both forms from CLI v2.36.0 onwards:
```
kosli attest generic Dockerfile --artifact-type file --compliant false ...
```
On earlier versions an explicitly specified boolean flag value **must** use an `=`.
Either upgrade the CLI, or write the flag as `--compliant=false`.
Without the `=` the command above fails with:
```
Error: accepts at most 1 arg(s), received 2
```
because `--compliant` is parsed as if *implicitly* defaulting to `--compliant=true`, leaving:
```
kosli attest generic Dockerfile false ...
```
The parser then sees `Dockerfile` and `false` as the two
arguments to `kosli attest generic`.

## Empty flag values

A flag given an empty value is an error from CLI v2.37.0 onwards:
```
kosli attest generic Dockerfile --artifact-type file --exclude "" ...
Error: flag '--exclude' was given an empty value
```
The usual cause is a shell variable that is unset, so `--exclude "$BUILD_TMP"`
reaches the CLI as `--exclude ""`. The same applies to a value from a `KOSLI_`
environment variable or from `~/.kosli.yml`, and to an empty element of a
comma-separated list such as `--exclude "node_modules,,vendor"`.

On earlier versions most of these were accepted silently. `--exclude ""`
excluded nothing, so the fingerprint was one no artifact matched;
`--fingerprint ""` recorded an attestation against the trail rather than the
artifact named; `--redact-commit-info ""` sent the commit author and message
the flag exists to withhold. Each exited 0 and printed what success prints.

Either give the flag a real value, or remove it. In almost every case an empty
value did what leaving the flag out does, so removing it keeps the earlier
behavior and says so plainly.

Leaving a flag out is unchanged, including the values filled in from your CI
environment, such as `--build-url`, `--commit-url` and `--repository`.

One case the CLI cannot catch: a boolean flag written without quotes loses the
empty value in the shell rather than in the CLI, so `--compliant ${UNSET}`
arrives as `--compliant` with nothing after it, which is indistinguishable from
typing `--compliant` deliberately. Quote the variable, `--compliant "${VAR}"`,
and it is refused like any other empty value.
