# Competitive Intelligence Briefing Automation

Automated competitive intelligence briefings for HubSpot leadership tracking AI-native CRM competitors.

## Quick Start

### Recommended: /start-week Command

**Get your complete Monday morning briefing:**
```bash
# In Claude Code, run:
/start-week
```

This orchestrates everything:
- Calendar review and 1:1 prep
- Priority tasks and deadlines
- **Auto-generates competitive intel** (weekly on Mondays, monthly on first Monday)
- Recent conversations and action items
- Strategic context and priorities for the week

### Alternative: Manual Generation

**Weekly briefing only:**
```bash
# In Claude Code, run:
Use skill: competitive-intel-briefing

Generate weekly light briefing for this week.
```

**Monthly briefing only:**
```bash
# In Claude Code, run:
Use skill: competitive-intel-briefing

Generate monthly deep dive briefing for this month.
```

## Automated Scheduling

### LaunchAgent Reminders (Installed)

LaunchAgents are configured to pop up Terminal reminders:

- **Every Monday at 8:00 AM**: Reminder to run `/start-week`
- **First Monday of month at 8:00 AM**: Reminder to run `/start-week` (generates both briefings)

When the Terminal opens, you'll see instructions to run `/start-week` in Claude Code.

1. Copy launchd plist files:
```bash
cp ~/.claude/skills/competitive-intel-briefing/com.claude.competitive-intel.weekly.plist ~/Library/LaunchAgents/
cp ~/.claude/skills/competitive-intel-briefing/com.claude.competitive-intel.monthly.plist ~/Library/LaunchAgents/
```

2. Load the launch agents:
```bash
launchctl load ~/Library/LaunchAgents/com.claude.competitive-intel.weekly.plist
launchctl load ~/Library/LaunchAgents/com.claude.competitive-intel.monthly.plist
```

3. Verify they're loaded:
```bash
launchctl list | grep competitive-intel
```

### Option 3: Cron Alternative

Add to crontab (`crontab -e`):
```bash
# Weekly briefing - Every Monday at 8:00 AM
0 8 * * 1 /Users/jvincent/.claude/skills/competitive-intel-briefing/weekly-reminder.sh

# Monthly briefing - First Monday at 8:00 AM
0 8 1-7 * 1 /Users/jvincent/.claude/skills/competitive-intel-briefing/monthly-reminder.sh
```

## Output Files

Briefings are saved to:
```
~/Projects/Knowledge System/notes/competitive-intelligence/briefings/
├── YYYY-MM-DD-weekly-light.md
├── YYYY-MM-DD-weekly-email.html
├── YYYY-MM-DD-monthly-deep.md
└── YYYY-MM-DD-monthly-email.html
```

Emails are automatically sent to: jvincent@hubspot.com

## Competitors Tracked

**Top 5 (Weekly):**
- Attio
- Day.ai
- Clarify
- Salesforce Agentforce
- Microsoft Copilot Studio

**All 12 (Monthly):**
- Above 5 plus:
- Gumloop
- Zapier Agents
- UiPath Agentic Automation
- Notion AI
- Airtable AI
- Linear AI
- Make.com

## Research Quality

Every briefing follows strict verification:
- WebSearch for recent developments
- WebFetch to read full source articles
- Primary sources only (company blogs, press releases, verified tech news)
- All major claims verified before inclusion

## Customization

Edit `SKILL.md` to:
- Add/remove competitors
- Adjust briefing structure
- Modify research methodology
- Change email recipients
- Update styling/formatting

## Logs

Execution logs: `~/.claude/skills/competitive-intel-briefing/briefing.log`

## Troubleshooting

**Emails not sending:**
- Verify personal Gmail account is authenticated: `cd ~/.claude/skills/gmail-skill && node scripts/manage-accounts.js --list`
- Re-authenticate if needed: `cd ~/.claude/skills/gmail-skill && npm run setup`

**Missing competitors:**
- Check if WebSearch returned results
- Try searching with different date ranges
- Some weeks may have no significant updates (this is normal)

**Formatting issues:**
- Verify inline HTML format (no <!DOCTYPE> or <html> wrapper)
- Check that all styles are inline attributes
- Test by sending to yourself first

## Cost Estimate

- Weekly briefing: ~$0.80/week = ~$42/year
- Monthly briefing: ~$3.45/month = ~$41/year
- Combined: ~$83/year in LLM costs

## Future Enhancements

Potential improvements:
- [ ] Add automated testing of email formatting
- [ ] Create summary dashboard of competitor activity
- [ ] Add sentiment analysis trends over time
- [ ] Generate quarterly strategic reports
- [ ] Integration with HubSpot CRM for tracking competitive deals
