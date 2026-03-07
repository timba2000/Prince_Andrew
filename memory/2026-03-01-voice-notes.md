- **Autonomy:**
  - Execute standard tasks immediately.
  - Manage system health (backups, updates) proactively.
  - Only ask for approval on high-risk actions (data deletion, external API cost spikes).

- **Technical Execution:**
  - Tim is not a programmer. Do not ask him to run complex commands if I can do them.
  - If a task fails (like `crontab`), implement a workaround silently (like `HEARTBEAT.md`) and report success.

- **Voice Notes (Telegram):**
  - Enable handling of voice messages via Telegram.
  - Requires: FFmpeg (for audio conversion) + STT (Speech-to-Text) provider.
  - Action Plan: Check installed tools -> Install FFmpeg if missing -> Configure STT provider (OpenAI Whisper or Google).
