---
name: todoist-search
description: Search tasks in Todoist with keyword and filter options
version: 2.0.0
allowed-tools: [mcp__claude_ai_Todoist__find-tasks, mcp__claude_ai_Todoist__find-tasks-by-date]
---

# Search Tasks in Todoist

Find tasks using keywords and filtering options.

## How to Search Tasks

Call `mcp__claude_ai_Todoist__find-tasks` with:

```
searchText: "blog"        # keyword search in title/description
label: "work"             # filter by label
projectId: "..."          # filter by project
isCompleted: false        # incomplete tasks (default)
```

For date-based search, use `find-tasks-by-date`:
```
startDate: "2026-05-01"
endDate: "2026-05-31"
```

## Available Filters

| Filter | Description | Example |
|--------|-------------|---------|
| `searchText` | Keyword in title/description | "blog" |
| `label` | Filter by label | "work", "meeting" |
| `projectId` | Filter by project | inbox or project ID |
| `isCompleted` | Task status | false (default) |

## Instructions

1. **Parse** the user's search request for keywords and filters
2. **Search** using `find-tasks` with appropriate parameters
3. **Display** results clearly
4. **Suggest** broadening search if no results found

## Examples

**User**: "Find all tasks with 'meeting' in them"
```
searchText: "meeting"
isCompleted: false
```

**User**: "Show work tasks due this week"
Use `find-tasks-by-date` with `startDate="today"` and `endDate="[end of week]"`, then filter results by `label: "work"`.

**User**: "What completed tasks mention 'deployment'?"
```
searchText: "deployment"
isCompleted: true
```

## Pro Tips

- Default to incomplete tasks unless user asks for completed
- Combine label + searchText for precise results
- Use `find-completed-tasks` for historical queries
