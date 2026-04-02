
import sqlite3
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def update_article_in_db_and_combined_file(site_ids, site_name, article_text, combined_file_path="dive_site_articles/SDU_dive_sites.md"):
    conn = None
    try:
        conn = sqlite3.connect('dive_sites.db')
        cursor = conn.cursor()

        # Update database for all provided site IDs
        for site_id in site_ids:
            cursor.execute(
                "UPDATE dive_sites SET article_status = ?, article_full_text = ? WHERE ID = ?",
                ('Completed', article_text, site_id)
            )
            print(f"Successfully updated article in DB for Site ID {site_id}.")
        conn.commit()

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

# Article for Julian Rocks / Julian Rocks Marine Sanctuary (IDs 3 and 240)
article_text_julian_rocks = """# Julian Rocks Marine Sanctuary: Byron Bay's Underwater Jewel for All Divers

Just 2.5 kilometres offshore from the iconic Byron Bay, New South Wales, lies the majestic Julian Rocks Marine Sanctuary—a world-class dive site nestled within the broader Cape Byron Marine Park. This ancient volcanic rock formation is a pulsating hub of marine life, offering an unparalleled underwater experience for divers of all levels. Plunging from 5 metres down to 35 metres, Julian Rocks is a vibrant intersection where tropical currents from the Great Barrier Reef meet the cooler temperate waters of Australia's south, fostering an extraordinary biodiversity of over 1,000 marine species. Year-round accessibility, primarily by boat, ensures that this aquatic wonderland remains a beloved destination for underwater photographers, marine enthusiasts, and curious divers alike.

The Essentials:
*   Depth Range: Catering to all skill levels, depths vary from a shallow 5 metres to a profound 35 metres.
*   Visibility: Generally excellent, ranging from 15 to 30 metres during calm conditions. However, visibility can be reduced after heavy rainfall, during periods of strong currents, or in the presence of large swells. Optimal conditions are typically experienced year-round, with the best clarity often found during periods of minimal coastal runoff and stable oceanic currents. Minimal coastal runoff from the nearby national park contributes to its overall clarity. Strong currents, particularly during tidal changes, can bring in plankton or sediment, temporarily affecting visibility.
*   Water Temperature: Water temperatures range from a comfortable 18°C in cooler months to a warm 24°C during summer, accommodating year-round diving.
*   Current/Conditions: Divers can expect anything from mild to seasonally strong currents, necessitating good finning skills and careful planning. Boat traffic is also a consideration given its popularity. The site is exposed to ocean swells, so conditions can vary.
*   Viz Implications: Heavy rainfall, strong currents, and large swells are the primary factors affecting visibility. Diving during calm weather and avoiding periods of heavy rain will ensure the best possible clarity.

Terrain & Navigation:
Julian Rocks is a spectacular labyrinth of underwater formations, including walls, caves, gutters, and bommies. The volcanic rock creates dramatic swim-throughs and overhangs that are heavily encrusted with soft corals, sponges, and anemones. Navigation is generally intuitive, following the contours of the main rock formations, but dive guides are highly recommended for new visitors to explore the best features. Iconic spots like "The Nursery," "Cod Hole," and "Hugo's Trench" offer distinct environments to explore. The diverse topography provides endless opportunities for discovery, from wide-angle vistas to intricate macro details.

Marine Life Highlights:
Julian Rocks is an absolute paradise for marine life. It's world-renowned for its aggregations of grey nurse sharks (during winter) and the graceful leopard sharks (in summer), often found resting on the sandy bottom. Divers will also be treated to frequent encounters with various species of turtles (green, loggerhead, hawksbill), majestic manta rays gliding effortlessly, and a dazzling array of tropical and temperate reef fish. Moray eels peer from crevices, while schools of trevally and barracuda cruise the deeper sections. The sheer diversity of life here is breathtaking, making every dive a unique experience.

Logistics & Facilities:
Access to Julian Rocks is predominantly by boat, with numerous reputable dive operators departing from Byron Bay. While shore dives are technically possible for some parts of the wider marine park, the primary rock formations are boat access only. Excellent beach amenities are available in Byron Bay. The site is diveable year-round, but specific seasonal highlights (e.g., sharks) may influence timing. As a protected marine sanctuary, strict conservation guidelines apply; divers are expected to observe marine life responsibly and practice a "look but don't touch" policy, respecting the delicate ecosystem.

Who Is It For?:
Julian Rocks Marine Sanctuary truly caters to **All Levels** of divers. Beginners can enjoy the shallower, more protected areas teeming with life, while intermediate and advanced divers can explore deeper sections, navigate stronger currents, and seek out specific large marine encounters. It's also a phenomenal site for underwater photographers.

Pro-Tip:
Consider diving Julian Rocks at different times of the year to experience its full marine diversity. Winter brings grey nurse sharks, while summer is excellent for leopard sharks and manta rays. Each season offers a unique spectacle!

75-word excerpt:
Julian Rocks Marine Sanctuary, off Byron Bay (5-35m), is a world-class site for all divers. Excellent visibility (15-30m) is influenced by currents/rainfall. It boasts over 1,000 species, including grey nurse/leopard sharks, turtles, and rays, where tropical and temperate waters meet. Accessible year-round by boat, it offers diverse terrain and rich biodiversity, a true underwater jewel."""

# Execute the updates for both IDs
update_article_in_db_and_combined_file([3, 240], "Julian Rocks Marine Sanctuary", article_text_julian_rocks)
