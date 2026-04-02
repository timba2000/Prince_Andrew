
import sqlite3
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def update_article_in_db_and_combined_file(site_id, site_name, article_text, combined_file_path="dive_site_articles/SDU_dive_sites.md"):
    conn = None
    try:
        conn = sqlite3.connect('dive_sites.db')
        cursor = conn.cursor()

        # Update database
        cursor.execute(
            "UPDATE dive_sites SET article_status = ?, article_full_text = ? WHERE ID = ?",
            ('Completed', article_text, site_id)
        )
        conn.commit()
        print(f"Successfully updated article in DB for Site ID {site_id}.")

        # Append to the combined Markdown file
        target_dir = os.path.dirname(combined_file_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        with open(combined_file_path, 'a', encoding='utf-8') as outfile:
            outfile.write("\n\n---\n\n") # Separator for new articles
            outfile.write(article_text)
        print(f"Appended article for '{site_name}' to {combined_file_path}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except IOError as e:
        print(f"File I/O error: {e}")
    finally:
        if conn:
            conn.close()

# Article for Julian Rocks – Cod Hole (ID 166)
article_text_166 = """# Julian Rocks – Cod Hole: A Swim-Through Sanctuary for Intermediate Divers

Within the renowned Julian Rocks Marine Sanctuary off Byron Bay, New South Wales, lies the exhilarating Cod Hole—a must-visit swim-through for intermediate divers. Descending to depths between 10 and 22 metres, this specific site is celebrated for its unique geological formation and the impressive congregation of marine life it attracts, particularly large cod and pelagic species. The thrill of navigating the swim-through, combined with the promise of encountering diverse aquatic residents, makes Cod Hole a highlight of any Julian Rocks dive trip. Accessible by boat, it offers a focused and thrilling experience, showcasing a microcosm of the sanctuary's vibrant biodiversity.

The Essentials:
*   Depth Range: This intermediate dive takes you from 10 metres down to 22 metres, offering ample opportunity for exploration within the swim-through and surrounding areas.
*   Visibility: Renowned for its "Crystal Clear" waters. While Julian Rocks generally boasts excellent visibility (15-30m), Cod Hole often exceeds expectations. Visibility can experience some reduction from strong currents, heavy rainfall, and large swells. The site's specific conditions can be influenced by currents pushing through the swim-through, but generally, clear oceanic water prevails. Optimal conditions are almost always accessible, with large schools of fish often present in winter.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 26°C, making for pleasant diving year-round.
*   Current/Conditions: Divers can expect moderate to strong currents, especially on the northern side of the swim-through. Good finning skills and awareness of current direction are crucial. The site is part of the larger Julian Rocks system, exposed to ocean swells, but the swim-through offers a unique experience with specific current patterns.
*   Viz Implications: While often exceptional, strong currents can occasionally bring in nutrient-rich waters with plankton, or stirred sediment, temporarily affecting clarity. However, the inherent cleanliness of this oceanic site means significant impacts are less frequent.

Terrain & Navigation:
Cod Hole's primary feature is a spectacular swim-through, a natural tunnel carved into the volcanic rock. Navigation involves carefully entering and exiting this passage, which is typically wide enough for divers. The surrounding terrain includes rocky reefs and sandy patches where various creatures seek shelter. Good buoyancy control is essential to navigate the swim-through gracefully and avoid disturbing the delicate marine life within. The clear water, when present, aids significantly in navigation.

Marine Life Highlights:
As its name suggests, Cod Hole is famous for its large potato cod, which often reside within or near the swim-through, providing incredible photographic opportunities. Divers will also encounter impressive schools of snapper, various species of colourful reef fish, and majestic eagle rays gliding by the entrance. Keep an eye out for wobbegong sharks tucked under ledges, and a variety of smaller invertebrates clinging to the walls of the swim-through. The crystal-clear conditions often enhance these encounters.

Logistics & Facilities:
Access to Cod Hole is exclusively by boat, typically arranged through dive operators in Byron Bay. There are no on-site facilities directly at the dive site. The prime diving season is from October to April for warmer waters and peak marine activity. As part of a protected marine park, strict conservation guidelines apply; divers are expected to observe marine life responsibly and practice a "look but don't touch" policy, especially within the confines of the swim-through.

Who Is It For?:
This is an excellent site for **Intermediate** divers who are comfortable with swim-throughs, capable of handling moderate to strong currents, and adept at navigating reef systems. It offers a thrilling and rewarding experience for those seeking unique geological features and abundant marine encounters.

Pro-Tip:
Always check your gauge and remaining air pressure before entering the swim-through to ensure you have ample air to navigate through it safely and enjoy the marine life within. A well-maintained dive light will also illuminate the darker corners!

75-word excerpt:
Julian Rocks – Cod Hole, an intermediate swim-through dive in Byron Bay (10-22m), boasts "Crystal Clear" waters and large cod and pelagic species. Expect moderate to strong currents, with visibility potentially impacted by heavy rainfall or swells. Accessible by boat, it offers a thrilling geological feature and abundant marine life for divers comfortable with currents and swim-throughs, a highlight of Julian Rocks Marine Sanctuary."""

# Article for Julian Rocks – Hugo's Trench (ID 197)
article_text_197 = """# Julian Rocks – Hugo's Trench: A Dramatic Passage for Intermediate Divers

Another captivating jewel within Byron Bay's Julian Rocks Marine Sanctuary, Hugo's Trench offers an exhilarating and dramatic dive experience for intermediate divers. This narrow, distinctive trench, ranging in depth from 10 to 22 metres, is celebrated for its unique geological structure and the impressive encounters with reef sharks, rays, and groupers that frequent its depths. The trench's strong visibility and its reputation as a haven for larger marine life make it a thrilling and memorable dive. Accessible by boat, it promises an intimate glimpse into the powerful oceanic forces that shaped Julian Rocks and the resilient creatures that thrive within.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 10 metres to 22 metres, focusing on the trench and its immediate surroundings.
*   Visibility: Visibility typically ranges from 10 to 18 metres, known for its "strong visibility" on good days. Optimal clarity is generally experienced during spring and summer, particularly when conditions are calm and dry. However, visibility can be influenced by strong currents, large swells impacting the trench, and heavy rainfall. While generally excellent (15-30m for Julian Rocks as a whole), specific conditions within the trench can vary due to localised water movement. Strong currents can bring in plankton or stir up sediment.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 26°C, supporting vibrant marine activity.
*   Current/Conditions: Divers should be prepared for strong currents that can sweep through the narrow trench. Good finning technique and careful dive planning are essential. The site is exposed to ocean swells, and larger swells can create significant surge within the trench.
*   Viz Implications: Heavy rainfall and large swells are the primary factors that can reduce visibility by introducing sediment or creating turbid conditions. Strong currents can also influence clarity by keeping particles in suspension. Calm weather with minimal swell is ideal for the best visibility within the trench.

Terrain & Navigation:
Hugo's Trench is a dramatic, narrow geological feature, a deep cut in the reef. Navigation involves carefully following the trench's contours, being mindful of its enclosed nature and the potential for strong currents. The walls of the trench are adorned with a variety of invertebrate life, while the bottom is often sandy. Good buoyancy control is paramount to avoid contact with the trench walls and to safely observe the marine life. The clear water, when present, allows for excellent visual navigation.

Marine Life Highlights:
Hugo's Trench is a renowned spot for encounters with impressive marine predators. Divers frequently spot various species of reef sharks, including wobbegongs and, occasionally, grey nurse sharks, resting or patrolling the trench. Majestic rays, such as eagle rays, can be seen gliding through the passage. Large groupers often take shelter within its deeper sections. The narrow confines of the trench provide a unique vantage point for observing these larger species in a more intimate setting.

Logistics & Facilities:
Access to Hugo's Trench is exclusively by boat, typically organised through dive operators in Byron Bay. There are no on-site facilities directly at the dive site. The optimal diving season is during spring and summer (September to March) for warmer waters and peak marine encounters. As part of a protected marine park, strict conservation guidelines apply; divers are expected to observe marine life responsibly and avoid disturbing the delicate trench ecosystem.

Who Is It For?:
This is an excellent site for **Intermediate** divers who are comfortable with navigating narrow passages, capable of handling strong currents, and experienced in observing larger marine life. It offers a thrilling and unique experience for those seeking a more dramatic and challenging dive within Julian Rocks.

Pro-Tip:
When diving Hugo's Trench, try to time your dive during periods of slack tide to minimise the impact of strong currents, allowing for a more relaxed and extended exploration of this fascinating geological feature. Always keep an eye on your dive guide and maintain close proximity to your buddy.

75-word excerpt:
Julian Rocks – Hugo's Trench, an intermediate boat dive in Byron Bay (10-22m), is a narrow, dramatic passage known for reef sharks, rays, and groupers. Visibility (10-18m) is strong on calm days but influenced by currents, swells, and rainfall. This exhilarating trench offers a thrilling, intimate experience for capable divers comfortable with strong currents and close encounters with larger marine life."""

# Execute the updates for both IDs
update_article_in_db_and_combined_file(166, "Julian Rocks – Cod Hole", article_text_166)
update_article_in_db_and_combined_file(197, "Julian Rocks – Hugo's Trench", article_text_197)
