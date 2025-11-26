# List Today's Tasks from Things 3

You are helping the user view their tasks scheduled for today.

## Your Task

Use the Things 3 library to fetch and display all tasks scheduled for today in a clear, readable format.

## How to List Today's Tasks

```python
import sys
sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')

from reader import ThingsReader
from helpers import ThingsFormatter

# Get today's tasks
tasks = ThingsReader.get_today()

# Format and display
if tasks:
    print(f"📅 Today's Tasks ({len(tasks)})\n")
    print(ThingsFormatter.format_task_list(tasks, verbose=True, show_uuid=True))
    print("\n" + ThingsFormatter.summarize_tasks(tasks))
else:
    print("🎉 No tasks scheduled for today!")
```

## Display Options

**Default (verbose)**: Shows task with notes, tags, project, area, deadlines
**Compact**: Just checkboxes and titles
**Grouped**: Group by project or area

You can adjust the display based on what the user asks for:
- `verbose=True` - Include all metadata
- `verbose=False` - Just titles
- `show_uuid=True` - Include UUIDs (useful for completing tasks later)
- `group_by='project'` - Group by project
- `group_by='area'` - Group by area

## Instructions

1. Fetch today's tasks using `ThingsReader.get_today()`
2. Format them using `ThingsFormatter.format_task_list()`
3. Display a summary using `ThingsFormatter.summarize_tasks()`
4. If there are many tasks, ask if the user wants to see them grouped or filtered
5. Always show UUIDs so users can complete tasks easily

## Example Output

```
📅 Today's Tasks (3)

☐ Write blog post [ABC-123]
   📝 Focus on API design patterns
   🏷️  writing, work
   📂 Content Creation

☐ Call dentist [DEF-456]
   🏷️  health, calls

☑ Review pull request [GHI-789]
   📂 Engineering

📊 Summary: 3 total tasks
   ☐ 2 incomplete
   ☑ 1 completed
   🏷️  3 tagged
```

Now proceed to show the user their today tasks!
