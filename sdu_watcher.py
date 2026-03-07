
import time
import json
import os

progress_log_path = "/data/.openclaw/workspace/sdu_progress.log"
watcher_log_path = "/data/.openclaw/workspace/memory/logs/sdu-watcher.log"

def log_activity(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(watcher_log_path, 'a') as f:
        f.write(f"[{timestamp}] SDU-Watcher: {message}\n")

log_activity("Starting SDU progress monitor.")
last_position = 0

while True:
    try:
        if not os.path.exists(progress_log_path):
            log_activity(f"Progress log file not found: {progress_log_path}. Waiting...")
            time.sleep(30)
            continue

        with open(progress_log_path, 'r') as f:
            f.seek(last_position)
            new_lines = f.readlines()
            last_position = f.tell()

            for line in new_lines:
                line = line.strip()
                if line:
                    try:
                        data = json.loads(line)
                        total_sites = data.get('total_sites', 'N/A')
                        corroborated_sites = data.get('corroborated_sites', 'N/A')
                        percentage_complete = data.get('percentage_complete', 'N/A')

                        message_to_chat = (
                            f"SDU progress: {corroborated_sites}/"
                            f"{total_sites} corroborated ({percentage_complete}%)."
                        )
                        print(message_to_chat) # This will be sent to the chat
                        log_activity(f"Sent message to chat: '{message_to_chat}'")
                    except json.JSONDecodeError:
                        log_activity(f"Skipping non-JSON line: '{line}'")
                    except KeyError as e:
                        log_activity(f"Missing expected key in JSON line: {e} - '{line}'")
    except Exception as e:
        log_activity(f"An error occurred in the monitoring loop: {e}")

    time.sleep(30)
