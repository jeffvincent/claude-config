#!/bin/bash

# Uninstall Competitive Intelligence Briefing Automation

set -e

echo "========================================="
echo "  Uninstalling Competitive Intel Automation"
echo "========================================="
echo ""

LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"

# Unload launch agents
echo "Unloading launch agents..."
launchctl unload "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.weekly.plist" 2>/dev/null || echo "Weekly scheduler not loaded"
launchctl unload "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.monthly.plist" 2>/dev/null || echo "Monthly scheduler not loaded"

# Remove plist files
echo "Removing plist files..."
rm -f "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.weekly.plist"
rm -f "$LAUNCH_AGENTS_DIR/com.claude.competitive-intel.monthly.plist"

echo ""
echo "========================================="
echo "  Uninstallation Complete!"
echo "========================================="
echo ""
echo "The automation has been removed."
echo "Briefing files in your Knowledge System are preserved."
echo ""
echo "To reinstall, run:"
echo "  ~/.claude/skills/competitive-intel-briefing/install.sh"
echo ""
