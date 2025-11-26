# Claude Code Configuration Repository

This is the user's personal Claude Code configuration directory, which is also a git repository published at https://github.com/jeffvincent/claude-config.

## Repository Purpose

This repository contains:
- **Custom Skills**: 11 specialized skills for Gmail, Calendar, Wistia, video processing, browser automation, etc.
- **Commands**: Custom slash commands for workflows
- **Hooks**: Event-driven automation scripts
- **Plugins**: Plugin configurations
- **Settings**: Claude Code configuration

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
