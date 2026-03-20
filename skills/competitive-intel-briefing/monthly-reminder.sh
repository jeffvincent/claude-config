#!/bin/bash

# Monthly Competitive Intel Deep Dive Reminder
# Opens Terminal with instructions to generate briefing

osascript <<EOF
tell application "Terminal"
    activate
    do script "
echo '========================================='
echo '  MONTHLY COMPETITIVE INTEL DEEP DIVE'
echo '========================================='
echo ''
echo 'It\\'s the first Monday of the month!'
echo 'Time to generate the monthly deep dive briefing.'
echo ''
echo 'Run this command in Claude Code:'
echo ''
echo '  Use skill: competitive-intel-briefing'
echo '  Generate monthly deep dive briefing for this month.'
echo ''
echo '========================================='
echo ''
echo 'Press any key to open Claude Code...'
read -n 1
open -a 'Claude Code'
"
end tell
EOF
