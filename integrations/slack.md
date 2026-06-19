---
title: Slack
description: Integrate Kosli with Slack using the Kosli Slack App to receive notifications and query your environments and artifacts directly from Slack.
---

Allows you to configure and receive notifications about changes in your environments and query Kosli about your environments and artifacts without leaving Slack window.

<Steps>
  <Step title="Installation">
    Visit https://slack.kosli.com to add Kosli Slack App to your Slack workspace.
  </Step>
  <Step title="Usage">
    Now that Kosli Slack App is installed you can start using all `/kosli` commands in any channel.

    At any time you can run `/kosli help` to see which commands are available.

    The next step is connecting your Slack user with your Kosli user, use the command below to do that:
    ```
    /kosli login
    ```

    After that you may want to set up default Kosli organization, so you don't have to provide it every time you want to run `/kosli` commands from slack.

    E.g. if the organization name is **my-org**:

    ```
    /kosli config org my-org
    ```

    In case of commands referring to snapshots you can specify snapshot(s) you're interested in multiple ways:
    - `environmentName~N` *N'th behind the latest snapshot*
    - `environmentName#N` *snapshot number N*
    - `environmentName@{YYYY-MM-DDTHH:MM:SS}` *snapshot at specific moment in time in UTC*
    - `environmentName` *the latest snapshot*
  </Step>
  <Step title="Example: Search for an artifact">
    <Card title="Example" img="/images/slack-kosli-search.png">
      Here is an example of *search* command and the response:
      `/kosli search edb1a262`
    </Card>
  </Step>
</Steps>

