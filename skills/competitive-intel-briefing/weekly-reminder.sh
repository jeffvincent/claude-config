#!/bin/bash

# Weekly Competitive Intel Briefing Reminder
# Opens Terminal with instructions to generate briefing

osascript <<EOF
tell application "Terminal"
    activate
    do script "
echo '========================================='
echo '   WEEKLY COMPETITIVE INTEL BRIEFING'
echo '========================================='
echo ''
echo 'It\\'s Monday morning! Time to generate'
echo 'this week\\'s competitive intelligence briefing.'
echo ''
echo 'Run this command in Claude Code:'
echo ''
echo '  Use skill: competitive-intel-briefing'
echo '  Generate weekly light briefing for this week.'
echo ''
echo '========================================='
echo ''
echo 'Press any key to open Claude Code...'
read -n 1
open -a 'Claude Code'
"
end tell
EOF
