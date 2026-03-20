#!/bin/bash

# Weekly Competitive Intel Briefing Reminder
# Opens Terminal with instructions to generate briefing

osascript <<EOF
tell application "Terminal"
    activate
    do script "
echo '========================================='
echo '      START YOUR WEEK BRIEFING'
echo '========================================='
echo ''
echo 'It\\'s Monday morning!'
echo ''
echo 'Get your complete weekly briefing with:'
echo '  • Calendar highlights & 1:1 prep'
echo '  • Priority tasks & deadlines'
echo '  • Competitive intelligence'
echo '  • Strategic context'
echo '  • Week ahead priorities'
echo ''
echo 'Run this command in Claude Code:'
echo ''
echo '  /start-week'
echo ''
echo '========================================='
echo ''
echo 'Press any key to open Claude Code...'
read -n 1
open -a 'Claude Code'
"
end tell
EOF
