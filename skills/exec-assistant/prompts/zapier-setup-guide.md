# Zapier Setup Guide: Automated Weekly Briefings

This guide walks through setting up a Zapier automation to generate weekly leadership briefings and save them directly to the Knowledge System repository on GitHub.

## Overview

**Goal**: Every Sunday at 9pm, automatically:
1. Fetch current month's management journal notes from GitHub
2. Fetch upcoming week's calendar from Google Calendar
3. Generate briefing using Claude API
4. Save briefing to `resources/exec-assistant/briefings/YYYY-MM-DD.md` on GitHub
5. Optionally send email copy

**Requirements**:
- Zapier account (Pro plan recommended for Code by Zapier steps)
- GitHub account with access to Knowledge System repository
- Google Calendar API access
- Anthropic API key (for Claude)
- Knowledge System repository must be on GitHub

## Zapier Zap Structure

### Trigger: Schedule by Zapier

**Configuration**:
- Event: Every Week
- Day: Sunday
- Time: 9:00 PM
- Timezone: Your local timezone

### Step 1: Get Sunday Date (Code by Zapier - Python)

Generate the correct filename date (Sunday that starts the coming week).

**Code**:
```python
from datetime import datetime, timedelta

# Get current date
now = datetime.now()

# Find next Sunday (or today if it's Sunday)
days_until_sunday = (6 - now.weekday()) % 7
if days_until_sunday == 0 and now.weekday() == 6:
    # Today is Sunday, use today
    next_sunday = now
else:
    next_sunday = now + timedelta(days=days_until_sunday)

# Format as YYYY-MM-DD
filename_date = next_sunday.strftime('%Y-%m-%d')
year_month = next_sunday.strftime('%Y-%m')

output = {
    'filename_date': filename_date,
    'year_month': year_month,
    'week_start': next_sunday.strftime('%B %d, %Y'),
    'week_end': (next_sunday + timedelta(days=6)).strftime('%B %d, %Y')
}
```

**Output**:
- `filename_date`: e.g., "2026-03-02"
- `year_month`: e.g., "2026-03"
- `week_start`: e.g., "March 2, 2026"
- `week_end`: e.g., "March 8, 2026"

### Step 2: Fetch Management Journal Notes from GitHub

**App**: GitHub
**Action**: Get File Content
**Configuration**:
- Account: Your GitHub account
- Repository: `jeffvincent/knowledge-system` (or your repo name)
- File Path: `notes/management-journal/{{year_month}}.md` (use output from Step 1)
- Branch: `main`

**Output**: Store in variable `management_journal_content`

**Error Handling**: If file doesn't exist (new month), use empty content or fetch previous month.

### Step 3: Fetch Priorities and Expectations from GitHub

**App**: GitHub (run two parallel steps)
**Action**: Get File Content

**3a. Fetch priorities.md**:
- File Path: `resources/exec-assistant/priorities.md`
- Branch: `main`

**3b. Fetch expectations.md**:
- File Path: `resources/exec-assistant/expectations.md`
- Branch: `main`

### Step 4: Fetch Calendar Events (Google Calendar)

**App**: Google Calendar
**Action**: Find Events
**Configuration**:
- Calendar: Your work calendar
- Start Time: `{{week_start}}` (from Step 1)
- End Time: `{{week_end}}` (from Step 1)
- Max Results: 100
- Order By: Start Time

**Output**: Store calendar events in variable `calendar_events`

### Step 5: Analyze Calendar (Code by Zapier - Python)

Parse calendar events into time allocation summary.

**Code**:
```python
from datetime import datetime
import json

# Parse input (calendar events from Step 4)
events = input.get('calendar_events', [])

# Initialize time tracking
meeting_hours = 0
focus_time_hours = 0
categories = {
    '1:1s': 0,
    'Team Meetings': 0,
    'Strategic Planning': 0,
    'Cross-functional': 0,
    'External': 0
}

# Analyze each event
for event in events:
    # Calculate duration
    start = datetime.fromisoformat(event['start'])
    end = datetime.fromisoformat(event['end'])
    duration_hours = (end - start).total_seconds() / 3600

    # Categorize (simple keyword matching)
    title_lower = event['summary'].lower()
    if '1:1' in title_lower or 'one on one' in title_lower:
        categories['1:1s'] += duration_hours
    elif 'team' in title_lower:
        categories['Team Meetings'] += duration_hours
    elif 'strategy' in title_lower or 'planning' in title_lower:
        categories['Strategic Planning'] += duration_hours
    elif 'external' in title_lower or 'customer' in title_lower:
        categories['External'] += duration_hours
    else:
        categories['Cross-functional'] += duration_hours

    meeting_hours += duration_hours

# Calculate focus time (assuming 40 hour week)
focus_time_hours = max(0, 40 - meeting_hours)

# Format output
calendar_summary = f"""
**Meeting Load**: {meeting_hours:.1f} hours ({meeting_hours/40*100:.0f}% of week)
**Focus Time**: {focus_time_hours:.1f} hours ({focus_time_hours/40*100:.0f}% of week)

**Time Breakdown**:
- 1:1s: {categories['1:1s']:.1f} hours
- Team Meetings: {categories['Team Meetings']:.1f} hours
- Strategic Planning: {categories['Strategic Planning']:.1f} hours
- Cross-functional: {categories['Cross-functional']:.1f} hours
- External: {categories['External']:.1f} hours
"""

output = {'calendar_summary': calendar_summary}
```

### Step 6: Fetch Briefing Prompt from GitHub

**App**: GitHub
**Action**: Get File Content
**Configuration**:
- File Path: `.claude/skills/exec-assistant/prompts/weekly-briefing-prep.md`
- Branch: `main`

### Step 7: Generate Briefing (Code by Zapier - Python)

Call Claude API to generate the briefing.

**Code**:
```python
import anthropic
import os
from datetime import datetime

# Initialize Claude client
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# Get inputs from previous steps
briefing_prompt = input.get('briefing_prompt_content')
priorities = input.get('priorities_content')
expectations = input.get('expectations_content')
management_journal = input.get('management_journal_content', '')
calendar_summary = input.get('calendar_summary')
week_start = input.get('week_start')
week_end = input.get('week_end')

# Construct full prompt
full_prompt = f"""
{briefing_prompt}

## Context for This Week

**Week**: {week_start} - {week_end}
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Inputs

### Leadership Priorities
{priorities}

### Performance Expectations
{expectations}

### This Week's Management Journal Notes
{management_journal if management_journal else '(No management journal notes available yet for this month)'}

### Calendar Analysis
{calendar_summary}

---

Please generate a comprehensive weekly briefing following the structure outlined above.
"""

# Call Claude API
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4000,
    messages=[
        {"role": "user", "content": full_prompt}
    ]
)

# Extract briefing content
briefing_content = message.content[0].text

# Format with header
formatted_briefing = f"""# Weekly Briefing: Week of {week_start} - {week_end}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

{briefing_content}

---

## End-of-Week Reflection

*(Add your reflections here after the week concludes)*

**What landed:**
-

**What shifted:**
-

**Insights:**
-

**For next week:**
-
"""

output = {'briefing_content': formatted_briefing}
```

**Environment Variables** (set in Zapier):
- `ANTHROPIC_API_KEY`: Your Claude API key

### Step 8: Save Briefing to GitHub

**App**: GitHub
**Action**: Create or Update File
**Configuration**:
- Repository: `jeffvincent/knowledge-system`
- File Path: `resources/exec-assistant/briefings/{{filename_date}}.md` (from Step 1)
- File Content: `{{briefing_content}}` (from Step 7)
- Commit Message: `Add weekly briefing for week of {{week_start}}`
- Branch: `main`

### Step 9 (Optional): Send Email Copy

**App**: Email by Zapier
**Action**: Send Outbound Email
**Configuration**:
- To: Your email
- Subject: `Weekly Briefing: Week of {{week_start}}`
- Body: `{{briefing_content}}`

## Environment Setup in Zapier

### Required Secrets

In your Zapier account, go to **Code by Zapier** settings and add:

**Environment Variables**:
```
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### GitHub Authentication

Connect your GitHub account in Zapier:
1. Go to **My Apps** → **GitHub**
2. Click **Connect a new account**
3. Authorize Zapier to access your repositories
4. Grant read/write permissions for repository content

### Google Calendar Authentication

Connect Google Calendar:
1. Go to **My Apps** → **Google Calendar**
2. Click **Connect a new account**
3. Authorize Zapier to read calendar events

## Testing the Zap

### Test Each Step

1. **Test Trigger**: Run manually to verify Sunday date calculation
2. **Test GitHub Fetch**: Verify management journal notes, priorities, expectations are retrieved
3. **Test Calendar Fetch**: Check events are retrieved for the correct week
4. **Test Calendar Analysis**: Verify time categorization is accurate
5. **Test Claude API**: Ensure briefing generates with proper structure
6. **Test GitHub Commit**: Verify file is created in correct location

### First Run

Before activating:
1. Run a manual test on a Thursday or Friday (not Sunday)
2. Verify output file appears in `resources/exec-assistant/briefings/`
3. Check GitHub for commit
4. Review briefing content for quality
5. Adjust prompts or logic as needed

### Activate

Once tested:
1. Turn on the Zap
2. Set schedule for Sunday 9:00 PM
3. Monitor first few weeks for any errors

## Troubleshooting

### Management Journal File Not Found

If it's the first week of a new month and `notes/management-journal/YYYY-MM.md` doesn't exist yet:

**Solution**: Add error handling in Step 2:
```python
# In Code by Zapier after GitHub fetch attempt
if not management_journal_content:
    management_journal_content = "(No management journal notes available yet for this month)"
```

### Calendar Events Not Parsing

Check date format matching between Step 1 and Step 4.

**Solution**: Ensure `week_start` and `week_end` use format expected by Google Calendar API.

### Claude API Rate Limits

If you hit rate limits:

**Solution**:
- Use Claude Haiku instead of Sonnet for lower cost/rate
- Add retry logic with exponential backoff
- Schedule at off-peak times

### GitHub Commit Conflicts

If someone manually commits while Zap is running:

**Solution**: Use "Create or Update File" action (not "Create File") to allow overwrites.

## Cost Estimate

**Zapier**:
- Pro plan: $19.99/month (includes Code by Zapier)
- ~4 tasks per run × 52 weeks = ~208 tasks/year (well within limits)

**Claude API**:
- ~2000 tokens input + 1500 tokens output per briefing
- Cost: ~$0.02 per briefing × 52 weeks = ~$1/year

**Total**: ~$20/month for Zapier Pro

## Alternative: Simpler Email-Only Version

If you prefer a simpler setup without GitHub integration:

**Simplified Zap**:
1. Schedule (Sunday 9pm)
2. Fetch management journal notes via GitHub API (Code by Zapier)
3. Fetch calendar events
4. Generate briefing with Claude (Code by Zapier)
5. Send email

Then **manually**:
- Copy email content to `resources/exec-assistant/briefings/YYYY-MM-DD.md`
- Commit to git: `git add . && git commit -m "Add briefing for week of YYYY-MM-DD"`

**Trade-off**: Less automation, but simpler setup and no GitHub integration complexity.

## Next Steps

1. **Create Zapier account** (if needed): https://zapier.com
2. **Get Anthropic API key**: https://console.anthropic.com
3. **Build the Zap** using steps outlined above
4. **Test thoroughly** before activating
5. **Run first briefing** and review output
6. **Iterate on prompts** based on output quality

## Support

- Zapier Documentation: https://zapier.com/help
- Anthropic API Docs: https://docs.anthropic.com
- GitHub API Docs: https://docs.github.com/en/rest

For Knowledge System-specific questions, see `resources/exec-assistant/briefings/README.md`.
