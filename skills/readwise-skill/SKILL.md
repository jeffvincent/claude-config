---
name: readwise-skill
description: Import books, articles, podcasts, and other content from Readwise into Content Notes with all highlights and annotations. Use when user wants to import specific content from their Readwise library.
version: 2.0.0
allowed-tools: [ToolSearch, Read, Write, Edit, Bash]
---

# Readwise Import Skill

## Overview

Imports content from Readwise/Reader into Content Notes as source documents using the Readwise MCP server. Fetches highlights, annotations, and metadata, creating a formatted markdown document for analysis.

No Python scripts, no API token management — the MCP handles auth.

## When to Apply

Use this skill when:
- User wants to import specific content from Readwise
- User says "just import" or "import only"
- User wants to search their Readwise library without importing
- User wants to sync/update an existing import with new highlights

**For analysis requests** ("analyze X from Readwise", "generate insights from X"), use `readwise-content-analyzer` instead — it handles both import and analysis.

## Inputs

1. **Item identifier** — title, author name, or topic
2. **Action** — import (new) or sync (update existing)

## Outputs

- Source document at: `"/Users/jvincent/Projects/Knowledge System/notes/content notes/sources/YYYY-MM-DD_Author_Title_Readwise.md"`
- Git commit (automatic)

---

## Instructions for Claude

### Step 0: Load MCP Tools

Before any Readwise operation, load the required tools:

```
ToolSearch("select:mcp__readwise__reader_search_documents,mcp__readwise__reader_get_document_details,mcp__readwise__reader_get_document_highlights,mcp__readwise__readwise_search_highlights,mcp__readwise__reader_list_documents")
```

---

### Step 1: Check for Existing Local File

Search for an existing import:
```
Glob: /Users/jvincent/Projects/Knowledge System/notes/content notes/sources/*_Readwise.md
```

Check if any filename fuzzy-matches the requested title. If found → jump to **Sync** section below.

---

### Step 2: Search Readwise/Reader

Use `reader_search_documents` with the title or author as the query. This uses semantic search and returns document metadata including IDs, URLs, and summaries.

If Reader search returns no match, try `readwise_search_highlights` with the same query — some older imports exist in Readwise classic but not Reader.

Show results to user (title, author, category, highlight count) and ask which to import if multiple matches.

---

### Step 3: Get Document Details + Highlights

Once you have the document ID:

1. Call `reader_get_document_details` with the document ID — returns full metadata (title, author, URL, category, tags, summary)
2. Call `reader_get_document_highlights` with the document ID — returns all highlights with text, notes, and location

---

### Step 4: Write the Local Source File

Create the file at:
```
/Users/jvincent/Projects/Knowledge System/notes/content notes/sources/YYYY-MM-DD_Author_Title_Readwise.md
```

Use today's date. Sanitize author and title for the filename (Title-Case, hyphens for spaces).

**File format:**

```markdown
# [Title] | [Author] - Readwise

## Metadata
- **Type**: [book / article / podcast / video / tweet]
- **Author**: [Author name]
- **Source URL**: [URL if available]
- **Date Imported**: YYYY-MM-DD
- **Total Highlights**: [count]
- **Readwise Tags**: [tags if any]
- **Reader Document ID**: [id]

## Document Notes
[Document-level note from Readwise, if any]

## Your Highlights

### Highlight 1
> "[highlight text]"

**Your Note**: [annotation, if any]

**Location**: [page number or position if available]

---

### Highlight 2
> "[highlight text]"

---

[... all highlights in order ...]

## Synthesis Analysis
_To be completed during analysis phase_

## Key Themes Identified
_To be completed during analysis phase_

## Related Synthesis Documents
_Add connections to existing themes:_
- [[Theme 1]]
- [[Theme 2]]

## Source Information
- **Reader Document ID**: [id]
- **Category**: [category]
- **Original URL**: [url]
```

---

### Step 5: Commit to Git

```bash
cd "/Users/jvincent/Projects/Knowledge System/notes/content notes"
git add "sources/[filename].md"
git commit -m "Add Readwise import: [Title] by [Author]

[N] highlights imported via Readwise MCP

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

---

### Step 6: Report and Suggest Next Steps

Tell the user:
- Imported [Title] by [Author]
- [N] highlights
- Saved to: `sources/[filename]`

Ask: "Would you like me to analyze this content and generate insights?" → leads to `readwise-content-analyzer`

---

## Syncing an Existing Import

If the local file already exists and user wants to update with new highlights:

1. Read the existing file to extract the Reader Document ID from `## Source Information`
2. Call `reader_get_document_highlights` with that ID
3. Compare returned highlights against what's in the file
4. If new highlights exist: append them in the `## Your Highlights` section, update `Total Highlights` count in metadata
5. Commit: `"Sync Readwise highlights: [Title] — [N] new highlights"`

---

## Browsing the Inbox / Unread Queue

If user asks "what's in my Readwise inbox" or "what have I saved recently":

Load `reader_list_documents` and filter by location:
- `location: "new"` for the inbox (unread)
- `location: "shortlist"` for prioritized reading
- `location: "later"` for the read-later queue

Present as a table: title, author, category, summary.

---

## Error Handling

- **No search results**: Try broader terms, or try `readwise_search_highlights` as fallback
- **Document found but no highlights**: Note this — content may be saved but not yet read/highlighted
- **MCP tools unavailable**: ToolSearch will report if the Readwise MCP server is disconnected; tell the user and skip

---

## Related Skills

```
readwise-skill (YOU ARE HERE)
    ↓ import + local file
readwise-content-analyzer
    ↓ analyze highlights + update syntheses
reading-partner
    ↓ intellectual discussion of content
```

`/reading-review` uses the MCP directly without this skill — it's a weekly sweep, not a per-item import.

## MCP Reference

Docs: https://readwise.io/mcp

Key tools used by this skill:
- `reader_search_documents` — semantic search across Reader library
- `reader_get_document_details` — full metadata for a document
- `reader_get_document_highlights` — all highlights for a document
- `reader_list_documents` — browse by location (new/later/shortlist/archive)
- `readwise_search_highlights` — fallback search via Readwise classic API
