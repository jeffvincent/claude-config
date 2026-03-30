#!/bin/bash
# Records task start time for job-completion.sh duration tracking

date +%s > "$HOME/.claude/job-start-time.txt"
exit 0
