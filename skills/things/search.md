# Search Tasks in Things 3

You are helping the user search for tasks across their entire Things 3 database.

## Your Task

Use the Things 3 library to search for tasks based on keywords and filters, then display the results in a clear format.

## How to Search Tasks

```python
import sys
sys.path.insert(0, '/Users/jvincent/.claude/skills/things/lib')

from reader import ThingsReader
from helpers import ThingsFormatter

# Search with filters
results = ThingsReader.search(
    query="blog",           # Required: search term
    status="incomplete",     # Optional: incomplete, completed, canceled
    area="Work",            # Optional: filter by area name
    project="Content",      # Optional: filter by project name
    tag="urgent"            # Optional: filter by tag name
)

# Display results
if results:
    print(f"🔍 Found {len(results)} task(s) matching 'blog'\n")
    print(ThingsFormatter.format_task_list(results, verbose=True, show_uuid=True))
else:
    print("No tasks found matching your criteria.")
```

## Available Filters

- **query** (required): Keyword to search in title and notes
- **status**: Filter by status
  - `incomplete` - Only active tasks
  - `completed` - Only completed tasks
  - `canceled` - Only canceled tasks
  - `None` - All statuses (default)
- **area**: Filter by area name (e.g., "Work", "Personal")
- **project**: Filter by project name
- **tag**: Filter by tag name

## Instructions

1. Parse the user's search request to extract:
   - The search keyword/query
   - Any filters they mentioned
2. Use `ThingsReader.search()` with appropriate parameters
3. Display results with `ThingsFormatter.format_task_list()`
4. If many results, offer to group by project/area
5. Always include UUIDs for follow-up actions
6. If no results, suggest broadening the search

## Example Searches

**User**: "Find all tasks with 'meeting' in them"
```python
results = ThingsReader.search(query="meeting")
```

**User**: "Show incomplete tasks in the Marketing area tagged urgent"
```python
results = ThingsReader.search(
    query="",  # Empty query matches all
    status="incomplete",
    area="Marketing",
    tag="urgent"
)
```

**User**: "What completed tasks mention 'deployment'?"
```python
results = ThingsReader.search(
    query="deployment",
    status="completed"
)
```

**User**: "Search for 'api' in the Backend project"
```python
results = ThingsReader.search(
    query="api",
    project="Backend"
)
```

## Advanced Options

For large result sets, group the output:
```python
print(ThingsFormatter.format_task_list(results, verbose=True, show_uuid=True, group_by='project'))
```

## Example Output

```
🔍 Found 3 task(s) matching 'blog'

☐ Write blog post [ABC-123]
   📝 Focus on API design patterns
   🏷️  writing, work
   📂 Content Creation
   📍 Work

☐ Edit blog images [DEF-456]
   📂 Content Creation
   📍 Work

☑ Research blog topics [GHI-789]
   📝 Found 5 good topics
   🏷️  research
   📂 Content Creation
```

## Pro Tips

- Empty query ("") with filters is useful for browsing by area/project/tag
- Combine filters to narrow down large task lists
- Use status="incomplete" by default unless user asks for completed/canceled
- Suggest related searches if results are empty

Now proceed to help the user search their Things 3 tasks!
