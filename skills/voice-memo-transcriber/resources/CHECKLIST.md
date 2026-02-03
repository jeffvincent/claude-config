# Voice Memo Transcriber - Testing Checklist

Use this checklist to validate the skill is working correctly.

## Pre-Processing Validation

- [ ] **File path validation**
  - File exists at specified path
  - File has audio/video extension (.m4a, .mp3, .mov, .mp4, .wav, etc.)
  - User has read permissions for the file

- [ ] **Output directory validation**
  - Output directory exists (or use source file directory)
  - User has write permissions for output directory
  - Sufficient disk space available (~3x source file size recommended)

- [ ] **Model validation**
  - If whisper_model specified, it's one of: tiny, base, small, medium, large
  - Default to "base" if not specified

## Dependency Checks

- [ ] **ffmpeg installed**
  - Run: `which ffmpeg`
  - If missing, provide installation instructions
  - Version check: `ffmpeg -version` (any recent version OK)

- [ ] **pipx installed**
  - Run: `which pipx`
  - If missing, install with: `brew install pipx && pipx ensurepath`

- [ ] **openai-whisper installed**
  - Run: `pipx list | grep openai-whisper`
  - If missing, install with: `pipx install openai-whisper`
  - Verify installation: `whisper --help`

## Audio Conversion

- [ ] **Format detection**
  - Correctly identify if file is already MP3
  - Skip conversion for MP3 files

- [ ] **Conversion execution** (for non-MP3 files)
  - ffmpeg command runs successfully
  - Output file created with .mp3 extension
  - Audio quality preserved (16kHz, mono, 96kbps)
  - No video stream in output (audio only)

- [ ] **Error handling**
  - Corrupted files detected and reported
  - Empty files rejected
  - Unsupported formats reported with helpful message

## Transcription

- [ ] **Whisper execution**
  - Command runs with correct model parameter
  - Both txt and srt formats specified
  - Output directory correctly specified
  - Language set to English (or auto-detect)

- [ ] **First-run model download**
  - Model downloads automatically on first use
  - Progress visible to user
  - Model cached for future use (~/.cache/whisper/)

- [ ] **Processing time**
  - Progress updates shown during long transcriptions
  - User kept informed of status
  - Reasonable timeout (allow ~10-20 seconds per minute of audio)

- [ ] **Output files generated**
  - .txt file created with plain text transcript
  - .srt file created with timestamps
  - Both files in correct output directory
  - Filenames match source file basename

## Summary Generation

- [ ] **Transcript reading**
  - Successfully read generated .txt file
  - Handle long transcripts (may need to read in chunks)

- [ ] **Summary quality**
  - 1-3 sentence summary generated
  - Captures main topics or themes
  - Identifies action items if present
  - Clear and concise language

## Output Reporting

- [ ] **File paths**
  - All generated file paths displayed
  - Paths are absolute and correct
  - User can easily locate files

- [ ] **Summary display**
  - Summary shown to user
  - Well formatted and readable

- [ ] **Processing metadata**
  - Processing time reported
  - Model used stated
  - Any warnings or notes included

## Error Scenarios

- [ ] **File not found**
  - Clear error message
  - Suggests checking path and permissions

- [ ] **Unsupported format**
  - Lists supported formats
  - Suggests conversion or different file

- [ ] **Missing dependencies**
  - Identifies which dependency is missing
  - Provides installation instructions
  - Offers to help with installation

- [ ] **Insufficient disk space**
  - Detects low disk space
  - Reports required vs available space
  - Suggests cleanup or different output location

- [ ] **Corrupted audio**
  - Detects ffmpeg errors
  - Reports file may be corrupted
  - Suggests trying different file

- [ ] **Whisper errors**
  - Handles model download failures
  - Reports transcription errors clearly
  - Suggests troubleshooting steps

## Security and Privacy

- [ ] **Local processing**
  - No external API calls made
  - All data stays on user's machine
  - Models downloaded from official sources only

- [ ] **File handling**
  - No files uploaded anywhere
  - Temporary files cleaned up (optional)
  - Original file never modified

- [ ] **Permissions**
  - Only requested permissions used
  - No unnecessary file access
  - User's privacy respected

## Validation Tests

### Test 1: Basic M4A Transcription
```
Input: test-file.m4a (5 minutes)
Expected: txt, srt, mp3 files generated, summary provided
```

### Test 2: Already MP3
```
Input: podcast.mp3
Expected: No conversion, only txt and srt generated
```

### Test 3: Custom Output Directory
```
Input: voice-memo.m4a, output_dir: /custom/path/
Expected: Files in /custom/path/ instead of source directory
```

### Test 4: Different Model Sizes
```
Input: Same file with tiny, base, small models
Expected: Varying accuracy and processing times
```

### Test 5: Long Audio File
```
Input: 60-minute recording
Expected: Completes successfully, progress updates shown
```

### Test 6: First-Time Setup
```
Input: Any file, dependencies not installed
Expected: Prompts to install, completes after installation
```

## Success Criteria

The skill is working correctly if:
- ✓ All three output files generated successfully
- ✓ Transcript content is accurate and readable
- ✓ SRT timestamps are correctly formatted
- ✓ Summary captures main content
- ✓ Error messages are clear and helpful
- ✓ Processing time is reasonable
- ✓ No data leaves the local machine
