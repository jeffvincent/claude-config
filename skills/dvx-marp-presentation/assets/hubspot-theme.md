# HubSpot MARP Theme (Brand Identity)

HubSpot **brand-identity** palette — cream, orange, dark teal, maroon, with Lexend Deca Light typography and Caveat hand-drawn accents. Sourced from HubSpot's `slide-deck-builder` (the deck system used for executive and external presentations).

For HubSpot's **product-UI** palette (dark navy + magenta + cyan, Trellis design tokens), see [trellis-theme.md](trellis-theme.md).

**When to use:** executive memos, leadership alignment decks, external / brand-aligned presentations, anything where you want an editorial, identity-first feel instead of a product-UI feel.

Copy this frontmatter block to the top of your `slides.md` file.

```yaml
---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@300;400;700&family=Caveat:wght@400;700&display=swap');
  section {
    font-family: 'Lexend Deca', system-ui, sans-serif;
    font-weight: 400;
    background: #F5F0EB;
    color: #2D3748;
    padding: 56px 72px;
  }
  h1, h2, h3 {
    font-family: 'Lexend Deca', system-ui, sans-serif;
    font-weight: 300;
    color: #FF5C35;
    letter-spacing: -0.01em;
  }
  h1 { font-size: 2.2em; margin-bottom: 0.3em; }
  h2 { font-size: 1.6em; }
  h3 {
    font-size: 1em;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #FF5C35;
    margin-bottom: 0.4em;
  }
  strong { color: #2D3748; font-weight: 700; }
  em { color: #718096; font-style: normal; }
  a { color: #FF5C35; }
  blockquote {
    border-left: 4px solid #FF5C35;
    padding-left: 20px;
    font-weight: 300;
    color: #4A5568;
    font-size: 1.4em;
    line-height: 1.4;
  }
  code {
    background: #ECE7E1;
    color: #2D3748;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.9em;
  }
  pre {
    background: #ECE7E1;
    border-radius: 8px;
    padding: 20px;
  }
  pre code {
    background: none;
    padding: 0;
    font-size: 0.7em;
    color: #2D3748;
  }
  table { font-size: 0.85em; border-collapse: collapse; }
  th {
    background: #FF5C35;
    color: #fff;
    padding: 10px 14px;
    text-align: left;
    font-weight: 700;
  }
  td {
    background: #F5F0EB;
    color: #2D3748;
    padding: 10px 14px;
    border-bottom: 1px solid #DDD8D2;
  }

  /* --- Slide class variants --- */
  section.lead {
    background: #F5F0EB;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.lead h1 {
    color: #FF5C35;
    font-size: 3.2em;
    font-weight: 300;
    margin-bottom: 0.3em;
  }
  section.lead p {
    color: #4A5568;
    font-size: 1.25em;
    max-width: 80%;
  }
  section.section-divider {
    background: #3D1126;
    color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.section-divider h1 {
    color: #fff;
    font-size: 2.6em;
    font-weight: 300;
    margin-bottom: 0.2em;
  }
  section.section-divider p {
    color: rgba(255, 255, 255, 0.85);
    font-size: 1.2em;
  }
  section.section-divider p em,
  section.section-divider em,
  section.section-divider strong {
    color: rgba(255, 255, 255, 0.95);
    font-style: normal;
  }
  section.dark {
    background: #042729;
    color: #F5F0EB;
  }
  section.dark h1, section.dark h2, section.dark h3 {
    color: #FF5C35;
  }
  section.dark strong { color: #F5F0EB; }
  section.dark em { color: #B8C5A8; }
  section.agenda { background: #F5F0EB; }
  section.agenda h1 {
    font-size: 2em;
    margin-bottom: 0.6em;
  }
  section.agenda ol {
    list-style: none;
    padding: 0;
    font-size: 1.2em;
    line-height: 2;
    color: #2D3748;
  }
  section.agenda ol li::before {
    content: "";
    display: inline-block;
    width: 10px;
    height: 10px;
    background: #FF5C35;
    border-radius: 50%;
    margin-right: 14px;
    vertical-align: middle;
  }

  /* --- Custom component classes --- */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 32px;
    margin-top: 0.4em;
  }
  .two-col > div {
    background: #ECE7E1;
    border-radius: 8px;
    padding: 20px 24px;
    color: #2D3748;
  }
  .two-col h3 {
    margin-top: 0;
    border-bottom: 2px solid #FF5C35;
    padding-bottom: 6px;
  }
  .two-col.compare .then h3 {
    color: #3D1126;
    border-bottom-color: #3D1126;
  }
  .two-col.compare .now h3 {
    color: #FF5C35;
    border-bottom-color: #FF5C35;
  }
  .two-col ul {
    padding-left: 1.1em;
    margin: 0;
    line-height: 1.7;
  }
  .stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 0.6em;
  }
  .stat-card {
    background: #ECE7E1;
    border-left: 6px solid #FF5C35;
    border-radius: 6px;
    padding: 18px 24px;
  }
  .stat-card .label {
    color: #4A5568;
    font-size: 0.8em;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 700;
  }
  .stat-card .number {
    color: #FF5C35;
    font-size: 2.6em;
    font-weight: 300;
    line-height: 1.05;
    margin: 4px 0;
  }
  .stat-card .desc {
    color: #4A5568;
    font-size: 0.85em;
    line-height: 1.4;
  }
  .play-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px 28px;
    margin-top: 0.4em;
  }
  .play-grid .full { grid-column: 1 / -1; }
  .play-grid .cell h3 {
    color: #FF5C35;
    font-size: 0.78em;
    letter-spacing: 0.14em;
    margin: 0 0 4px 0;
    border-bottom: 1px solid #DDD8D2;
    padding-bottom: 4px;
    text-transform: uppercase;
    font-weight: 700;
  }
  .play-grid .cell p {
    margin: 0;
    line-height: 1.4;
    color: #2D3748;
  }
  .metric,
  .play-grid .cell p.metric,
  .play-grid .cell .metric {
    background: #042729;
    border-left: 4px solid #FF5C35;
    border-radius: 4px;
    padding: 10px 16px;
    font-weight: 600;
    color: #FFFFFF;
  }
  .metric strong, .metric em, .metric * {
    color: #FFFFFF;
  }
  .caveat {
    font-family: 'Caveat', cursive;
    font-weight: 700;
    color: #FF5C35;
  }
---
```

## Color Palette

Sourced from `pm-skills/skills/slide-deck-builder/scripts/build_deck.py`.

| Name | Hex | Usage |
|---|---|---|
| Cream | `#F5F0EB` | Default slide background, lead slides, body panels on dark |
| Dark Text | `#2D3748` | Default body text |
| Subtle | `#4A5568` | Secondary text, descriptions, blockquote body |
| Gray | `#718096` | Muted text, `em` |
| Panel BG | `#ECE7E1` | Card surface (stat-card, two-col panels) |
| Divider | `#DDD8D2` | Hairline dividers between cells / tables |
| **HubSpot Orange** | `#FF5C35` | H1/H2/H3, accent bars, numbers, links, bullets |
| Faint Orange | `#FDE0D8` | Soft highlight fill (reserved) |
| **Maroon** | `#3D1126` | Section dividers, "Then" heading in compare |
| **Dark Teal** | `#042729` | Metric card, `section.dark` accent slides |
| Sage | `#B8C5A8` | `em` on dark sections |

## Typography

- **Body:** `Lexend Deca` weight 400, 16px base (Marp default)
- **Headings:** `Lexend Deca` weight **300 (Light)** — the HubSpot editorial tell
- **Small-caps labels (H3):** `Lexend Deca` weight 700 uppercase with letter-spacing
- **Hand-drawn accent:** `Caveat` — apply via `<span class="caveat">…</span>`

## Slide Class Variants

Use MARP's `<!-- _class: classname -->` directive:

- **`lead`** — Title / hook slides. Cream background, large orange heading, centered.
- **`section-divider`** — Major topic transitions. Maroon background, white text, centered.
- **`dark`** — High-contrast accent slide. Dark teal background, cream text, orange headings. Good for "the turn" / climax moments or a break in rhythm.
- **`agenda`** — Agenda slide. Cream background with orange bullet dots on ordered list.

## Component Classes (inline HTML)

Wrap content in `<div class="...">` when you want a structured layout Marp's plain Markdown can't express.

- **`two-col`** — Two equal columns, each on a cream panel with orange underline heading. Add `.compare` + `.then` / `.now` children for "before/after" slides (maroon Then / orange Now).
- **`stat-grid` + `stat-card`** — 2×2 grid of stat cards. Each card has a label (small caps), a large orange number, and a description.
- **`play-grid` + `cell`** — Flexible grid for comparing initiatives / plays. Cells have an orange small-caps H3 with a hairline divider below.
- **`metric`** — Highlight card: dark teal background, orange accent bar, cream text. Good for "the one number that matters" callouts at the bottom of a slide.
- **`caveat`** — Inline hand-drawn accent. Use sparingly — good for a single annotation or a quoted name.

## Example

```markdown
<!-- _class: lead -->

# Three billion automated actions per day.

That advantage is about to be rewritten.
```

```markdown
<!-- _class: dark -->

# The turn.

Competitors can log what ran. Only **HubSpot** can prove what *changed*.
```
