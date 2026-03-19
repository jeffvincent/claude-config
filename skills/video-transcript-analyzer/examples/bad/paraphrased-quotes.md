# Anti-Pattern: Paraphrased Quotes

The most common and most damaging mistake in transcript analysis.

---

## What went wrong

The analyst "cleaned up" quotes to sound more professional. This destroys the customer's actual voice and makes the analysis unreliable.

## Bad Example

```markdown
## Key Quotes

> "The registration email system lacks bulk management capabilities, which significantly impacts our team's productivity when dealing with large membership lists."
>
> — Emma, on membership management
```

## What the customer actually said

```markdown
> "I have to manually resend registration emails one by one. When you've got 2,000 members, that's just not feasible."
>
> — Emma, on membership email management
```

## Why this matters

1. **The real quote has emotion** — "just not feasible" conveys frustration. "Significantly impacts productivity" is corporate.
2. **The real quote has specifics** — "one by one" and "2,000 members" are concrete. "Lacks bulk management capabilities" is abstract.
3. **The real quote sounds like a person** — stakeholders reading this can hear Emma's voice. The paraphrased version sounds like a requirements doc.
4. **Trust is destroyed** — if a PM sees cleaned-up quotes, they can't trust ANY quote in the document.

## The Rule

If you can't find the exact string in the transcript, it's not a quote. Period.
