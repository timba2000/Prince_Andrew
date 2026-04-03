
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

# Article for Split Solitary Island (ID 178)
article_text_178 = """# Split Solitary Island: A Coral and Fish Wonderland for Intermediate Divers

Off the stunning coastline of Coffs Harbour, New South Wales, lies Split Solitary Island, a captivating dive site perfect for intermediate divers. Ranging in depth from 8 to 20 metres, this island is renowned for its distinctive split reef structure, vibrant coral formations, and abundant fish life. Accessible primarily by boat, Split Solitary Island offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species. It’s a jewel within the Solitary Islands Marine Park, promising engaging dives with impressive biodiversity and healthy ecosystems for those seeking a memorable exploration.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 8 to 20 metres, offering a good vertical range along the reef.
*   Visibility: Consistently excellent year-round, typically ranging from 20 to 40 metres. However, divers may experience seasonal thermoclines and plankton events in warmer months, which can slightly reduce clarity. Given its minimal coastal runoff from the natural island environment, visibility is largely influenced by strong oceanic currents, localised plankton blooms, and offshore weather systems. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 19°C to 25°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers can expect moderate to strong oceanic currents, requiring good finning technique and careful dive planning. The site is generally exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive.
*   Viz Implications: While generally superb, strong oceanic currents can bring in nutrient-rich waters that may, at times, foster plankton blooms, temporarily affecting visibility. Offshore weather systems, particularly during significant swells, can also introduce suspended particles.

Terrain & Navigation:
Split Solitary Island is characterized by its distinctive split reef structure, with impressive coral formations covering vast areas. The terrain includes rocky outcrops, sand channels, and gentle slopes adorned with hard and soft corals. Navigation is relatively straightforward, following the reef's contours around the island. Divers will find numerous ledges, gutters, and small caves to explore, providing ample hiding spots for marine life. The clear water typically allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This site is a haven for an incredible variety of marine life. Divers can expect frequent encounters with large schools of morwong and various species of leatherjackets, gracefully navigating the coral gardens. Colourful parrotfish are abundant, grazing on the reef. Keep an eye out for inquisitive blue groupers, wobbegong sharks tucked away under ledges, and a dazzling array of tropical and temperate reef fish. The healthy coral ecosystems support diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Split Solitary Island is exclusively by boat, typically arranged through dive charter operators in Coffs Harbour. There are no on-site facilities, so divers must be self-sufficient. The optimal diving season is between October and March for warmer waters and peak marine activity. As part of a protected marine park, strict conservation guidelines apply; divers are expected to observe marine life responsibly without touching or disturbing the delicate ecosystem.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate to strong currents, and adept at navigating reef systems. It's an excellent site for those looking to expand their experience in a pristine and dynamic environment.

Pro-Tip:
Due to the consistent excellent visibility and vibrant colours, Split Solitary Island is a fantastic site for wide-angle underwater photography. Consider bringing a strobed setup to capture the full beauty of its coral gardens and fish schools.

75-word excerpt:
Split Solitary Island, off Coffs Harbour (8-20m), is an intermediate boat dive with a distinctive split reef, vibrant corals, and abundant fish life. Consistently excellent visibility (20-40m) is influenced by oceanic currents and plankton. It hosts morwong, leatherjackets, and parrotfish, offering a dynamic exploration within the Solitary Islands Marine Park for capable divers seeking impressive biodiversity and healthy ecosystems."""

# Article for The Looking Glass – South Solitary Island (ID 175)
article_text_175 = """# The Looking Glass – South Solitary Island: A Thrilling Swim-Through for Intermediate Divers

South of Coffs Harbour, New South Wales, within the renowned Solitary Islands Marine Park, lies "The Looking Glass"—a truly spectacular dive site at South Solitary Island, ideal for intermediate divers. This famous swim-through, located between dramatic vertical rock walls and descending to depths of 10 to 22 metres, offers an exhilarating journey. It’s renowned for its impressive encounters with grey nurse sharks and wobbegongs, making it a thrilling adventure. Accessible solely by boat, The Looking Glass promises an unforgettable exploration into one of Australia’s most biologically rich underwater passages, where geological grandeur meets vibrant marine biodiversity in consistently excellent visibility.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 10 metres to 22 metres, primarily within and around the swim-through.
*   Visibility: Consistently excellent year-round, typically ranging from 20 to 40 metres. However, divers may experience seasonal thermoclines and plankton events in warmer months, which can slightly reduce clarity. Given its minimal coastal runoff from the natural island environment, visibility is largely influenced by strong oceanic currents, localised plankton blooms, and offshore weather systems. Calm conditions are generally best for uninhibited views within the dramatic swim-through.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 19°C to 25°C, making for pleasant diving conditions throughout the prime season (Spring–Autumn).
*   Current/Conditions: Divers can expect moderate to strong currents, particularly when navigating the swim-through. Good finning technique, excellent buoyancy control, and careful dive planning are essential. The site is exposed to ocean swells, and surge can be significant, especially at the entrances of the swim-through.
*   Viz Implications: While generally superb, strong oceanic currents can bring in nutrient-rich waters that may, at times, foster plankton blooms, temporarily affecting visibility. Offshore weather systems, particularly during significant swells, can also introduce suspended particles, making the swim-through more challenging.

Terrain & Navigation:
The Looking Glass is defined by its unique geological feature: a prominent swim-through carved between towering vertical rock walls. Navigation involves carefully entering and exiting this passage, which can be narrow in sections. The surrounding terrain includes rocky reefs and sandy channels adorned with corals and sponges. Excellent buoyancy control is critical for navigating the swim-through safely and avoiding contact with the walls or the silty bottom. The clear water, when present, greatly assists in navigation, but awareness of current is paramount.

Marine Life Highlights:
This site is famous for its aggregations of impressive marine life, particularly its resident grey nurse sharks, which are often seen cruising through or resting within the swim-through during certain seasons. Divers will also encounter wobbegong sharks tucked into crevices, various species of reef fish, and occasionally larger pelagics in the surrounding waters. The dramatic rock formations themselves host a vibrant array of invertebrates, making for a visually rich experience.

Logistics & Facilities:
Access to The Looking Glass is exclusively by boat, typically arranged through dive charter operators in Coffs Harbour. There are no on-site facilities directly at the dive site. The optimal diving season is from spring to autumn (September to May) for warmer waters and peak marine activity. As part of a protected marine park, strict conservation guidelines apply; divers are expected to observe marine life responsibly and practice a "look but don't touch" policy, especially within the confined spaces of the swim-through.

Who Is It For?:
This is an excellent site for **Intermediate** divers who are comfortable with swim-throughs, capable of handling moderate to strong currents, and adept at navigating reef systems with challenging features. It offers a thrilling and memorable experience for those seeking unique geological features and encounters with impressive marine life.

Pro-Tip:
Due to the presence of grey nurse sharks and the nature of the swim-through, maintain calm, slow movements to avoid disturbing the sharks. Carrying a powerful dive light will enhance your experience, illuminating the darker corners and revealing hidden details within the swim-through.

75-word excerpt:
"The Looking Glass" at South Solitary Island, Coffs Harbour (10-22m), is an intermediate boat dive featuring a famous swim-through between vertical walls. Consistently excellent visibility (20-40m) is influenced by oceanic currents and plankton. It's renowned for grey nurse sharks and wobbegongs, offering a thrilling geological and wildlife experience for capable divers within the Solitary Islands Marine Park. Requires excellent buoyancy and current management."""

# Execute the updates for both IDs
update_article_in_db_and_combined_file(178, "Split Solitary Island", article_text_178)
update_article_in_db_and_combined_file(175, "The Looking Glass – South Solitary Island", article_text_175)
