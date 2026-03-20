#!/bin/bash

# Read JSON input from stdin
input=$(cat)

# Extract current directory from JSON
current_dir=$(echo "$input" | jq -r '.workspace.current_dir')

# Shorten the directory path (replace home with ~)
short_dir="${current_dir/#$HOME/\~}"

# Get git info if in a repository
git_info=""
if git -C "$current_dir" rev-parse --git-dir > /dev/null 2>&1; then
    # Get the remote URL and extract repo name
    remote_url=$(git -C "$current_dir" config --get remote.origin.url 2>/dev/null)

    if [[ -n "$remote_url" ]]; then
        # Extract repo name from GitHub URL
        # Handles both SSH (git@github.com:user/repo.git) and HTTPS (https://github.com/user/repo.git)
        repo_name=$(echo "$remote_url" | sed -E 's/.*[:/]([^/]+\/[^/]+)(\.git)?$/\1/' | sed 's/\.git$//')

        # Get current branch
        branch=$(git -C "$current_dir" branch --show-current 2>/dev/null)

        if [[ -n "$branch" ]]; then
            git_info=" | ${repo_name} (${branch})"
        else
            git_info=" | ${repo_name}"
        fi
    else
        # No remote, just show branch
        branch=$(git -C "$current_dir" branch --show-current 2>/dev/null)
        if [[ -n "$branch" ]]; then
            git_info=" | git (${branch})"
        fi
    fi
fi

# Output the status line
echo "${short_dir}${git_info}"
