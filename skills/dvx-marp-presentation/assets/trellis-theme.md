# Trellis MARP Theme

HubSpot **product-UI** palette — dark navy, magenta, cyan. Derived from Trellis design tokens. Use this theme for internal engineering / product-context decks.

For HubSpot's **brand-identity** palette (cream + orange + dark teal + maroon, Lexend Deca), see [hubspot-theme.md](hubspot-theme.md).

Copy this frontmatter block to the top of your `slides.md` file.

```yaml
---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: 'Avenir Next', 'Helvetica Neue', Arial, sans-serif;
    background: #33475B;
    color: #f5f8fa;
  }
  section.section-divider {
    background: #A83D5C;
  }
  section.lead {
    background: #FDEDF2;
  }
  section.lead h1 {
    color: #A83D5C;
  }
  section.lead p {
    color: #33475B;
  }
  h1 {
    color: #FF5C35;
    font-size: 2.2em;
  }
  h2 {
    color: #FF5C35;
    font-size: 1.6em;
  }
  code {
    background: #e8ecf0;
    color: #2D3E50;
    padding: 2px 8px;
    border-radius: 4px;
  }
  pre {
    background: #f5f8fa;
    border-radius: 8px;
    padding: 20px;
  }
  pre code {
    background: none;
    padding: 0;
    font-size: 0.7em;
    color: #2D3E50;
  }
  blockquote {
    border-left: 4px solid #FF5C35;
    padding-left: 20px;
    font-style: italic;
    color: #99acc2;
  }
  strong {
    color: #fff;
  }
  section.lead h1 {
    font-size: 3em;
    text-align: center;
  }
  section.lead p {
    text-align: center;
    font-size: 1.3em;
    color: #33475B;
  }
  section.section-divider {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: #A83D5C;
    color: #fff;
  }
  section.section-divider h1 {
    font-size: 2.8em;
    margin-bottom: 0.2em;
    color: #fff;
  }
  section.section-divider p {
    font-size: 1.3em;
    color: rgba(255, 255, 255, 0.85);
  }
  section.agenda {
    background: #33475B;
  }
  section.agenda h1 {
    font-size: 2.2em;
    margin-bottom: 0.6em;
  }
  section.agenda ol {
    list-style: none;
    padding: 0;
    font-size: 1.3em;
    line-height: 2;
  }
  section.agenda ol li::before {
    content: "";
    display: inline-block;
    width: 12px;
    height: 12px;
    background: #FF5C35;
    border-radius: 50%;
    margin-right: 16px;
  }
  em {
    color: #00A4BD;
    font-style: normal;
  }
  table {
    font-size: 0.8em;
  }
  th {
    background: #1a2633;
    color: #FF5C35;
  }
  td {
    background: #425B76;
  }
  a {
    color: #00A4BD;
  }
---
```

## Color Palette

These colors are derived from HubSpot's Trellis design system:

| Name | Hex | CSS Variable | Usage |
|---|---|---|---|
| Slate | `#33475B` | — | Default slide background |
| Dark Slate | `#2D3E50` | — | Code text color |
| Darkest | `#1a2633` | — | Table headers, dark accents |
| HubSpot Orange | `#FF5C35` | `--hs-orange` | H1/H2 headings, list bullets |
| Trellis Magenta Default | `#F2547D` | `--trellis-fill-accent-magenta-default` | — |
| Trellis Magenta Pressed | `#A83D5C` | `--trellis-fill-accent-magenta-pressed` | Section dividers, CTA slides |
| Trellis Magenta Subtle | `#FDEDF2` | `--trellis-fill-accent-magenta-subtle` | Lead/title slide background |
| Trellis Cyan | `#00A4BD` | `--trellis-fill-accent-cyan-default` | Emphasis text, links |
| Light Gray | `#e8ecf0` | — | Inline code background |
| Off White | `#f5f8fa` | — | Body text, code block background |
| Mid Gray | `#99acc2` | — | Blockquote text, subtitles |
| Table Cell | `#425B76` | — | Table cell background |