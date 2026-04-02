
import re
import os

def deduplicate_sdu_articles(sdu_master_file="SDU_dive_sites.md"):
    if not os.path.exists(sdu_master_file):
        print(f"Error: {sdu_master_file} not found.")
        return

    with open(sdu_master_file, "r") as f:
        content = f.read()

    # Use a regex to find all articles, assuming each starts with '## [Dive Site Name]' and ends with '***' or end of file
    # This regex is an approximation and might need refinement based on exact formatting
    article_pattern = re.compile(r'(## .*?\n.*?)(?:\n\n\*\*\*\n\n|\Z)', re.DOTALL)
    
    # Find all matches (articles)
    matches = article_pattern.findall(content)

    # Use a dictionary to store unique articles, keyed by the dive site name
    # Keeping the last seen article if duplicates are present
    unique_articles = {}
    for match in matches:
        # Extract the heading to use as a key
        heading_match = re.search(r'## (.*?)\n', match)
        if heading_match:
            title = heading_match.group(1).strip()
            unique_articles[title] = match # Store the entire article content
        else:
            # If an article has no proper heading, it's an anomaly, just append it
            print(f"Warning: Article found without a proper heading: {match[:50]}...")
            unique_articles[f"Anomaly_{len(unique_articles)}"] = match

    # Reconstruct the content from unique articles
    new_content_parts = []
    for title, article_content in unique_articles.items():
        new_content_parts.append(article_content.strip())
        new_content_parts.append("\n\n***\n\n") # Add separator after each article

    # Join and write back to the file
    final_content = "".join(new_content_parts).strip()

    with open(sdu_master_file, "w") as f:
        f.write(final_content)
    print(f"Successfully deduplicated {sdu_master_file}. Kept {len(unique_articles)} unique articles.")

if __name__ == "__main__":
    deduplicate_sdu_articles()
