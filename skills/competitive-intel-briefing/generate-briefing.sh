#!/bin/bash

# Competitive Intelligence Briefing Generator
# Runs via launchd every Monday at 8:00 AM
# Generates weekly briefing always, monthly briefing on first Monday

set -e

LOG_FILE="$HOME/.claude/skills/competitive-intel-briefing/briefing.log"
BRIEFINGS_DIR="$HOME/Projects/Knowledge System/notes/competitive-intelligence/briefings"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== Starting Competitive Intel Briefing Generation ==="

# Get current date info
CURRENT_DATE=$(date +%Y-%m-%d)
DAY_OF_MONTH=$(date +%d)
DAY_OF_WEEK=$(date +%u)  # 1=Monday, 7=Sunday

log "Date: $CURRENT_DATE, Day of month: $DAY_OF_MONTH, Day of week: $DAY_OF_WEEK"

# Determine if it's the first Monday of the month
# First Monday = Monday (day 1) AND day of month is between 1-7
IS_FIRST_MONDAY=false
if [ "$DAY_OF_WEEK" -eq 1 ] && [ "$DAY_OF_MONTH" -le 7 ]; then
    IS_FIRST_MONDAY=true
    log "This is the FIRST MONDAY of the month - generating both weekly and monthly briefings"
else
    log "Regular Monday - generating weekly briefing only"
fi

# Create briefings directory if it doesn't exist
mkdir -p "$BRIEFINGS_DIR"

# Generate weekly briefing (always on Monday)
log "Generating weekly briefing..."

claude-code << 'EOF'
Please use the competitive-intel-briefing skill to generate this week's competitive intelligence briefing.

Generate a weekly light briefing covering the top 5 competitors (Attio, Day.ai, Clarify, Salesforce Agentforce, Microsoft Copilot Studio).

Follow all guidelines in the skill:
1. Research using WebSearch and WebFetch verification
2. Generate inline HTML format for email
3. Save files to the briefings directory
4. Send email to jvincent@hubspot.com using personal Gmail account

Use skill: competitive-intel-briefing
EOF

if [ $? -eq 0 ]; then
    log "Weekly briefing generated successfully"
else
    log "ERROR: Weekly briefing generation failed"
    exit 1
fi

# Generate monthly briefing (only on first Monday)
if [ "$IS_FIRST_MONDAY" = true ]; then
    log "Generating monthly deep dive briefing..."

    claude-code << 'EOF'
Please use the competitive-intel-briefing skill to generate this month's competitive intelligence deep dive.

Generate a monthly deep dive briefing covering all 12 competitors with 3 comprehensive deep dives on the most significant developments from the past month.

Follow all guidelines in the skill:
1. Research using WebSearch and WebFetch verification
2. Generate inline HTML format for email
3. Save files to the briefings directory
4. Send email to jvincent@hubspot.com using personal Gmail account

Use skill: competitive-intel-briefing
EOF

    if [ $? -eq 0 ]; then
        log "Monthly briefing generated successfully"
    else
        log "ERROR: Monthly briefing generation failed"
        exit 1
    fi
fi

log "=== Briefing generation completed ==="
exit 0
