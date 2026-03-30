#!/bin/bash
# Claude Code Job Completion Hook
# Plays sound notification when long-running tasks (5+ minutes) complete
# Configured for macOS with osascript

set -e

# Read JSON input from stdin
INPUT=$(cat)

# Extract relevant fields using jq (fallback to grep if jq not available)
if command -v jq &> /dev/null; then
    SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // "unknown"')
    IS_CONTINUING=$(echo "$INPUT" | jq -r '.is_continuing // false')
    CWD=$(echo "$INPUT" | jq -r '.cwd // "unknown"')
else
    # Fallback parsing if jq not installed
    SESSION_ID=$(echo "$INPUT" | grep -o '"session_id":"[^"]*"' | cut -d'"' -f4 || echo "unknown")
    IS_CONTINUING=$(echo "$INPUT" | grep -o '"is_continuing":[^,}]*' | cut -d':' -f2 | tr -d ' ' || echo "false")
    CWD=$(echo "$INPUT" | grep -o '"cwd":"[^"]*"' | cut -d'"' -f4 || echo "unknown")
fi

# State file written by job-start.sh (UserPromptSubmit hook)
START_FILE="$HOME/.claude/job-start-time.txt"
LOG_FILE="$HOME/.claude/job-completion.log"

# Get current timestamp (seconds since epoch)
CURRENT_TIME=$(date +%s)

# Only check timing if Claude is not continuing (task truly complete)
if [[ "$IS_CONTINUING" == "false" ]]; then
    # Check if we have a start timestamp from this task
    if [[ -f "$START_FILE" ]]; then
        START_TIME=$(cat "$START_FILE")

        # Calculate duration in seconds
        DURATION=$((CURRENT_TIME - START_TIME))

        # Convert to minutes for display
        DURATION_MINUTES=$((DURATION / 60))
        DURATION_SECONDS=$((DURATION % 60))

        # Define threshold: notify if task took 5+ minutes
        MIN_DURATION=300    # 5 minutes in seconds

        # Check if this was a long-running task
        if [[ $DURATION -ge $MIN_DURATION ]]; then
            # Play custom sound notification for long-running tasks
            afplay "$HOME/.claude/sounds/job-complete.mp3" &
            osascript -e 'display notification "Long-running task completed" with title "Claude Code" subtitle "Duration: '"${DURATION_MINUTES}m ${DURATION_SECONDS}s"'"'

            # Log long task completion
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] LONG TASK completed | Duration: ${DURATION_MINUTES}m ${DURATION_SECONDS}s | Session: $SESSION_ID | CWD: $CWD" >> "$LOG_FILE"
        else
            # Log all completions for debugging (no sound)
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] Task completed | Duration: ${DURATION_MINUTES}m ${DURATION_SECONDS}s | Session: $SESSION_ID | CWD: $CWD" >> "$LOG_FILE"
        fi

        # Clear start file so a missing file = no prompt submitted yet
        rm -f "$START_FILE"
    else
        # No start time recorded, skip notification
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Task completed | Duration: N/A (no start time) | Session: $SESSION_ID | CWD: $CWD" >> "$LOG_FILE"
    fi
fi

exit 0
