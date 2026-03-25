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

## Content Notes in Knowledge System

**MIGRATED 2026-03-20**: Content Notes is now integrated into Knowledge System at `~/Projects/Knowledge System/notes/content notes/`

**Structure:**
- **sources/**: Podcast/interview analysis documents
- **transcripts/**: SRT and text transcripts
- **syntheses/**: Cross-domain thematic insights (leadership, business-strategy, ai-trends, life-philosophy)

**Previous external repository** (`~/Projects/Personal/Content Notes/`) has been deprecated. All new content goes into Knowledge System.

### Auto-Commit Workflow for Content Notes

**IMPORTANT**: After processing each new podcast/interview, automatically commit and push to Knowledge System:

```bash
cd "/Users/jvincent/Projects/Knowledge System"
git add notes/content\ notes/sources/ notes/content\ notes/transcripts/ notes/content\ notes/syntheses/
git commit -m "Add content notes analysis: [Guest Name] - [Topic]

New content:
- Source document with analysis
- Transcript
- Updated synthesis notes: [Theme 1], [Theme 2], [Theme 3]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push
```

**When to commit:**
1. After processing new podcast/interview content
2. After creating new synthesis notes
3. After updating existing synthesis notes with new examples

**DO NOT wait for user to request commit** - proactively commit after each completed analysis.

## Voice Authenticity System

The user has a comprehensive voice authenticity system for ensuring consistent, authentic communication across all contexts.

### Voice-Patterns Repository

**Location**: `~/Projects/Personal/Voice-Patterns/` [GIT - private]
**Repository**: Will be added to GitHub (private)
**Purpose**: Personal voice patterns for authentic communication

**Contents**:
- `analysis/voice-patterns-v1.md` (665 lines) - Comprehensive voice analysis
  - Vocabulary preferences (words to use vs avoid)
  - Sentence structure patterns
  - Tone and formality guidelines
  - Authentic voice markers
  - Red flags and anti-patterns
- `transcripts/` - 7 meeting transcripts from 2025 (source material)
- `examples/` - Before/after voice reviews
- `evolution/` - Voice pattern evolution tracking
  - `changelog.md` - Version history
  - `refinements.md` - Ongoing pattern discoveries

**Based on**: Analysis of 7 meeting transcripts covering various communication contexts

### voice-authenticity Skill

**Location**: `~/.claude/skills/voice-authenticity/`
**Purpose**: Review any content for authentic voice alignment
**Available**: Globally across all projects

**How it works**:
1. Reads voice patterns from Voice-Patterns project
2. Analyzes provided content systematically
3. Identifies voice mismatches (High/Medium/Low priority)
4. Suggests authentic rewrites with specific improvements
5. Highlights authentic moments to preserve
6. Provides voice metrics (sentence length, vocabulary, tone)
7. Offers quick wins (top 3 changes for maximum impact)

**Output**: Structured review with:
- Overall assessment (rating + confidence)
- Issues by priority level
- Authentic moments (what works)
- Voice metrics (quantitative)
- Quick wins
- Before/after examples
- Next steps with time estimates

### Commands

**Global**: `/check-voice`
- Review any content for voice authenticity
- Available in all projects
- Prompts for content if not provided

### Integration

**Knowledge System Projects**:
- `/produce-memo` - Voice check in Step 6 (Integration and Polish)
- `/critique` - Voice authenticity review after main critique
- Recommended before sharing important docs

**Use Cases**:
- Strategic memos before leadership review
- Important emails before sending
- Presentation scripts before delivery
- Documentation for external sharing
- Any high-stakes communication

### Evolution Process

**Continuous Improvement**:
1. After each review, can log insights to `evolution/refinements.md`
2. Quarterly reviews analyze patterns and update voice-patterns
3. Version control tracks voice evolution over time
4. New patterns create new versions (currently v1.0)

**Quarterly Reviews**:
- Review refinements collected over quarter
- Identify recurring themes
- Update voice patterns if significant changes
- Create v2.0 if major evolution
- Update skill to reference new version

### Context-Specific Variations

The skill adapts review approach based on content type:
- **Strategic Memos**: Thorough, executive alignment check
- **Emails**: Lighter touch, focus on clarity
- **Presentations**: Spoken rhythm, energy, engagement
- **Documentation**: Balance authenticity with technical clarity

### Success Metrics

After 1 month:
- Voice check integrated into project workflows
- Used on 3+ memos
- Initial refinements documented

After 3 months:
- 10+ documents reviewed
- First quarterly pattern review completed
- Voice patterns updated based on feedback

After 6 months:
- Voice check routine for all important docs
- 25+ documents reviewed
- Voice evolution trends visible
- Considering v2.0 patterns

**Created**: 2026-03-19
**Current Version**: v1.0

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

**Layer 3: OUTPUT GENERATION** (Knowledge System projects/ directory)
- Polished deliverables informed by syntheses
- Final work products

### Directory Structure

```
~/Projects/Work/
└── (empty - all content archived or migrated to Knowledge System)

~/Projects/Knowledge System/    [GIT + OBSIDIAN VAULT] Integrated knowledge & people management
├── people/                     33 person files (direct reports & colleagues)
├── conversations/              Meeting transcripts and recordings
├── notes/
│   ├── content notes/          MIGRATED 2026-03-20: Personal learning content (podcasts, books, articles)
│   │   ├── sources/            Podcast/interview analysis documents (9 files)
│   │   ├── transcripts/        SRT and text transcripts (8 files)
│   │   └── syntheses/          Cross-domain thematic insights (17 documents)
│   │       ├── leadership/     4 syntheses
│   │       ├── business-strategy/ 8 syntheses
│   │       ├── ai-trends/      4 syntheses
│   │       └── life-philosophy/ 3 syntheses
│   ├── management-journal/     Monthly leadership notes (YYYY-MM.md)
│   ├── hex-notes/              PLT hex meeting notes
│   ├── customer-research/      MIGRATED 2026-03-19: Customer interviews + syntheses (22 synthesis docs)
│   │   ├── interviews/         9 interview analysis files
│   │   ├── syntheses/          Product/theme/persona syntheses
│   │   ├── clips/              Video clips (gitignored)
│   │   └── to-process/         Unprocessed interviews
│   ├── competitive-intelligence/ MIGRATED 2026-03-18: Competitor tracking (15 competitor files)
│   ├── strategic-projects/     Project-specific notes & running logs
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
OUTPUTS (Knowledge System projects/)
```

**Sources** = Raw content (now integrated into Knowledge System at notes/content notes/)
**Syntheses** = Cross-domain insights that connect personal learning with work data
**Outputs** = Polished memos, presentations, strategy documents (in Knowledge System projects/)

### Key Workflows

**Content Notes → Syntheses** (integrated workflow):
- New podcast analysis added to notes/content notes/sources/
- Themes identified and updated in notes/content notes/syntheses/
- Cross-domain connections documented across Knowledge System

**Work Data → Syntheses**:
- Customer interviews (notes/customer-research/), product feedback (Work repos), competitive intel (notes/competitive-intelligence/)
- Patterns identified that connect to personal learning themes from content notes
- Cross-domain syntheses created in notes/content notes/syntheses/

**Syntheses → Outputs**:
- Thinking and memo development happens in notes/ using links and tags
- Draw from content notes syntheses, customer research, and competitive intel
- When ready for drafting, work directly in Knowledge System projects/ directory
- Final polished work published from projects/ to GSuite

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
2. Develop thinking in notes/ using links and tags
3. Reference sources from both personal learning and work data
4. When ready to draft, work directly in Knowledge System projects/ directory

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
- `/think [topic]` - Create thinking note with auto-synthesized context from across Knowledge System
- `/weekly-review` - Weekly knowledge system review

**Skills Available:**
- `grove-action-manager` - Things 3 integration for action items
- `note-creator` - Create structured notes in Knowledge System
- `name-validator` - Validate names against people-list.md
- `performance-review-generator` - Generate GPS-based reviews
- `promotion-proposal-reviewer` - Review promotion proposals

### Git and Privacy Controls

**Git-tracked repositories** (public or private):
- Content Notes (public) - https://github.com/jeffvincent/content-notes
- Knowledge System (private) - https://github.com/jeffvincent/knowledge-system

**Archived repositories**:
- Writing (private) - Integrated into Knowledge System on 2026-03-25
  - Backup: `/Users/jvincent/Backups/Writing-backup-2026-03-25.tar.gz`
  - Content migrated: projects/, resources/global/, agents, commands, skills
- Grove (private) - Integrated into Knowledge System on 2026-03-18
  - Backup: `/Users/jvincent/Backups/Grove-backup-2026-03-18.tar.gz`
  - Content migrated: people/, conversations/, resources/, management journal
- Product-Feedback (local-only) - Archived on 2026-03-25
  - Backup: `/Users/jvincent/Backups/Product-Feedback-backup-2026-03-25.tar.gz`
  - Last analysis: November 3, 2025 (Data Platform Code Orange - 3,664 issues)
  - Reason: Dormant for 4.5 months, customer insights work moved to Knowledge System

**Local-only** (sensitive data):
- (none - all Work repositories have been archived or migrated)

**Knowledge System** (Obsidian Vault):
- Git-tracked as private repository
- Contains: people files, conversations, management journal, customer research, competitive intelligence, syntheses, resources, projects, agents, commands, skills
- Includes sensitive performance data (private repo)
- Customer research video files gitignored (too large)
- Migrated content:
  - Competitive Intelligence (2026-03-18)
  - Customer Research (2026-03-19)
  - Writing repo integration (2026-03-25): projects/, resources/global/, agents, commands, skills

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
