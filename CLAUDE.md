# Claude Code Configuration Repository

This is the user's personal Claude Code configuration directory, which is also a git repository published at https://github.com/jeffvincent/claude-config.

## Repository Purpose

This repository contains:
- **Custom Skills**: 11 specialized skills for Gmail, Calendar, Wistia, video processing, browser automation, etc.
- **Commands**: Custom slash commands for workflows
- **Hooks**: Event-driven automation scripts
- **Plugins**: Plugin configurations
- **Settings**: Claude Code configuration

## Task Management - CRITICAL

**ALWAYS use Things 3 for task management, NOT TodoWrite.**

When creating action items, todos, or tasks:
1. **Use the `things` skill** to add tasks to Things 3
2. Include appropriate deadline dates (YYYY-MM-DD format)
3. Add relevant tags (e.g., "work", "grove", "meeting")
4. Add notes with context when helpful

**DO NOT use TodoWrite tool** - it's an internal conversation tracker, not the user's actual task management system.

### When to Create Tasks in Things 3:
- Action items from meetings (especially via `/log-meeting` command)
- Project planning tasks with specific due dates
- Follow-up items from strategic discussions
- User explicitly requests tasks to be created
- User says "implement action items" or "create todos"

### Example Usage:
```python
import os, sys
sys.path.insert(0, os.path.expanduser('~/.claude/skills/things/lib'))
from writer import ThingsWriter

ThingsWriter.add_task(
    title="Task title",
    notes="Additional context",
    deadline="2026-01-15",
    tags=["work", "grove"]
)
```

## Content Notes Repository

The user also has a separate git repository for Content Notes at `/Users/jvincent/Projects/Personal/Content Notes/`:
- **Repository**: https://github.com/jeffvincent/content-notes
- **Purpose**: Knowledge base for extracting insights from podcasts and interviews
- **Contents**: Source documents, synthesis notes, transcripts, and automation scripts

### Auto-Commit Workflow for Content Notes

**IMPORTANT**: After processing each new podcast/interview (via `/process-media` command or manual workflow), automatically commit and push the new content:

```bash
cd "/Users/jvincent/Projects/Personal/Content Notes"
git add .
git commit -m "Add analysis for [Guest Name] - [Topic]

New content:
- Source document with interview analysis
- Transcript (SRT format)
- Updated synthesis notes: [Theme 1], [Theme 2], [Theme 3]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

**When to commit to Content Notes:**
1. After completing `/process-media` workflow (new source document created)
2. After creating new synthesis notes
3. After updating existing synthesis notes with new examples
4. After script improvements or documentation updates

**DO NOT wait for user to request commit** - proactively commit after each completed analysis.

## Important: Secrets Management

All credentials are stored in the `secrets/` directory with this structure:
```
secrets/
├── wistia/
│   ├── .env (API tokens)
│   └── .env.example
├── google-calendar/
│   ├── credentials.json (OAuth)
│   ├── tokens.json (OAuth tokens)
│   └── README.md
└── gmail/
    ├── credentials.json (OAuth)
    ├── tokens.json (OAuth tokens)
    └── README.md
```

**CRITICAL**: The `secrets/` directory is gitignored. Never commit credentials.

## Skill Code Structure

Skills that reference secrets use relative paths:
- **Wistia**: `../../secrets/wistia/.env`
- **Google Calendar**: `../../../../secrets/google-calendar/` (from scripts/auth/)
- **Gmail**: `../../../../secrets/gmail/` (from scripts/auth/)

When modifying skill code, maintain these path references.

## Git Workflow - IMPORTANT

### When to Commit and Push

**Always commit and push** when you make:
1. **New Skills**: Any new skill added to `skills/`
2. **New Commands**: New slash commands in `commands/`
3. **New Hooks**: New hook scripts in `hooks/`
4. **Skill Modifications**: Significant updates to existing skills
5. **Configuration Changes**: Updates to settings, plugins, or structure
6. **Documentation**: Updates to README files or documentation
7. **Bug Fixes**: Any bug fixes or improvements

### How to Commit

Use this workflow for any significant changes:

```bash
# Stage all changes
git add .

# Check what will be committed (verify no secrets)
git status

# Commit with descriptive message
git commit -m "Brief description of changes

Detailed explanation if needed.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push to GitHub
git push
```

### Commit Message Guidelines

- Use present tense ("Add skill" not "Added skill")
- Be descriptive about what changed
- Include Co-Authored-By tag
- Examples:
  - "Add new Discord integration skill"
  - "Update gmail-skill to support batch operations"
  - "Fix OAuth token refresh in google-calendar-skill"
  - "Add command for processing podcast transcripts"

### What NOT to Commit

The `.gitignore` handles this, but never commit:
- `secrets/` directory (credentials)
- `history.jsonl` (conversation history)
- `debug/`, `session-env/`, `file-history/` (runtime data)
- `node_modules/` (dependencies)
- Personal data directories

## Development Guidelines

### Adding a New Skill

1. Create directory in `skills/`
2. Add `Skill.md` or `SKILL.md` with skill prompt
3. Add implementation scripts and `package.json` if needed
4. If credentials needed:
   - Add to `secrets/` directory (create subdirectory)
   - Create `.example` files
   - Update `.gitignore` if necessary
   - Document in README
5. **Commit and push the new skill**

### Modifying Existing Skills

1. Make changes to skill code
2. Test the skill works correctly
3. Update documentation if needed
4. **Commit and push the changes**

### Adding Commands or Hooks

1. Create the command/hook file
2. Update relevant configuration
3. Test it works
4. **Commit and push**

## Dependencies

Skills with `package.json` require `npm install`:
- `skills/gmail-skill/`
- `skills/google-calendar-skill/`
- `skills/wistia-uploader/`
- `skills/interview-synthesis-updater/`

Dependencies are gitignored and must be reinstalled after cloning.

## Testing Changes

Before committing:
1. Verify secrets are not exposed
2. Test modified skills/commands work
3. Check `git status` for unexpected files
4. Review `git diff` for sensitive data

## Proactive Git Management

**YOU SHOULD PROACTIVELY** commit and push whenever you:
- Complete a user request that adds/modifies functionality
- Add or update a skill at the user's request
- Fix a bug or improve existing code
- Add documentation or examples

Don't wait for the user to ask you to commit - do it automatically after completing significant work.

## Quick Reference

**Check status**: `git status`
**View changes**: `git diff`
**Commit all**: `git add . && git commit -m "message" && git push`
**View log**: `git log --oneline`

## Repository Link

https://github.com/jeffvincent/claude-config
