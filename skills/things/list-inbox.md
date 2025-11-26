# List Inbox Tasks from Things 3

You are helping the user view their inbox tasks that need to be triaged.

## Your Task

Use the Things 3 library to fetch and display all tasks in the inbox that haven't been organized yet.

## How to List Inbox Tasks

```python
import sys
sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')

from reader import ThingsReader
from helpers import ThingsFormatter

# Get inbox tasks
tasks = ThingsReader.get_inbox()

# Format and display
if tasks:
    print(f"📥 Inbox ({len(tasks)} tasks to triage)\n")
    print(ThingsFormatter.format_task_list(tasks, verbose=True, show_uuid=True))
    print("\n" + ThingsFormatter.summarize_tasks(tasks))
else:
    print("✨ Inbox is empty! Everything is organized.")
```

## Purpose of Inbox

The inbox contains:
- Newly captured tasks that haven't been organized
- Tasks that need to be scheduled or assigned to projects
- Quick captures waiting for processing

This is typically used during daily/weekly reviews to triage and organize work.

## Display Options

You can adjust the display based on what the user asks for:
- `verbose=True` - Include notes and tags (default for inbox review)
- `verbose=False` - Just titles (for quick count)
- `show_uuid=True` - Include UUIDs (useful for moving/completing tasks)

## Instructions

1. Fetch inbox tasks using `ThingsReader.get_inbox()`
2. Format them using `ThingsFormatter.format_task_list()`
3. Display a summary
4. If the inbox is large (>10 tasks), suggest grouping or filtering options
5. Always show UUIDs so users can act on tasks

## Example Output

```
📥 Inbox (5 tasks to triage)

☐ Research new framework [ABC-123]
   📝 Look into React 19 features

☐ Buy groceries [DEF-456]
   🏷️  personal, errands

☐ Schedule team meeting [GHI-789]
   📝 Discuss Q1 roadmap
   🏷️  work, meetings

☐ Read article on AI [JKL-012]

☐ Fix bug in login flow [MNO-345]
   🏷️  urgent, bugs

📊 Summary: 5 total tasks
   ☐ 5 incomplete
   🏷️  4 tagged
```

## Pro Tips

- Empty inbox means good organization!
- Suggest scheduling or adding to projects during review
- Highlight tasks with tags as they're partially organized

Now proceed to show the user their inbox tasks!
