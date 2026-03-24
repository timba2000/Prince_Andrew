# HEARTBEAT.md

# Daily Backup Check
- Every day (check current time vs last backup time):
  - If no backup exists for today in `/data/backups/`, run `/data/backup-openclaw.sh`.
  - Log "Backup completed: <filename>" to `memory/logs/backup.log`.

# Project Updates
- Every 30 minutes (during active hours):
  - Provide a quick update on all active projects. 

  - updates must be via Telegram

# Keep this file small to limit token burn.
