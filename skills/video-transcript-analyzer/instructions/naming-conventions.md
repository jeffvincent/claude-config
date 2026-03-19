# File Naming Conventions

## Required Information

Prompt the user for:
1. "What is the customer's first name?" (e.g., Emma, Martin, Sarah)
2. "What is the customer's last name (or press Enter to skip)?" (e.g., McKenna, Jones)
3. "What is the company name?" (e.g., HubSpot, Acme, TechCorp)

## Filename Format

**With last name:**
`YYYY-MM-DD_FirstName_LastName_CompanyName.md`
- Example: `2025-11-15_Martin_McKenna_HubSpot.md`

**Without last name:**
`YYYY-MM-DD_FirstName_CompanyName.md`
- Example: `2025-11-11_Emma_Ax.md`

## Rules

- Use today's date for YYYY-MM-DD
- Include last name only if provided (skip if not available)
- Use company name only (no legal entity suffix like "Inc." or "Ltd.")
- Use underscores between all parts
- No spaces in filenames
- Preserve original casing of names
