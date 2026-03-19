# Voice Authenticity Reviewer

## Purpose
Review any written content for alignment with authentic speaking and writing voice using analyzed patterns from 7 meeting transcripts and strategic memos.

## When to Use This Skill
- Before sharing strategic memos with leadership
- Before sending important emails
- When drafting presentation scripts
- When reviewing documentation for external sharing
- As part of Writing /produce-memo workflow (Step 6)
- Anytime voice authenticity verification is needed

---

## Workflow

### Step 1: Load Voice Patterns

**CRITICAL:** Read the complete voice patterns file before doing anything else:

```
Read: /Users/jvincent/Projects/Personal/Voice-Patterns/analysis/voice-patterns-v1.md
```

This 665-line analysis is the foundation for the entire review. Do not skim it.

### Step 2: Get Content to Review

Content can be provided three ways:
1. **Pasted directly** in the conversation
2. **File path** provided (use Read tool)
3. **Current context** (already in conversation)

If no content provided, ask: "What content would you like me to review for voice authenticity?"

### Step 3: Determine Content Type

Identify the content type to calibrate the review:
- Strategic memo → thorough review, all dimensions
- Email → lighter touch, clarity focus
- Presentation → rhythm and energy focus
- Documentation → balance authenticity with clarity

**Read:** `instructions/context-variations.md` for detailed guidance per type.

### Step 4: Analyze Content

Systematically check all five voice dimensions from `instructions/voice-dimensions.md`:
1. Vocabulary alignment
2. Sentence structure
3. Tone consistency
4. Authentic patterns
5. Red flags

For each issue found, record: **location + current text + pattern violated + concrete rewrite.**

Follow the tone guidelines in `instructions/reviewer-tone.md` — be direct, constructive, and actionable.

### Step 5: Run Advisory Board Review

Before finalizing, run the draft through the three reviewer personas in `eval/advisory-board.md`:
1. **The Authenticity Purist** — catches AI/corporate voice
2. **The Executive Reader** — evaluates clarity and impact
3. **The Voice Coach** — checks quantitative metrics

Synthesize their feedback. Adjust priorities if the personas flag something the initial pass missed.

### Step 6: Assemble Final Review

Use the output template in `templates/review-output.md` to structure the final review. Include:
- Overall assessment with confidence level (see `instructions/confidence-levels.md`)
- Issues by priority (High/Medium/Low)
- Authentic moments (3-5 things that work)
- Voice metrics table
- Quick wins (top 3 changes)
- Before/after examples
- Next steps with time estimates

### Step 7: Validate Against Checklist

Before delivering, run through every item in `eval/checklist.md`. All items must pass.

### Step 8: Offer Evolution Tracking

After delivering the review, follow the prompt in `instructions/evolution-tracking.md` to offer logging new voice insights to the refinements tracker.

---

## Reference Examples

- **Good review:** `examples/good/strategic-memo-review.md` — annotated example of a thorough, specific review
- **Bad review (anti-pattern):** `examples/bad/vague-review.md` — what to avoid

---

## File Map

```
voice-authenticity/
├── Skill.md                              ← You are here (orchestrator)
├── instructions/
│   ├── voice-dimensions.md               ← 5 analysis dimensions
│   ├── context-variations.md             ← Memo vs email vs presentation guidance
│   ├── confidence-levels.md              ← High/Medium/Low criteria
│   ├── reviewer-tone.md                  ← How to deliver feedback
│   └── evolution-tracking.md             ← Post-review pattern logging
├── templates/
│   └── review-output.md                  ← Output format template
├── examples/
│   ├── good/
│   │   └── strategic-memo-review.md      ← Annotated good review
│   └── bad/
│       └── vague-review.md               ← Anti-pattern to avoid
└── eval/
    ├── checklist.md                      ← Pass/fail validation
    └── advisory-board.md                 ← 3 reviewer personas
```
