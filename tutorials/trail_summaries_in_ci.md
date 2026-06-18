---
title: "Adding trail summaries to CI pipeline runs"
description: "Use `kosli get trail --output markdown` to publish a Kosli trail summary directly to GitHub Actions and GitLab CI pipeline runs."
---

`kosli get trail --output markdown` renders a trail as GitHub-Flavored Markdown — compliance state, git commit, attestation statuses, and events, with links back to the Kosli app. Pipe it into your CI's job summary and every pipeline run becomes an information radiator for the trail it produced.

By the end of this tutorial, you will have added a Kosli trail summary to a GitHub Actions job summary and to a GitLab CI pipeline.

## Prerequisites

* [Install Kosli CLI](/getting_started/install) on your CI runner (e.g. via [`kosli-dev/setup-cli-action`](https://github.com/marketplace/actions/setup-kosli-cli) on GitHub).
* A flow and trail you are already reporting to during the pipeline. See [Querying Kosli](/tutorials/querying_kosli) if you need to find the flow and trail name.
* `KOSLI_API_TOKEN` and `KOSLI_ORG` available to the job (see [Authenticating to Kosli](/getting_started/authenticating_to_kosli)).

## What the markdown output looks like

Run the command locally first to see what will end up in your CI summary:

```shell
kosli get trail my-trail-name --flow my-flow --output markdown
```

The output is a markdown document with:

- A `## Trail: <name>` heading linked to the trail page in the Kosli app.
- A metadata table (name, description, compliance, last modified, origin).
- A `### Git commit` table with the commit author, timestamp, and subject.
- An `### Attestations` section with one headerless table per artifact (and one for trail-level attestations), with each attestation linked to its place on the trail page. Statuses are prefixed with ✅ / ❌ / ⏳; attestations reported but not expected by the template are marked with `(+)`.
- An `### Events` table with timestamps, descriptions, commit links, and compliance state.

## Publishing the summary

<Tabs>
  <Tab title="GitHub" icon="github">

GitHub Actions exposes a per-job markdown summary via the [`$GITHUB_STEP_SUMMARY`](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-job-summary) environment variable. Anything you append to that file is rendered on the workflow run page.

Add a final step to your job that writes the trail summary to it:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      KOSLI_API_TOKEN: ${{ secrets.KOSLI_API_TOKEN }}
      KOSLI_ORG: my-org
      KOSLI_FLOW: my-flow
      KOSLI_TRAIL: ${{ github.sha }}
    steps:
      - uses: actions/checkout@v7

      - name: Setup Kosli CLI
        uses: kosli-dev/setup-cli-action@v5

      # ... your build, attest, and report steps ...

      - name: Publish Kosli trail summary
        if: always()
        run: |
          kosli get trail "$KOSLI_TRAIL" \
            --flow "$KOSLI_FLOW" \
            --output markdown >> "$GITHUB_STEP_SUMMARY"
```

`if: always()` makes sure the summary is published even when an earlier step fails — that is when you most want to see which attestation is missing or non-compliant.

The summary appears on the run's page under the job, with the trail name linking back to the trail in the Kosli app and every attestation linking to its position on the trail.

  </Tab>
  <Tab title="GitLab" icon="gitlab">

GitLab does not natively render markdown inline on the job page, but [`artifacts:expose_as`](https://docs.gitlab.com/ci/yaml/#artifactsexpose_as) surfaces the `summary.md` artifact as a labeled link in the merge request widget, one click away from the rendered file in the GitLab UI.

Add a job (or a final step in your existing job) that produces that artifact:

```yaml
kosli-trail-summary:
  stage: .post
  image: ubuntu:24.04
  variables:
    KOSLI_FLOW: my-flow
    KOSLI_TRAIL: $CI_COMMIT_SHA
  before_script:
    - apt-get update && apt-get install -y curl ca-certificates
    - curl -fsSL https://get.kosli.com/install.sh | bash
  script:
    - >
      kosli get trail "$KOSLI_TRAIL"
      --flow "$KOSLI_FLOW"
      --output markdown > summary.md
  artifacts:
    when: always
    paths:
      - summary.md
    expose_as: "Kosli trail summary"
```

`KOSLI_API_TOKEN` and `KOSLI_ORG` should be set as [CI/CD variables](https://docs.gitlab.com/ci/variables/) on the project or group, masked, so the job picks them up automatically.

`when: always` mirrors the GitHub `if: always()` pattern: the summary is uploaded even if earlier stages fail.

  </Tab>
</Tabs>

## Tips

- Pin a specific trail by exporting `KOSLI_TRAIL` early in the pipeline (commonly to the commit SHA you used in `kosli begin trail`). Every later step — including the summary — then targets the same trail.
- The markdown output is stable text. You can also commit it as a build artifact or attach it to a release for an audit-friendly record of what was reported for that build.
- Run `kosli get trail --output markdown` locally against a real trail before wiring it into CI. It is the fastest way to see what your team will see on the pipeline page.

## What you've accomplished

You have published a live Kosli trail summary — compliance state, attestations, and events — directly onto your GitHub Actions and GitLab CI pipeline pages, turning every build into a feedback channel for the trail it produced.

From here you can:

- Read the full [`kosli get trail`](/client_reference/kosli_get_trail) reference.
- Browse other [CI/CD integration patterns](/integrations/ci_cd).
