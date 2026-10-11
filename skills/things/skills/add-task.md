---
name: todoist-add-task
description: Add a new task to Todoist with description, labels, due date, deadline, and priority
version: 2.0.0
allowed-tools: [mcp__claude_ai_Todoist__add-tasks]
---

# Add Task to Todoist

Create a new task in Todoist based on the user's natural language request.

## Available Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `content` | Yes | Task title | "Write blog post" |
| `description` | No | Detailed notes/context | "Focus on API design" |
| `dueString` | No | Movable due date (natural language) | "tomorrow", "next Monday", "in 3 days" |
| `deadlineDate` | No | Immovable hard deadline (ISO) | "2026-06-01" |
| `labels` | No | List of labels | ["work", "meeting"] |
| `priority` | No | p1 (highest) to p4 (lowest) | "p2" |

**Due date vs. Deadline:**
- Use `dueString` for regular action items (movable)
- Use `deadlineDate` for meeting-prep tasks and fixed commitments (immovable)

## How to Add a Task

Call `mcp__claude_ai_Todoist__add-tasks` directly:

```
tasks: [
  {
    content: "Write blog post",
    description: "Focus on API design patterns",
    dueString: "tomorrow",
    labels: ["work"],
    priority: "p3"
  }
]
```

## Instructions

1. **Parse** the user's request to extract task details
2. **Call** `mcp__claude_ai_Todoist__add-tasks` with appropriate parameters
3. **Confirm** the task was added successfully

## Examples

**User**: "Add a task to call the dentist tomorrow, label health"
```
content: "Call dentist"
dueString: "tomorrow"
labels: ["health"]
```

**User**: "Create task to review Q4 report, hard deadline December 1st"
```
content: "Review Q4 report"
deadlineDate: "2025-12-01"
labels: ["work"]
```

**User**: "Add 'Prep for Thursday sync' with note 'bring draft agenda', due Wednesday, p2"
```
content: "Prep for Thursday sync"
description: "Bring draft agenda"
dueString: "Wednesday"
priority: "p2"
labels: ["work", "meeting"]
```

## Output

Confirm success:
```
Task added to Todoist!

Title: Call dentist
Due: Tomorrow
Labels: health
```
