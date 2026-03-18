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

## Knowledge System Architecture

The user's knowledge management system uses a three-layer architecture designed to enable cross-domain insight generation and inform work outputs.

### Three-Layer Architecture

**Layer 1: SOURCE REPOSITORIES** (Version-controlled, domain-specific)
- Single source of truth for raw content
- Each domain has its own repository with appropriate git/privacy controls

**Layer 2: SYNTHESIS ENGINE** (Obsidian Vault at `~/Projects/Knowledge System/`)
- Cross-domain thematic insights
- Combines personal learning with work data
- Active thinking and project development space

**Layer 3: OUTPUT GENERATION** (Writing repo + presentations)
- Polished deliverables informed by syntheses
- Final work products

### Directory Structure

```
~/Projects/Personal/
└── Content Notes/              [GIT] Personal learning (podcasts, books)
    ├── sources/               Podcast/interview analyses
    ├── syntheses/             Original thematic insights (17 documents)
    └── transcripts/           SRT files

~/Projects/Work/
├── Writing/                    [GIT] Strategic documents and presentations
├── Competitive-Intel/          [LOCAL] Competitive intelligence
├── Customer-Research/          [LOCAL] Customer interviews and analyses
├── Product-Feedback/           [LOCAL] Support data and insights
└── FDF-Progress-Matrix/        [LOCAL] Foundational data fixes tracking

~/Projects/Knowledge System/    [GIT + OBSIDIAN VAULT] Integrated knowledge & people management
├── people/                     33 person files (direct reports & colleagues)
├── conversations/              Meeting transcripts and recordings
├── notes/
│   ├── management-journal/     Monthly leadership notes (YYYY-MM.md)
│   ├── hex-notes/              PLT hex meeting notes
│   ├── strategic-projects/     Project-specific notes & running logs
│   ├── customer-research/      Customer interview notes
│   ├── ai-automation/          AI automation research
│   ├── leadership/             Leadership observations
│   └── platform-architecture/  Technical architecture patterns
├── resources/
│   ├── global-resources/       GPS framework, performance expectations
│   ├── exec-assistant/         Weekly briefing system
│   ├── reviews/                Performance review templates
│   ├── promotions/             Promotion resources
│   ├── PM-Coaching.md          Coaching insights repository
│   ├── AI-CRM-Disruption.md    Strategic signal tracker
│   └── people-list.md          Canonical name reference
├── syntheses/                  Cross-domain thematic insights
│   ├── leadership/             4 syntheses from Content Notes
│   ├── business-strategy/      6 syntheses + cross-domain frameworks
│   ├── ai-trends/              4 syntheses on AI/knowledge work
│   └── life-philosophy/        3 syntheses on curiosity/relationships
├── active-projects/            Current thinking projects
├── Readwise/                   Auto-synced highlights (900+ items)
├── _inbox/                     Quick capture
├── _daily/                     Daily notes and reflections
├── scripts/                    Node.js automation (Wistia, person files)
└── .claude/                    Commands and skills
    ├── commands/               9 slash commands (/log-meeting, /grove-note, etc.)
    └── skills/                 9 specialized skills
```

### Information Flow

```
SOURCES (Layer 1 repos)
  ↓
SYNTHESES (Obsidian vault)
  ↓
OUTPUTS (Writing repo)
```

**Sources** = Raw content in domain-specific repositories
**Syntheses** = Cross-domain insights that connect personal learning with work data
**Outputs** = Polished memos, presentations, strategy documents

### Key Workflows

**Content Notes → Syntheses**:
- New podcast analysis added to Content Notes sources
- Themes identified and added to Content Notes syntheses
- Cross-domain connections identified and documented in Obsidian syntheses

**Work Data → Syntheses**:
- Customer interviews, product feedback, competitive intel collected in Work repos
- Patterns identified that connect to personal learning themes
- Cross-domain syntheses created in Obsidian (e.g., Product Excellence Framework)

**Syntheses → Outputs**:
- Active projects developed in Obsidian's active-projects/ folder
- Draw from multiple syntheses for depth
- Final polished work moved to Writing repo

### Cross-Domain Synthesis Examples

**Product Excellence Framework**:
- Combines "Quality Obsession" + "Focus Strategy" (Content Notes)
- With customer research, product feedback, competitive intel (Work)
- Creates actionable framework for product strategy

**AI-Native Leadership**:
- Combines "Judgment in AI Era" (Content Notes)
- With PM coaching insights (Knowledge System), Agentic Automation Strategy (Work)
- Creates leadership framework for AI transformation

**Customer-Centric Strategy**:
- Combines "Deep Relationships" + "Curiosity" (Content Notes)
- With customer interviews, product feedback (Work)
- Creates customer research-driven strategy process

### Using the System

**When adding new content to Content Notes**:
1. Process media via `/process-media` (automated)
2. New source document created in Content Notes
3. Syntheses updated in Content Notes repo
4. Review for cross-domain connections → add to Obsidian syntheses

**When doing work projects**:
1. Check relevant Knowledge System syntheses for insights
2. Develop thinking in active-projects/ folder
3. Reference sources from both personal learning and work data
4. Move final output to Writing repo when complete

**When logging meetings** (via `/log-meeting`):
1. Creates Conversation file in conversations/ with summary + transcript
2. Updates person file in people/ with key points and feedback
3. Extracts strategic insights to notes/management-journal/
4. Detects and updates running logs in notes/strategic-projects/
5. Suggests new notes for learnings (via note-creator skill)
6. Offers to create Things 3 tasks for action items

### Knowledge System Commands

The Knowledge System includes these slash commands (in `.claude/commands/`):

**People Management:**
- `/log-meeting [transcript or video]` - Comprehensive meeting logging
- `/note [content]` - Add timestamped note to management journal
- `/feedback [PersonName]: [content]` - Quick feedback with auto-tagging
- `/generate-performance-review [name] [cycle]` - GPS-aligned performance review

**Knowledge Development:**
- `/think [topic]` - Create thinking project with auto-synthesized context from across Knowledge System
- `/weekly-review` - Weekly knowledge system review

**Skills Available:**
- `grove-action-manager` - Things 3 integration for action items
- `note-creator` - Create structured notes in Knowledge System
- `active-project-manager` - Update strategic thinking projects
- `name-validator` - Validate names against people-list.md
- `performance-review-generator` - Generate GPS-based reviews
- `promotion-proposal-reviewer` - Review promotion proposals

**How /think works**:
1. Give it a topic for a potential memo/presentation
2. Automatically searches across all Knowledge System content (people files, conversations, notes, syntheses, Readwise, resources)
3. Synthesizes findings on-the-fly: extracts quotes, identifies themes, finds patterns across source types
4. Creates pre-populated thinking project with evidence organized, quotes ready to use, and suggested narrative angles
5. Result: Workspace ready for developing memo idea over 1-2 weeks before formal drafting

### Git and Privacy Controls

**Git-tracked repositories** (public or private):
- Content Notes (public) - https://github.com/jeffvincent/content-notes
- Knowledge System (private) - https://github.com/jeffvincent/knowledge-system
- Writing (private) - https://github.com/jeffvincent/hs-writing

**Archived repositories**:
- Grove (private) - Integrated into Knowledge System on 2026-03-18
  - Backup: `/Users/jvincent/Backups/Grove-backup-2026-03-18.tar.gz`
  - Content migrated: people/, conversations/, resources/, management journal

**Local-only** (sensitive data):
- Competitive-Intel (competitive data)
- Customer-Research (customer privacy)
- Product-Feedback (customer data)
- FDF-Progress-Matrix (internal tracking)

**Knowledge System** (Obsidian Vault):
- Now git-tracked as private repository
- Contains: people files, conversations, management journal, syntheses, resources
- Includes sensitive performance data (private repo)

### System Documentation

All system documentation lives in `~/Projects/Knowledge System/meta/`:
- **source-index.md**: Complete guide to all source repositories
- **synthesis-map.md**: Visual map of cross-domain synthesis opportunities

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
