Execute a comprehensive weekly planning session that aligns your calendar with your priorities.

# Weekly Planning Process

## ⚠️ CRITICAL PRINCIPLE: ASK, DON'T INTERPRET

**Never guess or interpret meeting content based on titles.**
- Present EXACT calendar data (exact meeting titles, times, etc.)
- ASK the user which meetings need prep, align with priorities, etc.
- Let the user make strategic decisions based on accurate data
- Only create tasks/take actions based on explicit user input

This command orchestrates a multi-step planning workflow:

## Step 1: Review Priorities

First, check if priorities are set. Priorities are stored in `~/.claude/weekly-plan-priorities.json`.

**If priorities exist:**
- Display current priorities (max 3)
- Ask user: "These are your current priorities. Do you want to update them?"
- If yes, proceed to update. If no, continue to Step 2.

**If priorities don't exist:**
- Explain: "Let's set your top 3 priorities for this planning period. These will guide all planning decisions."
- Prompt user to list their top 3 priorities
- Save to `~/.claude/weekly-plan-priorities.json` as:
  ```json
  {
    "priorities": [
      "Priority 1",
      "Priority 2",
      "Priority 3"
    ],
    "updated": "2025-12-09T10:00:00Z"
  }
  ```

## Step 2: Calendar Review & Preparation Needs

### CRITICAL: Fetch BOTH Calendars

User has multiple calendar accounts. Always fetch BOTH:

```bash
cd ~/.claude/skills/google-calendar-skill/scripts

# Calculate time range (today through Sunday)
TODAY=$(date -u +"%Y-%m-%d")
# For Sunday end date, calculate properly based on day of week
WEEK_END="[calculate Sunday date]"

TIME_MIN="${TODAY}T00:00:00Z"
TIME_MAX="${WEEK_END}T23:59:59Z"

# Fetch WORK calendar
node calendar-events-list.js --account work \
  --timeMin "$TIME_MIN" --timeMax "$TIME_MAX" \
  --limit 100 > /tmp/work-events.json

# Fetch PERSONAL calendar (default account)
node calendar-events-list.js \
  --timeMin "$TIME_MIN" --timeMax "$TIME_MAX" \
  --limit 100 > /tmp/personal-events.json
```

### Parse and Present Calendar Data

**CRITICAL RULE: Never interpret or guess meeting content. Present EXACT data only.**

Use Python to parse JSON safely:

```python
import json
from datetime import datetime

def parse_event(event):
    """Parse event - handle both dict and string formats for 'start' field"""
    start_field = event['start']

    # Handle both formats: dict or string
    if isinstance(start_field, dict):
        start = start_field.get('dateTime') or start_field.get('date')
    else:
        start = start_field

    # Parse datetime
    if 'T' in start:
        dt = datetime.fromisoformat(start.replace('Z', '+00:00'))
        date_str = dt.strftime('%Y-%m-%d')
        time_str = dt.strftime('%I:%M%p').lstrip('0').lower()
    else:
        date_str = start
        time_str = 'All Day'

    return {
        'date': date_str,
        'time': time_str,
        'summary': event['summary'],  # EXACT summary - don't interpret!
        'start_raw': start
    }

# Load and parse both calendars
# Group by date, sort by time
# Present to user with EXACT titles
```

### Present Calendar and ASK User

Present the merged calendar grouped by day with exact meeting titles.

**Then ASK the user (don't guess!):**

"Looking at your calendar for this week, which meetings require preparation?"

For each meeting they identify, ASK:
- "How much prep time do you need?"
- "Do you need time scheduled, or just a reminder?"

### Create Preparation Tasks

Only create tasks based on user's explicit answers:

```python
import os, sys
sys.path.insert(0, os.path.expanduser('~/.claude/skills/things/lib'))
from writer import ThingsWriter

# For meetings needing TIME SCHEDULED:
ThingsWriter.add_task(
    title='Prep: [Exact Meeting Title] ([X]min)',
    notes='Meeting: [Day] [Date], [Time]\nAction: [What user said]\nTime needed: [X] minutes - schedule this!',
    when='[due-date]',
    tags=['preparation', 'calendar', 'time-block-needed']
)

# For meetings needing REMINDER ONLY:
ThingsWriter.add_task(
    title='Prep: [Exact Meeting Title]',
    notes='Meeting: [Day] [Date], [Time]\nReminder: [What user said] (no time block needed)',
    when='[due-date]',
    tags=['preparation', 'calendar']
)
```

## Step 3: Identify Focus Time & Suggest Activities

1. **Identify open focus blocks:**
   - Parse calendar to find unscheduled blocks >= 2 hours
   - Categorize by day and time (e.g., "Tuesday 9am-12pm", "Thursday 2pm-5pm")

2. **Get existing tasks from Things:**
   ```python
   python3 -c "
   import os, sys
   sys.path.insert(0, os.path.expanduser('~/.claude/skills/things/lib'))
   from reader import ThingsReader
   print(ThingsReader.get_today())
   print(ThingsReader.search(query='', status='incomplete'))
   "
   ```

3. **Match tasks to focus time:**
   - For each focus block, suggest 2-3 high-priority tasks that:
     * Align with user's priorities
     * Fit the time block duration
     * Are not already scheduled

4. **Present recommendations:**
   ```
   📅 Focus Time Opportunities:

   Tuesday 9am-12pm (3 hours)
   Suggested activities:
   - [Task 1 from Things] (aligns with Priority 1)
   - [Task 2 from Things] (aligns with Priority 2)

   Thursday 2pm-5pm (3 hours)
   Suggested activities:
   - [Task 3 from Things] (aligns with Priority 1)
   ```

5. **Offer to schedule:**
   - Ask: "Would you like me to add any of these to your calendar as focus blocks?"
   - If yes, use calendar-events-create.js to block the time

## Step 4: Priority Alignment Check

**CRITICAL: ASK the user about alignment. Don't guess based on meeting titles.**

### Present Priorities and ASK

Show the user their 3 priorities again, then ASK:

"Looking at your calendar, which meetings directly support each of your priorities?"

For example:
- Priority #1: [User's priority]
  - Which meetings support this?

- Priority #2: [User's priority]
  - Which meetings support this?

- Priority #3: [User's priority]
  - Which meetings support this?

### Identify Misaligned Meetings

Once user identifies aligned meetings, calculate which meetings DON'T align.

Then ASK: "You have [X] meetings this week that don't directly align with your stated priorities. Would you like to review these?"

If yes, present the list and ASK for each:
- "Is this meeting necessary? Could it be:"
  - Declined?
  - Delegated to someone else?
  - Made less frequent (bi-weekly instead of weekly)?
  - Shortened?

### Help with Rescheduling/Declining

Only if user wants to decline/reschedule, offer:
- Draft decline messages
- Suggest alternative attendees for delegation
- Use calendar scripts to reschedule

## Step 5: Weekly Summary

Generate a summary view:

```
📊 Your Week Ahead

🎯 Priorities:
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

📅 Key Events: [count] events
- [count] require preparation → [count] prep tasks created
- [count] aligned with priorities
- [count] flagged for review

⏰ Focus Time: [count] blocks ([total hours] hours)
- [count] blocks with suggested activities

✅ Action Items Created:
- [count] preparation tasks added to Things
- [count] focus blocks suggested for scheduling

⚠️ Recommendations:
- [count] meetings to consider rescheduling/declining
```

## Guidelines

**Tone:** Supportive and coaching. Help the user make strategic choices about their time.

**Interactivity:** After each step, pause for user input before proceeding. Don't rush through.

**Flexibility:** If user wants to skip a step or focus on one area, accommodate that.

**Follow-up:** At the end, ask: "What else would you like to adjust for the week ahead?"

## Technical Notes

- Always change to appropriate script directories before running commands
- Parse JSON output from calendar/Things scripts
- Handle timezone conversions properly (user is in Pacific Time)
- Store priorities file in user's home directory for persistence
- Use both --account flags if user has multiple calendars configured
