#!/bin/bash

# Install Competitive Intelligence Briefing Automation

set -e

echo "========================================="
echo "  Competitive Intel Briefing Setup"
echo "========================================="
echo ""

# Check if launchd directory exists
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
if [ ! -d "$LAUNCH_AGENTS_DIR" ]; then
    echo "Creating LaunchAgents directory..."
    mkdir -p "$LAUNCH_AGENTS_DIR"
fi

# Copy plist files
echo "Installing launchd configurations..."
cp ~/.claude/skills/competitive-intel-briefing/com.claude.competitive-intel.weekly.plist "$LAUNCH_AGENTS_DIR/"
cp ~/.claude/skills/competitive-intel-briefing/com.claude.competitive-intel.monthly.plist "$LAUNCH_AGENTS_DIR/"

# Unload if already loaded (in case of reinstall)
launchctl unload "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.weekly.plist" 2>/dev/null || true
launchctl unload "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.monthly.plist" 2>/dev/null || true

# Load the launch agents
echo "Loading launch agents..."
launchctl load "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.weekly.plist"
launchctl load "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.monthly.plist"

# Verify
echo ""
echo "Verifying installation..."
if launchctl list | grep -q "com.claude.competitive-intel.weekly"; then
    echo "✓ Weekly briefing scheduler installed"
else
    echo "✗ Weekly briefing scheduler NOT installed"
fi

if launchctl list | grep -q "com.claude.competitive-intel.monthly"; then
    echo "✓ Monthly briefing scheduler installed"
else
    echo "✗ Monthly briefing scheduler NOT installed"
fi

echo ""
echo "========================================="
echo "  Installation Complete!"
echo "========================================="
echo ""
echo "Schedules:"
echo "  - Weekly:  Every Monday at 8:00 AM"
echo "  - Monthly: First Monday of month at 8:00 AM"
echo ""
echo "A Terminal window will open with instructions"
echo "when it's time to generate a briefing."
echo ""
echo "To uninstall:"
echo "  launchctl unload ~/Library/LaunchAgents/com.claude.competitive-intel.*.plist"
echo "  rm ~/Library/LaunchAgents/com.claude.competitive-intel.*.plist"
echo ""
echo "Logs:"
echo "  ~/.claude/skills/competitive-intel-briefing/weekly.log"
echo "  ~/.claude/skills/competitive-intel-briefing/monthly.log"
echo ""
