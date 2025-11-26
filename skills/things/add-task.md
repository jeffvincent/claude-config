# Add Task to Things 3

You are helping the user add a new task to Things 3.

## Your Task

Use the Things 3 library to create a new task based on the user's request. Extract the relevant information from their natural language input.

## Available Parameters

- **title** (required): The task title
- **notes**: Detailed notes or description
- **when**: When to schedule the task:
  - `today` - Schedule for today
  - `tomorrow` - Schedule for tomorrow
  - `evening` - Schedule for this evening
  - `anytime` - Add to Anytime list
  - `someday` - Add to Someday list
  - `YYYY-MM-DD` - Specific date (e.g., 2025-11-20)
- **deadline**: Deadline date in YYYY-MM-DD format
- **tags**: List of tags (e.g., ["work", "urgent"])
- **list_name**: Name of project or area to add to
- **checklist_items**: List of checklist items (e.g., ["Step 1", "Step 2"])

## How to Add a Task

```python
import sys
sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')

from writer import ThingsWriter

# Example: Add a simple task
ThingsWriter.add_task(
    title="Write blog post",
    notes="Focus on API design patterns",
    when="today",
    tags=["writing", "work"]
)

print("✅ Task added to Things!")
```

## Instructions

1. Parse the user's request to extract task details
2. Use ThingsWriter.add_task() with the appropriate parameters
3. Confirm the task was added successfully
4. If the user's request is ambiguous, ask clarifying questions

## Examples

**User**: "Add a task to call the dentist tomorrow with tag health"
**Action**:
```python
ThingsWriter.add_task(
    title="Call dentist",
    when="tomorrow",
    tags=["health"]
)
```

**User**: "Create a task to review Q4 report in the Work project, due December 1st"
**Action**:
```python
ThingsWriter.add_task(
    title="Review Q4 report",
    list_name="Work",
    deadline="2025-12-01"
)
```

**User**: "Add task 'Plan vacation' with checklist: book flights, reserve hotel, pack bags"
**Action**:
```python
ThingsWriter.add_task(
    title="Plan vacation",
    checklist_items=["Book flights", "Reserve hotel", "Pack bags"]
)
```

Now proceed to help the user add their task to Things 3!
