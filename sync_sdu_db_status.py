
import sqlite3
import re
import os

def sync_db_from_sdu_master(db_path, sdu_master_file="SDU_dive_sites.md"):
    if not os.path.exists(sdu_master_file):
        print(f"Error: {sdu_master_file} not found.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(sdu_master_file, "r") as f:
        content = f.read()

    # Regex to find all article titles in the master file
    # Assumes titles start with '## ' or '### ' and are followed by a newline
    article_titles_in_master = set()
    # Updated regex to capture both ## and ###, and extract the main title before any subtitle
    for match in re.finditer(r'^(?:#){2,3}\s*(.*?)(?::.*)?\n', content, re.MULTILINE):
        full_article_title_line = match.group(1).strip()
        # Extract core dive site name by splitting at the first ':' or ' - '
        core_dive_site_name = full_article_title_line.split(' : ')[0].split(' - ')[0].strip()
        article_titles_in_master.add(core_dive_site_name)

    updated_count = 0
    # Iterate through titles found in the master file and update their status in DB
    for title in article_titles_in_master:
        try:
            cursor.execute("UPDATE dive_sites SET article_status = 'Completed' WHERE name = ? AND article_status IS NOT 'Completed'", (title,))
            if cursor.rowcount > 0:
                updated_count += cursor.rowcount
                print(f"Updated DB status to 'Completed' for: {title}")
        except sqlite3.Error as e:
            print(f"Error updating DB for {title}: {e}")

    conn.commit()
    conn.close()
    print(f"Database synchronization complete. Updated {updated_count} entries to 'Completed'.")

if __name__ == "__main__":
    db_file = "dive_sites.db"
    sync_db_from_sdu_master(db_file)
