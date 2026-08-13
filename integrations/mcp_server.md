---
title: MCP server
description: Connect AI assistants such as Claude Code and Claude Desktop to the Kosli API using the Model Context Protocol.
tag: "BETA"
---

The Kosli MCP server is a [Model Context Protocol](https://modelcontextprotocol.io) server that exposes the Kosli API to AI assistants. Once it is connected, you can ask questions like _"which environments are non-compliant, and why?"_ and the assistant calls the relevant Kosli endpoints to answer.

It is published from [`kosli-dev/mcp-server`](https://github.com/kosli-dev/mcp-server) and distributed as an npm package (`@kosli/mcp-server`) and as a `.mcpb` bundle for Claude Desktop.

<Warning>
The Kosli MCP server is in beta. Tool names, parameters, and behavior may change between releases. Pin a version if you need stability: `npx -y @kosli/mcp-server@0.5.0`.
</Warning>

<Note>
This server reads the data in your Kosli organization. To let an AI assistant search this documentation instead, see [AI access to these docs](/understand_kosli/ai_docs_access). The two are complementary, and you can connect both.
</Note>

## How it works

Rather than ship one tool per Kosli endpoint, the server generates a catalog of actions from Kosli's OpenAPI spec and exposes three generic tools:

| Tool | Purpose |
|------|---------|
| `search_actions` | Fuzzy-search the catalog for relevant actions by natural-language query. |
| `execute_read_action` | Invoke any `GET` action by ID. Auto-allowed in MCP clients. |
| `execute_write_action` | Invoke any `POST`, `PUT`, `PATCH`, or `DELETE` action by ID. Gated behind user approval. |

These are the tool names your client shows as the assistant works, and the name in the prompt when it asks you to approve a write.

<Warning>
`execute_write_action` creates, modifies, and deletes real resources in your Kosli organization. MCP clients gate these calls behind an approval prompt, and that prompt is the only checkpoint before the call is made. An assistant may choose the wrong action, or the right action with the wrong parameters, so read the action ID and parameters before approving. Treat deletions and anything touching service accounts or API keys with particular care.
</Warning>

## Prerequisites

- Node.js v22 or higher, for the `npx`-based install methods. You do not need it for the `.mcpb` bundle, because Claude Desktop ships its own Node runtime.
- A Kosli API key. Use a [personal API key](/user/personal_api_keys) when you run the server on your own machine, or a [service account key](/administration/authentication/service_accounts) for automation.
- An MCP-capable client, such as Claude Code or Claude Desktop.

## Install

<Tabs>
  <Tab title="Claude Code">
    Run this from your project directory, or add `--scope user` to install it globally:

    ```bash
    claude mcp add kosli \
      -e KOSLI_API_TOKEN=your-token \
      -e KOSLI_ORG=your-org \
      -- npx -y @kosli/mcp-server
    ```
  </Tab>
  <Tab title="Claude Desktop (.mcpb)">
    Download the latest `.mcpb` file from the [releases page](https://github.com/kosli-dev/mcp-server/releases) and drag it into Claude Desktop, or double-click it to install. Claude Desktop prompts you for your API key and organization, and stores the secrets in your operating system keychain.

    This is the recommended method for Claude Desktop.

    <Note>
      Extensions installed from a file show an "unverified by Anthropic" warning and do not auto-update, so you need to download and reinstall new versions manually. Both limitations go away once the extension is listed in Anthropic's [Connectors Directory](https://claude.com/docs/connectors/building/submission).
    </Note>
  </Tab>
  <Tab title="Claude Desktop (manual)">
    Add the following to `claude_desktop_config.json`, which you can open from **Settings → Developer → Edit Config**:

    ```json
    {
      "mcpServers": {
        "kosli": {
          "command": "npx",
          "args": ["-y", "@kosli/mcp-server"],
          "env": {
            "KOSLI_API_TOKEN": "your-token",
            "KOSLI_ORG": "your-org"
          }
        }
      }
    }
    ```

    This method auto-updates through `npx` on each restart, but stores your API key in plain text.
  </Tab>
  <Tab title="Other MCP clients">
    The server communicates over stdio. Point any MCP-capable client at the package with `npx -y @kosli/mcp-server` and set the environment variables below.
  </Tab>
</Tabs>

## Configuration

The server reads its configuration from environment variables.

| Variable | Required | Default | Notes |
|----------|----------|---------|-------|
| `KOSLI_API_TOKEN` | yes | - | `KOSLI_API_KEY` is accepted as a fallback. |
| `KOSLI_ORG` | yes | - | Default org. Used as the `org` path parameter when an action does not supply one. |
| `KOSLI_BASE_URL` | no | `https://app.kosli.com` | Use `https://app.us.kosli.com` for US, or your own single-tenant endpoint. |

## Example prompts

These prompts only read data, so they run without an approval step. Replace the environment, flow, and trail names with your own.

### Environments and compliance

- "Which of my environments are non-compliant, and why?"
- "What is running in `prod-aws` right now?"
- "Has anything changed in `prod-aws` since yesterday?"

The assistant answers these from [environment snapshots](/getting_started/environments), so it can report both the current state and the reasons an environment is not compliant.

### Audit and evidence

- "List every deployment to `prod-aws` in the last 30 days."
- "What attestations are on trail `release-456` in flow `my-release`?"
- "Which artifacts running in `prod-aws` have no security scan attestation?"

The last prompt takes several tool calls, because the assistant has to list what is running and then check the [attestations](/getting_started/attestations) on each artifact. Expect it to be slower than a single lookup, and check the artifact list it worked from before relying on the answer.

## Limitations

- The action catalog is generated from a snapshot of the OpenAPI spec. New endpoints become available when the catalog is regenerated and a new version of the package is published.
- Ambiguous questions may take several `search_actions` calls before the assistant settles on the right action.
- Responses are whatever the Kosli API returns. Large responses consume a lot of context, so ask for specific fields when you can.

## Feedback

The server is in beta and we want to hear how it works for you. Email [support@kosli.com](mailto:support@kosli.com) or open an issue in [`kosli-dev/mcp-server`](https://github.com/kosli-dev/mcp-server/issues).
