# Voice Authenticity Skill

Reviews written content for alignment with authentic voice patterns analyzed from meeting transcripts and strategic documents.

## Purpose

Systematically check any written content against comprehensive voice analysis to ensure authentic, consistent communication across all contexts.

## Usage

### In Any Claude Code Conversation

```
Use voice-authenticity skill to review this content:
[paste content or provide file path]
```

### With File Path

```
Use voice-authenticity skill to review:
~/Projects/Work/Writing/Active/My-Memo/memo-draft.md
```

### In Context

```
Use voice-authenticity skill to review the memo draft above
```

## What It Does

1. **Reads voice patterns** from ~/Projects/Personal/Voice-Patterns/analysis/voice-patterns-v1.md
2. **Analyzes provided content** systematically
3. **Identifies mismatches** at three priority levels (High/Medium/Low)
4. **Suggests authentic rewrites** with specific improvements
5. **Highlights what works** (authentic moments to preserve)
6. **Provides metrics** (sentence length, vocabulary match, tone)
7. **Recommends quick wins** (top 3 changes for biggest impact)
8. **Estimates effort** (time to address issues)

## Output Structure

- **Overall Assessment:** Rating + confidence level
- **Executive Summary:** Key findings in 2-3 sentences
- **Issues by Priority:** Organized High → Medium → Low
- **Authentic Moments:** What's working well
- **Voice Metrics:** Quantitative analysis
- **Quick Wins:** Top 3 changes for maximum impact
- **Before/After Examples:** Demonstration rewrites
- **Next Steps:** Clear action plan

## Voice Patterns Source

Based on comprehensive analysis of:
- **7 meeting transcripts** from 2025
- **665-line voice analysis** covering:
  - Vocabulary preferences
  - Sentence structure patterns
  - Tone and formality guidelines
  - Authentic voice markers
  - Red flags and anti-patterns

## Integration Points

### Global Command
- `/check-voice` - Invokes this skill globally

### Writing Workflow
- Integrated into `/produce-memo` command (Step 6: Final Polish)
- Available in `/critique` command (voice dimension)
- Recommended before sharing important docs

### Evolution Tracking
- After each review, can log insights to refinements tracker
- Helps evolve voice patterns over time
- Quarterly reviews update patterns based on learnings

## Context-Specific Handling

The skill adapts review approach based on content type:

- **Strategic Memos:** Thorough, executive alignment check
- **Emails:** Lighter touch, focus on clarity
- **Presentations:** Spoken rhythm, energy, engagement
- **Documentation:** Balance authenticity with technical clarity

## Available Globally

This skill works in any project or directory where Claude Code is running. Voice patterns are accessed from fixed location: `~/Projects/Personal/Voice-Patterns/`

## Version

**Current:** v1.0 (2026-03-19)
- References voice-patterns-v1.md
- Based on 7 transcripts from 2025
- Initial implementation

Future versions will reference updated pattern files as voice evolves.

## Related Files

- **Voice Patterns:** `~/Projects/Personal/Voice-Patterns/`
- **Global Command:** `~/.claude/commands/check-voice.md`
- **Evolution Tracking:** `~/Projects/Personal/Voice-Patterns/evolution/refinements.md`
- **Changelog:** `~/Projects/Personal/Voice-Patterns/evolution/changelog.md`

## Example Use Cases

1. **Before memo review meeting:** Check authentic voice alignment
2. **Email to exec team:** Verify tone appropriate for audience
3. **Presentation script:** Check spoken rhythm and energy
4. **Documentation:** Balance clarity with authentic voice
5. **Slack announcement:** Quick check for authentic tone

## Success Metrics

After using this skill:
- **Time saved:** Systematic vs ad-hoc voice checking
- **Consistency:** Authentic voice across all communication
- **Confidence:** Know content matches authentic voice before sharing
- **Evolution:** Voice patterns improve based on learnings

---

**Created:** 2026-03-19
**Last Updated:** 2026-03-19
**Version:** 1.0
