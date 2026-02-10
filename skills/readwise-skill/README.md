# Readwise Integration Skill

Import books, articles, podcasts, and other content from your Readwise library into Content Notes.

## Setup

### 1. Get Your Readwise API Token

1. Log in to your Readwise account
2. Go to [https://readwise.io/access_token](https://readwise.io/access_token)
3. Copy your access token

### 2. Configure Credentials

The API token is stored in the centralized secrets directory:

```bash
# Create the secrets directory
mkdir -p ~/.claude/secrets/readwise

# Add your API token
echo "READWISE_API_TOKEN=your_token_here" > ~/.claude/secrets/readwise/.env
```

### 3. Install Dependencies

**Option A: Using Homebrew (Recommended for macOS)**
```bash
brew install python-requests
pip3 install --break-system-packages python-dotenv
```

**Option B: Using pipx with venv**
```bash
python3 -m venv ~/.claude/skills/readwise-skill/venv
source ~/.claude/skills/readwise-skill/venv/bin/activate
pip install -r ~/.claude/skills/readwise-skill/requirements.txt
deactivate
```

**Option C: Global install (if allowed)**
```bash
pip3 install -r ~/.claude/skills/readwise-skill/requirements.txt
```

## Usage

Use natural language commands:
- "Import 'Atomic Habits' from Readwise"
- "Search my Readwise library for articles about productivity"
- "Import that article from Tim Urban"
- "Sync updates for The Mom Test"

## Features

- **Search**: Find books, articles, podcasts, etc. in your Readwise library
- **Import**: Create source documents with all highlights and annotations
- **Sync**: Update existing imports with new highlights
- **Auto-commit**: Automatically commits changes to git

## Output Format

Creates source documents in `/sources/` directory:

```
sources/2026-02-10_James-Clear_Atomic-Habits_Readwise.md
```

Each document includes:
- Title, author, and metadata
- All highlights in chronological order
- Your annotations and notes
- Tags from Readwise
- Empty sections for theme connections

## API Rate Limits

- Default: 240 requests/minute
- List endpoints (highlights, books): 20 requests/minute
- The skill automatically handles rate limiting

## Related Workflows

After importing content:
1. Use `readwise-content-analyzer` skill to analyze highlights
2. Generate thematic insights and synthesis documents
3. Connect to existing themes in your Content Notes
