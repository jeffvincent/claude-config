# Readwise Content Analyzer Skill

Analyze Readwise source documents (imported via readwise-skill) to generate thematic insights and update synthesis documents.

## Overview

This skill works with Readwise source documents to:
1. Analyze highlights and annotations
2. For articles/videos/podcasts: fetch original content via URL
3. Identify key themes and patterns
4. Generate or update synthesis documents
5. Create cross-references to existing themes

## Usage

Use after importing content with `readwise-skill`:

```
You: "Analyze the Rob Fitzpatrick source doc and generate insights"
```

## Features

- **Highlight Analysis**: Extracts themes from your curated highlights
- **Content Fetching**: Retrieves original article/video content when available
- **Theme Identification**: Identifies patterns across highlights
- **Synthesis Generation**: Creates or updates synthesis documents
- **Cross-Referencing**: Connects to existing themes in Content Notes

## Workflow

1. Import content using `readwise-skill`
2. Invoke this skill to analyze
3. Review suggested themes and connections
4. Approve synthesis document updates
5. Auto-commit changes to git

## Related Skills

- `readwise-skill`: Import content from Readwise
- `interview-synthesis-updater`: Similar workflow for video interviews
