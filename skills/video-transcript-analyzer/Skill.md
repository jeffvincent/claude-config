---
name: Video Transcript Analyzer
description: Analyze customer interview transcripts (SRT or plain text) to generate thematic breakdowns with summary, quotes, topics, timestamps, and full transcript. Use when given video transcripts or asked to create chapter markers.
version: 2.0.0
allowed-tools: [Read, Write]
---

# Video Transcript Analyzer

## Overview
Analyze video transcripts from customer interviews, user research sessions, or feedback calls. Produces a comprehensive structured document with thematic analysis, key insights, chapter markers, and the complete original transcript.

## When to Apply
- User provides a video transcript file (.srt or .txt)
- User asks to "analyze this customer call/interview"
- User requests "chapter markers" or "topical breakdown" from a transcript
- User wants to extract insights from a recorded conversation

Do NOT use for:
- General text summarization (not conversation transcripts)
- Meeting notes that aren't transcripts
- Live conversations (only recorded/transcribed ones)

---

## Workflow

### Step 1: Detect Format

Read the transcript file and determine SRT vs plain text format.
**Read:** `instructions/format-detection.md` for detection rules.

If no video URL found in user context, prompt for it before proceeding.

### Step 2: Collect Metadata

Prompt the user for customer name and company.
**Read:** `instructions/naming-conventions.md` for filename format and prompting rules.

### Step 3: Analyze Themes

Read the entire conversation and identify 5-10 major topics.
**Read:** `instructions/theme-analysis.md` for grouping rules and per-theme structure.

Key rule: group thematically, NOT chronologically.

### Step 4: Extract Quotes

Select 5-8 verbatim quotes from the customer/interviewee.
**Read:** `instructions/quote-extraction.md` for selection criteria and critical rules.

Key rule: quotes must be EXACTLY as spoken. Zero paraphrasing.

### Step 5: Write Call Summary

Write 2-3 paragraphs covering:
- Who was on the call and their role
- What was discussed at high level
- Main themes that emerged
- Key outcomes or next steps

Keep it concise — someone should be able to skip the rest and still understand.

### Step 6: Assemble Document

Use the output template in `templates/analysis-output.md` to structure the final document.

Output filename follows `instructions/naming-conventions.md`.

### Step 7: Run Advisory Board Review

Before finalizing, run the draft through the three personas in `eval/advisory-board.md`:
1. **The Product Researcher** — checks no insights were lost
2. **The Quote Verifier** — ensures verbatim fidelity
3. **The Structure Editor** — evaluates readability and flow

Fix any issues found. Quote Verifier findings are zero-tolerance.

### Step 8: Validate Against Checklist

Run through every item in `eval/checklist.md`. All items must pass before delivering.

### Step 9: Save and Report

Save the document to the appropriate location. Confirm with the user:
- File path and name
- Number of themes identified
- Number of quotes extracted

---

## Related Skills (Workflow Chain)

```
┌─────────────────────┐
│   wistia-uploader   │  → Upload video, get transcript
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────┐
│  video-transcript-analyzer  │  ← YOU ARE HERE
│  (analyze transcript)       │
└──────────┬──────────────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌──────────┐ ┌───────────────────────────┐
│  video-  │ │ interview-synthesis-      │
│  clipper │ │ updater                   │
│ (clips)  │ │ (update synthesis docs)   │
└──────────┘ └───────────────────────────┘
```

---

## Reference Examples

- **Good (SRT + full name):** `examples/good/srt-with-full-name.md`
- **Good (plain text, no URL):** `examples/good/plain-text-no-url.md`
- **Bad (paraphrased quotes):** `examples/bad/paraphrased-quotes.md`

---

## File Map

```
video-transcript-analyzer/
├── Skill.md                              ← You are here (orchestrator)
├── instructions/
│   ├── format-detection.md               ← SRT vs plain text rules
│   ├── quote-extraction.md               ← Verbatim quote selection
│   ├── theme-analysis.md                 ← Grouping and structure rules
│   └── naming-conventions.md             ← Filename format and prompts
├── templates/
│   └── analysis-output.md                ← Output document template
├── examples/
│   ├── good/
│   │   ├── srt-with-full-name.md         ← SRT with timestamps
│   │   └── plain-text-no-url.md          ← Plain text, no video
│   └── bad/
│       └── paraphrased-quotes.md         ← Anti-pattern: cleaned-up quotes
├── eval/
│   ├── checklist.md                      ← Pass/fail validation
│   └── advisory-board.md                 ← 3 reviewer personas
└── resources/
    ├── EXAMPLES.md                       ← [legacy — see examples/]
    └── REFERENCE.md                      ← [legacy — see instructions/]
```

## Security and Privacy
- Handle customer names and company information with care
- If transcript contains sensitive data (credentials, PII beyond names), warn user
- Do not modify or sanitize quotes unless explicitly requested
- Preserve all content from original transcript
