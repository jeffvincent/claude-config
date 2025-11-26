# Complete Task in Things 3

You are helping the user mark a task as complete.

## Your Task

Use the Things 3 library to mark one or more tasks as complete based on the user's request.

## How to Complete a Task

```python
import sys
sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')

from reader import ThingsReader
from writer import ThingsWriter

# Option 1: Complete by UUID (most reliable)
task_id = "ABC-123-DEF-456"
ThingsWriter.complete_task(task_id)
print(f"✅ Task {task_id} marked as complete!")

# Option 2: Find by title and complete
tasks = ThingsReader.find_by_title("Write blog post")
if tasks:
    task = tasks[0]  # Take first match
    ThingsWriter.complete_task(task['uuid'])
    print(f"✅ Completed: {task['title']}")
else:
    print("❌ Task not found")
```

## Finding Tasks to Complete

**By UUID** (recommended - shown from list/search results):
```python
ThingsWriter.complete_task("ABC-123-DEF-456")
```

**By Title** (when user references task by name):
```python
# Search for the task
tasks = ThingsReader.find_by_title("dentist")

# If multiple matches, ask user to clarify
if len(tasks) > 1:
    print(f"Found {len(tasks)} tasks matching 'dentist':")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} [{task['uuid']}]")
    # Ask user which one
elif len(tasks) == 1:
    ThingsWriter.complete_task(tasks[0]['uuid'])
    print(f"✅ Completed: {tasks[0]['title']}")
else:
    print("❌ No tasks found matching 'dentist'")
```

## Instructions

1. **Identify the task** the user wants to complete:
   - If they provide a UUID, use it directly
   - If they reference by title, search for it
   - If they say "the task from earlier", look at conversation context

2. **Handle multiple matches**:
   - If multiple tasks match the title, show options and ask user to pick
   - Include enough context (project, area, notes preview) to distinguish

3. **Complete the task**:
   - Use `ThingsWriter.complete_task(uuid)`
   - Confirm with a success message

4. **Handle errors**:
   - If task not found, suggest searching
   - If auth token missing, provide setup instructions

## Auth Token Setup

**IMPORTANT**: Completing tasks requires an auth token. If you get an auth token error:

1. Tell the user to:
   - Open Things 3
   - Go to Preferences > General
   - Check "Enable Things URLs"
   - Copy the auth token

2. Save the token:
```python
from writer import ThingsWriter
ThingsWriter.set_auth_token("paste-token-here")
```

Or set environment variable:
```bash
export THINGS_AUTH_TOKEN="paste-token-here"
```

## Examples

**User**: "Mark task ABC-123 as done"
```python
ThingsWriter.complete_task("ABC-123")
```

**User**: "Complete the dentist task"
```python
tasks = ThingsReader.find_by_title("dentist")
if len(tasks) == 1:
    ThingsWriter.complete_task(tasks[0]['uuid'])
    print(f"✅ Completed: {tasks[0]['title']}")
```

**User**: "Mark all today tasks as complete"
```python
today_tasks = ThingsReader.get_today()
incomplete = [t for t in today_tasks if t['status'] == 'incomplete']

print(f"Completing {len(incomplete)} tasks:")
for task in incomplete:
    print(f"  ☐ {task['title']}")
    ThingsWriter.complete_task(task['uuid'])

print(f"\n✅ All {len(incomplete)} tasks completed!")
```

## Example Output

```
✅ Task completed: Call dentist

Task marked as complete in Things 3!
```

**Multiple matches:**
```
Found 3 tasks matching 'blog':
1. Write blog post [ABC-123] - Content Creation
2. Edit blog images [DEF-456] - Content Creation
3. Review blog draft [GHI-789] - Marketing

Which one would you like to complete? (1-3)
```

## Pro Tips

- Always confirm what was completed
- For batch completion, show progress
- Suggest using UUIDs from list/search results for precision
- If completing many tasks, consider rate limits (250/10sec)

Now proceed to help the user complete their task(s)!
