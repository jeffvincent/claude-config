---
name: things-3-manager
description: "macOS only: Manage Things 3 tasks - add, search, list, and complete tasks using natural language. Requires Things 3 app installed."
version: 2.0.0
location: user
allowed-tools: [Bash, Read, Write]
---

# Things 3 Task Management (macOS Only)

Manage your Things 3 tasks through natural language. This skill dispatches to focused sub-skills for specific operations.

**Platform:** macOS only (Things 3 is a Mac app)

## When to Apply

Use this skill when:
- User is on macOS with Things 3 installed
- User wants to add/create tasks or projects
- User wants to view today's tasks or inbox
- User wants to search for tasks
- User wants to complete/mark tasks as done

**Do NOT use when:**
- User is on Windows/Linux (Things 3 not available)
- User mentions other task apps (Todoist, OmniFocus, etc.)

## Sub-Skills

| Intent | Sub-Skill | Example |
|--------|-----------|---------|
| Add tasks | `skills/add-task.md` | "Add task to write blog post" |
| View today | `skills/list-today.md` | "What's on my plate today?" |
| View inbox | `skills/list-inbox.md` | "Show my inbox" |
| Search tasks | `skills/search.md` | "Find tasks tagged urgent" |
| Complete tasks | `skills/complete-task.md` | "Mark task ABC-123 done" |

## Quick Reference

### Library Imports
```python
import os, sys
sys.path.insert(0, os.path.expanduser('~/.claude/skills/things/lib'))

from reader import ThingsReader   # Database queries
from writer import ThingsWriter   # URL scheme operations
from helpers import ThingsFormatter  # Display formatting
```

### Common Operations
```python
# List tasks
tasks = ThingsReader.get_today()
tasks = ThingsReader.get_inbox()
tasks = ThingsReader.search(query="blog", status="incomplete")

# Add task
ThingsWriter.add_task(title="New task", when="today", tags=["work"])

# Complete task
ThingsWriter.complete_task("task-uuid")

# Format output
print(ThingsFormatter.format_task_list(tasks, verbose=True, show_uuid=True))
```

## Setup

See `README.md` for installation and configuration instructions.

**Quick install:**
```bash
cd ~/.claude/skills/things && pip3 install -r requirements.txt
```

## Dispatching

When user requests Things 3 operations:

1. **Identify intent** from natural language
2. **Read the appropriate sub-skill** for detailed instructions
3. **Execute** using the library functions
4. **Report results** clearly to user

### Intent Mapping

| User Says | Intent | Action |
|-----------|--------|--------|
| "Add...", "Create task...", "New task..." | Add | Read `skills/add-task.md` |
| "What's today?", "Show today", "My tasks" | List Today | Read `skills/list-today.md` |
| "Inbox", "What needs organizing?" | List Inbox | Read `skills/list-inbox.md` |
| "Find...", "Search...", "Show tasks with..." | Search | Read `skills/search.md` |
| "Complete...", "Done...", "Finished..." | Complete | Read `skills/complete-task.md` |

## Limitations

- **macOS only** - Things 3 database only exists on Mac
- **No iOS sync** - Cannot access Things on mobile
- **Auth token needed** for completing tasks (see README.md)
