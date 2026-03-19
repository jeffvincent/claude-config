# Executive Assistant Briefing System

This directory contains three specialized prompts for weekly leadership synthesis:

## Prompt Files

**1. grove-notes-reflection.md**
Extracts leadership signal from the last 7 days of management journal notes (notes/management-journal/YYYY-MM.md). Produces a reflection focused on lessons, strategic shifts, people signals, and focus areas.

**2. calendar-analysis.md**
Optimizes calendar for impact. Identifies prep priorities, misalignment, cuts, and structural problems.

**3. weekly-briefing-prep.md**
Integrates reflection + calendar analysis into one comprehensive Sunday briefing. This is what I actually read.

## Usage Pattern

1. Run grove-notes-reflection.md with last 7 days of notes from notes/management-journal/YYYY-MM.md
2. Run calendar-analysis.md with next week's calendar
3. Run weekly-briefing-prep.md to synthesize outputs from steps 1 and 2

## Inputs Required

All three prompts reference:
- **priorities.md**: Leadership focus areas from resources/exec-assistant/priorities.md
- **expectations.md**: Role performance expectations from resources/exec-assistant/expectations.md

Additionally:
- **Management journal notes**: Working notes from notes/management-journal/YYYY-MM.md
- **Calendar data**: Meeting hours, alignment %, prep/prune lists

## Output

A single ~600-800 word plain text briefing delivered Sunday night that:
- Reflects on what mattered this week
- Identifies where attention goes next
- Flags where time is misused
- Prepares for key conversations
- Defines Monday focus

## Principles

- Be ruthlessly selective — most things don't matter
- Be blunt and opinionated
- Extract meaning, not summaries
- Challenge misaligned attention
- Optimize for leadership effectiveness
