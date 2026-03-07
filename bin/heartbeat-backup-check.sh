#!/bin/bash
mkdir -p /data/backups
TODAY=$(date +%F)
if ls /data/backups/*${TODAY}* 1>/dev/null 2>&1; then
  exit 0
fi
if [ -x /data/backup-openclaw.sh ]; then
  /data/backup-openclaw.sh
  NEW=$(ls -t /data/backups 2>/dev/null | head -n1 || true)
  if [ -n "$NEW" ]; then
    mkdir -p /data/.openclaw/workspace/memory/logs
    echo "Backup completed: $NEW" >> /data/.openclaw/workspace/memory/logs/backup.log
  fi
fi
