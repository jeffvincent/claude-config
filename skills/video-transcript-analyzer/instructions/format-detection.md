# Format Detection Rules

When a transcript file is provided, determine its format before processing.

## SRT Format (with timestamps)

**Detected by:** Presence of timestamp patterns like `00:05:30,120 --> 00:05:33,450`

**Characteristics:**
- Numbered subtitle blocks
- Timestamp lines with `-->` separator
- Dialogue text between timestamp blocks
- May include speaker identification

**Processing:** Parse timestamps and dialogue separately. Use timestamps for chapter markers in topical breakdown.

## Plain Text Format (no timestamps)

**Detected by:** Absence of SRT timestamp patterns

**Characteristics:**
- Dialogue text only
- May have speaker labels (e.g., "Interviewer:", "Customer:")
- No timing information

**Processing:** Create topic sections without timestamps. Use `## Topic #N: Title` format instead of timestamp markers.

## Post-Detection Steps

1. If SRT, parse all timestamps into a lookup table for chapter marker creation
2. Identify participants (interviewer vs customer/interviewee) from dialogue patterns
3. Check if a video URL was provided in the user's message or context
4. If NO video URL found, prompt: "Do you have a link to the video recording? If so, please share it and I'll include it in the analysis."
5. Wait for user response before proceeding
