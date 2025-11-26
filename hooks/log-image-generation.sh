#!/bin/bash
# Hook to automatically log Gemini image generation

# This runs after every Bash command
# Check if it was an image generation command

COMMAND="$TOOL_INPUT"

# Check if this is a Gemini image generation command
if [[ "$COMMAND" =~ generate_image\.py|edit_image\.py|compose_images\.py|multi_turn_chat\.py ]]; then

    # Ensure log directory exists
    LOG_DIR="$HOME/.claude/logs"
    mkdir -p "$LOG_DIR"
    LOG_FILE="$LOG_DIR/image-generation-log.jsonl"

    # Extract information from the command
    # Extract the full prompt - it's the first argument to the Python script
    # Use a more robust extraction that handles long prompts

    # Method: Find everything between "script.py " and the filename.png
    if [[ "$COMMAND" =~ generate_image\.py[[:space:]]+\"([^\"]+)\" ]] || \
       [[ "$COMMAND" =~ edit_image\.py[[:space:]]+\"([^\"]+)\" ]] || \
       [[ "$COMMAND" =~ compose_images\.py[[:space:]]+\"([^\"]+)\" ]]; then
        PROMPT="${BASH_REMATCH[1]}"
    elif [[ "$COMMAND" =~ generate_image\.py[[:space:]]+\'([^\']+)\' ]] || \
         [[ "$COMMAND" =~ edit_image\.py[[:space:]]+\'([^\']+)\' ]] || \
         [[ "$COMMAND" =~ compose_images\.py[[:space:]]+\'([^\']+)\' ]]; then
        PROMPT="${BASH_REMATCH[1]}"
    else
        # Fallback: try to extract any quoted string
        if [[ "$COMMAND" =~ \"([^\"]+)\" ]]; then
            PROMPT="${BASH_REMATCH[1]}"
        else
            PROMPT="[No prompt extracted from command]"
        fi
    fi

    # Note: This captures prompts without embedded quotes.
    # If your prompt contains quotes, they should be escaped in the command.

    # Extract output filename (usually after prompt, before flags)
    FILENAME=$(echo "$COMMAND" | grep -oP '\S+\.png|\S+\.jpg|\S+\.jpeg' | head -1)

    # Extract model if specified
    if echo "$COMMAND" | grep -q -- "--model"; then
        MODEL=$(echo "$COMMAND" | grep -oP -- '--model\s+\K[^\s]+')
    else
        MODEL="gemini-2.5-flash-image"
    fi

    # Extract aspect ratio if specified
    if echo "$COMMAND" | grep -q -- "--aspect"; then
        ASPECT=$(echo "$COMMAND" | grep -oP -- '--aspect\s+\K[^\s]+')
    else
        ASPECT="unknown"
    fi

    # Determine full output path
    DEFAULT_OUTPUT_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Resources/Images/AI Nonsense"

    if [[ "$FILENAME" = /* ]]; then
        FULL_PATH="$FILENAME"
    else
        FULL_PATH="$DEFAULT_OUTPUT_DIR/$FILENAME"
    fi

    # Generate timestamp
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Create a simple description based on prompt length
    if [ -n "$PROMPT" ]; then
        # Truncate very long prompts for the description
        if [ ${#PROMPT} -gt 100 ]; then
            DESCRIPTION="Image generation: ${PROMPT:0:100}..."
        else
            DESCRIPTION="Image generation: $PROMPT"
        fi
    else
        DESCRIPTION="Image generation command executed"
    fi

    # Escape special characters for JSON
    PROMPT_ESCAPED=$(echo "$PROMPT" | sed 's/"/\\"/g' | sed "s/'/\\'/g")
    DESC_ESCAPED=$(echo "$DESCRIPTION" | sed 's/"/\\"/g' | sed "s/'/\\'/g")
    COMMAND_ESCAPED=$(echo "$COMMAND" | sed 's/"/\\"/g' | sed "s/'/\\'/g")

    # Create JSON log entry
    LOG_ENTRY=$(cat <<EOF
{"timestamp":"$TIMESTAMP","prompt":"$PROMPT_ESCAPED","output_file":"$FILENAME","output_path":"$FULL_PATH","description":"$DESC_ESCAPED","model":"$MODEL","aspect_ratio":"$ASPECT","command":"$COMMAND_ESCAPED"}
EOF
)

    # Append to log file
    echo "$LOG_ENTRY" >> "$LOG_FILE"

    # Optional: Print confirmation (comment out if too noisy)
    # echo "✓ Image generation logged to $LOG_FILE" >&2
fi
