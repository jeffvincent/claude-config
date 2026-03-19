# Voice Authenticity Reviewer

## Purpose
Review any written content for alignment with your authentic speaking and writing voice using analyzed patterns from 7 meeting transcripts and strategic memos. Identify voice mismatches and suggest authentic rewrites.

## When to Use This Skill
- Before sharing strategic memos with leadership
- Before sending important emails
- When drafting presentation scripts
- When reviewing documentation for external sharing
- Anytime you want voice authenticity verification
- As part of Writing /produce-memo workflow

## Required Context

**CRITICAL:** Before starting any review, ALWAYS read the current voice patterns:

```
Read: /Users/jvincent/Projects/Personal/Voice-Patterns/analysis/voice-patterns-v1.md
```

This 665-line analysis contains:
- Vocabulary preferences (words to use vs avoid)
- Sentence structure patterns (length, complexity, rhythm)
- Tone guidelines (directness, formality level, emotional expression)
- Authentic voice markers (specific constructions)
- Red flags and anti-patterns

## Workflow

### Step 1: Load Voice Patterns

Read the complete voice analysis file. Take time to understand the patterns deeply - this is the foundation for accurate review.

### Step 2: Get Content to Review

Content can be provided in three ways:
1. **Pasted directly** in the conversation
2. **File path** provided (use Read tool to load)
3. **Current context** (if reviewing something already in conversation)

If no content provided, ask: "What content would you like me to review for voice authenticity?"

### Step 3: Analyze Content Against Patterns

Systematically check the content for:

**Vocabulary Alignment:**
- Using preferred words vs avoiding buzzwords
- Authentic phrases vs corporate speak
- Specific terminology choices
- Word frequency and variety

**Sentence Structure:**
- Length (target: 12-18 words based on patterns)
- Complexity (simple vs compound vs complex)
- Rhythm and pacing
- Paragraph structure

**Tone Consistency:**
- Directness (avoiding hedging language)
- Formality level (appropriate for context)
- Emotional expression (measured vs expressive)
- Confidence vs uncertainty

**Authentic Patterns:**
- Specific constructions that match voice
- Natural transitions
- Emphasis patterns
- Logical flow

**Red Flags:**
- Overly formal language
- Passive voice overuse
- Buzzwords and jargon
- Hedging language ("I think", "maybe", "perhaps")
- Corporate speak

### Step 4: Provide Structured Feedback

**Output Format:**

```markdown
# Voice Authenticity Review

## Overall Assessment
**Rating:** [Highly Authentic / Mostly Authentic / Mixed / Needs Work]
**Confidence:** [High / Medium / Low]

## Executive Summary
[2-3 sentences: overall voice match, main issues identified, estimated effort to fix]

---

## Detailed Analysis

### Content Overview
- **Total paragraphs:** X
- **Total sentences:** Y
- **Word count:** Z
- **Average sentence length:** X words (Target: 12-18)

### Issues Found

#### 🔴 High Priority (Voice Breakers)
These issues significantly break authentic voice and should be addressed immediately.

**1. [Location - Para X, Sentence Y]**
- **Current:** "[exact quote from content]"
- **Issue:** [Specific explanation of why this breaks voice - reference voice patterns]
- **Suggestion:** "[authentic rewrite preserving meaning]"
- **Impact:** [Why this matters - clarity, authenticity, executive alignment, etc.]

[Repeat for each high-priority issue]

#### 🟡 Medium Priority (Voice Drift)
These issues represent drift from authentic voice but aren't critical.

**1. [Location]**
- **Current:** "[quote]"
- **Issue:** [Explanation]
- **Suggestion:** "[rewrite]"
- **Impact:** [Why this matters]

[Repeat for each medium-priority issue]

#### 🟢 Low Priority (Polish)
Minor improvements that would enhance authenticity.

**1. [Location]**
- **Current:** "[quote]"
- **Issue:** [Explanation]
- **Suggestion:** "[rewrite]"
- **Impact:** [Enhancement benefit]

[Repeat for each low-priority issue]

### ✅ Authentic Moments (What Works)

These sections demonstrate strong voice alignment:

1. **"[Quote from content]"** (Para X)
   - **Why this works:** [Specific pattern match from voice-patterns]
   - **Strength:** [What makes this authentic]

2. **"[Another quote]"** (Para Y)
   - **Why this works:** [Pattern match]
   - **Strength:** [Authenticity element]

[Include 3-5 authentic moments to reinforce what's working]

### 📊 Voice Metrics

| Metric | Current | Target | Assessment |
|--------|---------|--------|------------|
| Avg sentence length | X words | 12-18 words | [Pass/Needs work] |
| Vocabulary match | Y% | 80%+ | [Pass/Needs work] |
| Tone consistency | [Rating] | Consistent | [Assessment] |
| Pattern alignment | Z matches | Strong | [Assessment] |

**Sentence Length Distribution:**
- Short (1-10 words): X%
- Medium (11-20 words): Y%
- Long (21+ words): Z%

---

## Quick Wins (Top 3 Changes for Maximum Impact)

Focus on these changes first for biggest voice improvement:

1. **[Specific high-impact change]**
   - Location: [Para X]
   - Change: [Brief description]
   - Impact: [Why this matters most]

2. **[Second high-impact change]**
   - Location: [Para Y]
   - Change: [Description]
   - Impact: [Benefit]

3. **[Third high-impact change]**
   - Location: [Para Z]
   - Change: [Description]
   - Impact: [Benefit]

---

## Before/After Examples

[If major rewrites suggested, show 2-3 complete examples]

### Example 1: [Issue type]

**Original:**
> [Full quote from content]

**Authentic Version:**
> [Complete rewrite in authentic voice]

**Why this is better:**
- [Specific improvement 1]
- [Specific improvement 2]
- [Pattern match from voice-patterns]

### Example 2: [Issue type]

[Same format]

---

## Context-Specific Guidance

### [If Strategic Memo]
- **Executive alignment:** [Check against Duncan/Yamini language patterns if applicable]
- **Formality level:** [Appropriate for leadership audience?]
- **Clarity:** [Direct and unambiguous?]

### [If Email]
- **Tone:** [Matches relationship context?]
- **Brevity:** [Appropriate length for email?]
- **Call to action:** [Clear and authentic?]

### [If Presentation]
- **Spoken rhythm:** [Flows naturally when read aloud?]
- **Energy:** [Engaging and authentic?]
- **Transitions:** [Natural signposting?]

---

## Recommended Next Steps

1. **Address High Priority issues** (Est. time: [X minutes])
   - Focus on voice breakers first
   - Use suggested rewrites or adapt them

2. **Consider Medium Priority improvements** (Est. time: [Y minutes])
   - Voice drift items that would strengthen authenticity
   - Not critical but beneficial

3. **Review authentic moments**
   - Note what's working well
   - Preserve these sections in any revisions

4. **Re-review if major changes made**
   - If addressing 5+ High Priority issues
   - Run voice check again after revisions

5. **Optional: Log insights**
   - If new patterns observed, document in:
     `/Users/jvincent/Projects/Personal/Voice-Patterns/evolution/refinements.md`

---

## Voice Evolution Note

After completing this review, consider:
- Are new patterns emerging that aren't in voice-patterns-v1.md?
- Are some guidelines proving less useful?
- Has authentic voice evolved since patterns were created?

Document insights in evolution/refinements.md for quarterly pattern review.

```

## Special Considerations

### For Different Content Types

**Strategic Memos:**
- Higher stakes - be more thorough
- Check executive language alignment
- Verify appropriate formality
- Ensure clarity and directness

**Emails:**
- Lighter touch (email is naturally more casual)
- Focus on clarity and brevity
- Check tone matches relationship
- Quick wins only - don't over-polish

**Presentations:**
- Read aloud mentally - check spoken rhythm
- Energy and engagement matter
- Verify natural transitions
- Check pacing and emphasis

**Documentation:**
- Balance authenticity with technical clarity
- Some formality appropriate
- Focus on clarity over personality

### Confidence Levels

**High Confidence:**
- Content closely matches analyzed patterns
- Clear voice breakers identified
- Specific rewrites possible

**Medium Confidence:**
- Some ambiguity in voice match
- Context-dependent issues
- Multiple valid interpretations

**Low Confidence:**
- Unfamiliar content type
- Minimal pattern matches found
- Need more context to assess

If confidence is Medium or Low, note this clearly and explain why.

## Quality Checklist

Before finalizing review, verify:

- [ ] Read voice-patterns-v1.md completely
- [ ] Analyzed all content (not just excerpts)
- [ ] Identified issues at all priority levels
- [ ] Provided specific, actionable suggestions
- [ ] Included authentic moments (what works)
- [ ] Calculated voice metrics
- [ ] Provided quick wins
- [ ] Included before/after examples for major issues
- [ ] Gave clear next steps
- [ ] Estimated time to address issues
- [ ] Noted any new patterns for evolution tracking

## Output Tone

Be:
- **Direct:** Clear, specific feedback
- **Constructive:** Focus on improvement, not criticism
- **Actionable:** Provide concrete rewrites
- **Encouraging:** Highlight what works
- **Systematic:** Organize by priority

Avoid:
- Vague feedback ("this doesn't sound right")
- Perfectionism (not every sentence needs fixing)
- Generic advice (be specific to voice patterns)
- Overwhelming user with too many changes

## Evolution Integration

After each review, prompt:

"Would you like me to log any new voice insights from this review to the refinements tracker? This helps evolve the voice patterns over time."

If yes, offer to append relevant observations to:
`/Users/jvincent/Projects/Personal/Voice-Patterns/evolution/refinements.md`

Format:
```markdown
## [Date] - [Document Type]

**New Pattern Observed:**
[Description]

**Example:**
[Quote from reviewed content]

**Guidance to Add:**
[How this should inform future reviews]
```
