---
name: readwise-content-analyzer
description: Analyze Readwise source documents (books, articles, podcasts) to generate thematic insights, extract key patterns, and update synthesis documents. Use after importing content with readwise-skill.
version: 1.0.0
dependencies:
  - python3
  - requests
allowed-tools: [Read, Write, Edit, Glob, WebFetch, Bash]
---

# Readwise Content Analyzer

## Overview
This skill analyzes imported Readwise source documents to extract themes, generate insights, and update or create synthesis documents. It works with your curated highlights as the primary signal, optionally fetching original content for additional context.

## When to Apply
Use this skill:
- When user says "analyze [book/article name] from Readwise"
- When user asks to "generate insights" from a Readwise item
- When user wants to identify themes in their Readwise highlights
- When user wants to update synthesis documents with new examples
- When user says "what themes are in [book/article name]?"
- After importing content with `readwise-skill` (if already imported)

**IMPORTANT**: This skill handles BOTH import and analysis in a single workflow. If the content isn't already imported, it will import it first, then analyze it.

Do NOT use this skill for:
- Just browsing/searching Readwise (use `readwise-skill` for search only)
- Analyzing non-Readwise source documents

## Inputs
1. **Item identifier** - Either:
   - Item title/name (e.g., "The Mom Test", "Atomic Habits")
   - Author name (e.g., "Tim Urban")
   - Existing source document path (if already imported)
2. **Analysis depth** (optional) - Quick overview vs. deep analysis

## Outputs
- Theme identification report
- Key insights and patterns
- Suggested synthesis document connections
- New or updated synthesis documents (with user approval)
- Git commit (automatic)

## Instructions for Claude

### Step 0: Check if Import is Needed (CRITICAL)
Before analyzing, determine if the content needs to be imported first:

**A. If user provides a title/name (e.g., "analyze 'The Mom Test' from Readwise")**:
1. Search for existing source document:
   ```
   Glob: /Users/jvincent/Projects/Personal/Content Notes/sources/*_Readwise.md
   ```
2. Check if any filename matches the title (case-insensitive, fuzzy match)
3. **If NOT found**: Import first using readwise-skill
   - Search Readwise library: `cd ~/.claude/skills/readwise-skill/scripts && python3 search.py --query "the mom test"`
   - Show results to user for confirmation
   - Import: `python3 import_item.py --book-id [id] --output-dir "/Users/jvincent/Projects/Personal/Content Notes/sources"`
   - Commit the import to git
   - Then proceed to analysis (Step 1 below)
4. **If found**: Proceed directly to analysis (Step 1 below)

**B. If user provides a file path**: Skip to Step 1 (already imported)

**Example**:
```
User: "analyze 'the mom test' from readwise"

Claude:
1. Searches sources/ directory - not found
2. Searches Readwise: python3 search.py --query "the mom test"
3. Shows: "Found: The Mom Test by Rob Fitzpatrick (23 highlights)"
4. User confirms (or auto-confirm if only one match)
5. Imports: python3 import_item.py --book-id 12345 ...
6. Reports: "✅ Imported The Mom Test with 23 highlights"
7. Proceeds to analysis below
```

### Step 1: Read the Source Document
Use the Read tool to load the Readwise source document:
```
Read: /Users/jvincent/Projects/Personal/Content Notes/sources/YYYY-MM-DD_Author_Title_Readwise.md
```

Extract:
- Title, author, and type (book, article, podcast)
- Source URL (if available)
- All highlights with their locations
- All annotations/notes
- Existing Readwise tags

### Step 2: Fetch Original Content (If Applicable)
For articles, blog posts, videos, and podcasts with URLs:
- Use WebFetch tool to retrieve the original content
- This provides additional context beyond just highlights
- For videos: extract key concepts from the description/transcript if available
- For podcasts: look for show notes or episode descriptions

**Example**:
```
WebFetch:
  url: [source URL from metadata]
  prompt: "Extract the main arguments, key points, and overall thesis of this content.
          Provide a comprehensive summary that complements the user's highlights."
```

Skip this step for books (no URL) or if user's highlights are sufficient.

### Step 3: Analyze Highlights and Identify Themes
Analyze all highlights to identify:

**A. Core Themes**
- What recurring concepts appear across highlights?
- What patterns emerge?
- Group related highlights by theme

**B. Key Insights**
- What are the most powerful ideas?
- What actionable takeaways exist?
- What surprising or counterintuitive points appear?

**C. Connections to Existing Synthesis Documents**
Read existing synthesis documents to find connections:
```
Glob: /Users/jvincent/Projects/Personal/Content Notes/syntheses/*.md
```

For each existing synthesis:
- Does this source provide examples or quotes?
- Does it reinforce, challenge, or extend existing themes?
- Identify 2-3 most relevant synthesis documents

### Step 4: Present Analysis to User
Create a comprehensive report:

```markdown
## Analysis: [Title] by [Author]

### Content Overview
[2-3 sentence summary based on highlights and/or original content]

### Identified Themes

#### 1. [Theme Name]
**Definition**: [What this theme is about]

**Supporting Highlights**:
- [Highlight 1 with location]
- [Highlight 2 with location]
- [Highlight 3 with location]

**Key Insight**: [Synthesis of what these highlights reveal]

#### 2. [Theme Name]
[Repeat structure]

### Connections to Existing Synthesis Documents

#### Recommended Updates:
1. **[[Deep Relationships]]**
   - Add example from Highlight 5 about [topic]
   - Reinforces concept of [existing idea in synthesis]

2. **[[Quality Obsession]]**
   - Add quote from Highlight 12
   - Provides new angle on [existing concept]

3. **[[New Theme Name]]** (CREATE NEW)
   - This source introduces a theme not yet in synthesis documents
   - Based on highlights 3, 7, 15, 23
   - Would complement existing themes on [related topics]

### Recommended Actions
- [ ] Update [[Existing Synthesis 1]] with 3 new examples
- [ ] Update [[Existing Synthesis 2]] with 2 quotes
- [ ] Create new synthesis document: [[New Theme]]
- [ ] Add cross-references between related themes
```

Ask user: "Would you like me to proceed with updating the synthesis documents?"

### Step 5: Update Synthesis Documents (With Approval)
For each synthesis document to update:

**A. Read Existing Synthesis**
```
Read: /Users/jvincent/Projects/Personal/Content Notes/syntheses/[theme-name].md
```

**B. Identify Update Locations**
- Find appropriate section for new examples
- Maintain existing structure
- Add after similar examples

**C. Add New Content**
Use Edit tool to add:
- New quotes from highlights (with source attribution)
- New examples with context
- Source reference at bottom

**Example Edit**:
```
Edit: syntheses/Quality Obsession.md
old_string: |
  ## Sources
  - [[2026-01-15_Michael-Dell_Building-Dell_Podcast]]

new_string: |
  ## Examples from [New Source]
  ### [Specific Example Title]
  [Quote from highlight]

  [2-3 sentences explaining significance and connection to theme]

  ## Sources
  - [[2026-01-15_Michael-Dell_Building-Dell_Podcast]]
  - [[2026-02-10_Author_Title_Readwise]]
```

**D. Create New Synthesis Documents (If Needed)**
If a new theme emerges:
1. Check existing synthesis structure and templates
2. Create new synthesis document following the pattern
3. Include core concept, examples, and sources
4. Add cross-references to related themes

### Step 6: Update Source Document
Add analysis results back to the source document:

```
Edit: sources/YYYY-MM-DD_Author_Title_Readwise.md
old_string: |
  ## Synthesis Analysis
  _To be completed during analysis phase_

  ## Key Themes Identified
  _To be completed during analysis phase_

  ## Related Synthesis Documents
  _Add connections to existing themes:_
  - [[Theme 1]]
  - [[Theme 2]]

new_string: |
  ## Synthesis Analysis
  [2-3 paragraph summary of key insights and patterns]

  ## Key Themes Identified
  1. **[Theme 1]**: [Brief description]
  2. **[Theme 2]**: [Brief description]
  3. **[Theme 3]**: [Brief description]

  ## Related Synthesis Documents
  - [[Existing Theme 1]] - [How it connects]
  - [[Existing Theme 2]] - [How it connects]
  - [[New Theme]] - [New synthesis created from this source]
```

### Step 7: Commit Changes to Git
After all updates are complete:
```bash
cd "/Users/jvincent/Projects/Personal/Content Notes"
git add .
git commit -m "Analyze Readwise content: [Title] by [Author]

Analysis and synthesis updates:
- Identified themes: [theme1], [theme2], [theme3]
- Updated [N] synthesis documents
- Added [N] new examples and quotes

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

### Step 8: Summary Report
Provide final summary:
```
✅ Analysis complete for "[Title]"

📊 Analysis Results:
  - [N] themes identified
  - [N] synthesis documents updated
  - [N] new synthesis documents created
  - [N] quotes and examples added

📁 Updated Files:
  - sources/[filename].md (added analysis)
  - syntheses/[theme1].md (added X examples)
  - syntheses/[theme2].md (added X quotes)
  - syntheses/[new-theme].md (created new)

🔗 Key Connections:
  - [[Theme 1]]: [Brief note]
  - [[Theme 2]]: [Brief note]

✨ Next Steps:
  Consider reviewing related content:
  - [[Related Source 1]]
  - [[Related Source 2]]
```

## Analysis Best Practices

### For Books
- Focus on user's highlights (they've already done the curation)
- Group highlights by chapter/section if location data available
- Look for progression of ideas across the book
- Identify author's main thesis and supporting arguments

### For Articles
- Fetch original content for full context
- Compare what user highlighted vs. full article
- Extract author's main argument
- Note any counterarguments or nuances

### For Podcasts
- Highlights are key moments/quotes
- Fetch show notes or episode description if available
- Note guest name and background
- Identify actionable advice or mental models shared

### For Videos
- Similar to podcasts
- Fetch video description/transcript if possible
- Note timestamps in highlights
- Identify visual concepts that were demonstrated

## Quality Checks
- [ ] All themes have supporting quotes from highlights
- [ ] Synthesis updates maintain existing document structure
- [ ] Source attributions are accurate (author, location)
- [ ] Cross-references use correct wiki-link format `[[filename]]`
- [ ] New synthesis documents follow existing template patterns
- [ ] Git commit message accurately describes changes
- [ ] No duplicate quotes in synthesis documents

## Error Handling
- If source URL is dead/inaccessible: analyze highlights only
- If WebFetch fails: continue with highlights-based analysis
- If synthesis document structure is unclear: ask user for guidance
- If theme doesn't fit existing syntheses: propose new synthesis document

## Examples

### Example 1: Analyze and Import (Combined Workflow)
**User**: "analyze 'the mom test' from readwise"

**Claude**:
1. Searches sources/ directory - not found
2. Imports from Readwise:
   - Searches: `python3 search.py --query "the mom test"`
   - Shows: "Found: The Mom Test by Rob Fitzpatrick (23 highlights)"
   - Imports: Creates `sources/2026-02-10_Rob-Fitzpatrick_The-Mom-Test_Readwise.md`
   - Commits import
3. Analyzes 23 highlights
4. Identifies themes:
   - Customer Discovery
   - Asking Better Questions
   - Validation vs. Compliments
5. Finds connections:
   - Relates to [[Curiosity - Deep Understanding]]
   - Relates to [[Quality Obsession]]
6. Presents analysis
7. User approves updates
8. Adds 5 new examples to existing syntheses
9. Updates source document with analysis
10. Commits analysis changes

### Example 2: Analyze Already Imported Content
**User**: "Analyze The Mom Test highlights"

**Claude**:
1. Searches sources/ and finds: `sources/2026-02-10_Rob-Fitzpatrick_The-Mom-Test_Readwise.md`
2. Skips import (already exists)
3. Proceeds directly to analysis
4. [Same as steps 3-10 above]

### Example 3: Analyze an Article with URL
**User**: "Analyze that Tim Urban article from Readwise"

**Claude**:
1. Reads: `sources/2026-02-10_Tim-Urban_AI-Revolution_Readwise.md`
2. Uses WebFetch to get full article
3. Analyzes 15 highlights + full article context
4. Identifies themes:
   - Exponential Progress
   - Existential Risk
   - Human vs. AI Intelligence
5. Proposes new synthesis: [[Exponential Thinking]]
6. User approves
7. Creates new synthesis document
8. Updates source with analysis
9. Commits to git

### Example 4: Quick Theme Overview
**User**: "What themes are in my Atomic Habits highlights from Readwise?"

**Claude**:
1. Reads source document
2. Quickly scans highlights
3. Reports themes:
   - Systems over goals
   - Identity-based habits
   - Environment design
   - 1% improvements
4. Shows which synthesis docs could be updated
5. Asks if user wants full analysis

## Related Skills

Workflow sequence:

```
[readwise-skill]
    ↓
    Import content + highlights
    ↓
    Creates source document
    ↓
[readwise-content-analyzer]  ← YOU ARE HERE
    ↓
    Analyzes highlights
    ↓
    Updates/creates synthesis docs
    ↓
    Cross-references themes
```

## Notes
- This skill is **collaborative** - always show analysis before making updates
- User's highlights are the **primary signal** - they've already curated the content
- Original content is **supplementary** - adds context but highlights are key
- Synthesis documents should **grow organically** - only create new ones when truly needed
- **Preserve existing structure** in synthesis documents
- **Maintain voice consistency** - match tone of existing syntheses
