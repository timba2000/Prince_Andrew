
import os
import re
import hashlib

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def combine_and_deduplicate_articles(
    source_dir="sdu_articles",
    target_file_path="dive_site_articles/SDU_dive_sites.md"
):
    combined_content = []
    seen_hashes = set()
    
    # Ensure the target directory exists
    target_dir = os.path.dirname(target_file_path)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate through each markdown file in the source directory
    for filename in sorted(os.listdir(source_dir)):
        if filename.endswith(".md"):
            file_path = os.path.join(source_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                article_content = f.read()
            
            # Simple deduplication based on content hash
            content_hash = hashlib.md5(article_content.encode('utf-8')).hexdigest()
            if content_hash not in seen_hashes:
                combined_content.append(article_content)
                seen_hashes.add(content_hash)
                print(f"Added '{filename}' to combined file.")
            else:
                print(f"Skipped duplicate article: '{filename}'")

            # Delete the individual markdown file after processing
            os.remove(file_path)
            print(f"Deleted individual article file: '{filename}'")

    # Write the combined content to the target file
    with open(target_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write("\n\n---\n\n".join(combined_content))
    print(f"Successfully combined and deduplicated articles into {target_file_path}")

if __name__ == "__main__":
    combine_and_deduplicate_articles()
