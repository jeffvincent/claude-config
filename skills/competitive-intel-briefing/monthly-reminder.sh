#!/bin/bash

# Monthly Competitive Intel Deep Dive Reminder
# Opens Terminal with instructions to generate briefing

osascript <<EOF
tell application "Terminal"
    activate
    do script "
echo '========================================='
echo '   START YOUR WEEK + MONTHLY DEEP DIVE'
echo '========================================='
echo ''
echo 'It\\'s the first Monday of the month!'
echo ''
echo 'Get your complete briefing including:'
echo '  • Calendar highlights & 1:1 prep'
echo '  • Priority tasks & deadlines'
echo '  • Competitive intel WEEKLY briefing'
echo '  • Competitive intel MONTHLY deep dive'
echo '  • Strategic context'
echo '  • Week ahead priorities'
echo ''
echo 'Run this command in Claude Code:'
echo ''
echo '  /start-week'
echo ''
echo '(Will auto-generate both briefings since'
echo ' it\\'s the first Monday of the month)'
echo ''
echo '========================================='
echo ''
echo 'Press any key to open Claude Code...'
read -n 1
open -a 'Claude Code'
"
end tell
EOF
