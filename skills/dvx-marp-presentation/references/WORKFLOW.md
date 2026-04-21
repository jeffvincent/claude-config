# MARP Presentation Reference

## Workflow

The recommended workflow for building presentations with this skill:

1. **Dictate** — Record yourself talking through the talk, feed the transcript to Claude
2. **Structure** — Have Claude organize the dictation into sections and speaker notes
3. **Build slides** — Create `slides.md` with the HubSpot theme frontmatter
4. **Dev server** — Run `npx @marp-team/marp-cli --server .` for live preview
5. **Iterate** — Do dry runs, feed transcripts back for refinement
6. **Lint** — Run slidegauge to catch issues
7. **Images** — Generate illustrations with `generate-image.py` for visual slides
8. **Export** — `npx @marp-team/marp-cli slides.md -o slides.pdf` for PDF

## Image Generation Tips

### Style consistency
When generating multiple images for a deck, always pass previous images as references with `-i` to maintain a consistent art style. For example:

```bash
# First image establishes the style
uv run scripts/generate-image.py -o images/hero.png "a friendly cartoon robot"

# Subsequent images reference the first
uv run scripts/generate-image.py -o images/scene2.png -i images/hero.png "the same robot building something"
```

### Aspect ratios for MARP
- Section dividers with `bg left:35%` → use `-a 9:16` (portrait)
- Content slides with `bg right:40% contain` → use `-a 9:16` or `-a 4:3`
- Full-width background images → use `-a 16:9` (landscape)
- Character portraits or icons → use default `1:1`

### Prompt tips
- Be very specific about what you want: colors, poses, expressions
- Say "no text" to avoid the model adding text to images
- Specify "simple clean background" to keep images slide-friendly
- For HubSpot mascots, reference the base images (sidekick.png, aviator_logo.png, chirp.png)

## Slidegauge Thresholds

| Metric | Threshold | Fix |
|---|---|---|
| Adjusted content | ≤ 350 chars | Move text to speaker notes |
| Code block lines | ≤ 10 lines | Split slide or use scoped smaller font |
| Title length | ≤ 35 chars | Shorten title |
| Total lines | ≤ 15 | Split into two slides |
| Overall score | ≥ 70 | Address warnings above |

## MARP Markdown Tips

### Slide separators
Use `---` between slides.

### Background images
```markdown
![bg](image.png)              <!-- Full background -->
![bg left:35%](image.png)     <!-- Left 35%, content right -->
![bg right:30%](image.png)    <!-- Right 30%, content left -->
![bg contain](image.png)      <!-- Fit within slide -->
![bg cover](image.png)        <!-- Fill and crop -->
```

### Per-slide classes
```markdown
<!-- _class: lead -->          <!-- Title slide styling -->
<!-- _class: section-divider -->  <!-- Section break styling -->
<!-- _class: agenda -->        <!-- Agenda list styling -->
```

### Per-slide style overrides
```markdown
<style scoped>
pre code { font-size: 0.45em; line-height: 1.1; }
h1 { font-size: 1.4em; }
</style>
```

### Hide page numbers on specific slides
```markdown
<!-- _paginate: false -->
```

## Exporting

```bash
# PDF
npx @marp-team/marp-cli slides.md -o slides.pdf

# PowerPoint
npx @marp-team/marp-cli slides.md -o slides.pptx

# HTML (single file)
npx @marp-team/marp-cli slides.md -o slides.html
```