#!/usr/bin/env python3
"""PostToolUse hook: auto-appends skill invocations to _system/agent-log.md"""
import json, sys, os
from datetime import datetime

try:
    data = json.load(sys.stdin)
    skill_name = data.get("tool_input", {}).get("skill", "unknown")
    args = data.get("tool_input", {}).get("args", "")

    ks_root = os.path.expanduser("~/Projects/Knowledge System")
    log_path = os.path.join(ks_root, "_system/agent-log.md")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n[{timestamp}] | {skill_name} | invoked"
    if args:
        entry += f" | args: {args[:80]}"

    with open(log_path, "a") as f:
        f.write(entry)
except Exception:
    pass  # Never block on log failure
