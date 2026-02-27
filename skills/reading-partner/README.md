# Reading Partner Skill

A skill that transforms Claude into an intellectual reading partner - someone you can bounce ideas off of and who will give you open, direct feedback about content you're exploring.

## What It Does

The reading partner skill helps you think more deeply about articles, podcasts, books, and other content by:

1. **Loading the content** - Finds and reads your source documents and related synthesis notes
2. **Performing ultrathink** - Analyzes tensions, missing connections, provocative questions, and practical implications
3. **Engaging in discussion** - Flexibly adapts between Socratic questioning, devil's advocate, and creative connector modes
4. **Documenting everything** - Appends the entire discussion to your source document for future reference

## How to Use

### Method 1: Use the `/discuss` slash command (recommended)

```
/discuss Machines of Loving Grace
```

or just:

```
/discuss
```

Then specify what you want to discuss when prompted.

### Method 2: Invoke the skill directly

```
skill: reading-partner
```

Then tell Claude what content you want to discuss.

## What Happens

### Phase 0: Content Acquisition (if needed)

If the content isn't already in your Content Notes repository, Claude will:
- Ask your permission to import it from Readwise
- Import the content using `readwise-skill`
- Analyze it using `readwise-content-analyzer`

### Phase 1: Content Loading

Claude loads:
- The source document (article text + your highlights, or transcript + analysis)
- Related synthesis documents that connect to this content
- Other potentially relevant content from your knowledge base

### Phase 2: Ultrathink Analysis

Claude performs deep analysis and presents findings:

- **Tensions & Contradictions** - Where arguments conflict with your existing frameworks
- **Missing Connections** - What synthesis docs should connect but don't yet
- **Provocative Questions** - Challenging questions to push thinking deeper
- **Practical Implications** - How theoretical frameworks translate to action

### Phase 3: Discussion

Claude engages in flexible, adaptive conversation:

- **Socratic questioning** - Helps you discover insights through questions
- **Devil's advocate** - Pushes back to find weaknesses in arguments
- **Creative connector** - Makes unexpected connections between ideas
- **Adapts to what you need** - Shifts style based on the conversation flow

### Phase 4: Documentation

At the end of the discussion, Claude:
- Appends the full ultrathink analysis and conversation to the source document
- Adds a "Discussion Session - [Date]" section
- Summarizes key insights discovered

## Example Session

```
You: /discuss Machines of Loving Grace

Claude: I found the source document for "Machines of Loving Grace" by Dario Amodei.
Let me load it along with the related synthesis documents...

[Loads content and related syntheses]

Let me start with my ultrathink analysis:

### Tensions & Contradictions
1. Amodei's "marginal returns to intelligence" framework suggests...
[etc.]

### Discussion Principles

Your reading partner will:
- Give you direct, honest feedback (even when challenging)
- Make unexpected connections across your knowledge base
- Ask provocative questions that push your thinking
- Adapt conversation style to what you need
- Be genuinely curious and collaborative

## Discussion Tips

**For best results:**

- **Let conversations breathe** - Deep thinking takes time
- **Challenge back** - Push back on Claude's ideas too
- **Request mode shifts** - Ask for Socratic questions, devil's advocate, or creative connections
- **Signal when done** - Say "let's wrap up" when insights stop flowing

**Example prompts during discussion:**

- "Play devil's advocate on that idea"
- "What connections am I missing?"
- "Ask me some hard questions about this"
- "How does this relate to [other framework]?"
- "Challenge my assumption about..."

## Where Discussions Are Saved

All discussion sessions are appended to the source document in:

```
/Users/jvincent/Projects/Personal/Content Notes/sources/
```

Each discussion creates a new timestamped section with:
- Ultrathink analysis
- Full conversation transcript
- Key insights summary

## Content Sources Supported

- **Readwise articles** (imported or to-be-imported)
- **Podcast transcripts** (from video-transcript-analyzer)
- **Interview analyses** (from video-transcript-analyzer)
- **Books** (from Readwise)
- Any content in your Content Notes sources directory

## Examples

### Discussing existing content

```
/discuss Machines of Loving Grace
```

### Discussing content not yet imported

```
/discuss https://readwise.io/reader/document_url/xyz
```

Claude will ask permission to import it, then proceed with the discussion.

### Open-ended invocation

```
/discuss
```

Then specify: "Let's talk about the Gokul Rajaram interview"

## Behind the Scenes

The reading partner skill:
- Searches for content in `sources/` using Glob
- Loads related synthesis docs mentioned in the source
- Uses Grep to find other potential connections
- Can invoke `readwise-skill` and `readwise-content-analyzer` if needed
- Appends discussion using the Edit tool
- Does NOT commit to git (you control commits)

## Integration with Other Skills

The reading partner complements:
- **readwise-skill** - Imports content for discussion
- **readwise-content-analyzer** - Creates initial analysis
- **interview-synthesis-updater** - Updates syntheses after video analysis

## Requirements

- Content Notes repository at `/Users/jvincent/Projects/Personal/Content Notes/`
- Readwise integration configured (if importing new content)

## Troubleshooting

**"I can't find that content"**
- Check the exact title in your `sources/` directory
- Try providing the file path directly
- Offer to import from Readwise if not found

**"Discussion isn't challenging enough"**
- Request devil's advocate mode explicitly
- Say "push back harder on that"
- Ask "what am I missing?"

**"Too much Socratic questioning"**
- Say "just tell me directly what you think"
- Request creative connector mode
- Ask for synthesis instead of questions

## Version

Created: 2026-02-27
