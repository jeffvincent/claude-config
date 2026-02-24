# Refresh Priorities Command

Analyze the last 90 days of Grove activity and refresh the `priorities.md` document in the Grove directory.

## Task

You are helping Jeff refresh his leadership priorities document based on recent activity in Grove.

**Location:** `/Users/jvincent/Projects/Work/HubSpot/Grove/priorities.md`

## Process

1. **Read current priorities.md** to understand what's currently documented

2. **Analyze recent Grove activity** (last 90 days):
   - Read monthly grove notes files (grove-notes/YYYY-MM.md format) covering the last 90 days
     - Example: If today is 2026-01-28, read grove-notes/2026-01.md, grove-notes/2025-12.md, and grove-notes/2025-11.md
     - Focus on entries from the last 90 days across these files
   - Sample 5-7 person files from `people/` directory, focusing on recent notes
   - Review `resources/PM-Coaching.md` for recent coaching patterns
   - Look for recurring themes, concerns, and focus areas

3. **Identify what's changed:**
   - New priorities that emerged
   - Priorities that have faded or been resolved
   - Shifts in emphasis or framing
   - New recurring concerns
   - What energizes/drains have changed

4. **Generate updated priorities.md:**
   - Replace the "Core Priorities" section (max 5 items):
     - Specific projects and initiatives with clear timelines
     - Examples: "Foundational Data Fixes project", "Data Platform vision"
     - Focus on what's time-bound and project-focused
   - Replace the "Evergreen Priorities" section (max 5 items):
     - Ongoing leadership themes and development areas that persist over time
     - Examples: "Making platform work like a platform", "Understanding how AI changes CRM"
     - Focus on recurring patterns, coaching themes, and continuous concerns
   - Update "Recurring Concerns" based on what's actually recurring recently
   - Update "What Energizes Me" section
   - Update "Last Updated" date to today
   - **Note:** Do NOT add a "What Changed Since Last Update" section to the file (keep that summary for Jeff's review only)

5. **Present the changes** to Jeff:
   - Show a summary of what changed
   - Ask if he wants to commit the updated document
   - If yes, commit with a descriptive message noting key shifts

## Important Guidelines

- **Replace, don't just append** - if something isn't showing up in the last 90 days, it shouldn't be in the current priorities
- **Distinguish Core vs Evergreen carefully**:
  - Core = Specific projects/initiatives with deliverables (time-bound)
  - Evergreen = Ongoing leadership patterns that persist across months (timeless themes)
- **Max 5 items per section** - be ruthless about prioritization
- **Be specific, not generic** - use actual examples and quotes from recent notes
- **Keep it jargon-free** - use plain language, not corporate speak
- **Stay concise** - Core priorities can be brief (1 line), Evergreen can be 2-3 sentences with context
- **Focus on patterns** - what comes up repeatedly, not one-off mentions
- **Maintain the energizing/honest tone** - this is a personal document, not a performance review

## Output Format

After analysis, show Jeff:

```
## Priorities Refresh Analysis (Last 90 Days: YYYY-MM-DD to YYYY-MM-DD)

### Core Priorities (max 5)
**What's New:** [New project-focused priorities]
**What Dropped Off:** [Projects completed or deprioritized]
**What Shifted:** [Projects that changed scope or emphasis]

### Evergreen Priorities (max 5)
**What's New:** [New recurring themes that emerged]
**What Dropped Off:** [Themes that are no longer recurring]
**What Shifted:** [Themes that changed emphasis or framing]

### Other Sections
- Recurring Concerns: [Key changes]
- What Energizes Me: [Key changes]

### Summary
[2-3 sentence summary of how focus has evolved]

Ready to update priorities.md with these changes?
```

Then proceed with updating the file if approved.
