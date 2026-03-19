# Good Example: SRT Transcript with Full Name

**Input:** `customer-feedback-call.srt` + user says "Here's the recording: https://vimeo.com/example123"
**Prompted for:** First name: Martin, Last name: McKenna, Company: HubSpot
**Output filename:** `2025-11-15_Martin_McKenna_HubSpot.md`

## What makes this good

1. Video URL included from user context
2. Summary is exactly 2 paragraphs — concise, informative, standalone
3. Quotes are verbatim (note the natural speech patterns preserved)
4. Topical breakdown uses timestamps and descriptive headers
5. Full transcript included unmodified at the end

---

## Output

```markdown
# Customer Feedback Call - Martin McKenna (Product Manager at HubSpot)

## Video
https://vimeo.com/example123

## Call Summary
Emma, the main HubSpot admin at AX for 4 years, discussed several critical pain points around membership management, list functionality, and admin workflows. The conversation revealed deep frustration with manual processes that should be automated, particularly around bulk email management and property resets.

Key themes included the disconnect between lists and views, limitations in form customization, and the impact of these issues on her team's ability to serve their largest dealer groups. Emma described a "panic moment" when support limitations blocked a critical campaign, highlighting the business impact of current tool constraints.

## Key Quotes
> "I had it was a proper panic moment for me, because we had our biggest dealer group about to resend. We were on a timeline for their campaign. And there was nothing like, I was completely powerless."
>
> — Emma, on being blocked by support limitations

> "I have to manually resend registration emails one by one. When you've got 2,000 members, that's just not feasible."
>
> — Emma, on membership email management

[3-6 more quotes following same format]

## Topical Breakdown

**00:02:57 - Membership Registration Email Management**
Cannot bulk manage registration emails for large membership lists.

- Must manually resend registration emails one by one to 2,000+ members
- Search functionality constantly refreshes while typing, making it difficult to use
- Requires HubSpot support intervention for "hard resets" of properties
- No ability to filter membership lists or create segments from membership data

**00:09:41 - Lists vs Views Disconnect**
Fundamental gap between list building and view customization capabilities.

- Views lack the filtering power of lists
- Cannot apply list-level logic within table views
- Workaround: export to Excel, manipulate, re-import
- Affects daily operational workflows for the entire admin team

[Continue for all topics]

## Full Transcript
1
00:00:00,000 --> 00:00:03,300
Hi, Emma. Hi, how are you, Hannah?

[Complete unmodified transcript...]
```
