---
title: Linking trails across branches
description: How to connect compliance evidence from PR trails to main-branch trails in Kosli.
---

Many teams run compliance checks — tests, security scans, code review — during a pull request build and want to carry that evidence forward when the code merges into the main branch. Because each build typically creates its own Kosli trail, the question arises: **how do you prove on the main-branch trail that the PR-branch checks already passed?**

This guide explains the problem, the recommended workaround today, and the risks to be aware of.

## The problem

A typical CI workflow uses two Kosli flows:

| Flow | Triggered by | Trail name | What it records |
|---|---|---|---|
| `app-pr` | Pull request builds | PR number or branch commit | Tests, scans, code review |
| `app-main` | Merges to main | Merge commit SHA | Artifact build, deployment approval |

After a PR merges, the main-branch build produces the release artifact. But the compliance evidence (tests, scans) lives on the PR trail in a different flow. Kosli does not yet have a built-in way to formally link one trail to another.

## Recommended approach

Use `kosli evaluate trail` on the main-branch build to evaluate the PR trail against a Rego policy, then record the result as an attestation on the main trail.

<Steps>
  <Step title="Identify the PR trail name from the main build">
    Derive the PR trail name from information available in your main-branch CI context. Common strategies:

    - **Git ancestry** — find the merge commit's parent that matches a PR trail name.
    - **Branch naming convention** — extract the PR number from the merge commit message (e.g. `Merge pull request #42`).
    - **CI environment variables** — some CI systems expose the originating PR number on merge builds.

    ```bash
    # Example: extract PR number from a GitHub merge commit message
    PR_NUMBER=$(git log -1 --format='%s' | grep -oP '#\K[0-9]+')
    PR_TRAIL="PR-${PR_NUMBER}"
    ```
  </Step>

  <Step title="Check the PR trail compliance">
    There are two ways to check the PR trail's compliance. Use `kosli evaluate trail` with a Rego policy for a formal, policy-driven check that fails the CI step automatically. Alternatively, use `kosli get trail` with JSON output for a lighter approach that does not require a policy file.

    <Tabs>
      <Tab title="evaluate trail (Rego policy)">
        Use `kosli evaluate trail` to check the PR trail against a Rego policy. Create a policy file (e.g. `pr-compliant.rego`):

        ```rego pr-compliant.rego
        package main

        default allow = false

        allow {
          input.trail.compliance.is_compliant == true
        }
        ```

        Then evaluate the PR trail:

        ```bash
        kosli evaluate trail "$PR_TRAIL" \
          --flow app-pr \
          --policy pr-compliant.rego
        ```

        The command exits with a non-zero code if the trail does not satisfy the policy, which fails the CI step automatically.
      </Tab>
      <Tab title="get trail (JSON + jq)">
        Use `kosli get trail` with JSON output and parse the compliance status:

        ```bash
        IS_COMPLIANT=$(kosli get trail "$PR_TRAIL" \
          --flow app-pr \
          --output json | jq -r '.compliance.is_compliant')
        ```

        This is simpler but does not use a formal policy. You will need `$IS_COMPLIANT` in the next step.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Attest the result on the main trail">
    Record a generic attestation on your main-branch trail with the PR trail's compliance result.

    <Tabs>
      <Tab title="evaluate trail (Rego policy)">
        Because `kosli evaluate trail` fails the CI step on a non-compliant trail, this attestation only runs when the trail is compliant:

        ```bash
        kosli attest generic \
          --name pr-build-compliance \
          --flow app-main \
          --trail "$(git rev-parse HEAD)" \
          --compliant=true \
          --description "PR trail ${PR_TRAIL} in flow app-pr passed policy evaluation"
        ```
      </Tab>
      <Tab title="get trail (JSON + jq)">
        Pass the `$IS_COMPLIANT` value from the previous step:

        ```bash
        kosli attest generic \
          --name pr-build-compliance \
          --flow app-main \
          --trail "$(git rev-parse HEAD)" \
          --compliant="$IS_COMPLIANT" \
          --description "PR trail ${PR_TRAIL} in flow app-pr was compliant: ${IS_COMPLIANT}"
        ```
      </Tab>
    </Tabs>

    Add `pr-build-compliance` to your main flow's template so that missing evidence is flagged:

    ```yaml
    # yaml-language-server: $schema=https://kosli.mintlify.app/schemas/flow-template.json
    version: 1
    trail:
      attestations:
      - name: pr-build-compliance
        type: generic
      artifacts:
      - name: app
        attestations:
        - name: artifact-build
          type: generic
    ```
  </Step>
</Steps>

## Risks and considerations

This approach works, but carries assumptions you should evaluate for your environment:

### Code equivalence between PR and main

A PR build runs against the branch head at build time. Between the PR build and the merge to main, the main branch may have received other commits. If the merge is not a **fast-forward**, the code on main after the merge may differ from what the PR build tested.

Mitigations:

- **Require linear history** in your repository settings (GitHub, GitLab, Bitbucket all support this). This forces rebasing before merge, ensuring the PR build tested the exact code that lands on main.
- **Require up-to-date branches** before merging, so the PR build always includes the latest main-branch changes.
- **Re-run critical tests on main** if fast-forward merges are not practical. This adds time but removes ambiguity.

<Warning>
Without one of these mitigations, a PR trail's compliance does not guarantee that the merged code on main behaves identically. Evaluate whether this risk is acceptable for your compliance requirements.
</Warning>

### Binary reproducibility

If your build process is not reproducible, the artifact built on main may differ from the one built on the PR branch — even from identical source code. In that case, the PR trail's attestations apply to a different artifact than the one you deploy.

If your builds are reproducible, you can strengthen the link by verifying that the artifact fingerprint on main matches one attested in the PR trail.

### Trust boundaries

The approach above relies on the Kosli API token used in CI having read access to the PR flow. Ensure your CI secrets and permissions are configured so that:

- The main-branch build can query `app-pr` trails.
- Only authorized pipelines can write attestations to `app-main`.

## Example: GitHub Actions

Below is a simplified GitHub Actions workflow for a main-branch build that links back to the PR trail:

<Tabs>
  <Tab title="evaluate trail (Rego policy)">
    ```yaml
    name: Main build
    on:
      push:
        branches: [main]

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
            with:
              fetch-depth: 2

          - name: Identify PR trail
            id: pr
            run: |
              PR_NUMBER=$(git log -1 --format='%s' | grep -oP '#\K[0-9]+' || echo "")
              echo "trail=PR-${PR_NUMBER}" >> "$GITHUB_OUTPUT"
              echo "found=${PR_NUMBER:+true}" >> "$GITHUB_OUTPUT"

          - name: Begin trail
            run: |
              kosli begin trail "$(git rev-parse HEAD)" \
                --flow app-main

          - name: Build artifact
            run: docker build -t myapp:latest .

          - name: Attest artifact
            run: |
              kosli attest artifact myapp:latest \
                --artifact-type docker \
                --name app \
                --flow app-main \
                --trail "$(git rev-parse HEAD)"

          - name: Evaluate PR trail compliance
            if: steps.pr.outputs.found == 'true'
            run: |
              kosli evaluate trail "${{ steps.pr.outputs.trail }}" \
                --flow app-pr \
                --policy pr-compliant.rego

              kosli attest generic \
                --name pr-build-compliance \
                --flow app-main \
                --trail "$(git rev-parse HEAD)" \
                --compliant=true \
                --description "PR trail ${{ steps.pr.outputs.trail }} passed policy evaluation"
    ```
  </Tab>
  <Tab title="get trail (JSON + jq)">
    ```yaml
    name: Main build
    on:
      push:
        branches: [main]

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
            with:
              fetch-depth: 2

          - name: Identify PR trail
            id: pr
            run: |
              PR_NUMBER=$(git log -1 --format='%s' | grep -oP '#\K[0-9]+' || echo "")
              echo "trail=PR-${PR_NUMBER}" >> "$GITHUB_OUTPUT"
              echo "found=${PR_NUMBER:+true}" >> "$GITHUB_OUTPUT"

          - name: Begin trail
            run: |
              kosli begin trail "$(git rev-parse HEAD)" \
                --flow app-main

          - name: Build artifact
            run: docker build -t myapp:latest .

          - name: Attest artifact
            run: |
              kosli attest artifact myapp:latest \
                --artifact-type docker \
                --name app \
                --flow app-main \
                --trail "$(git rev-parse HEAD)"

          - name: Check PR trail compliance
            if: steps.pr.outputs.found == 'true'
            run: |
              IS_COMPLIANT=$(kosli get trail "${{ steps.pr.outputs.trail }}" \
                --flow app-pr \
                --output json | jq -r '.compliance.is_compliant')

              kosli attest generic \
                --name pr-build-compliance \
                --flow app-main \
                --trail "$(git rev-parse HEAD)" \
                --compliant="$IS_COMPLIANT" \
                --description "PR trail ${{ steps.pr.outputs.trail }} was compliant: ${IS_COMPLIANT}"
    ```
  </Tab>
</Tabs>

## Looking ahead

Kosli is exploring native support for linking trails across flows — removing the need for the scripted approach described above. When available, this will allow you to declare trail dependencies directly in the flow template, with Kosli resolving and evaluating the linked trail's compliance automatically.

Until then, the `kosli evaluate trail` approach described here is the recommended pattern.
