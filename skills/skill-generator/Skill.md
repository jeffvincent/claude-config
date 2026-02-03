---
name: Skill Generator
description: Create complete Claude Skills from a short brief, with templates and checks.
version: 1.0.0
allowed-tools: [Read, Write, Glob]
---

## Overview
This Skill helps you rapidly author high‑quality Claude Skills from a short prompt. It converts a brief into a complete Skill folder structure that follows official guidelines, including correct YAML frontmatter, focused scope, clear instructions, examples, and optional resources/scripts. It enforces naming and description limits so Claude selects and loads generated Skills appropriately.

## When to Use
- Drafting a new Skill from a one‑to‑two paragraph brief
- Converting existing SOPs or playbooks into a Claude Skill
- Standardizing Skills across a team with consistent structure, language, and checks

## Inputs
- Working brief: purpose, audience, and the repeatable workflow this Skill will cover
- Triggers: when to apply the Skill; clear “in vs out of scope” boundaries
- Constraints: security, compliance, and privacy notes (no secrets)
- Optional resources: links/files to include as references
- Optional scripts: languages/dependencies if executable helpers are needed

## Outputs
- A new Skill folder named after the Skill
- Skill.md with valid YAML frontmatter and structured body
- Optional `resources/` files (templates, references, examples, checklists)
- Optional stub scripts and declared dependencies

## Guardrails and Rules
- Name: ≤ 64 chars; Description: ≤ 200 chars (succinct, specific triggers)
- Always start with YAML frontmatter containing `name` and `description`
- Keep one workflow per Skill; split multi‑workflow briefs into separate Skills
- Don’t hardcode secrets; list dependencies in frontmatter if scripts are included
- Prefer reference files under `resources/` for long or situational content
- Provide at least one concrete example input and output
- Include a short "When to Apply" section so Claude can load this Skill correctly

## Generation Steps (what to do when invoked)

**Phase 1: Plan and Review**
1) Parse the brief and propose a clear Skill `name` (≤64 chars) and `description` (≤200 chars) that explicitly states when to use it.
2) Plan the `Skill.md` structure using `resources/SKILL_TEMPLATE.md`:
   - Overview, When to Apply, Inputs, Outputs, Instructions for Claude, Examples, Testing Checklist, Security/Privacy.
3) Identify `resources/` files that will increase clarity:
   - References (REFERENCE.md), CHECKLIST.md, EXAMPLES.md, or domain snippets.
4) If scripts are requested, identify what stubs are needed and dependencies in frontmatter `dependencies:`.
5) Validate plan against the checklist (see `resources/CHECKLIST.md`).
6) **Present the complete plan to the user:**
   - Proposed folder structure (all paths and filenames)
   - Skill name and description
   - Key sections and what each file will contain
   - High-level outline of Instructions for Claude
   - Number of examples that will be included
7) **STOP and wait for user approval before creating any files.**

**Phase 2: Generate Files (only after user approval)**
8) Use the Write tool to create each file:
   - Start with `Skill.md` (include YAML frontmatter)
   - Create all `resources/` files
   - Create any optional scripts or package.json
9) Confirm all files were created successfully.
10) Provide a summary of what was generated and how to use the new skill.

## Instructions for Claude (authoring voice)
- Use imperative, testable instructions; avoid vague language.
- Prefer short sections and bullets; add examples where ambiguity is likely.
- State explicit "in-scope" and "out-of-scope" to keep the Skill focused.
- Embed only essential context in `Skill.md`; move long details to `resources/`.

## Examples

### Example Plan Presentation (Phase 1)
```
User: Create a 'Meeting Notetaker' Skill that extracts action items and owners from transcripts.

Claude: I'll create a Meeting Notetaker skill. Here's my plan:

**Skill Details:**
- Name: meeting-notetaker (17 chars ✓)
- Description: Extract action items and owners from meeting transcripts. Use when user provides meeting transcript and asks to identify action items, tasks, or follow-ups. (184 chars ✓)

**File Structure:**
meeting-notetaker/
├── Skill.md (main skill instructions)
├── README.md (user documentation)
└── resources/
    ├── EXAMPLES.md (3 examples: basic extraction, complex meeting, unclear owners)
    └── CHECKLIST.md (validation checklist)

**Skill.md will include:**
- Overview: Purpose and what the skill does
- When to Apply: Trigger phrases and in/out of scope
- Inputs: Meeting transcript (text or markdown), optional format preference
- Outputs: Structured list of action items with owners, deadlines, status
- Instructions for Claude:
  1. Parse transcript for imperative statements and commitments
  2. Identify person names or roles as owners
  3. Extract deadlines or time references
  4. Format as checklist or table based on user preference
  5. Flag unclear action items for user clarification
- Examples: 3 detailed scenarios
- Security: No PII logging, keep meeting content private

**Key Features:**
- Handles multiple formats (plain text, markdown, SRT)
- Identifies explicit and implicit action items
- Flags ambiguous owners
- Supports different output formats

Does this plan look good? Should I proceed with creating the files?
```

### After User Approval
- Claude uses Write tool to create all files
- Confirms creation and provides usage instructions

## Testing Checklist (summary)
- Name/description limits respected; YAML frontmatter present
- Description clearly states when to use the Skill
- Includes at least one input/output example
- Optional resources referenced and present
- If scripts exist, dependencies listed; no secrets hardcoded

## References
- Based on Claude Skills guidance and best practices: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills


