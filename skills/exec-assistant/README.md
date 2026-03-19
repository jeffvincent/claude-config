# Executive Assistant - Weekly Leadership Briefing System

A comprehensive system for generating automated weekly leadership briefings that synthesize management notes, calendar patterns, and strategic priorities into actionable Sunday night briefings.

## Overview

This skill provides a three-phase prompting system for weekly leadership synthesis:

1. **Extract reflection** from weekly management journal notes (lessons, people signals, focus areas)
2. **Analyze calendar** for time optimization (prep priorities, cuts, misalignment)
3. **Generate briefing** that synthesizes reflection + calendar into strategic guidance

## What's Included

**Documentation:**
- **SKILL.md** - Complete system documentation and setup guide
- **briefings-README.md** - Archival and usage documentation
- **README.md** - This file

**Prompts:** (in `prompts/`)
- **weekly-briefing-prep.md** - Main briefing synthesis prompt
- **grove-notes-reflection.md** - Weekly notes reflection prompt
- **calendar-analysis.md** - Calendar optimization prompt
- **executive-assistant-prompt.md** - System overview
- **zapier-setup-guide.md** - Complete Zapier automation setup

## What You Need to Provide

To use this system, you'll need to create these input files in your own project:

**Content Inputs:**
- **priorities.md** - Your current leadership priorities (quarterly focus areas)
- **expectations.md** - Your role performance standards
- **Management journal notes** - Monthly working notes (meetings, reflections, 1:1s)

See SKILL.md for example structure and content.

## How It Works

**Manual Usage:**
1. Use prompts with your current management notes, calendar, and priorities
2. Generate briefing following the three-phase process
3. Save output to dated file (YYYY-MM-DD.md)

**Automated Usage (Zapier):**
- See `prompts/zapier-setup-guide.md` for complete setup
- Every Sunday at 9pm: fetches notes, analyzes calendar, generates briefing
- Saves directly to GitHub with auto-commit
- Optional email delivery

## Briefing Output Structure

Each briefing includes:
- **THIS WEEK IN ONE SENTENCE** - Sharp tactical summary
- **THE MOMENT** - Strategic context (3-4 paragraphs)
- **THREE THINGS THAT MATTER MOST** - Concrete strategic moves
- **STATUS** - Key items requiring attention (with momentum tracking)
- **FRAMEWORKS WORTH KEEPING** - Reusable mental models
- **CONNECTING TO YOUR PRIORITIES** - Week mapped to standing priorities
- **WHERE TO SPEND YOUR ENERGY** - Focus areas for coming week

## Key Features

- **Ruthlessly selective** - Focuses on what matters, ignores noise
- **Blunt and opinionated** - Challenges misaligned attention
- **Extracts meaning, not summaries** - Finds strategic shifts and trajectory changes
- **Optimizes for leadership effectiveness** - Connects daily work to impact
- **Tracks evolution** - Git history shows patterns over time

## Getting Started

1. **Read** `SKILL.md` for complete documentation
2. **Create** your priorities.md and expectations.md files (see examples in SKILL.md)
3. **Set up** monthly management journal (YYYY-MM.md format)
4. **Test** manual generation first to validate output quality
5. **Optionally** set up Zapier automation (see `prompts/zapier-setup-guide.md`)

## Requirements

**For manual usage:**
- Management notes in markdown
- Calendar access (Google Calendar or similar)
- Claude API access or Claude Code

**For Zapier automation:**
- Zapier Pro account (~$20/month)
- Anthropic API key
- GitHub repository (for auto-commit)
- Google Calendar API access

## Privacy Note

This is the **public version** of the exec-assistant skill. The prompts and system documentation are shared as examples for others building similar systems.

**Not included:** Actual priorities.md, expectations.md, or generated briefings (contain work-specific PII).

You'll need to create your own content inputs based on your context.

## Cost Estimate

**Zapier automation:**
- Zapier Pro: $19.99/month
- Claude API: ~$0.02 per briefing × 52 weeks = ~$1/year
- **Total**: ~$20/month

**Manual usage:**
- Free (using Claude Code)
- Or minimal Claude API costs if using direct API

## Example Content

See `SKILL.md` for examples of:
- priorities.md structure
- expectations.md format
- Sample briefing output
- Best practices

## Repository

Part of the claude-config repository: https://github.com/jeffvincent/claude-config

For questions or issues, see SKILL.md or open an issue on GitHub.

## License

MIT - Feel free to use and adapt for your own workflows.

---

**Created**: 2026-03-19
**Status**: Production-ready (actively used)
