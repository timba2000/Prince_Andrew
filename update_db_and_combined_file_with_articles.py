
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

# Article for Fishery Bay Reef (ID 123)
article_text_123 = """# Fishery Bay Reef: Eyre Peninsula's Scenic Gullies and Bommies for Intermediate Divers

Off the stunning coastline of the Eyre Peninsula, South Australia, Fishery Bay Reef presents a captivating and scenic dive site, ideally suited for intermediate divers. Descending to depths between 5 to 14 metres, this expansive reef is renowned for its intricate gullies, impressive bommies, and vibrant, colourful sponges. Accessible primarily by boat, Fishery Bay Reef offers a dynamic underwater landscape, showcasing a rich diversity of temperate marine species. It’s an inviting site for those seeking engaging encounters with wrasse, graceful rays, and intriguing sea cucumbers against a backdrop of unique geological formations, particularly during the prime season of October to March.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 5 to 14 metres, offering a good vertical range along the reef.
*   Visibility: Variable, typically ranging from 10 to 14 metres, but can extend to 15 metres on exceptionally clear days. Optimal visibility is generally found between October and March, particularly during calm periods. As an oceanic site, visibility is largely influenced by strong southerly swells, strong currents, and high winds, which can create very turbulent and murky conditions. Minimal coastal runoff from the natural coastline contributes to overall clarity. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures range from a cool 14°C in winter to a more moderate 20°C in summer.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. Surge can also be significant, particularly during larger southerly swells. This is a boat-only dive, requiring careful planning and execution. Awareness of boat traffic in the area is also wise.
*   Viz Implications: Strong southerly swells, strong currents, and high winds are the primary factors in reducing visibility, creating turbulent and murky conditions. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Fishery Bay Reef features a dynamic rocky reef terrain with numerous intricate gullies, impressive bommies, and sand patches. The reef structures are heavily adorned with a variety of colourful sponges, soft corals, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef contours. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive. Boat ramp access is nearby.

Marine Life Highlights:
This vibrant reef is home to an incredible array of marine life. Divers can expect frequent encounters with various species of colourful wrasse, gracefully navigating the coral gardens. Graceful rays, including stingrays and eagle rays, are often spotted cruising over the sandy bottom. Intriguing sea cucumbers can be found meticulously crawling across the reef. Keep an eye out for inquisitive blue gropers, wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the sponges. The healthy ecosystem supports diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Fishery Bay Reef is exclusively by boat, typically arranged through dive charter operators from nearby ports on the Eyre Peninsula. A boat ramp is conveniently located nearby for private vessels. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is from October to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents and surge, and adept at navigating reef systems. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the scenic nature of the reef, take your time to explore the gullies and bommies. These areas often provide excellent photographic opportunities, particularly for wide-angle shots showcasing the vibrant sponges and schooling fish. Always check local weather and swell forecasts before heading out.

75-word excerpt:
Fishery Bay Reef, Eyre Peninsula (5-14m), is an intermediate boat dive with scenic gullies, bommies, and vibrant sponges. Visibility (10-14m) is best October-March during calm periods, but impacted by southerly swells and strong currents. It hosts wrasse, rays, and sea cucumbers. This dynamic site demands moderate current/surge handling for a rewarding exploration of its unique geological formations and rich marine life off South Australia's coast."""

# Execute the update for the ID
update_article_in_db_and_combined_file(123, "Fishery Bay Reef", article_text_123)
