---
name: marp-presentation
description: Create and iterate on MARP Markdown slide decks with HubSpot styling (two themes available — Trellis product palette and HubSpot brand-identity palette), AI-generated images via LiteLLM/Gemini, and slidegauge linting. Use when the user wants to create a presentation, build slides, make a slide deck, or work on a talk.
license: MIT
compatibility: Requires npx (for marp-cli) and uv (for image generation script and slidegauge). Designed for HubSpot engineers.
metadata:
  author: zeev-klapow
  version: "1.0"
allowed-tools: Bash(*) Read Write Edit Glob Grep
---

# MARP Presentation Skill

Build polished MARP slide decks with HubSpot styling and AI-generated illustrations.

## Overview

This skill helps you create Markdown-based presentations using [MARP](https://marp.app). It includes:
- **Two HubSpot-branded CSS themes** — pick the one that matches your audience:
  - `assets/trellis-theme.md` — HubSpot **product-UI** palette (dark navy + magenta + cyan, Trellis design tokens). Good for internal engineering / product-context decks.
  - `assets/hubspot-theme.md` — HubSpot **brand-identity** palette (cream + orange + dark teal + maroon, Lexend Deca + Caveat). Good for executive, external, or brand-aligned decks.
- An image generation script using HubSpot's LiteLLM proxy (Gemini/Nano Banana)
- Integration with slidegauge for slide quality linting

## Setup

### MARP CLI
MARP converts Markdown to slides. It runs via npx (no global install needed):

```bash
# Test it works
npx @marp-team/marp-cli --version
```

If npx is not available, install Node.js first. Alternatively, install marp-cli globally:

```bash
npm install -g @marp-team/marp-cli
```

### uv (for image generation)
The image generation script uses `uv` to manage Python dependencies inline. Install uv if not present:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### slidegauge (for linting)
Install globally via uv:

```bash
uv tool install "slidegauge @ git+ssh://git@github.com/HubSpotEngineering/slidegauge"
slidegauge --help
```

## Quick Start

1. Pick a theme and copy its frontmatter block to the top of your new `slides.md`:
   - `assets/trellis-theme.md` — product-UI palette (Trellis: dark navy + magenta + cyan). For internal engineering / product-context decks.
   - `assets/hubspot-theme.md` — brand-identity palette (cream + orange + dark teal + maroon, Lexend Deca). For executive / external / brand-aligned decks.
2. Start the MARP dev server: `npx @marp-team/marp-cli --server <directory>`
3. Write slides using the theme classes documented below (both themes support the same `lead` / `section-divider` / `agenda` slide classes; the HubSpot brand theme adds a `dark` class)
4. Generate images: `uv run scripts/generate-image.py -o images/my-image.png "a friendly robot"`
5. Lint slides: `slidegauge slides.md`

## Slide Authoring Guidelines

### Style principles
- **Minimal text on slides** — aim for ~5 words visible per slide
- **One point per slide** — never put multiple ideas on one slide
- **Details go in speaker notes** — use `<!-- ... -->` HTML comments for talk track
- **Code blocks should be short** — max 10 lines, scale down font if needed

### Theme classes

Use MARP's `<!-- _class: classname -->` directive. Both themes support the shared classes; the HubSpot brand theme adds `dark`.

**Shared (both themes):**
- **`lead`** — Title/intro slides, centered heading.
- **`section-divider`** — Section breaks. Magenta (Trellis) or maroon (HubSpot brand), white text.
- **`agenda`** — Agenda slide with styled ordered list.

**HubSpot brand theme only:**
- **`dark`** — High-contrast accent slide. Dark teal background, cream text, orange headings. Good for climax / turn moments.

See each theme file for exact colors and per-class CSS.

### Adding images to slides

```markdown
![bg left:35%](images/my-image.png)    <!-- Left side, 35% width -->
![bg right:30% contain](images/x.png)  <!-- Right side, contained -->
```

For section divider slides, use `bg left:35%` so the image fills the left and text stays right.

### Speaker notes

Always include speaker notes with your talk track:

```markdown
# Slide Title.

Visible text here.

<!--
This is the speaker note. Include your full talk track here — everything you plan to say.
Keep slide text minimal, put the detail in notes.
-->
```

### Per-slide style overrides

For slides that need custom sizing (e.g., large code samples):

```markdown
<style scoped>pre code { font-size: 0.43em; line-height: 1.1; }</style>

# My code slide.
```

## Image Generation

Use `scripts/generate-image.py` to create illustrations via HubSpot's LiteLLM proxy (Gemini).

```bash
# Text-only prompt
uv run scripts/generate-image.py -o images/output.png "a friendly cartoon robot"

# With reference image(s) for style matching
uv run scripts/generate-image.py -o images/output.png -i reference.png "redraw this character waving"

# Specify aspect ratio (default 1:1)
uv run scripts/generate-image.py -o images/output.png -a 9:16 "tall portrait illustration"
uv run scripts/generate-image.py -o images/output.png -a 16:9 "wide landscape scene"

# Use the pro model for higher quality
uv run scripts/generate-image.py -o images/output.png --pro "detailed illustration"
```

### Image tips
- Use `9:16` aspect ratio for images that will be `bg left:35%` on section dividers
- Use `16:9` for images that will be `bg right:40% contain` on content slides
- Use `1:1` for character portraits or icons
- Include reference images with `-i` to maintain consistent art style across a deck
- Uses `hs-py-auth` for authentication (auto-managed by uv inline deps)

## Diagrams

When creating diagrams for slides, follow this two-step process:

### Step 1: Draft in ASCII

First draft the diagram as ASCII art in a markdown code block. This lets you iterate on structure and content quickly without waiting for image generation. Use box-drawing characters (`┌─┐│└─┘├┤`), arrows (`→ ↓ ←`), and clear labels.

### Step 2: Convert to image via Nano Banana

Once the ASCII diagram is approved, convert it to a clean generated image using the image generation script:

```bash
uv run scripts/generate-image.py -a 16:9 -o images/<name>.png "Create a clean, professional infographic diagram on a white background with monospace font. [DESCRIBE THE DIAGRAM STRUCTURE]. Clean lines, minimal, dark text on white. Professional technical diagram style, not cartoon. Use subtle color coding: blue for user/input elements, gray for processing/thinking, orange for actions/tools, green for output/success, red for errors/failures. No decorations or illustrations."
```

### Diagram prompting rules

- Always specify "white background with monospace font"
- Always say "professional technical diagram style, not cartoon"
- Always say "clean lines, minimal, dark text on white"
- Use the color palette: blue=input, gray=processing, orange=actions, green=success, red=failure
- Describe layout explicitly: "three boxes at the top", "arrow pointing down to", "diamond decision box"
- For flowcharts, describe entry point and exit point explicitly
- For conversations, specify color coding per role: "blue for USER, gray for ASSISTANT, orange for TOOL_CALL, green for TOOL"
- Use `-a 16:9` for full-width diagrams, `-a 9:16` for sidebar images
- If including reference images with `-i`, add "matching the clean style, not the cartoon style"

### Embedding diagrams in slides

Replace the ASCII code block with:

```markdown
![center w:900](images/<name>.png)
```

Adjust `w:` value based on slide layout (900 for full-width, 500-550 for slides with sidebar images).

## Linting

Run slidegauge to check slide quality:

```bash
slidegauge slides.md
```

Parse results for quick summary:

```bash
slidegauge slides.md 2>/dev/null | \
  python3 -c "
import json, sys
data = json.load(sys.stdin)
s = data['summary']
print(f'Score: {s[\"avg_score\"]:.0f}/100 | {s[\"total_slides\"]} slides | {s[\"passing\"]}/{s[\"total_slides\"]} passing')
for sl in data['slides']:
    if sl['score'] < 70:
        print(f'  FAIL: \"{sl[\"title\"]}\" ({sl[\"score\"]})')
        for d in sl['diagnostics']:
            print(f'    {d[\"message\"]}')
"
```

### Key thresholds
- Score ≥ 70 = passing
- Adjusted content ≤ 350 chars (slide body text only, speaker notes excluded)
- Code blocks ≤ 10 lines
- Slide titles ≤ 35 characters
- Total lines per slide ≤ 15

## Dev Server

Start the MARP preview server for live reload:

```bash
npx @marp-team/marp-cli --server <directory-containing-slides>
```

This serves at `http://localhost:8080/` and auto-reloads on file changes.

**Important:** The server only serves static files — it does **not** auto-convert `.md` → `.html` on request. You must render HTML first (see Claude review loop below).

## Claude review loop (fast iteration)

When you're iterating on styling and want Claude to verify a single slide visually, use this loop instead of re-rendering all PNGs on every change:

### One-time setup

```bash
cd <deck-directory>
npx --yes --registry=https://registry.npmjs.org/ @marp-team/marp-cli@latest --server . &   # dev server
node ~/.claude/skills/browser-automation/resources/browser-start.js --headless              # headless Chrome
```

### Per-iteration (< 5s total)

1. **Edit** the deck `.md` or theme asset.
2. **Render HTML only** (fast — ~2s, skips image/PDF):

   ```bash
   npx --yes --registry=https://registry.npmjs.org/ @marp-team/marp-cli@latest deck-marp.md --html --allow-local-files -o deck-marp.html
   ```

3. **Navigate** (hard-load the page so new styles pick up):

   ```bash
   node ~/.claude/skills/browser-automation/resources/browser-navigate.js "http://localhost:8080/deck-marp.html"
   ```

4. **Advance to slide N** by dispatching `N-1` right-arrow keystrokes (hash-routing doesn't trigger bespoke's listeners after a page load):

   ```bash
   node ~/.claude/skills/browser-automation/resources/browser-eval.js \
     'for(let i=0;i<13;i++){document.body.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowRight",code:"ArrowRight",keyCode:39,which:39,bubbles:true}))} new Promise(r=>setTimeout(()=>r(document.querySelector("svg.bespoke-marp-active").querySelector("section").id), 400))'
   ```

   (13 ArrowRight presses lands on slide 14 — adjust the loop count.)

5. **Screenshot** just the active slide element:

   ```bash
   node ~/.claude/skills/browser-automation/resources/browser-screenshot.js \
     --output=slide-N.png --element="svg.bespoke-marp-active"
   ```

6. **Read** the PNG in the Claude conversation and verify.

### Teardown

```bash
node ~/.claude/skills/browser-automation/resources/browser-close.js
# then kill the marp --server background job
```

### Why arrow-key navigation instead of `#/N` hash

Marp bespoke's slide router attaches its `hashchange` listener after the initial goto. Setting `location.hash = "#/14"` after page load fires a hashchange but bespoke's handler often doesn't wire up in time. Dispatching ArrowRight keydown events on `document.body` is the most reliable way to drive bespoke's internal state.

### Why render HTML-only (not PDF/PNG)

Rendering all 23 slides to PNG takes 30+ seconds. Rendering the same deck to a single `.html` file takes ~2s. The browser-driven screenshot gives you a single-slide visual in the same time you'd otherwise wait for one re-render.

## Color Reference

### Trellis theme (product-UI palette)

See [assets/trellis-theme.md](assets/trellis-theme.md) for the full theme. Key colors:

| Token | Hex | Usage |
|---|---|---|
| Slate | `#33475B` | Default slide background |
| Dark Slate | `#1a2633` | Code block / table header |
| HubSpot Orange | `#FF5C35` | Headings, accent |
| Trellis Magenta | `#A83D5C` | Section dividers, CTA slides |
| Light Pink | `#FDEDF2` | Lead/title slides |
| Cyan | `#00A4BD` | Emphasis text, links |
| Off White | `#f5f8fa` | Body text |

### HubSpot brand-identity theme

See [assets/hubspot-theme.md](assets/hubspot-theme.md) for the full theme. Key colors:

| Token | Hex | Usage |
|---|---|---|
| Cream | `#F5F0EB` | Default background, lead slides |
| Dark Text | `#2D3748` | Default body text |
| Panel BG | `#ECE7E1` | Card surface |
| HubSpot Orange | `#FF5C35` | Headings, numbers, bullets, accent bars |
| Maroon | `#3D1126` | Section dividers, "Then" heading in compare |
| Dark Teal | `#042729` | `.metric` card, `.dark` accent slides |
| Divider | `#DDD8D2` | Hairline dividers |

**Fonts:** Lexend Deca (300 Light for headings, 400 for body), Caveat (hand-drawn accents).