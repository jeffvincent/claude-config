Execute a comprehensive weekly planning session that aligns your calendar with your priorities.

# Weekly Planning Process

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

Use the google-calendar-skill to:

1. **List current week's events (today through Sunday):**
   ```bash
   cd ~/.claude/skills/google-calendar-skill/scripts

   # Calculate next Sunday at 11:59pm
   # If today is Sunday, go to the following Sunday
   DAY_OF_WEEK=$(date +%u)  # 1=Monday, 7=Sunday
   if [ "$DAY_OF_WEEK" -eq 7 ]; then
     DAYS_TO_SUNDAY=7  # If today is Sunday, go to next Sunday
   else
     DAYS_TO_SUNDAY=$((7 - DAY_OF_WEEK))  # Days until this Sunday
   fi

   # Get events from now through end of week (Sunday 11:59pm)
   TIME_MIN=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   TIME_MAX=$(date -u -v+${DAYS_TO_SUNDAY}d +"%Y-%m-%dT23:59:59Z")

   node calendar-events-list.js --timeMin "$TIME_MIN" --timeMax "$TIME_MAX"
   ```

   **Time range examples:**
   - Run on Monday: Reviews Monday through Sunday (6 days)
   - Run on Wednesday: Reviews Wednesday through Sunday (4 days)
   - Run on Sunday: Reviews Sunday through next Sunday (7 days)
   - Accounts for long weekends and holidays naturally

2. **Analyze each event for preparation needs:**
   - Identify meetings/events that require preparation (presentations, important meetings, reviews, etc.)
   - Group by: "Needs Preparation" vs "Standard Attendance"

3. **Create preparation tasks:**
   - For each event needing preparation, ask: "What preparation is needed for [Event Name]?"
   - Use the things skill to create tasks:
     ```python
     # Example for each prep item
     python3 -c "
     import sys
     sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')
     from writer import ThingsWriter
     ThingsWriter.add_task(
         title='Prepare for [Event Name]',
         notes='Event: [Date/Time]\nPreparation: [Details]',
         when='[due-date]',
         tags=['preparation', 'calendar']
     )
     "
     ```

## Step 3: Identify Focus Time & Suggest Activities

1. **Identify open focus blocks:**
   - Parse calendar to find unscheduled blocks >= 2 hours
   - Categorize by day and time (e.g., "Tuesday 9am-12pm", "Thursday 2pm-5pm")

2. **Get existing tasks from Things:**
   ```python
   python3 -c "
   import sys
   sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')
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

1. **Analyze calendar events against priorities:**
   - For each non-preparation meeting, evaluate:
     * Does this directly support Priority 1, 2, or 3?
     * If no, mark as "Low Priority Alignment"

2. **Flag misaligned meetings:**
   ```
   ⚠️ Calendar Items Not Aligned with Priorities:

   - "Weekly status meeting" (Tuesday 2pm)
     Reason: Doesn't directly support any current priority
     Suggestion: Consider delegating or making this bi-weekly

   - "Vendor demo" (Thursday 10am)
     Reason: Not aligned with current focus areas
     Suggestion: Reschedule to next month or decline
   ```

3. **Present options:**
   - "Would you like help rescheduling or declining any of these?"
   - If yes, draft decline messages or reschedule using calendar scripts

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
