---
title: 'AI access to these docs'
description: 'Use MCP servers, skill.md, and llms.txt to let AI tools read and search Kosli documentation.'
---

Kosli documentation supports AI-friendly access through three mechanisms: an **MCP server** for semantic search, a **skill.md** endpoint that teaches AI assistants how the docs are organized, and **llms.txt** files that provide full documentation content. These let you query Kosli documentation directly from AI coding assistants like Cursor, Claude Code, Windsurf, VS Code with Copilot, and others.

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
    claude mcp add --transport http kosli-docs https://docs.kosli.com/mcp
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

- Ask "How do I attest a Snyk scan in a GitHub Actions workflow?" and get an answer grounded in the official docs.
- Look up Kosli CLI commands, API endpoints, or configuration options while coding.
- Get accurate, up-to-date answers without leaving your editor.

### Inline MCP access

Each documentation page also has a **Copy page** button in the top-right corner. Click it to access options like copying the page as Markdown for LLMs, opening it directly in ChatGPT, Claude, or Perplexity, copying the MCP server URL, or installing the MCP server in Cursor or VS Code.

## skill.md

The `skill.md` endpoint provides a structured overview of Kosli documentation that AI assistants can use to understand how the docs are organized and what topics they cover.

**Endpoint:** `https://docs.kosli.com/skill.md`

This is useful when you want an AI assistant to have a broad understanding of Kosli's documentation structure without loading every page. Your AI tool can read this file to learn:

- What Kosli is and what the docs cover.
- How the documentation is organized (sections, categories).
- Where to find specific topics.

### Use skill.md with Claude Code

To register the Kosli docs as a Claude Code skill, create the skill directory and download the file:

```bash
mkdir -p ~/.claude/skills/kosli-docs
curl -o ~/.claude/skills/kosli-docs/SKILL.md https://docs.kosli.com/skill.md
```

Claude Code auto-discovers skills from `~/.claude/skills/` and will reference the Kosli documentation during your sessions.

<Note>The local skills directory (`~/.claude/skills/`) is specific to Claude Code. Other AI tools can consume `skill.md` directly by fetching the URL — for example, by pasting it into a conversation or configuring the tool to read it as context.</Note>

## llms.txt

Kosli documentation also provides standard `llms.txt` files for AI consumption:

- **`https://docs.kosli.com/llms.txt`** — An index of all documentation pages with descriptions.
- **`https://docs.kosli.com/llms-full.txt`** — The full content of all documentation pages in a single file.

These follow the [llms.txt standard](https://llmstxt.org/) and can be used by any AI tool that supports it. Pass the URL to a tool that accepts an llms.txt source, or download the file and include it as context in your prompt.

## When to use each method

| Method | Best for |
| --- | --- |
| **MCP server** | Targeted questions while coding. Your AI assistant searches the docs and returns relevant answers. |
| **skill.md** | Giving an AI assistant a high-level understanding of what Kosli docs cover and how they are structured. |
| **llms.txt** | Feeding full documentation content to an AI tool that supports the llms.txt standard. |
