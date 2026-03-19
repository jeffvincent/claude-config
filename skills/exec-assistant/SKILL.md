# Executive Assistant - Weekly Leadership Briefing System

Generate automated weekly leadership briefings that synthesize management journal notes, calendar patterns, and strategic priorities into actionable Sunday night briefings.

## Purpose

This skill provides a comprehensive weekly briefing system designed to:
- Extract leadership signal from the week's management journal notes
- Analyze next week's calendar for time optimization
- Connect daily work to strategic priorities
- Identify what matters most and where to focus energy
- Track progress against role expectations

## How It Works

The system uses three specialized prompts that work together:

1. **grove-notes-reflection.md** - Extracts lessons and people signals from the last 7 days of management journal notes
2. **calendar-analysis.md** - Optimizes next week's calendar for impact and alignment
3. **weekly-briefing-prep.md** - Synthesizes reflection + calendar into one comprehensive briefing

## File Structure

```
.claude/skills/exec-assistant/
├── SKILL.md (this file)
├── prompts/
│   ├── weekly-briefing-prep.md        # Main briefing generation prompt
│   ├── grove-notes-reflection.md      # Weekly notes reflection prompt
│   ├── calendar-analysis.md           # Calendar optimization prompt
│   ├── executive-assistant-prompt.md  # System overview
│   └── zapier-setup-guide.md         # Zapier automation setup
└── briefings-README.md                # Archival documentation

resources/exec-assistant/  (in repo root)
├── priorities.md           # Current leadership priorities (input)
├── expectations.md         # Role performance standards (input)
└── briefings/             # Generated briefings saved here
    ├── 2026-03-02.md
    ├── 2026-02-23.md
    └── ...
```

## Required Inputs

The briefing prompts reference these files from the Knowledge System:

- **Management Journal**: `notes/management-journal/YYYY-MM.md` - Monthly working notes with meeting reflections, strategic thoughts, 1:1s
- **Priorities**: `resources/exec-assistant/priorities.md` - Current leadership focus areas (updated quarterly)
- **Expectations**: `resources/exec-assistant/expectations.md` - Role performance expectations and GPS framework mapping
- **Calendar Data**: Meeting hours, alignment %, prep/prune lists from Google Calendar

## Outputs

Each Sunday night briefing includes:

- **THIS WEEK IN ONE SENTENCE**: Sharp, tactical summary
- **THE MOMENT**: 3-4 paragraphs of strategic context
- **THREE THINGS THAT MATTER MOST**: Concrete strategic moves with people observations
- **STATUS**: 3-5 key items requiring attention (with momentum tracking)
- **FRAMEWORKS WORTH KEEPING**: Reusable mental models that emerged
- **CONNECTING TO YOUR PRIORITIES**: How the week mapped to standing priorities
- **WHERE TO SPEND YOUR ENERGY**: Inspiring close on 2-3 focus areas

Briefings are saved to: `resources/exec-assistant/briefings/YYYY-MM-DD.md`

## Usage

### Option 1: Manual Generation (Current)

1. **Extract weekly reflection**:
   - Use `prompts/grove-notes-reflection.md` with last 7 days of `notes/management-journal/YYYY-MM.md`
   - Produces: lessons, focus items, people signals, quotes

2. **Analyze calendar**:
   - Use `prompts/calendar-analysis.md` with next week's calendar
   - Produces: prep priorities, cuts, misalignment, recovery plan

3. **Generate briefing**:
   - Use `prompts/weekly-briefing-prep.md` with outputs from steps 1-2
   - Produces: Complete Sunday night briefing (~800-1200 words)

4. **Save briefing**:
   - Create file: `resources/exec-assistant/briefings/YYYY-MM-DD.md` (use Sunday date)
   - Commit to git

### Option 2: Automated via Zapier (Recommended)

**Setup**: See `prompts/zapier-setup-guide.md` for complete Zapier workflow

**What it does**:
- Every Sunday at 9pm
- Fetches management journal notes from GitHub
- Fetches calendar from Google Calendar
- Generates briefing using Claude API
- Saves to `resources/exec-assistant/briefings/YYYY-MM-DD.md` on GitHub
- Optionally sends email copy

**Requirements**:
- Zapier Pro account
- Anthropic API key
- GitHub + Google Calendar access
- ~$20/month cost

### After the Week: Add Reflections

Annotate each briefing after the week concludes:

```markdown
---

## End-of-Week Reflection

**What landed:**
- [What actually got focus/traction]

**What shifted:**
- [Unexpected changes or pivots]

**Insights:**
- [Patterns or learnings]

**For next week:**
- [Adjustments or carry-forward items]
```

## Integration with Knowledge System

**Reads from:**
- `notes/management-journal/YYYY-MM.md` - Monthly working notes (via `/log-meeting`, `/note`)
- `resources/exec-assistant/priorities.md` - Strategic priorities (updated via `/refresh-priorities` or manually)
- `resources/exec-assistant/expectations.md` - Role expectations

**Outputs to:**
- `resources/exec-assistant/briefings/YYYY-MM-DD.md` - Weekly briefings

**Related commands:**
- `/log-meeting` - Populates management journal with meeting notes
- `/note` - Adds timestamped reflections to management journal
- `/weekly-review` - Tactical weekly review (different from strategic briefing)

## Principles

The briefing system follows these core principles:

1. **Be ruthlessly selective** — Most things don't matter, focus on what does
2. **Be blunt and opinionated** — Challenge misaligned attention
3. **Extract meaning, not summaries** — Find strategic shifts and trajectory changes
4. **Optimize for leadership effectiveness** — Connect daily work to impact
5. **Track evolution** — Use git history to see patterns over time

## Best Practices

1. **Use Sunday dates**: Briefings prepare for the coming week, so use Sunday date that starts the week
2. **Add reflections**: After the week, annotate with what actually happened
3. **Review quarterly**: When running `/refresh-priorities`, review last 3 months of briefings
4. **Share selectively**: Briefings contain sensitive strategic information
5. **Track themes**: Use grep/search to find recurring patterns across weeks

## Files You Can Share Publicly

Since you plan to share this system publicly, these files contain no PII:

**Shareable** (system prompts):
- `prompts/weekly-briefing-prep.md`
- `prompts/grove-notes-reflection.md`
- `prompts/calendar-analysis.md`
- `prompts/executive-assistant-prompt.md`
- `prompts/zapier-setup-guide.md`
- `briefings-README.md`
- `SKILL.md` (this file)

**Private** (contain work-specific data):
- `resources/exec-assistant/priorities.md` - Your actual priorities
- `resources/exec-assistant/expectations.md` - Your role expectations
- `resources/exec-assistant/briefings/*.md` - Generated briefings

When sharing, you can copy the prompts to a blog post or gist and add example placeholder content for priorities/expectations.

## Maintenance

- **Update priorities**: Quarterly via `/refresh-priorities` or manual edit
- **Update expectations**: As role evolves or GPS framework changes
- **Archive briefings**: Keep all in git (valuable history)
- **Review prompts**: Iterate based on briefing quality

## Getting Started

1. **Ensure inputs exist**:
   - `resources/exec-assistant/priorities.md` (your current priorities)
   - `resources/exec-assistant/expectations.md` (your role expectations)
   - `notes/management-journal/YYYY-MM.md` (current month's notes)

2. **Generate first briefing manually** to test:
   - Copy `prompts/weekly-briefing-prep.md` into a new conversation
   - Add last 7 days of management journal notes
   - Add your priorities.md and expectations.md
   - Review output quality

3. **If quality is good**, set up Zapier automation:
   - Follow `prompts/zapier-setup-guide.md`
   - Test thoroughly before activating
   - Monitor first few weeks

4. **After each week**:
   - Review the briefing
   - Add end-of-week reflections
   - Commit to git

## Status

**Current State**: System designed but not yet activated
- Prompts: Complete and tested
- Zapier workflow: Documented but not implemented
- Briefings generated: None yet (directory empty)

**Next Steps**:
1. Test manual generation with current priorities/expectations
2. Validate output quality and iterate on prompts
3. Decide whether to implement Zapier automation
4. Generate first few briefings manually
5. Review value before committing to automation

## Support

For questions or issues:
- Review `prompts/executive-assistant-prompt.md` for system overview
- Check `prompts/zapier-setup-guide.md` for automation setup
- See `briefings-README.md` for archival best practices
