---
name: todoist-manager
description: "Manage Todoist tasks — add, search, list, complete, and reschedule tasks using natural language. Uses Todoist MCP tools."
version: 3.0.0
location: user
allowed-tools: [mcp__claude_ai_Todoist__add-tasks, mcp__claude_ai_Todoist__find-tasks, mcp__claude_ai_Todoist__find-tasks-by-date, mcp__claude_ai_Todoist__complete-tasks, mcp__claude_ai_Todoist__reschedule-tasks, mcp__claude_ai_Todoist__update-tasks, mcp__claude_ai_Todoist__get-overview, mcp__claude_ai_Todoist__find-completed-tasks]
---

# Todoist Task Management

Manage tasks in Todoist through natural language. Uses Todoist MCP tools directly — no Python library required.

## When to Apply

Use this skill when:
- User wants to add/create tasks
- User wants to view today's tasks or inbox
- User wants to search for tasks
- User wants to complete or reschedule tasks
- User wants an overview of open work

## Sub-Skills

| Intent | Sub-Skill | Example |
|--------|-----------|---------|
| Add tasks | `skills/add-task.md` | "Add task to write blog post" |
| View today | `skills/list-today.md` | "What's on my plate today?" |
| View inbox | `skills/list-inbox.md` | "Show my inbox" |
| Search tasks | `skills/search.md` | "Find tasks tagged urgent" |
| Complete tasks | `skills/complete-task.md` | "Mark task done" |

## Key Todoist Concepts

**Due date vs. Deadline:**
- `dueString` — movable due date (natural language: "tomorrow", "next Monday", "in 3 days")
- `deadlineDate` — immovable hard constraint (ISO format: "2026-06-01") — use for meeting-prep tasks and fixed commitments

**Scheduling:**
- Always use `reschedule-tasks` (not `update-tasks`) when moving a task to a different date — preserves recurrence patterns
- Use `update-tasks` only for non-date changes (title, description, priority, labels)

**Labels:** `work`, `meeting`, `weekly-plan`, `knowledge-system`, `grove`

**Priorities:** `p1` (highest) → `p4` (lowest/default). Always pass as strings, not integers.

## Identifying Discrete Tasks

**IMPORTANT:** Not everything that looks like an action item should become a task. Apply these filters:

### ✅ Create Tasks For

**Discrete actions with clear completion:**
- "Deliver plan by Jan 17"
- "Schedule meeting with X"
- "Send email to Y about Z"
- "Review document and provide feedback"

**Characteristics of real tasks:**
- Has a verb + specific object
- Can be marked "done" at a point in time
- Usually has a deadline or timeframe
- Represents single deliverable or interaction

### ❌ Do NOT Create Tasks For

- Strategic mindsets / ongoing approaches ("Own entire product mentality")
- Framing guidance ("Frame work using X framing")
- Conceptual frameworks ("Prioritize by user exposure")

**When uncertain:** Can I mark this "done" at a specific moment? If no → not a task.

## Dispatching

When user requests Todoist operations:

1. **Identify intent** from natural language
2. **Filter for discrete tasks** (see above)
3. **Read the appropriate sub-skill** for detailed instructions
4. **Execute** using the Todoist MCP tools
5. **Report results** clearly to user

### Intent Mapping

| User Says | Intent | Action |
|-----------|--------|--------|
| "Add...", "Create task...", "New task..." | Add | Read `skills/add-task.md` |
| "What's today?", "Show today", "My tasks" | List Today | Read `skills/list-today.md` |
| "Inbox", "What needs organizing?" | List Inbox | Read `skills/list-inbox.md` |
| "Find...", "Search...", "Show tasks with..." | Search | Read `skills/search.md` |
| "Complete...", "Done...", "Finished..." | Complete | Read `skills/complete-task.md` |
