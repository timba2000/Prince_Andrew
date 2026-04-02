
import sqlite3
import os

def consolidate_and_cleanup_articles(db_path, sdu_master_file="SDU_dive_sites.md", workspace_path="."):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Get all dive site names from DB
    cursor.execute("SELECT name FROM dive_sites;")
    db_dive_site_names = {row[0] for row in cursor.fetchall()}
    print(f"DB Dive Site Names (Set): {db_dive_site_names}") # Debug print

    system_md_files = [
        "AGENTS.md", "BOOT.md", "BOOTSTRAP.md", "HEARTBEAT.md", "LICENSE",
        "MEMORY.md", "SOUL.md", "TOOLS.md", "USER.md", sdu_master_file
    ]

    individual_article_files = [
        "The Colours - Clovelly's Underwater Canvas of Vibrancy.md",
        "Smith Rock - Queensland's Formidable Underwater Landmark.md",
        "Whyalla Jetty - Witnessing the Cuttlefish Spectacle.md",
        "Kingscote Jetty - An Accessible Underwater Wonderland on Kangaroo Island.md",
        "North Bondi Bommie - Sydney's Underwater Gem.md",
        "Port Hughes Barge Wreck - A Sunken Gem of the Yorke Peninsula.md",
        "Weebubbie Cave - A Labyrinth of Limestone in the Nullarbor's Depths.md",
        "Henderson's Rock - A Sanctuary for Sharks in Queensland's Depths.md"
    ]

    append_buffer = []
    deleted_files_count = 0
    updated_db_status_count = 0

    # Process each identified individual article file
    for filename in individual_article_files:
        full_article_name = filename.replace(".md", "")
        # Extract core dive site name from the full article title (e.g., "The Colours")
        # Split at the first " - " and take the first part
        core_dive_site_name = full_article_name.split(" - ")[0]
        
        file_path = os.path.join(workspace_path, filename)
        
        print(f"Processing: {filename}") # Debug print
        print(f"  Full Article Name: {full_article_name}") # Debug print
        print(f"  Core Dive Site Name: {core_dive_site_name}") # Debug print
        print(f"  Does file exist? {os.path.exists(file_path)}") # Debug print
        print(f"  Is core dive site name in DB list? {core_dive_site_name in db_dive_site_names}") # Debug print

        if os.path.exists(file_path) and core_dive_site_name in db_dive_site_names:
            try:
                with open(file_path, "r") as f:
                    article_text = f.read()
                
                # Prepend heading and separator
                append_buffer.append(f"\n## {full_article_name}\n\n{article_text}\n\n***\n\n")
                
                # Delete individual file
                os.remove(file_path)
                print(f"Deleted individual article file: {filename}")
                deleted_files_count += 1
                
                # Update DB article_status using the core_dive_site_name
                cursor.execute("UPDATE dive_sites SET article_status = 'Completed' WHERE name = ?", (core_dive_site_name,))
                print(f"Updated article_status for '{core_dive_site_name}' to 'Completed' in database.")
                updated_db_status_count += 1

            except IOError as e:
                print(f"Error processing file {filename}: {e}")
            except sqlite3.Error as e:
                print(f"Error updating DB for {core_dive_site_name}: {e}")

    conn.commit()

    # Append all collected content to SDU_dive_sites.md
    if append_buffer:
        with open(sdu_master_file, "a") as f:
            f.write("".join(append_buffer))
        print(f"Appended {len(append_buffer)} articles to {sdu_master_file}")
    else:
        print("No new individual dive site articles found to append.")

    conn.close()
    print(f"Consolidation and cleanup complete. Deleted {deleted_files_count} files and updated {updated_db_status_count} DB entries.")

if __name__ == "__main__":
    db_file = "dive_sites.db"
    consolidate_and_cleanup_articles(db_file)
