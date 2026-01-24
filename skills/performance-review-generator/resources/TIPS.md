# Performance Review Generator - Tips & Best Practices

## Core Principles

### 1. Self-Review is Cross-Check, Not Source

**The Problem:**
Many managers copy-paste from employee self-reviews, losing their own perspective.

**The Solution:**
- Read the self-review LAST
- Start with your 1:1 notes and Glean data
- Write what YOU observed
- Use self-review to verify you didn't miss major achievements

**Example:**

❌ **Wrong** (copied from self-review):
> "I delivered the data quality platform, which was a complex project requiring cross-functional coordination."

✅ **Right** (manager's perspective):
> "Grace led the data quality platform, navigating complex technical tradeoffs I observed in our 1:1s. When engineering capacity constraints arose, she proactively proposed alternatives and maintained stakeholder trust."

### 2. Write from Manager's Observations

**Your 1:1 notes are gold.** They capture:
- What you observed directly
- Patterns over time
- Coaching conversations
- Real-time reactions to challenges

**How to mine your 1:1 notes:**
1. Read 6 months of Recent Notes in the person file
2. Look for patterns and themes
3. Find specific examples of GPS behaviors
4. Note coaching conversations about growth areas

**Example:**

❌ **Wrong** (vague):
> "Grace is good at stakeholder management."

✅ **Right** (specific, from 1:1 notes):
> "Grace excels at stakeholder management. In our October 1:1, we discussed how she navigated the data catalog prioritization with Data Science—she balanced their research needs with platform constraints, and both teams felt heard."

### 3. Use Specific Examples from Person Files

**Generic reviews are forgettable. Specific reviews are meaningful.**

**Structure for specific examples:**
- **Context**: What was the situation?
- **Behavior**: What did they do?
- **Impact**: What was the outcome?
- **GPS mapping**: Which Success Behavior does this demonstrate?

**Example:**

❌ **Wrong**:
> "Ben showed good judgment this year."

✅ **Right**:
> "Ben demonstrated strong judgment when the reporting redesign faced engineering pushback in Q3. Rather than forcing the original plan, he ran a design sprint with eng partners, incorporated their constraints, and shipped a simpler v1 that still delivered 80% of the value. This shows GPS Success Behaviors in Collaborative Teamwork and Navigating Change."

### 4. Map to GPS Framework

**Every achievement should map to GPS Success Behaviors.**

**GPS Quick Reference:**
- **Foundational**: Skill, Complexity, Supervision, Domain Expertise, Execution, Discretionary Impact
- **Impact**: Accountability, Drives for Results
- **Agility**: Collaborative Teamwork, Navigating Change
- **People Leadership**: Build & Develop Teams, Manages Performance, Engages Team

**Where to find GPS details:**
`/Users/jvincent/Projects/Work/HubSpot/Grove/global-resources/performance-expectations-by-level.md`

**How to map:**
1. Identify the achievement
2. Ask: "Which GPS dimension does this demonstrate?"
3. Reference the HUB-level expectation
4. Explicitly call it out in the review

**Example:**
> "Grace's work on the data quality platform demonstrates **Complexity** at the SPM I level—she navigated technical tradeoffs across multiple systems and stakeholders, a clear HUB 6 expectation."

### 5. Stay Under Character Limit (4,500)

**HubSpot's system has a hard 4,500 character limit.**

**Strategies to stay within limit:**

1. **Be concise with context**: Get to the impact quickly
2. **Use bullets**: More scannable than paragraphs
3. **Remove filler words**: "really", "very", "quite", etc.
4. **Combine related achievements**: Group similar projects
5. **Cut redundant examples**: One strong example > three weak ones

**Check character count:**
```bash
wc -m reviews/2026-H1/firstname-lastname-2026-H1.md
```

**If over limit:**
- Remove least impactful examples
- Tighten wording without losing meaning
- Preserve GPS mappings and specific metrics

### 6. Growth Areas Should Be Developmental

**Growth areas are NOT performance criticism.**

**Good growth areas:**
- Are discussed regularly in 1:1s (never a surprise)
- Are framed as development opportunities
- Have clear next steps and manager support
- Connect to career goals

**Example:**

❌ **Wrong** (punitive):
> "Ben struggles with strategic thinking and needs to improve his ability to see the big picture."

✅ **Right** (developmental):
> "Ben's key growth opportunity is **strategic influence at the executive level**. He's strong at tactical execution, and the next step is translating that into strategic narratives for senior audiences. In our 1:1s, we've discussed opportunities to write strategy docs and present to Director+ forums. Ben drafted his first exec memo in December, and continuing to develop this skill will position him well for Senior PM II."

### 7. Q1 Goals Need Measurable Success Criteria

**Vague goals are useless. Measurable goals drive accountability.**

**Goal structure:**
- **What**: Clear description of the goal
- **How**: Success metrics or criteria
- **Why**: Connection to team/org priorities
- **When**: Timeline (usually Q1)

**Examples:**

❌ **Wrong**:
> "Improve data platform performance"

✅ **Right**:
> "Reduce p95 query latency to under 200ms for 90% of data platform queries. Success measured by weekly performance dashboards. This supports the Data Platform OKR to improve developer experience."

❌ **Wrong**:
> "Build better relationships with stakeholders"

✅ **Right**:
> "Establish monthly check-ins with three key Director+ stakeholders: VP Eng, VP Product, Director of Data Science. Success looks like proactive strategic discussions, not just reactive issue resolution."

### 8. Maintain Consistent Voice

**The review should sound like you talking to calibration peers.**

**Voice patterns:**
- "In our 1:1s, I observed..."
- "Grace demonstrated..."
- "What stood out was..."
- "I've seen her..."
- "We discussed..."

**Avoid:**
- "I accomplished..." (employee voice)
- "Grace is amazing..." (over-the-top praise)
- "Grace sometimes..." (vague hedging)

### 9. Performance Ratings Should Align with Content

**The rating should not surprise anyone who reads the review.**

**Rating guidelines:**

| Rating | Review Content Should Show |
|--------|----------------------------|
| **5** | "Operating at next level", "transformative impact", "exceptional" |
| **4** | "Regularly exceeds", "strong performer", "clear impact" |
| **3** | "Consistently meets", "solid performer", "on track" |
| **2** | "Gaps in execution", "needs support", "growth plan" |
| **1** | "Not meeting expectations", "performance concerns" |

**Rating should reflect 1:1 conversations:**
If you've been telling someone they're doing great all year, a "3" rating will feel like a betrayal.

### 10. No Surprises

**Everything in the review should have been discussed in 1:1s.**

**Before finalizing:**
- Ask yourself: "Would this surprise the employee?"
- Growth areas should be familiar from coaching conversations
- Achievements should reflect your regular feedback
- Goals should align with recent priority discussions

**If it would be a surprise, one of two things is true:**
1. You haven't been giving enough feedback in 1:1s (fix this)
2. It shouldn't be in the review (remove it)

## Common Pitfalls to Avoid

### ❌ Copying Self-Review Verbatim
Self-reviews are the employee's perspective. Your review should be YOUR perspective.

### ❌ Generic Praise Without Examples
"Grace is a great PM" tells us nothing. "Grace navigated data catalog prioritization by..." tells a story.

### ❌ Growth Areas That Feel Like Surprises
If the employee reads the growth area and thinks "I had no idea Jeff thought this," you failed at continuous feedback.

### ❌ Goals Without Metrics
"Improve platform performance" is not a goal. "Reduce p95 latency to <200ms" is a goal.

### ❌ Missing GPS Mapping
Every achievement should map to GPS Success Behaviors at the HUB level. This is how we calibrate across the org.

### ❌ Exceeding Character Limit
4,500 characters is a hard limit. Check early and often.

### ❌ Wrong Voice
Writing "I delivered..." means you copied from self-review. Write "Grace delivered..." from YOUR observations.

## Time-Saving Tips

### 1. Mine Your 1:1 Notes Regularly
Don't wait until review time. Tag achievements as they happen:
```markdown
### 2025-10-15 - Grace 1:1

**Key Points:**
- Shipped data catalog v1 ✅ (GPS: Execution, Drives for Results)
- Navigated eng pushback well 👍 (GPS: Collaborative Teamwork)
```

### 2. Keep a Running "Wins" List
Add a section to person files:
```markdown
## Review Cycle Preparation

### H1 2026 Achievements
- [ ] Data quality platform (40% incident reduction)
- [ ] ML platform features (3 shipped)
- [ ] Data Platform Strategy doc
```

### 3. Reuse Strong Examples
If you wrote a strong example for one review, the structure works for others:
- [Achievement] + [Context] + [Impact] + [GPS]

### 4. Batch Reviews by Role
Write all SPM reviews together to ensure consistency in GPS expectations and rating calibration.

## Quality Checklist (Quick Version)

Before saving the review:

- [ ] Character count < 4,500
- [ ] Manager's voice (not employee's)
- [ ] 3+ specific examples from 1:1 notes
- [ ] GPS Success Behaviors mapped
- [ ] Growth area is developmental
- [ ] Q1 goals have metrics
- [ ] Rating aligns with content
- [ ] No surprises (all discussed in 1:1s)

## Resources

- **GPS Framework**: `/global-resources/GPS-Framework.md`
- **HUB Level Expectations**: `/global-resources/performance-expectations-by-level.md`
- **Evidence Guide**: `/global-resources/evidence-quantification-guide.md`
- **Validation Checklist**: `resources/VALIDATION_CHECKLIST.md`
- **Example Review**: `resources/EXAMPLE_REVIEW.md`

## Final Advice

**The best reviews are:**
1. Grounded in your direct observations from 1:1s
2. Specific with examples and metrics
3. Aligned with GPS framework at the HUB level
4. Developmental and forward-looking
5. Free of surprises (continuous feedback all year)

**Remember**: This is not a creative writing exercise. It's a reflection of the coaching relationship you've built throughout the year. If you've had good 1:1s, the review should practically write itself.
