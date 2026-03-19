# Good Example: Plain Text Transcript, No Video URL

**Input:** Plain text transcript file, no video link provided
**Prompted for:** First name: Sarah, Last name: [skipped], Company: TechCorp
**Output filename:** `2025-11-20_Sarah_TechCorp.md`

## What makes this good

1. "Not provided" for video link (not omitted)
2. Topic headers use `## Topic #N` format (no timestamps available)
3. Themes are grouped thematically despite linear transcript
4. Quotes preserved exactly as spoken in plain text

---

## Output

```markdown
# Product Feedback Interview - Sarah (Admin at TechCorp)

## Video
Not provided

## Call Summary
[2-3 paragraphs]

## Key Quotes
> "We spend about two hours every Monday morning just cleaning up data that should have been right from the start."
>
> — Sarah, on data quality workflows

[4-7 more quotes]

## Topical Breakdown

## Topic #1: Onboarding Complexity
New users struggle with initial setup and configuration.

- Users report spending 2-3 hours on first-time setup
- Lack of guided workflow causes confusion about next steps
- No way to preview changes before applying them
- Training documentation is outdated and doesn't match current UI

## Topic #2: Data Quality Workflows
Manual cleanup processes consuming significant team time.

- Monday morning "data scrub" routine takes 2+ hours
- No automated validation rules for required fields
- Duplicate detection misses variations in company names
- Bulk edit tools crash on datasets over 5,000 records

[Continue for all topics]

## Full Transcript
Interviewer: Thanks for joining today. Can you tell me about...
[Complete unmodified transcript...]
```
