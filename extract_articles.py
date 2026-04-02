
import sqlite3
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def extract_articles_to_markdown(db_path="dive_sites.db", output_dir="dive_site_articles"):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT ID, Name, article_full_text FROM dive_sites WHERE article_status = 'Completed' AND article_full_text IS NOT NULL")
        articles = cursor.fetchall()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for site_id, site_name, article_content in articles:
            # Generate a slug from the site name
            file_slug = slugify(site_name)
            file_name = f"{file_slug}.md"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(article_content)
            print(f"Extracted article for '{site_name}' to {file_path}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except IOError as e:
        print(f"File I/O error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    extract_articles_to_markdown()
