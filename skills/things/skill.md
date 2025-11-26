---
name: things
description: Manage your Things 3 tasks - add, search, list, and complete tasks using natural language
location: user
---

# Things 3 Task Management

Comprehensive task management integration with Things 3 using natural language commands.

## Overview

This skill provides seamless integration with Things 3, allowing you to manage your tasks through natural language. It combines fast database reads with the official Things URL scheme for reliable task management.

## Available Commands

### 1. Add Tasks
Create new tasks with rich metadata including notes, tags, dates, deadlines, and checklists.

**Examples:**
- "Add a task to write blog post today with tag work"
- "Create task 'Call dentist' tomorrow with tag health"
- "Add 'Plan vacation' with checklist: book flights, reserve hotel, pack"
- "New task 'Review Q4 report' in Work project, due December 1st"

**Sub-skill:** `add-task.md`

---

### 2. List Today's Tasks
View all tasks scheduled for today with full context.

**Examples:**
- "What's on my plate today?"
- "Show me today's tasks"
- "List today grouped by project"

**Sub-skill:** `list-today.md`

---

### 3. List Inbox
View tasks that need to be triaged and organized.

**Examples:**
- "Show my inbox"
- "What needs to be organized?"
- "List inbox tasks"

**Sub-skill:** `list-inbox.md`

---

### 4. Search Tasks
Find tasks by keyword with powerful filtering by status, area, project, and tags.

**Examples:**
- "Find all tasks mentioning 'API'"
- "Show incomplete tasks in Marketing area tagged urgent"
- "Search for 'deployment' in Backend project"
- "What completed tasks mention 'blog'?"

**Sub-skill:** `search.md`

---

### 5. Complete Tasks
Mark tasks as done by title or UUID.

**Examples:**
- "Mark task ABC-123 as complete"
- "Complete the dentist task"
- "Mark all today tasks as done"

**Sub-skill:** `complete-task.md`

---

## Setup Requirements

### 1. Install Dependencies

```bash
cd ~/.claude/skills/things
pip3 install -r requirements.txt
```

This installs:
- `things.py` - Python library for reading Things database
- `python-dateutil` - Date parsing utilities

### 2. Verify Things 3 Installation

Make sure Things 3 is installed and running on your Mac.

### 3. Enable Things URLs (Required for completing tasks)

To complete or update tasks, you need to enable Things URLs and get an auth token:

1. Open Things 3
2. Go to **Preferences** > **General**
3. Check **"Enable Things URLs"**
4. Copy the **auth token** that appears

Then save it:

```bash
# Method 1: Environment variable (temporary)
export THINGS_AUTH_TOKEN="your-token-here"

# Method 2: Save to config (permanent)
python3 -c "
import sys
sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')
from writer import ThingsWriter
ThingsWriter.set_auth_token('your-token-here')
"
```

**Note:** You only need the auth token for completing/updating tasks. Reading and adding tasks work without it.

---

## Technical Architecture

### Hybrid Approach

This skill uses a hybrid approach for optimal performance:

- **Reading data**: Direct SQLite database access via `things.py` (fast, comprehensive)
- **Writing data**: Things URL Scheme (official, reliable, fully-featured)

### Library Structure

```
~/.claude/skills/things/
├── skill.md                 (this file - skill manifest)
├── requirements.txt         (Python dependencies)
├── lib/
│   ├── reader.py           (ThingsReader - database queries)
│   ├── writer.py           (ThingsWriter - URL scheme operations)
│   └── helpers.py          (ThingsFormatter - display formatting)
├── add-task.md             (Add task sub-skill)
├── list-today.md           (List today sub-skill)
├── list-inbox.md           (List inbox sub-skill)
├── search.md               (Search tasks sub-skill)
└── complete-task.md        (Complete task sub-skill)
```

### Core Components

**ThingsReader** (`lib/reader.py`):
- `get_today()` - Today's tasks
- `get_inbox()` - Inbox tasks
- `search()` - Search with filters
- `get_projects()` - All projects
- `find_by_title()` - Find by title match

**ThingsWriter** (`lib/writer.py`):
- `add_task()` - Create new task
- `add_project()` - Create new project
- `complete_task()` - Mark as complete
- `update_task()` - Update existing task

**ThingsFormatter** (`lib/helpers.py`):
- `format_task()` - Format single task
- `format_task_list()` - Format task lists
- `summarize_tasks()` - Generate summaries

---

## Usage Patterns

### Morning Routine
```
1. "Show me today's tasks"
2. "What's in my inbox?"
3. "List upcoming tasks"
```

### Quick Capture
```
"Add task 'Buy groceries' today with tag errands"
"Create task 'Review PR #234' in Engineering project"
```

### Planning & Organization
```
"Search for tasks in Marketing area"
"Show incomplete tasks tagged urgent"
"List all projects in Work area"
```

### End of Day
```
"Complete task ABC-123"
"Mark the dentist task as done"
```

---

## Interpreting User Requests

When the user asks to work with Things 3, determine their intent and invoke the appropriate sub-skill:

| User Intent | Sub-Skill |
|-------------|-----------|
| Add/create new task or project | `add-task.md` |
| See today's schedule | `list-today.md` |
| Review inbox/triage | `list-inbox.md` |
| Find/search specific tasks | `search.md` |
| Mark task(s) as done | `complete-task.md` |

### Natural Language Examples

- "What do I need to do today?" → **list-today**
- "Add buy milk to my list" → **add-task**
- "Find all urgent tasks" → **search** (query="", tag="urgent")
- "I finished the blog post" → **complete-task** (title="blog post")
- "What's in my inbox?" → **list-inbox**
- "Create task for meeting tomorrow" → **add-task**

---

## Advanced Features

### Batch Operations

Complete multiple tasks:
```python
# Search for tasks
tasks = ThingsReader.search(query="cleanup", status="incomplete")

# Complete them all
for task in tasks:
    ThingsWriter.complete_task(task['uuid'])
```

### Rich Task Creation

Add tasks with full context:
```python
ThingsWriter.add_task(
    title="Launch marketing campaign",
    notes="Target Q1 audience\nBudget: $50k",
    when="2025-12-01",
    deadline="2025-12-15",
    tags=["marketing", "high-priority"],
    list_name="Marketing Projects",
    checklist_items=[
        "Design creatives",
        "Setup ad campaigns",
        "Create landing page",
        "Configure analytics"
    ]
)
```

### Smart Filtering

Combine multiple filters:
```python
# Urgent work tasks in a specific project
results = ThingsReader.search(
    query="",
    status="incomplete",
    area="Work",
    project="Product Launch",
    tag="urgent"
)
```

---

## Troubleshooting

### "things.py not found"
```bash
cd ~/.claude/skills/things
pip3 install -r requirements.txt
```

### "Auth token not configured" (when completing tasks)
1. Open Things 3 → Preferences → General
2. Enable "Enable Things URLs"
3. Copy the auth token
4. Save it using the setup instructions above

### "No tasks found" (when listing or searching)
- Verify Things 3 is installed and has data
- Check that the database path is accessible
- Try opening Things 3 to ensure it's initialized

### Tasks not appearing after adding
- Things URLs open the app but may take a moment to process
- Check Things 3 app to verify the task was created
- Ensure URL parameters are properly formatted

---

## Extending This Skill

Want to add more functionality? Here are ideas:

### Additional Sub-Skills

1. **list-upcoming.md** - Show upcoming scheduled tasks
2. **list-projects.md** - List all projects with task counts
3. **add-project.md** - Create full projects with tasks
4. **stats.md** - Show productivity statistics
5. **export.md** - Export tasks to JSON/CSV/Markdown

### Custom Workflows

Create workflow-specific skills:
- **weekly-review.md** - Guided weekly review process
- **daily-plan.md** - Plan your day interactively
- **batch-schedule.md** - Schedule multiple tasks at once

---

## Best Practices

1. **Always show UUIDs** when listing tasks - makes follow-up actions (completing, updating) easier
2. **Use verbose mode** for planning/review - see full context
3. **Group large result sets** - easier to scan by project or area
4. **Search before adding** - avoid duplicates
5. **Regular inbox triage** - keep your system organized

---

## Limitations

- **Mac only** - Things 3 database only exists on macOS
- **No iOS support** - Cannot access Things on iPhone/iPad remotely
- **No real-time sync** - Database reads don't reflect unsaved changes
- **Rate limits** - URL scheme limited to 250 operations per 10 seconds
- **No deletion** - URL scheme doesn't support deleting tasks (must do in app)

---

## Support & Resources

**Official Documentation:**
- Things URL Scheme: https://culturedcode.com/things/support/articles/2803573/
- AppleScript Guide: https://culturedcode.com/things/download/ThingsAppleScriptGuide.pdf

**things.py Library:**
- GitHub: https://github.com/thingsapi/things.py
- PyPI: https://pypi.org/project/things.py/

**Community:**
- Things Forum: https://culturedcode.com/things/support/
- Reddit: r/thingsapp

---

When a user asks to work with Things 3, identify their intent and invoke the appropriate sub-skill to help them manage their tasks naturally and efficiently.
