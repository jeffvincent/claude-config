---
name: readwise-skill
description: Import books, articles, podcasts, and other content from Readwise into Content Notes with all highlights and annotations. Use when user wants to import specific content from their Readwise library.
version: 1.0.0
dependencies:
  - python3
  - requests
  - python-dotenv
allowed-tools: [Bash, Read, Write]
---

# Readwise Import Skill

## Overview
This skill imports books, articles, podcasts, and other content from your Readwise library into Content Notes as source documents. It fetches all highlights, annotations, and metadata, creating a properly formatted markdown document that can be analyzed later.

## When to Apply
Use this skill when:
- User wants to import a specific book, article, or podcast from Readwise
- User says "import [item name] from Readwise"
- User asks to "pull in highlights from [item]"
- User wants to sync/update existing Readwise imports with new highlights
- User asks to search their Readwise library

Do NOT use this skill for:
- Bulk importing entire Readwise library (use on-demand only)
- Reading Readwise content without importing to Content Notes
- Managing Readwise account settings

## Inputs
1. **Item identifier** - Either:
   - Item title/name (e.g., "Atomic Habits", "The Mom Test")
   - Author name (e.g., "Tim Urban", "Rob Fitzpatrick")
   - Readwise book ID (if known)
2. **Action** - import (new) or sync (update existing)

## Outputs
- Source document in `/sources/` directory
- Filename format: `YYYY-MM-DD_Author_Title_Readwise.md`
- Includes: metadata, all highlights in chronological order, annotations, tags
- Git commit (automatic)
- Summary of what was imported

## Setup Instructions

### First Time Setup
1. **Get Readwise API Token**:
   - Visit: https://readwise.io/access_token
   - Copy your token

2. **Configure Credentials**:
   ```bash
   echo "READWISE_API_TOKEN=your_token_here" > ~/.claude/secrets/readwise/.env
   ```

3. **Install Dependencies**:
   ```bash
   cd ~/.claude/skills/readwise-skill
   pip3 install -r requirements.txt
   ```

4. **Test Authentication**:
   ```bash
   cd ~/.claude/skills/readwise-skill/scripts
   python3 auth.py
   ```

## Instructions for Claude

### Step 1: Validate Setup
- Check that `~/.claude/secrets/readwise/.env` exists with `READWISE_API_TOKEN`
- If not configured, provide setup instructions to user
- Test authentication:
  ```bash
  cd ~/.claude/skills/readwise-skill/scripts
  python3 auth.py
  ```

### Step 2: Search for Content
If user provides a title or author name (not book ID):
```bash
cd ~/.claude/skills/readwise-skill/scripts
python3 search.py --query "atomic habits"
```

For specific categories:
```bash
python3 search.py --query "tim urban" --category articles
```

Show results to user and ask which one to import.

### Step 3: Import Content
Once you have the book ID:
```bash
cd ~/.claude/skills/readwise-skill/scripts
python3 import_item.py --book-id 12345 --output-dir "/Users/jvincent/Projects/Personal/Content Notes/sources"
```

The script outputs JSON with:
```json
{
  "success": true,
  "filename": "2026-02-10_James-Clear_Atomic-Habits_Readwise.md",
  "filepath": "/full/path/to/file.md",
  "title": "Atomic Habits",
  "author": "James Clear",
  "category": "books",
  "num_highlights": 47,
  "book_id": "12345"
}
```

### Step 4: Report Results
Tell the user:
- ✅ Successfully imported [Title] by [Author]
- 📝 [N] highlights imported
- 📂 Saved to: `sources/[filename]`
- 🔗 Book ID: [id] (for future syncing)

### Step 5: Auto-Commit to Git
After successful import, automatically commit to git:
```bash
cd "/Users/jvincent/Projects/Personal/Content Notes"
git add .
git commit -m "Add Readwise import: [Title] by [Author]

Imported [N] highlights from Readwise

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

### Step 6: Suggest Next Steps
After import, ask:
- "Would you like me to analyze this content and generate insights?"
- This leads to the `readwise-content-analyzer` skill

## Syncing Updates

To update an existing import with new highlights:
```bash
cd ~/.claude/skills/readwise-skill/scripts
python3 sync.py --filepath "/Users/jvincent/Projects/Personal/Content Notes/sources/2026-02-10_James-Clear_Atomic-Habits_Readwise.md"
```

The script:
- Extracts book ID from the existing file
- Fetches latest highlights from Readwise
- Regenerates the entire document with all highlights
- Reports how many new highlights were added

After syncing, commit the changes to git.

## Output Format

Generated source documents have this structure:

```markdown
# [Title] | [Author] - Readwise

## Metadata
- **Type**: Book / Article / Podcast / etc.
- **Author**: [Author name]
- **Source URL**: [URL if available]
- **Date Imported**: YYYY-MM-DD
- **Total Highlights**: [count]
- **Readwise Tags**: #tag1, #tag2

## Document Notes
[Your document-level notes from Readwise]

## Your Highlights

### Highlight 1 (Page 15)
> "The highlighted text goes here"

**Your Note**: Your annotation from Readwise

**Tags**: #important, #actionable

---

### Highlight 2 (Position 234)
> "Another highlight"

---

[... all highlights in chronological order ...]

## Synthesis Analysis
_To be completed during analysis phase_

## Key Themes Identified
_To be completed during analysis phase_

## Related Synthesis Documents
_Add connections to existing themes:_
- [[Theme 1]]
- [[Theme 2]]

## Source Information
- **Readwise Book ID**: 12345
- **Category**: books
- **Original URL**: https://...
```

## Error Handling

Common errors:
- **"READWISE_API_TOKEN not found"**: Run setup instructions
- **"Authentication failed"**: Token is invalid, regenerate at readwise.io/access_token
- **"No results found"**: Try different search terms or check category
- **"No highlights found"**: Item exists but has no highlights
- **Rate limit exceeded**: Wait and retry (API limits: 240/min general, 20/min for list endpoints)

## Examples

### Example 1: Import a Book
**User**: "Import 'The Mom Test' from Readwise"

**Claude**:
1. Searches: `python3 search.py --query "the mom test"`
2. Shows results:
   ```
   Found 1 result(s):

   1. [BOOKS] The Mom Test
      Author: Rob Fitzpatrick
      Highlights: 23
      ID: 12345
   ```
3. Confirms with user
4. Imports: `python3 import_item.py --book-id 12345 --output-dir ".../sources"`
5. Reports: "✅ Imported The Mom Test by Rob Fitzpatrick with 23 highlights"
6. Commits to git
7. Asks: "Would you like me to analyze this content?"

### Example 2: Import an Article
**User**: "Import that Tim Urban article about AI"

**Claude**:
1. Searches: `python3 search.py --query "tim urban" --category articles`
2. Shows multiple results, user picks one
3. Imports the article
4. Commits to git

### Example 3: Sync Updates
**User**: "Sync my Atomic Habits import with new highlights"

**Claude**:
1. Finds existing file: `sources/2026-02-10_James-Clear_Atomic-Habits_Readwise.md`
2. Syncs: `python3 sync.py --filepath "..."`
3. Reports: "Updated: 3 new highlights (47 → 50)"
4. Commits changes to git

### Example 4: Search and Browse
**User**: "What articles do I have from Y Combinator in Readwise?"

**Claude**:
1. Searches: `python3 search.py --query "y combinator" --category articles`
2. Lists all matches
3. Asks if user wants to import any

## Related Skills

This skill is part of the Readwise → Analysis workflow:

```
┌─────────────────────┐
│   readwise-skill    │  ← YOU ARE HERE
│   (import content)  │
└──────────┬──────────┘
           │
           ▼
┌──────────────────────────────┐
│  readwise-content-analyzer   │  → Analyze highlights + content
│  (generate insights)         │     Generate synthesis documents
└──────────────────────────────┘
```

**Next steps after import**:
- Use `readwise-content-analyzer` to analyze the highlights
- Generate/update synthesis documents
- Connect to existing themes

## Testing Checklist
- [ ] Authentication works with valid token
- [ ] Can search by title
- [ ] Can search by author
- [ ] Can filter by category
- [ ] Can import book with highlights
- [ ] Can import article with highlights
- [ ] Generated markdown is valid
- [ ] Highlights are in chronological order
- [ ] Annotations are preserved
- [ ] Tags are preserved
- [ ] Can sync updates to existing file
- [ ] Git commits work correctly
- [ ] Proper error messages for missing setup
- [ ] Handles rate limiting gracefully

## API Rate Limits
- General endpoints: 240 requests/minute
- List endpoints (books, highlights): 20 requests/minute
- Scripts handle rate limits automatically
- Large imports may take several minutes

## Security
- **API Token**: Stored in `~/.claude/secrets/readwise/.env` (gitignored)
- **Never log or display token**
- If token compromised, regenerate at readwise.io/access_token
- Source documents may contain personal notes/highlights
- Always commit to private repository

## Readwise API Reference
- Base URL: https://readwise.io/api/v2
- Auth: Token-based header
- Docs: https://readwise.io/api_deets
- Categories: books, articles, tweets, podcasts, supplementals, videos
