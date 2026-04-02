
import sqlite3
import re
import os

def migrate_sdu_articles_to_db(db_path="dive_sites.db", sdu_master_file="SDU_dive_sites.md"):
    if not os.path.exists(sdu_master_file):
        print(f"Error: {sdu_master_file} not found. No articles to migrate.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read the master Markdown file content
    with open(sdu_master_file, "r") as f:
        content = f.read()

    # Regex to split the Markdown file into individual articles.
    # Articles are assumed to start with ## or ### and are separated by '***'
    # The regex non-greedily matches everything until the next '***' or end of string.
    # Using a negative lookahead to ensure we don't split in the middle of a title line.
    article_sections = re.split(r'\n\*\*\*\n', content)

    migrated_count = 0
    for section in article_sections:
        section = section.strip()
        if not section:
            continue

        # Extract the title. Handles ## Title: Subtitle or ### Title - Subtitle
        title_match = re.search(r'^(?:#){2,3}\s*(.*?)\n', section, re.MULTILINE)
        
        if title_match:
            full_article_title_line = title_match.group(1).strip()
            # Extract core dive site name by splitting at the first ':' or ' - '
            # This is crucial for matching with the 'Name' column in the DB
            core_dive_site_name = full_article_title_line.split(' : ')[0].split(' - ')[0].strip()
            
            # Clean up content to remove the heading used for parsing
            article_content = re.sub(r'^(?:#){2,3}\s*.*?\n', '', section, count=1, flags=re.MULTILINE).strip()

            try:
                # Check if the dive site exists and update it
                cursor.execute("UPDATE dive_sites SET article_status = 'Completed', article_full_text = ? WHERE name = ?", 
                               (article_content, core_dive_site_name))
                
                if cursor.rowcount > 0:
                    migrated_count += 1
                    print(f"Migrated article for '{core_dive_site_name}' and updated DB.")
                else:
                    print(f"Warning: No matching dive site found in DB for article: '{core_dive_site_name}'. Article not migrated.")

            except sqlite3.Error as e:
                print(f"Error migrating article '{core_dive_site_name}' to DB: {e}")
        else:
            print(f"Warning: Could not extract title from article section (first 50 chars): {section[:50]}...")

    conn.commit()
    conn.close()

    # Delete the SDU_dive_sites.md file after successful migration
    try:
        os.remove(sdu_master_file)
        print(f"Successfully deleted {sdu_master_file}.")
    except OSError as e:
        print(f"Error deleting {sdu_master_file}: {e}")

    print(f"Migration complete. Migrated {migrated_count} articles to the database.")

if __name__ == "__main__":
    migrate_sdu_articles_to_db()
