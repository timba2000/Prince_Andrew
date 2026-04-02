
import sqlite3
import os

def consolidate_articles(db_path, sdu_master_file="SDU_dive_sites.md", workspace_path="."):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Get all dive site names from DB
    cursor.execute("SELECT name FROM dive_sites;")
    db_dive_site_names = {row[0] for row in cursor.fetchall()}

    system_md_files = [
        "AGENTS.md", "BOOT.md", "BOOTSTRAP.md", "HEARTBEAT.md", "LICENSE",
        "MEMORY.md", "SOUL.md", "TOOLS.md", "USER.md", sdu_master_file
    ]

    articles_to_consolidate = []
    files_to_delete = []

    # 2. Filter .md files in the workspace that are actual dive site articles
    for filename in os.listdir(workspace_path):
        if filename.endswith(".md") and filename not in system_md_files:
            base_name = filename.replace(".md", "")
            # Check for direct match with dive site names from DB
            if base_name in db_dive_site_names:
                articles_to_consolidate.append({"filename": filename, "sitename": base_name})
                files_to_delete.append(filename)

    # Prepare content to append
    append_content = "\n" # Start with a newline for separation
    consolidated_site_names = []

    for article_info in articles_to_consolidate:
        filename = article_info["filename"]
        sitename = article_info["sitename"]
        file_path = os.path.join(workspace_path, filename)
        try:
            with open(file_path, "r") as f:
                article_text = f.read()
            append_content += f"\n## {sitename}\n\n{article_text}\n\n---\n\n"
            consolidated_site_names.append(sitename)
        except IOError as e:
            print(f"Error reading file {filename}: {e}")

    # 5. Read existing SDU_dive_sites.md content and append new articles
    existing_sdu_content = ""
    if os.path.exists(sdu_master_file):
        with open(sdu_master_file, "r") as f:
            existing_sdu_content = f.read()

    new_sdu_content = existing_sdu_content + append_content

    with open(sdu_master_file, "w") as f:
        f.write(new_sdu_content)
    print(f"Successfully consolidated {len(articles_to_consolidate)} articles into {sdu_master_file}")

    # 6. Delete individual files
    for filename in files_to_delete:
        try:
            os.remove(os.path.join(workspace_path, filename))
            print(f"Deleted individual article file: {filename}")
        except OSError as e:
            print(f"Error deleting file {filename}: {e}")

    # 7. Update DB article_status
    for sitename in consolidated_site_names:
        cursor.execute("UPDATE dive_sites SET article_status = 'Completed' WHERE name = ?", (sitename,))
    conn.commit()
    print(f"Updated article_status for {len(consolidated_site_names)} sites to 'Completed' in database.")

    conn.close()

if __name__ == "__main__":
    db_file = "dive_sites.db"
    consolidate_articles(db_file)
