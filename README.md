# Claude Code Configuration

My personal [Claude Code](https://claude.com/claude-code) configuration with custom skills, commands, hooks, and plugins.

## What's Included

### 🎯 Skills (11 custom skills)
- **gmail-skill** - Manage Gmail (send, read, search emails, manage labels)
- **google-calendar-skill** - Manage Google Calendar (search, create, update events)
- **wistia-uploader** - Upload videos to Wistia for hosting and transcription
- **video-clipper** - Create video clips from chapter timestamps using ffmpeg
- **video-transcript-analyzer** - Analyze video transcripts with thematic breakdowns
- **browser-automation** - Automate Chrome for web scraping and data extraction
- **support-data-analyzer** - Analyze customer support data and generate reports
- **uxr-report-analyzer** - Analyze UXR report PDFs with structured findings
- **interview-synthesis-updater** - Update interview synthesis notes
- **things** - Manage Things 3 tasks using natural language
- **skill-generator** - Generate new Claude Skills from briefs

### ⌨️ Commands
- **process-media** - Process Founders podcast from YouTube to analyzed content notes

### 🪝 Hooks
- **log-image-generation** - Automatically log Gemini image generation commands

### 🔌 Plugins
- Plugin configuration structure

### 🎨 Other
- **statusline-anchor.sh** - Custom status line configuration

## Setup

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/claude-config.git ~/.claude
cd ~/.claude
```

### 2. Install skill dependencies

Skills with `package.json` need dependencies installed:

```bash
# Gmail skill
cd skills/gmail-skill
npm install

# Google Calendar skill
cd ../google-calendar-skill
npm install

# Wistia uploader
cd ../wistia-uploader
npm install

# Interview synthesis updater
cd ../interview-synthesis-updater
npm install
```

### 3. Configure secrets

All credentials are stored in a central `secrets/` directory (not included in git).

#### Wistia Configuration

Create `secrets/wistia/.env`:
```bash
mkdir -p secrets/wistia
cp secrets/wistia/.env.example secrets/wistia/.env
# Edit secrets/wistia/.env with your Wistia API token
```

#### Google OAuth Setup

For Google Calendar and Gmail skills:

1. Follow instructions in:
   - `secrets/google-calendar/README.md`
   - `secrets/gmail/README.md`

2. Place your OAuth credentials from Google Cloud Console:
   - `secrets/google-calendar/credentials.json`
   - `secrets/gmail/credentials.json`

3. Run setup scripts to authenticate:
   ```bash
   cd skills/google-calendar-skill
   npm run setup

   cd ../gmail-skill
   npm run setup
   ```

## Directory Structure

```
.claude/
├── commands/           # Custom slash commands
├── hooks/             # Event hooks
├── skills/            # Custom Claude Skills
├── plugins/           # Plugin configurations
├── secrets/           # Credentials (gitignored)
│   ├── wistia/
│   ├── google-calendar/
│   └── gmail/
├── settings.json      # Claude Code settings
└── statusline-anchor.sh
```

## Usage

### Skills

Skills are invoked automatically by Claude Code when relevant to your requests. You can also invoke them explicitly using the skill name.

### Commands

Use slash commands in Claude Code:
```
/process-media YOUTUBE_URL DISPLAY_NAME
```

### Hooks

Hooks run automatically on events (e.g., after Bash commands). The log-image-generation hook automatically logs all Gemini image generation commands.

## Customization

### Adding New Skills

1. Create a new directory in `skills/`
2. Add a `Skill.md` or `skill.md` file with the skill prompt
3. Optionally add implementation scripts and `package.json`
4. Add any credentials to `secrets/` and update `.gitignore`

### Adding New Commands

Create a `.md` file in `commands/` with the command description and steps.

### Adding New Hooks

Create a shell script in `hooks/` and configure it in `settings.json`:

```json
{
  "hooks": {
    "post-tool": {
      "Bash": "~/.claude/hooks/your-hook.sh"
    }
  }
}
```

## Security Notes

- **NEVER commit the `secrets/` directory** - it contains API keys and OAuth tokens
- Review `.gitignore` before pushing to ensure no credentials are included
- Use `.example` files to document required credential structures
- Regenerate any credentials that are accidentally committed

## Contributing

Feel free to use this as a template for your own Claude Code configuration! If you create interesting skills or commands, consider sharing them.

## License

MIT License - feel free to use and modify as needed.
