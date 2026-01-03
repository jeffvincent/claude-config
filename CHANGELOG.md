# Changelog

All notable changes to this Claude Code configuration will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- `CHANGELOG.md` to track configuration changes
- `.editorconfig` for consistent code formatting
- Proper `Skill.md` for interview-synthesis-updater skill

### Changed
- Standardized all skill definition files to use `Skill.md` naming convention
  - Renamed `gmail-skill/SKILL.md` to `Skill.md`
  - Renamed `google-calendar-skill/SKILL.md` to `Skill.md`
  - Renamed `things/skill.md` to `Skill.md`
- Replaced all hardcoded `/Users/jvincent/` paths with portable `~/` paths
- Updated browser-automation to use correct skill directory path
- Standardized YAML frontmatter across all skills with `version` and `allowed-tools`
- **Restructured Things skill for composability** (v2.0.0):
  - Main `Skill.md` reduced from 360 to ~90 lines (lightweight dispatcher)
  - Sub-skills moved to `skills/` subdirectory with standalone YAML frontmatter
  - Each sub-skill now independently discoverable
  - Fixed hardcoded paths in all sub-skills and README.md

### Removed
- Empty `plugins/config.json` (unused)
- Old Things sub-skill files from skill root (moved to `skills/` subdirectory)

## [1.0.0] - 2026-01-03

### Added
- Initial repository structure
- 11 custom skills:
  - `gmail-skill` - Gmail management
  - `google-calendar-skill` - Calendar operations
  - `wistia-uploader` - Video upload to Wistia
  - `video-transcript-analyzer` - Transcript analysis
  - `video-clipper` - Video clip creation with ffmpeg
  - `support-data-analyzer` - Customer support data analysis
  - `uxr-report-analyzer` - UXR report PDF analysis
  - `things` - Things 3 task management
  - `browser-automation` - Chrome automation
  - `skill-generator` - Generate new skills
  - `interview-synthesis-updater` - Update synthesis docs
- 2 custom commands:
  - `/process-media` - Process podcast videos
  - `/weekly-plan` - Weekly planning workflow
- 1 hook:
  - `log-image-generation.sh` - Log Gemini image generation
- `CLAUDE.md` with repository guidelines
- Git workflow documentation
