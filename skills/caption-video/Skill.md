---
name: Caption Video
description: Render a video clip with captions overlaid, using the Remotion captioner at `/Users/jvincent/Projects/remotion-captioner/`. Use when user provides a video file and wants to add captions/subtitles, mentions "caption this video", "add captions", "burn in subtitles", or provides a video + SRT file pair.
version: 1.0.0
dependencies: node, remotion-captioner
allowed-tools: [Bash, Read]
---

# Caption Video

Render a video clip with captions overlaid using the Remotion captioner project.

## When to Apply

Use this skill when:
- User provides a video file and asks to add captions or subtitles
- User says "caption this", "add captions", "burn in subtitles", or similar
- User provides both a video file and an SRT file
- User wants to preview multiple caption styles on a video
- User has a video + SRT pair and wants styled caption output

Do NOT use this skill for:
- Transcribing audio to text (use voice-memo-transcriber instead)
- Splitting video into clips (use video-clipper instead)
- Uploading video (use wistia-uploader instead)

## Inputs

1. **Video file path** (required) — path to `.mp4` or other video file
2. **SRT file path** (optional) — if not provided, look for one with the same basename
3. **`--variant <name>`** (optional) — caption animation style. Default: `slide-up`
4. **`--end-seconds <n>`** (optional) — trim render to first N seconds (useful for previews)

## Available Variants

`fade`, `slide-up`, `spring-pop`, `blur-release`, `typewriter`, `underline-sweep`

Default is `slide-up` (HubSpot orange pill, white text, rises 24px while fading in).

## Instructions for Claude

### Step 1: Resolve Inputs

- If the user gave both a video path and an SRT path, use them.
- If only a video path is given, look for an SRT with the same basename in the same folder (e.g. `clip.mp4` -> `clip.srt`). If not found, ask the user for the SRT path.
- If the user gave a folder path, look inside it for exactly one `.mp4` + one `.srt` pair and use them. If multiple pairs exist, list them and ask which.

### Step 2: Run the Render

```bash
cd /Users/jvincent/Projects/remotion-captioner && node render.mjs "<video>" "<srt>" [--variant <name>] [--end-seconds <n>]
```

Use `run_in_background: true` — renders for a ~3min clip take ~1-2 minutes.

Only change the variant from `slide-up` if the user explicitly passes `--variant <name>`.

### Step 3: Report

When done, print the output file path and file size. Don't re-explain the styling unless asked.

## Output Naming

- Default style: `<video-basename>.captioned.mp4` alongside the source
- Non-default variant or trimmed: `<video-basename>.captioned.<variant>[.<Ns>].mp4`

## Previewing Multiple Styles

Pass `--variant all --end-seconds 25` to render 25-second samples of every style.

## Notes

- The `remotion-captioner` project is at `/Users/jvincent/Projects/remotion-captioner/` (outside Knowledge System repo)
- All processing is local — no external services
