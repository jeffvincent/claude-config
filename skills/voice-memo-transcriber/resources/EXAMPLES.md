# Voice Memo Transcriber - Examples

## Example 1: Basic Transcription (M4A voice memo)

**User Input:**
```
Please transcribe this voice memo: /Users/jeff/Desktop/meeting-notes.m4a
```

**Claude's Actions:**
1. Validates file exists
2. Checks dependencies (all installed)
3. Converts M4A to MP3
4. Runs Whisper transcription
5. Reads transcript and generates summary
6. Reports results

**Output:**
```
✓ Transcription complete!

Files generated:
- Transcript: /Users/jeff/Desktop/meeting-notes.txt
- Subtitles: /Users/jeff/Desktop/meeting-notes.srt
- Audio: /Users/jeff/Desktop/meeting-notes.mp3

Summary:
The meeting covered Q1 planning priorities including the product roadmap,
hiring plans for the engineering team, and budget allocation. Key action
items were assigned to department leads with a follow-up scheduled for
next week.

Processing time: 47 seconds
```

**Generated Files:**

`meeting-notes.txt`:
```
The meeting covered Q1 planning priorities. First, we discussed the product
roadmap for the next quarter, focusing on three major features: the new
dashboard, API improvements, and mobile app updates. Second, we reviewed
hiring plans for the engineering team. We need to fill five positions by
end of Q1. Finally, we allocated budget across departments. Marketing gets
an additional 20% for the product launch campaign. Action items: Sarah will
draft the job descriptions by Friday, Mike will finalize the roadmap
timeline by Monday, and Jennifer will distribute the budget spreadsheet by
end of week. Next meeting is scheduled for next Tuesday at 2 PM.
```

`meeting-notes.srt`:
```
1
00:00:00,000 --> 00:00:04,000
The meeting covered Q1 planning priorities.

2
00:00:04,000 --> 00:00:09,000
First, we discussed the product roadmap for the next quarter,

3
00:00:09,000 --> 00:00:14,000
focusing on three major features: the new dashboard, API improvements,

4
00:00:14,000 --> 00:00:17,000
and mobile app updates.

...
```

---

## Example 2: Custom Output Directory with Larger Model

**User Input:**
```
Transcribe /Users/jeff/Downloads/interview.mov to /Users/jeff/Documents/Transcripts/
using the medium model for better accuracy
```

**Claude's Actions:**
1. Validates file and output directory exist
2. Checks dependencies
3. Converts MOV to MP3
4. Runs Whisper with "medium" model
5. Generates summary
6. Reports results

**Output:**
```
✓ Transcription complete!

Files generated:
- Transcript: /Users/jeff/Documents/Transcripts/interview.txt
- Subtitles: /Users/jeff/Documents/Transcripts/interview.srt
- Audio: /Users/jeff/Documents/Transcripts/interview.mp3

Summary:
Customer interview discussing pain points with current CRM system,
specifically around data migration, API limitations, and reporting
capabilities. Customer expressed strong interest in automation features
and integration with marketing tools.

Processing time: 156 seconds
```

---

## Example 3: First-Time Setup (Missing Dependencies)

**User Input:**
```
Transcribe /Users/jeff/voice-memo.m4a
```

**Claude's Response (when dependencies missing):**
```
I'll transcribe your voice memo. First, I need to check and install dependencies.

Checking dependencies:
✗ ffmpeg not found
✗ pipx not found
✗ openai-whisper not found

I need to install these tools first. Here's what I'll do:

1. Install ffmpeg (audio conversion):
   brew install ffmpeg

2. Install pipx (Python app manager):
   brew install pipx
   pipx ensurepath

3. Install openai-whisper (transcription):
   pipx install openai-whisper

May I proceed with these installations? This is a one-time setup.
```

**After user approval:**
```
Installing dependencies...
✓ ffmpeg installed
✓ pipx installed
✓ openai-whisper installed

Note: The first transcription will download the Whisper model (~140MB for base model).
This is a one-time download.

Proceeding with transcription...
Downloading Whisper model... [progress bar]
✓ Model downloaded and cached

Transcribing audio...
✓ Transcription complete!

Files generated:
- Transcript: /Users/jeff/voice-memo.txt
- Subtitles: /Users/jeff/voice-memo.srt

Summary:
Quick voice note about grocery shopping list and reminder to call the dentist.

Processing time: 89 seconds (includes model download)
```

---

## Example 4: Already MP3 Format (No Conversion Needed)

**User Input:**
```
Transcribe this podcast excerpt: /Users/jeff/podcast-clip.mp3
```

**Claude's Response:**
```
✓ Transcription complete!

Files generated:
- Transcript: /Users/jeff/podcast-clip.txt
- Subtitles: /Users/jeff/podcast-clip.srt

Note: File was already in MP3 format, no conversion needed.

Summary:
Podcast discussion about the future of AI in healthcare, covering diagnostic
tools, patient data privacy concerns, and regulatory challenges facing the
industry.

Processing time: 34 seconds
```

---

## Example 5: Error Handling (File Not Found)

**User Input:**
```
Transcribe /Users/jeff/nonexistent.m4a
```

**Claude's Response:**
```
Error: Could not find file at /Users/jeff/nonexistent.m4a

Please check:
- The file path is correct
- The file exists at that location
- You have permission to read the file

Would you like to try a different file path?
```

---

## Example 6: Using Tiny Model for Speed

**User Input:**
```
Quick transcription of /Users/jeff/short-note.m4a using the tiny model
```

**Claude's Response:**
```
Using Whisper's "tiny" model for faster processing (lower accuracy).

✓ Transcription complete!

Files generated:
- Transcript: /Users/jeff/short-note.txt
- Subtitles: /Users/jeff/short-note.srt
- Audio: /Users/jeff/short-note.mp3

Summary:
Brief reminder about tomorrow's 10 AM team standup and preparing the quarterly report.

Processing time: 8 seconds

Note: The tiny model is faster but less accurate. For better results, use
the "base" (default) or "small" model.
```
