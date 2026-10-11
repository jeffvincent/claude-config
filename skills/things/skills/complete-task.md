---
name: todoist-complete-task
description: Mark tasks as complete in Todoist by ID or title search
version: 2.0.0
allowed-tools: [mcp__claude_ai_Todoist__complete-tasks, mcp__claude_ai_Todoist__find-tasks]
---

# Complete Task in Todoist

Mark one or more tasks as complete.

## How to Complete a Task

**By ID** (most reliable — use IDs from previous list/search results):
```
Call mcp__claude_ai_Todoist__complete-tasks with:
taskIds: ["6gjrxjXqwQQHCW6P"]
```

**By title search** (when user references task by name):
1. Call `find-tasks` with `searchText: "[task name]"`
2. Identify the matching task(s) from results
3. Call `complete-tasks` with the task ID(s)

## Instructions

1. **Identify** the task(s) to complete:
   - Use task ID directly if provided
   - Search by title if referenced by name
2. **Handle multiple matches** by showing options and asking which to complete
3. **Complete** using `complete-tasks`
4. **Confirm** with success message

## Examples

**User**: "Complete the dentist task"
1. `find-tasks` with `searchText: "dentist"`
2. Confirm match, then `complete-tasks` with its ID

**User**: "Mark all today's tasks as done"
1. `find-tasks-by-date` with `startDate="today"`, `endDate="today"`
2. `complete-tasks` with all returned IDs

## Example Output

```
✅ Task completed: Call dentist
```

**Multiple matches:**
```
Found 2 tasks matching 'blog':
1. Write blog post — Content · due tomorrow
2. Review blog draft — Content · no due date

Which one would you like to complete?
```

## Note on Rescheduling

To **move** a task to a different date (not complete it), use `reschedule-tasks` — not `update-tasks`. This preserves any recurrence patterns.
