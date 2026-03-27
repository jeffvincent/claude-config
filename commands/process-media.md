Process a Founders podcast or YouTube video into fully analyzed content notes.

Arguments: YOUTUBE_URL [DISPLAY_NAME]

Steps:
1. Extract transcript from YouTube using yt-dlp:
   ```
   yt-dlp --write-auto-sub --sub-format vtt --skip-download \
     -o "/tmp/yt-transcript" "YOUTUBE_URL"
   ```
2. Get video title/metadata:
   ```
   yt-dlp --get-title --get-id "YOUTUBE_URL"
   ```
3. Parse the .vtt file into clean readable text with timestamps:
   - Strip inline word-level tags (<c>, timing annotations)
   - Deduplicate consecutive identical lines
   - Group by minute with [MM:SS] markers
4. Analyze transcript and create comprehensive source document in:
   ~/Projects/Knowledge System/notes/content notes/sources/
   Named: YYYY-MM-DD_GuestName_Short-Title_Show.md

   Document structure:
   - Frontmatter: guest, show, date, YouTube URL, duration
   - Summary (2-3 paragraphs)
   - Key quotes (8-12 impactful quotes)
   - Topical breakdown with timestamps (10-15 sections)
   - Related themes
   - Connections to existing syntheses
5. Identify 2-3 major themes and create/update synthesis notes in:
   ~/Projects/Knowledge System/notes/content notes/syntheses/
6. Clean up /tmp/yt-transcript* files
7. Commit and push to Knowledge System git repo

Working directory: ~/Projects/Knowledge System/notes/content notes/
