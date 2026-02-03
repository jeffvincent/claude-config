# Voice Memo Transcriber

Automatically transcribe voice memos and audio files to text using OpenAI Whisper (open-source, local processing).

## Quick Start

**Trigger this skill by saying:**
- "Transcribe this voice memo: `/path/to/file.m4a`"
- "Create a transcript from `/path/to/recording.mov`"
- "Convert this audio to text: `/path/to/voice-note.mp3`"

## What It Does

1. ✓ Accepts audio/video files in multiple formats
2. ✓ Converts to MP3 if needed (using ffmpeg)
3. ✓ Transcribes using Whisper AI (runs locally)
4. ✓ Generates plain text transcript (.txt)
5. ✓ Generates subtitles with timestamps (.srt)
6. ✓ Provides a summary of the content

## Supported Formats

- `.m4a` (Voice Memos, QuickTime audio)
- `.mp3` (MP3 audio)
- `.mov` (QuickTime video)
- `.mp4` (MP4 video)
- `.wav` (WAV audio)
- `.aac`, `.flac`, `.ogg`, `.webm`

## Requirements

The skill will automatically check and help install:
- **ffmpeg** - Audio/video conversion
- **pipx** - Python application installer
- **openai-whisper** - Transcription engine

First-time setup takes a few minutes. After that, transcription is fast.

## Privacy

**All processing happens on your local machine.** No audio is sent to external servers. Whisper models are downloaded once and cached locally.

## Usage Examples

### Basic Transcription
```
You: Transcribe /Users/jeff/Desktop/meeting.m4a

Claude: [Checks dependencies, converts to MP3, transcribes, generates summary]

✓ Transcription complete!

Files generated:
- Transcript: /Users/jeff/Desktop/meeting.txt
- Subtitles: /Users/jeff/Desktop/meeting.srt
- Audio: /Users/jeff/Desktop/meeting.mp3

Summary: Meeting covered Q1 priorities, roadmap planning, and team hiring.
```

### Custom Output Directory
```
You: Transcribe /Users/jeff/voice-note.m4a to /Users/jeff/Documents/Transcripts/

Claude: [Saves all outputs to specified directory]
```

### Better Accuracy (Larger Model)
```
You: Transcribe interview.mov using the medium model for better accuracy

Claude: [Uses larger Whisper model, takes longer but more accurate]
```

## Processing Time

Approximate times for 10-minute audio:
- **tiny model**: ~30 seconds (lowest accuracy)
- **base model**: ~60 seconds (good balance) ← default
- **small model**: ~2 minutes (better accuracy)
- **medium model**: ~5 minutes (high accuracy)
- **large model**: ~10 minutes (highest accuracy)

First run includes one-time model download (~140MB for base model).

## Output Files

### Plain Text Transcript (`.txt`)
```
The meeting covered three main topics. First, we discussed the product
roadmap for Q1, focusing on new features including the dashboard redesign
and API improvements. Second, we reviewed the hiring plan...
```

### Subtitles with Timestamps (`.srt`)
```
1
00:00:00,000 --> 00:00:04,000
The meeting covered three main topics.

2
00:00:04,000 --> 00:00:08,000
First, we discussed the product roadmap for Q1,

3
00:00:08,000 --> 00:00:13,000
focusing on new features including the dashboard redesign
```

## Troubleshooting

**"Error: ffmpeg not found"**
→ Install: `brew install ffmpeg` (macOS) or see skill instructions

**"Error: File not found"**
→ Check the file path is correct and file exists

**"Processing very slow"**
→ Try using the "tiny" model for faster results: "transcribe file.m4a using tiny model"

**"Model download failed"**
→ Check internet connection. Models download once from HuggingFace.

## File Structure

```
voice-memo-transcriber/
├── Skill.md              # Main skill instructions for Claude
├── README.md             # This file (user documentation)
├── package.json          # Dependency documentation
└── resources/
    ├── EXAMPLES.md       # Detailed usage examples
    └── CHECKLIST.md      # Testing and validation checklist
```

## Model Information

Whisper models (trade-off between speed and accuracy):

| Model | Size | Speed | Accuracy | Best For |
|-------|------|-------|----------|----------|
| tiny | 75MB | Fastest | Lowest | Quick notes, low priority |
| base | 140MB | Fast | Good | General use (default) |
| small | 460MB | Medium | Better | Important meetings |
| medium | 1.5GB | Slow | High | Interviews, detailed content |
| large | 3GB | Slowest | Highest | Critical transcription needs |

## Privacy & Security

- ✓ All processing happens locally
- ✓ No data sent to cloud services
- ✓ No telemetry or tracking
- ✓ Original files never modified
- ✓ Models from official OpenAI/HuggingFace sources

**Note:** Voice memos may contain sensitive information. All files remain local and private.

## Support

For issues or questions:
1. Check `resources/EXAMPLES.md` for detailed examples
2. Check `resources/CHECKLIST.md` for troubleshooting
3. Verify dependencies are installed correctly
4. Try with a smaller test file first

## Credits

- Built with [OpenAI Whisper](https://github.com/openai/whisper)
- Uses ffmpeg for audio processing
- Generated with [Claude Code](https://claude.com/claude-code)
