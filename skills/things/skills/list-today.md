---
name: todoist-list-today
description: View all tasks due today in Todoist
version: 2.0.0
allowed-tools: [mcp__claude_ai_Todoist__find-tasks-by-date, mcp__claude_ai_Todoist__get-overview]
---

# List Today's Tasks from Todoist

Display all tasks due today with full context.

## How to List Today's Tasks

Call `mcp__claude_ai_Todoist__find-tasks-by-date` with:
```
startDate: "today"
endDate: "today"
```

Or use `mcp__claude_ai_Todoist__get-overview` for a broader view including overdue items.

## Instructions

1. **Fetch** today's tasks using `find-tasks-by-date` with `startDate="today"` and `endDate="today"`
2. **Also check** for overdue items using `get-overview` or a second query with `endDate` in the past
3. **Display** in a clear list with task IDs visible for follow-up actions

## Example Output

```
Today's Tasks (3)

[ ] Write blog post
    Focus on API design patterns
    Labels: writing, work

[ ] Call dentist
    Labels: health

[x] Review pull request

Summary: 3 total (2 incomplete, 1 completed)
```

## User Variations

- "What's on my plate today?" → List today + overdue
- "Show me today's tasks" → List today
- "What do I need to do?" → Use `get-overview` for full picture
