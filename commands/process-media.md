Process a podcast or video into fully analyzed content notes.

Arguments: URL_OR_FILE [DISPLAY_NAME]

Steps:
1. Determine transcript source based on input:

   **If YouTube URL** (youtube.com or youtu.be):
   - Extract transcript and metadata directly via yt-dlp (no video download needed):
     ```
     yt-dlp --get-title --get-id "URL"
     yt-dlp --write-auto-sub --sub-format vtt --skip-download \
       -o "/tmp/yt-transcript" "URL"
     ```

   **If not a YouTube URL** (local file, Vimeo, etc.):
   - Ask the user: "This isn't a YouTube URL — would you like to upload it to Wistia to get a transcript?"
   - If yes: upload to Wistia project d8417fem9e, wait for transcription, download transcript
   - If no: ask them to provide a transcript file directly

2. Parse the .vtt file into clean readable text with timestamps:
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
