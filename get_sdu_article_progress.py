
import sqlite3

def get_article_progress_and_last_site(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM dive_sites;")
    total_sites = cursor.fetchone()[0]

    # Count articles where article_status is explicitly 'Completed'
    cursor.execute("SELECT COUNT(*) FROM dive_sites WHERE article_status = 'Completed';")
    articles_completed = cursor.fetchone()[0]

    # Get the name of the last completed article based on ROWID, which often reflects insertion order
    cursor.execute("SELECT name FROM dive_sites WHERE article_status = 'Completed' ORDER BY ROWID DESC LIMIT 1;")
    last_completed_site_row = cursor.fetchone()
    last_completed_site = last_completed_site_row[0] if last_completed_site_row else "N/A"

    conn.close()
    return total_sites, articles_completed, last_completed_site

if __name__ == "__main__":
    db_file = "dive_sites.db"
    total, completed, last_site = get_article_progress_and_last_site(db_file)
    print(f"Total dive sites: {total}")
    print(f"Articles completed: {completed}")
    print(f"Last completed article: {last_site}")
