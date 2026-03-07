# HEARTBEAT.md

# Daily Backup Check
- Every day (check current time vs last backup time):
  - If no backup exists for today in `/data/backups/`, run `/data/backup-openclaw.sh`.
  - Log "Backup completed: <filename>" to `memory/logs/backup.log`.
Provide an update on tasks

# Keep this file small to limit token burn.
