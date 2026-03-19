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

# State file to track task start times
STATE_FILE="$HOME/.claude/job-timing-state.txt"
LOG_FILE="$HOME/.claude/job-completion.log"

# Get current timestamp (seconds since epoch)
CURRENT_TIME=$(date +%s)

# Only check timing if Claude is not continuing (task truly complete)
if [[ "$IS_CONTINUING" == "false" ]]; then
    # Check if we have a previous timestamp
    if [[ -f "$STATE_FILE" ]]; then
        LAST_TIME=$(cat "$STATE_FILE")

        # Calculate duration in seconds
        DURATION=$((CURRENT_TIME - LAST_TIME))

        # Convert to minutes for display
        DURATION_MINUTES=$((DURATION / 60))
        DURATION_SECONDS=$((DURATION % 60))

        # Define thresholds
        MIN_DURATION=300    # 5 minutes in seconds
        MAX_DURATION=3600   # 1 hour in seconds (to exclude long idle periods)

        # Check if this was a long-running task
        if [[ $DURATION -ge $MIN_DURATION ]] && [[ $DURATION -le $MAX_DURATION ]]; then
            # Play custom sound notification for long-running tasks
            afplay "$HOME/.claude/sounds/job-complete.mp3" &
            osascript -e 'display notification "Long-running task completed" with title "Claude Code" subtitle "Duration: '"${DURATION_MINUTES}m ${DURATION_SECONDS}s"'"'

            # Log long task completion
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] LONG TASK completed | Duration: ${DURATION_MINUTES}m ${DURATION_SECONDS}s | Session: $SESSION_ID | CWD: $CWD" >> "$LOG_FILE"
        else
            # Log all completions for debugging (no sound)
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] Task completed | Duration: ${DURATION_MINUTES}m ${DURATION_SECONDS}s | Session: $SESSION_ID | CWD: $CWD" >> "$LOG_FILE"
        fi
    else
        # First run - no previous timestamp, just log
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Task completed | Duration: N/A (first task) | Session: $SESSION_ID | CWD: $CWD" >> "$LOG_FILE"
    fi

    # Update state file with current timestamp
    echo "$CURRENT_TIME" > "$STATE_FILE"
fi

exit 0
