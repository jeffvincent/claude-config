---
name: todoist-list-inbox
description: View inbox tasks in Todoist that need to be triaged or organized
version: 2.0.0
allowed-tools: [mcp__claude_ai_Todoist__find-tasks]
---

# List Inbox Tasks from Todoist

Display tasks in the inbox that need to be organized and scheduled.

## How to List Inbox Tasks

Call `mcp__claude_ai_Todoist__find-tasks` with:
```
projectId: "inbox"
```

Or use `mcp__claude_ai_Todoist__get-overview` for a full picture.

## Purpose of Inbox

The inbox contains:
- Newly captured tasks not yet organized
- Tasks needing scheduling or project assignment
- Quick captures waiting for processing

## Instructions

1. **Fetch** inbox tasks using `find-tasks` filtered to inbox project
2. **Display** each task with any due dates or labels
3. **Suggest** organizing actions if inbox is large (add labels, set due dates)

## Example Output

```
Inbox (5 tasks to triage)

[ ] Research new framework
[ ] Buy groceries
[ ] Schedule team meeting
[ ] Read article on AI
[ ] Fix bug in login flow

Summary: 5 total — consider labeling and scheduling
```

## Pro Tips

- Empty inbox = good organization
- Suggest adding labels (`work`, `meeting`, etc.) for untagged tasks
- Tasks with no due date can get `dueString: "someday"` equivalent via no date
