
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

# Article for Julian Rocks – The Nursery (ID 165)
article_text_165 = """# Julian Rocks – The Nursery: A Protected Haven for Beginner Divers

Within the breathtaking expanse of Julian Rocks Marine Sanctuary, just off Byron Bay, New South Wales, lies a truly special site known as The Nursery. This sheltered haven, with depths ranging from a shallow 5 metres to 12 metres, is ideally suited for beginner divers, offering a serene and protected environment where marine life thrives. It’s a remarkable spot to encounter graceful turtles, the fascinating wobbegong sharks, and various rays in a calm setting. Accessible by boat, The Nursery provides a gentle introduction to the wonders of Julian Rocks, showcasing a rich tapestry of biodiversity in its sheltered waters, all while adhering to strict marine park regulations.

The Essentials:
*   Depth Range: A beginner-friendly depth range from 5 metres down to 12 metres, making it ideal for extended bottom times and relaxed exploration.
*   Visibility: Generally excellent, typically ranging from 10 to 15 metres. As part of Julian Rocks Marine Sanctuary, visibility can range from 15-30m during calm conditions, but can be reduced after heavy rainfall, during strong currents, or in the presence of large swells. Optimal clarity is often found from October to April when conditions are generally calmer. Minimal coastal runoff from the nearby national park helps maintain good water quality. Strong currents can bring in plankton or stirred sediment.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 26°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: This site is specifically noted for being sheltered, making it suitable for beginners. However, divers should still be mindful of boat traffic within the marine park. While generally calm, strong currents and large swells affecting other parts of Julian Rocks can have some influence.
*   Viz Implications: Heavy rainfall, strong currents, and large swells are the primary factors affecting visibility. Despite being sheltered, local conditions can still be influenced by broader oceanic dynamics. Calm, dry periods are ideal for the best experience.

Terrain & Navigation:
The Nursery features a varied terrain of rocky bommies and reef patches, interspersed with sandy channels. Navigation is straightforward due to the shallow depths and the sheltered nature of the site, allowing divers to leisurely explore the various formations. The reef structures are adorned with soft corals and sponges, creating numerous hiding spots for marine life. The clear water, when present, aids significantly in orientation and allows for easy observation.

Marine Life Highlights:
As its name suggests, The Nursery is a fantastic spot to observe a wide array of marine life. Divers frequently encounter green and loggerhead turtles, often resting or feeding. Wobbegong sharks, masters of camouflage, can be spotted nestled under ledges. Various species of rays gracefully cruise the sandy areas. The site is a haven for schooling fish, and a diverse range of nudibranchs and smaller invertebrates can be found meticulously crawling across the reef. It’s an ideal location for macro photography.

Logistics & Facilities:
Access to The Nursery is exclusively by boat, typically arranged through authorised dive operators in Byron Bay. There are no on-site facilities directly at the dive site. The optimal diving season is between October and April for warmer waters and peak marine activity. As a protected marine park, strict conservation rules apply; divers must adhere to all regulations, including no-touch policies and responsible interaction with marine life, especially in this sensitive nursery habitat.

Who Is It For?:
This site is perfectly suited for **Beginner** divers and those seeking a relaxed, abundant marine encounter. Its sheltered conditions and accessible depths make it ideal for introductory dives, refresher courses, and underwater photography where calm conditions are preferred.

Pro-Tip:
Spend time patiently observing the sandy patches around the reef structures in The Nursery. Many camouflaged creatures, like flatheads and various rays, are adept at blending in and reveal themselves to the attentive diver.

75-word excerpt:
Julian Rocks – The Nursery, a beginner-friendly boat dive in Byron Bay (5-12m), is a sheltered haven within Julian Rocks Marine Sanctuary. Visibility (10-15m) is generally excellent but can be reduced by rainfall or strong currents. It's teeming with turtles, wobbegongs, and rays, offering a serene introduction to the sanctuary's rich biodiversity under strict marine park rules. Ideal for relaxed marine encounters."""

# Article for Clovelly Pool (ID 49)
article_text_49 = """# Clovelly Pool: Sydney's Accessible Marine Sanctuary for Beginners

Nestled along Sydney's eastern coastline, Clovelly Pool in Clovelly, New South Wales, offers an unparalleled and highly accessible dive experience for beginner divers and snorkelers. This naturally formed, calm, and sheltered ocean pool, with depths ranging from 2 to 5 metres, is a local treasure, renowned for its resident blue gropers and abundant schooling fish. Its year-round accessibility, coupled with convenient beach amenities, makes it a perfect entry point for those new to the underwater world or seeking a relaxed and richly rewarding experience without venturing far offshore. Clovelly Pool is a vibrant marine sanctuary, a cherished spot where urban convenience meets astonishing biodiversity.

The Essentials:
*   Depth Range: An ideal beginner depth range of 2 to 5 metres, perfect for building confidence and observing marine life up close.
*   Visibility: Generally good, ranging from 5 to 8 metres, extending to 15 metres on exceptionally clear days. Visibility is best year-round, particularly during calm, dry periods. However, divers should be aware of urban stormwater runoff from surrounding residential areas, which, after heavy rainfall, can significantly reduce clarity. Strong easterly swells can also stir up sediment, and high bather numbers can sometimes affect water clarity. Optimal conditions are found on calm days with minimal swell.
*   Water Temperature: Water temperatures are comfortable, ranging from 17°C in cooler months to a pleasant 23°C in summer, supporting year-round diving.
*   Current/Conditions: The pool area is exceptionally calm and sheltered, making it very safe for beginners. There is limited depth, but minimal currents or surge, making it a truly relaxing experience. While shielded from open ocean conditions, very strong easterly swells might still cause some agitation at the entrance.
*   Viz Implications: Heavy rainfall leading to urban stormwater runoff is the primary factor that can significantly reduce visibility. Strong easterly swells can also decrease clarity by stirring up sand. Avoiding diving after heavy rain or during very rough ocean conditions will ensure the best visibility.

Terrain & Navigation:
Clovelly Pool features a sandy bottom transitioning to rocky edges and a concrete promenade that encloses the area. The natural rock formations within the pool provide ample shelter for marine life. Navigation is incredibly easy due to the enclosed nature of the site and its shallow depths. Divers can leisurely explore the entire area, following the rock formations or simply observing the marine life in the sandy patches. The clear water, when present, allows for excellent visual navigation and observation.

Marine Life Highlights:
This accessible sanctuary is a hotspot for fascinating marine encounters. Clovelly Pool is most famous for its resident blue gropers, often seen curiously interacting with divers. Divers will also encounter schools of bream and various species of wrasse darting amongst the rocks and over the sandy bottom. Keep an eye out for octopus, cuttlefish, and an array of smaller invertebrates. The sheltered conditions make it an ideal environment for observing juvenile fish and macro life in detail.

Logistics & Facilities:
Clovelly Pool offers unparalleled accessibility with easy entry from the beach/promenade area. Excellent facilities are available, including change rooms, toilets, and ample (though often busy) parking. The site is diveable year-round, with consistently calm conditions making it a reliable choice. Conservation is important here, and divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the natural and artificial structures.

Who Is It For?:
This is an ideal site for **Beginner** divers and snorkelers, as well as families and those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, friendly marine life make it perfect for introductory dives, training, and peaceful underwater photography.

Pro-Tip:
To truly appreciate the marine life, particularly the blue gropers, try to dive during weekdays or early mornings to avoid peak crowds. Moving slowly and observing patiently will reward you with closer encounters with the pool's fascinating residents.

75-word excerpt:
Clovelly Pool, Sydney (2-5m), is a beginner-friendly, sheltered ocean pool renowned for resident blue gropers and schooling fish. Visibility (5-15m) is best year-round in calm, dry periods but affected by urban runoff and easterly swells. Easily accessible with amenities, it offers a safe, vibrant marine sanctuary perfect for introductory dives, photography, and relaxed underwater exploration near Sydney's coastline."""

# Execute the updates for both IDs
update_article_in_db_and_combined_file(165, "Julian Rocks – The Nursery", article_text_165)
update_article_in_db_and_combined_file(49, "Clovelly Pool", article_text_49)
