---
title: "Flows and Trails"
description: "Recommended naming conventions for Flows and Trails in Kosli."
---

This document outlines recommended naming conventions for Flows and Trails as they closely relate to each other in Kosli. Adopting these conventions will help maintain clarity and consistency across your organization.

<Note>
Already have flows in use? See [Adopting a convention on existing flows](/implementation_guide/phase_2/plan_organizational_structure/naming_conventions/existing_flows) for how to rename them without losing history or coordinating a cutover.
</Note>

## Flows

A clear naming convention transforms a simple ID into a meaningful identifier that everyone understands. This shared language ensures attestations go to the right place and you can track your releases from start to finish.

The naming convention relates to `FLOW-NAME` in Kosli CLI command:

```bash
kosli create flow FLOW-NAME [flags]
```

See [CLI documentation](/client_reference/kosli_create_flow) for more details.

The following sections define conventions for the two main types of Flows in Kosli: Build Flows and Release Flows.

### Build Flows

Represent how code changes move from commit to artifact.

**Convention:** <Badge color="green">org unit</Badge> - <Badge color="green">repo</Badge>-<Badge color="green">[service]</Badge>

  <ParamField path="org unit" type="string" required>
    Your organizational unit, division or team name
  </ParamField>

  <ParamField path="repo" type="string" required>
    Your repository name
  </ParamField>

  <ParamField path="service" type="string">
    The specific service or component that the artifact belongs to
    <Tip>
    You can skip `service` if your repository produces only one artifact, i.e. non-monorepo setups.
    </Tip>
  </ParamField>

<Accordion title="examples on FLOW-NAME">

<Tabs>
  <Tab title="snake_case" >

  - `investment-web_app` (single artifact)
  - `investment-web_app-frontend` (with service: frontend)
  - `devops_team-mobile_app-backend` (with service: backend)

  **Regex:**

  ```bash
  ^[a-z][a-z0-9_]*-[a-z][a-z0-9_]*(-[a-z][a-z0-9_]*)?$
  ```
  </Tab>
  <Tab title="camelCase" >

  - `investment-webApp` (single artifact)
  - `investment-webApp-frontend` (with service: frontend)
  - `devopsTeam-mobileApp-backend` (with service: backend)

  **Regex:**

  ```bash
  ^[a-z][a-zA-Z0-9]*-[a-z][a-zA-Z0-9]*(-[a-z][a-zA-Z0-9]*)?$
  ```
  </Tab>
  <Tab title="PascalCase" >

  - `Investment-WebApp` (single artifact)
  - `Investment-WebApp-Frontend` (with service: frontend)
  - `DevOpsTeam-MobileApp-Backend` (with service: backend)

  **Regex:**

  ```bash
  ^[A-Z][a-zA-Z0-9]*-[A-Z][a-zA-Z0-9]*(-[A-Z][a-zA-Z0-9]*)?$
  ```
  </Tab>
</Tabs>
</Accordion>

### Release Flows

Represent how artifacts move from binary repository to deployment.

**Name Convention:** `org unit`-`repo`

<ParamField path="org unit" type="string" required="true">
  Your organizational unit, division or team name
</ParamField>

<ParamField path="repo" type="string" required="true">
  Your repository name
</ParamField>


<Accordion title="examples on FLOW-NAME">
  <Tabs>
    <Tab title="snake_case" >

    - `investment-web_app`
    - `devops_team-mobile_app`

    **Regex:**

    ```bash
    ^[a-z][a-z0-9_]*-[a-z][a-z0-9_]*$
    ```
    </Tab>
    <Tab title="camelCase" >

    - `investment-webApp`
    - `devopsTeam-mobileApp`

    **Regex:**

    ```bash
    ^[a-z][a-zA-Z0-9]*-[a-z][a-zA-Z0-9]*$
    ```
    </Tab>
    <Tab title="PascalCase">
    - `Investment-WebApp`
    - `DevOpsTeam-MobileApp`

    **Regex:**

    ```bash
    ^[A-Z][a-zA-Z0-9]*-[A-Z][a-zA-Z0-9]*$
    ```
    </Tab>
  </Tabs>
</Accordion>

## Trails

The naming convention for Trails depends on the type of Flow they are associated with: Build Flows or Release Flows and relates to `TRAIL-NAME` in Kosli CLI command:

```bash
kosli begin trail TRAIL-NAME \
  --flow FLOW-NAME \ # Build or Release Flow
  [other flags]
```

See [CLI documentation](/client_reference/kosli_begin_trail) for more details.


### Associated with [Build Flows](#build-flows)

**Name Convention:** `sha`

<ParamField path="sha" type="string" required>
  The Git commit HEAD SHA that triggered the build.
</ParamField>

<Accordion title="examples on TRAIL-NAME">

  <Note>
    Casing does not matter for SHA values, so we do not provide multiple casing options here.
  </Note>

  - `abcdef1234567890abcdef1234567890abcdef12` (full 40-char SHA)
  - `abcdef123` (short SHA)

  **Regex:**

  ```bash
  ^[a-f0-9]+$
  ```
</Accordion>

### Associated with [Release Flows](#release-flows)

**Convention:** <Badge color="green">env</Badge> - <Badge color="green">pr number</Badge>

<ParamField path="env" type="string" required>
  The target deployment environment (e.g., staging, production)
</ParamField>

<ParamField path="pr number" type="string" required>
  The pull request or change request number associated with the deployment.
</ParamField>

<Accordion title="examples on TRAIL-NAME">
  <Tabs>
    <Tab title="snake_case">

    - `staging-42`
    - `production-108`

    **Regex:**

    ```bash
    ^[a-z][a-z0-9_]*-[0-9]+$
    ```
    </Tab>
    <Tab title="camelCase">

    - `staging-42`
    - `production-108`

    **Regex:**

    ```bash
    ^[a-z][a-zA-Z0-9]*-[0-9]+$
    ```
    </Tab>
    <Tab title="PascalCase">

    - `Staging-42`
    - `Production-108`

    **Regex:**

    ```bash
    ^[A-Z][a-zA-Z0-9]*-[0-9]+$
    ```

    </Tab>
  </Tabs>
</Accordion>
