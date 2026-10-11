---
name: notebooklm-skill
description: "Query NotebookLM notebooks managed by others (e.g., customer feedback corpora). Ask questions, list notebooks, view sources. Use when user mentions NotebookLM, wants to query a shared notebook, or references a configured notebook alias."
version: 1.0.0
allowed-tools: [Bash, Read, Write]
---

# NotebookLM Integration Skill

Query Google NotebookLM notebooks from Claude Code. Designed for accessing shared notebooks managed by others (e.g., large customer feedback corpora, research collections).

## Prerequisites

Authentication must be set up first:
```bash
pip3 install --break-system-packages "notebooklm-py[browser]"
playwright install chromium
notebooklm login
```

Cookies expire every few weeks — re-run `notebooklm login` when you get auth errors.

## Notebook Registry

Notebooks can be registered with friendly aliases in:
`~/.claude/skills/notebooklm-skill/lib/notebooks.json`

Format:
```json
{
  "notebooks": {
    "customer-feedback": "abc123-notebook-id",
    "uxr-research": "def456-notebook-id"
  }
}
```

To discover notebook IDs:
```bash
python3 ~/.claude/skills/notebooklm-skill/lib/query.py list
```

## Operations

### Ask a Question
```bash
python3 ~/.claude/skills/notebooklm-skill/lib/query.py ask <notebook_id> "What are the top pain points?"
```

Returns JSON with `answer`, `conversation_id`, and `references` (with source titles and cited text).

### Follow-up Question (same conversation)
```bash
python3 ~/.claude/skills/notebooklm-skill/lib/query.py ask <notebook_id> "Tell me more about X" --conversation-id <conv_id>
```

### List All Notebooks
```bash
python3 ~/.claude/skills/notebooklm-skill/lib/query.py list
```

### Get Notebook Summary
```bash
python3 ~/.claude/skills/notebooklm-skill/lib/query.py summary <notebook_id>
```

### List Sources in a Notebook
```bash
python3 ~/.claude/skills/notebooklm-skill/lib/query.py sources <notebook_id>
```

## Usage Pattern

When the user asks a question targeting a NotebookLM notebook:

1. **Resolve the notebook**: Check the registry (`notebooks.json`) for the alias, or use the ID directly
2. **Ask the question**: Run the `ask` command and capture the JSON output
3. **Present the answer**: Show the answer with citations. Include source titles when available.
4. **Follow up if needed**: Use the `conversation_id` from the response for follow-up questions

When the user wants to browse available notebooks:
1. Run `list` to show all accessible notebooks
2. Optionally run `summary` on a specific notebook to see what it covers

## Error Handling

- **FileNotFoundError mentioning storage_state.json**: Auth expired. Tell user to run `! notebooklm login`
- **ChatError with rate limit**: Wait a few seconds and retry
- **RPCError**: Library may need updating (`pip3 install --break-system-packages --upgrade notebooklm-py`)

## Important Notes

- This uses **unofficial, reverse-engineered Google APIs** — it can break without notice
- Answers come from Google's Gemini model running against the notebook's sources, not from Claude
- Best for querying large corpora you don't want to duplicate locally
- Cookie auth expires every few weeks — user must re-authenticate via browser
