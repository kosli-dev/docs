---
title: 'AI access to these docs'
description: 'Use MCP servers and skill.md to let AI tools read and search Kosli documentation.'
---

Kosli documentation supports AI-friendly access through two mechanisms: an **MCP server** for semantic search and a **skill.md** endpoint that teaches AI assistants how to work with the docs. These let you query Kosli documentation directly from AI coding assistants like Cursor, Claude Code, Windsurf, VS Code with Copilot, and others.

## MCP server

The Model Context Protocol (MCP) server lets AI tools search Kosli documentation semantically. Instead of copy-pasting docs into a chat window, you connect your AI assistant to the MCP endpoint and it can search the docs on its own.

**Endpoint:** `https://docs.kosli.com/mcp`

### Set up MCP in your AI tool

<Tabs>
  <Tab title="Cursor">
    Add the following to your `.cursor/mcp.json` file:

    ```json
    {
      "mcpServers": {
        "kosli-docs": {
          "url": "https://docs.kosli.com/mcp"
        }
      }
    }
    ```
  </Tab>
  <Tab title="Claude Code">
    Run the following command:

    ```bash
    claude mcp add kosli-docs https://docs.kosli.com/mcp
    ```
  </Tab>
  <Tab title="Windsurf">
    Add the following to your `~/.codeium/windsurf/mcp_config.json` file:

    ```json
    {
      "mcpServers": {
        "kosli-docs": {
          "type": "http",
          "url": "https://docs.kosli.com/mcp"
        }
      }
    }
    ```
  </Tab>
  <Tab title="VS Code (Copilot)">
    Add the following to your `.vscode/mcp.json` file:

    ```json
    {
      "servers": {
        "kosli-docs": {
          "type": "http",
          "url": "https://docs.kosli.com/mcp"
        }
      }
    }
    ```
  </Tab>
</Tabs>

Once connected, your AI assistant gains a search tool it can use to look up Kosli concepts, CLI commands, API endpoints, and more — without you having to find and paste the relevant page.

### What you can do with it

- Ask your AI assistant questions about Kosli and it will search the docs automatically.
- Get accurate, up-to-date answers grounded in the official documentation.
- Reference Kosli CLI commands, API endpoints, or configuration options while coding.

### Inline MCP access

You can also connect to the MCP server directly from any documentation page. Look for the AI chat icon in the contextual toolbar on each page to ask questions about that page's content.

## skill.md

The `skill.md` endpoint provides a structured overview of Kosli documentation that AI assistants can use to understand how the docs are organized and what topics they cover.

**Endpoint:** `https://docs.kosli.com/skill.md`

This is useful when you want an AI assistant to have a broad understanding of Kosli's documentation structure without loading every page. Your AI tool can read this file to learn:

- What Kosli is and what the docs cover.
- How the documentation is organized (sections, categories).
- Where to find specific topics.

### Use skill.md with Claude Code

```bash
claude skills add https://docs.kosli.com/skill.md
```

This registers the Kosli documentation as a skill that Claude Code can reference during your session.

## llms.txt

Kosli documentation also provides standard `llms.txt` files for AI consumption:

- **`https://docs.kosli.com/llms.txt`** — An index of all documentation pages with descriptions.
- **`https://docs.kosli.com/llms-full.txt`** — The full content of all documentation pages in a single file.

These follow the [llms.txt standard](https://llmstxt.org/) and can be used by any AI tool that supports it.

## When to use each method

| Method | Best for |
| --- | --- |
| **MCP server** | Targeted questions while coding. Your AI assistant searches the docs and returns relevant answers. |
| **skill.md** | Giving an AI assistant a high-level understanding of what Kosli docs cover and how they are structured. |
| **llms.txt** | Feeding full documentation content to an AI tool that supports the llms.txt standard. |
