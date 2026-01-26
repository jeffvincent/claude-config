Download YouTube workout video, extract transcript, analyze workout details, and create formatted markdown file.

Arguments: YOUTUBE_URL [OPTIONAL_NAME]

This command performs a complete workflow:
1. Download video and transcript using download-workout.sh
2. Extract YouTube creator name and video title metadata
3. Read and analyze the transcript (SRT format)
4. Extract workout details including:
   - Warmup protocols
   - Exercise names, sets, reps, weights
   - Form cues and technique tips
   - Circuit structures
   - Key quotes and timestamps
   - Training philosophy
5. Format into comprehensive markdown document
6. Save as "{{ Creator }} - {{ Video Title }}.md"

Output structure:
- Video metadata and source links
- Workout overview
- Phase-by-phase breakdown
- Exercise details with timestamps
- Form tips and technique notes
- Training principles
- Links to local video and transcript files

The script will:
- Download the video using yt-dlp
- Extract auto-generated English subtitles/captions
- Save video to videos/ subdirectory
- Save transcript (SRT format) to transcripts/ subdirectory
- Create formatted workout markdown file in root directory
- Handle custom naming if provided

Files created:
- videos/{{ Video Title }}.webm (or .mp4)
- transcripts/{{ Video Title }}.srt
- {{ Creator }} - {{ Video Title }}.md

Examples:
- `/download-youtube-transcript "https://www.youtube.com/watch?v=abc123"`
- `/download-youtube-transcript "https://www.youtube.com/watch?v=abc123" "HIIT Cardio"`
