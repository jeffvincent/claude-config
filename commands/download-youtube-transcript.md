Download YouTube video and transcript to the current directory.

Arguments: YOUTUBE_URL [OPTIONAL_NAME]

Steps:
1. Check if download-workout.sh exists in current directory
2. If not, check if we're in the workouts directory or offer to use it from there
3. Run the script with provided arguments
4. Display results including video file and transcript location

The script will:
- Download the video using yt-dlp
- Extract auto-generated English subtitles/captions
- Save video to videos/ subdirectory
- Save transcript (SRT format) to transcripts/ subdirectory
- Handle custom naming if provided

Examples:
- `/download-youtube-transcript "https://www.youtube.com/watch?v=abc123"`
- `/download-youtube-transcript "https://www.youtube.com/watch?v=abc123" "HIIT Cardio"`
