---
name: autoresearcher-generator
description: Generate a self-improving "autoresearch" loop for any Claude skill. Given a skill to improve and 3-5 quality constraints, scaffolds a standalone project (modeled on karpathy/autoresearch) that iterates on the skill's prompt by generating N samples per cycle, evaluating them against the constraints, and editing the skill to fix recurring failures — up to 30 cycles or until results are consistently perfect. Use when the user says something like "make an autoresearcher for my X skill" or "build a self-improving loop for skill Y".
---

# autoresearcher-generator

Scaffolds a karpathy/autoresearch-style loop that iteratively improves a Claude skill's prompt by generating outputs, evaluating them against user-defined constraints, and having an "improver" subagent propose targeted edits to the skill prompt.

## When to use

The user asks for a self-improving loop / eval harness / autoresearcher for one of their skills. Typical triggers:
- "Build an autoresearcher for my X skill"
- "Make a self-improving loop for skill Y"
- "I want X to get better automatically"

## What you need from the user

Ask for **exactly two things** if not provided:

1. **The skill to improve** — path to its `Skill.md` (or `SKILL.md`).
2. **3–5 constraints** the generated outputs must satisfy. These are the eval rubric. Each constraint should be a single sentence describing a property the output must have.

If the user gives fewer than 3 constraints, ask for more. If more than 5, ask them to pick the top 5. Do NOT silently proceed with a bad input set — the constraint list is the soul of the loop.

After you have both, **propose 1–2 additional constraints you think are worth adding** (based on reading the skill). The user approves or rejects before you scaffold.

## What you will build

A standalone project directory (default location: `~/autoresearch-<skill-slug>/`, but ask the user to confirm). The directory contains:

```
autoresearch-<slug>/
├── program.md          # loop driver instructions — rendered from template
├── Skill.md            # COPY of the target skill; mutable; edited by the loop
├── eval.mjs            # programmatic checks synthesized from user constraints
├── judge-prompt.md     # qualitative checks synthesized from user constraints
├── inputs/pool.tsv     # rotating set of inputs for the skill (user confirms)
├── results.tsv         # per-cycle log (gitignored)
├── scratch/            # generated outputs per cycle (gitignored)
├── .gitignore
└── README.md
```

It is **its own git repo** on a dedicated branch. The live skill at the original path is NEVER modified by the loop — only the copy in the project directory is.

## Steps you follow

### Step 1: Read the skill
Read the user's target `Skill.md` in full. You need to understand what the skill produces and what "good output" looks like so you can (a) suggest extra constraints and (b) classify each constraint as programmatic vs qualitative.

### Step 2: Classify constraints
For each user constraint, decide:
- **Programmatic** — can be checked by a deterministic script. Examples: "output is valid JSON", "contains section X", "line count ≤ N", "all shapes have bound text", "file is under 2MB".
- **Qualitative** — needs an LLM judge. Examples: "covers the high-level concept", "tone matches voice", "flow is clear", "colors used meaningfully".

A constraint may require BOTH (e.g. "not too much text" → programmatic char count + judge for subjective overload). In that case, implement both and require both to pass.

### Step 3: Ask for inputs
The loop needs inputs to feed the skill. For the Excalidraw case it was "notes to diagram." For other skills, it could be prompts, source files, data files, etc. Ask the user to point at a directory or hand-pick 3–5 inputs. Do NOT proceed without real inputs — synthetic ones lead to a skill that overfits.

### Step 4: Confirm target directory and N (samples per cycle)
- Default directory: `~/autoresearch-<slug>/` where slug is derived from the skill name.
- Default N: **5 samples per cycle**. Ask the user if they want to change it.
- Default cycle cap: **30**.
- Default time cap per cycle: **5 minutes**.

### Step 5: Scaffold
Create the directory and write files using the templates in `templates/` as starting points. You **synthesize** `eval.mjs` and `judge-prompt.md` from the user's constraints — do not copy them verbatim from the Excalidraw example.

After writing files:
1. `git init` in the new directory.
2. `git checkout -b autoresearch/<slug>-initial`.
3. Stage everything and commit: `baseline: scaffold for <skill-name>`.

### Step 6: Hand off
Print a short summary:
- Path to the new project.
- The 9-ish checks that will be enforced (programmatic + judge).
- How to launch: open a fresh Claude Code session in that directory and say "Read program.md and run the autoresearch loop."
- Reminder that the live skill is untouched; user promotes manually via `diff` + `cp` after the loop.

## Non-negotiables you must enforce

- **Never edit the live skill.** Only the copy inside the scaffolded directory.
- **Never include `eval.mjs`, `judge-prompt.md`, or `inputs/pool.tsv` in the set of files the loop is allowed to edit.** These are the fixed yardstick. Say so explicitly in `program.md`.
- **The loop must use subagents for generation and evaluation.** Do not have the main loop agent generate outputs in its own context — that burns context and the loop stops after 2–3 cycles. Parallel Task subagents are load-bearing.
- **30-cycle hard cap.** Even if results aren't perfect.
- **Revert on regression.** If a cycle's edit makes the pass count worse on the same input, `git reset --hard HEAD~1`.

## Templates

Templates live in `templates/` next to this SKILL.md:
- `program.md.tmpl` — loop driver, with `{{PLACEHOLDERS}}` for slug, N, constraints summary, input source description.
- `eval.mjs.tmpl` — skeleton with helper functions; you fill in the actual checks based on the user's constraints.
- `judge-prompt.md.tmpl` — skeleton rubric; you fill in the qualitative criteria.
- `README.md.tmpl` — user-facing readme.

Read the templates, substitute the placeholders, and synthesize the per-skill eval logic. Do not just copy templates blindly — the checks are the whole point.

## Reference implementation

A working example of a scaffolded autoresearch project lives at `~/Projects/Knowledge System/autoresearch-excalidraw/`. When in doubt about structure or tone, look there. That project targets the Excalidraw Creator skill with 9 checks (5 programmatic, 4 qualitative). It is the canonical pattern.
