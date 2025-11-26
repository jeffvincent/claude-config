#!/bin/bash

# Read JSON input from stdin
input=$(cat)

# Extract current directory from JSON
current_dir=$(echo "$input" | jq -r '.workspace.current_dir')

# Only show status when in the Anchor project directory
if [[ "$current_dir" != "/Users/jvincent/Projects/Anchor"* ]]; then
    exit 0
fi

# Project name
project_name="Anchor Orthodontics"

# Extract first unchecked task from Active Tasks in CLAUDE.md
claude_md="/Users/jvincent/Projects/Anchor/CLAUDE.md"
if [[ -f "$claude_md" ]]; then
    # Find the first unchecked task after "Active Tasks:" section
    current_focus=$(awk '/\*\*Active Tasks:\*\*/{flag=1; next} flag && /^- \[ \]/{print; exit}' "$claude_md" | sed 's/^- \[ \] //' | sed 's/^[[:space:]]*//')
    
    # If no unchecked tasks, show "All tasks complete"
    if [[ -z "$current_focus" ]]; then
        current_focus="All tasks complete"
    fi
else
    current_focus="Unknown"
fi

# Calculate percent complete from SEO-RECOMMENDATIONS.md
seo_file="/Users/jvincent/Projects/Anchor/SEO-RECOMMENDATIONS.md"
if [[ -f "$seo_file" ]]; then
    # Count total checkboxes (both checked and unchecked)
    total=$(grep -o '\[[ x]\]' "$seo_file" | wc -l | tr -d ' ')
    # Count checked boxes
    checked=$(grep -o '\[x\]' "$seo_file" | wc -l | tr -d ' ')
    
    # Calculate percentage (avoid division by zero)
    if [[ $total -gt 0 ]]; then
        percent=$((checked * 100 / total))
    else
        percent=0
    fi
else
    percent=0
fi

# Output the status line
echo "${project_name} | ${current_focus} | ${percent}% complete"
