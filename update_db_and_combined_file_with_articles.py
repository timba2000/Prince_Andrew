
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

# Article for Latitude Rock (ID 188)
article_text_188 = """# Latitude Rock: Forster's Dramatic Reef Wall for Intermediate Divers

Off the picturesque coastline of Forster, New South Wales, Latitude Rock stands as a dramatic and exhilarating dive site, perfectly suited for intermediate divers. Descending to depths between 10 and 20 metres, this site is renowned for its steep reef wall, impressive bommies, and generally good visibility, making it a vibrant hub of marine activity. Accessible exclusively by boat, Latitude Rock offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species. It’s an inviting site for those seeking engaging encounters with moray eels, snapper, and gropers against a backdrop of unique geological formations in the dry season.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 10 to 20 metres, offering a significant vertical profile along the reef wall.
*   Visibility: Generally good, typically ranging from 12 to 18 metres. The dry season is often cited as optimal. As an oceanic site, visibility is largely influenced by strong oceanic currents and offshore weather systems. While typically good year-round, it can experience seasonal thermoclines and plankton events in warmer months. There's no specific coastal runoff information, implying oceanic influences are paramount. Divers should anticipate that strong currents can bring in plankton or stir up sediment, temporarily affecting clarity. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 18°C to 24°C, making for pleasant diving conditions throughout the prime dry season.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. The site is exposed to boat traffic, so caution is advised. While generally good, strong oceanic currents and offshore weather systems are the main external influences.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary factors in reducing visibility. Planning dives during calm, dry periods will ensure the best possible clarity and an enjoyable experience.

Terrain & Navigation:
Latitude Rock features a steep reef wall, characterised by impressive bommies and ledges that plunge into deeper sections. The reef structures are heavily adorned with a variety of soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef wall's contours. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant reef is home to a diverse array of marine life. Divers frequently encounter inquisitive moray eels peering from rocky crevices and large schools of snapper patrolling the reef. Impressive gropers often take shelter in the larger reef structures. Keep an eye out for various species of colourful reef fish, wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the soft corals. The healthy ecosystem supports diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Latitude Rock is exclusively by boat, typically arranged through dive charter operators in Forster. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is during the dry season (typically autumn to spring) for calmer weather and generally better visibility. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents, and adept at navigating reef systems with challenging features. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the steepness of the reef wall and potential for currents, ensure you maintain excellent buoyancy control. This will allow you to hover effortlessly along the wall and fully appreciate the marine life without physical exertion or damaging the delicate corals.

75-word excerpt:
Latitude Rock, Forster (10-20m), is an intermediate boat dive with a steep reef wall and bommies, offering good visibility (12-18m) during the dry season. It hosts moray eels, snapper, and gropers. Influenced by oceanic currents, it demands careful navigation and good buoyancy for an exhilarating exploration of its dramatic geological formations and rich marine life off the New South Wales coast."""

# Article for Mullaway Reef (ID 207)
article_text_207 = """# Mullaway Reef: A Vibrant Bommie Reef for Intermediate Divers

Off the serene coastline of Mullaway, New South Wales, Mullaway Reef offers a captivating and colourful dive site, ideally suited for intermediate divers. Ranging in depth from 6 to 14 metres, this bommie reef is celebrated for its impressive hard coral growth, bustling fish life, and frequent encounters with graceful turtles. Accessible primarily by boat, Mullaway Reef offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species. It’s an inviting site for those seeking engaging encounters with parrotfish, moray eels, and diverse reef life against a backdrop of healthy coral ecosystems during the spring and autumn seasons.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 6 to 14 metres, offering a good vertical range around the bommies.
*   Visibility: Generally good, typically ranging from 10 to 15 metres. Optimal visibility is often found during spring and autumn. As an oceanic site, visibility is largely influenced by oceanic conditions. However, it can be reduced by swell, particularly strong easterly swells, which can stir up sediment. Localised plankton blooms can also occur in warmer months. Calm days are generally best for uninhibited views. There's no specific coastal runoff information, implying oceanic influences are paramount.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 19°C to 25°C, making for pleasant diving conditions throughout the prime seasons.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. The site is exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive. Boat traffic in the area also requires caution.
*   Viz Implications: Swell, particularly strong easterly swells, is the primary factor in reducing visibility by stirring up sediment. Strong oceanic currents and localised plankton blooms can also contribute. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Mullaway Reef features a bommie reef terrain with numerous individual coral heads and rocky outcrops. These structures are heavily adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, circling the bommies and exploring the gutters and channels between them. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant reef is home to an incredible array of marine life. Divers can expect frequent encounters with graceful green and loggerhead turtles, often seen cruising along the reef. Large schools of colourful parrotfish are abundant, grazing on the corals. Inquisitive moray eels peer from rocky crevices, while various species of wrasse and surgeonfish add splashes of colour. Keep an eye out for wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the corals. The healthy hard coral ecosystems support diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Mullaway Reef is exclusively by boat, typically arranged through dive charter operators in nearby towns like Woolgoolga or Coffs Harbour. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is during spring and autumn (September to May) for warmer waters and peak marine activity, coinciding with generally calmer weather. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate coral ecosystems and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents, and adept at navigating reef systems with challenging features. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the beautiful hard coral growth, take extra care with your buoyancy to avoid accidental contact. Carry a macro lens if you're a photographer, as the reef offers fantastic opportunities for capturing intricate details of small invertebrates and colourful fish.

75-word excerpt:
Mullaway Reef, Mullaway (6-14m), is an intermediate boat dive featuring vibrant hard coral bommies. Visibility (10-15m) is best in spring/autumn, influenced by swell and oceanic currents. It hosts turtles, parrotfish, and moray eels. This dynamic site demands moderate current handling and good buoyancy, offering rich biodiversity for capable divers. Access is by boat, with no on-site facilities, ideal for engaging encounters in a healthy coral ecosystem."""

# Article for Woody Head Reef (ID 210)
article_text_210 = """# Woody Head Reef: Iluka's Macro Paradise for Intermediate Shore Divers

Nestled near the scenic campground at Woody Head, Iluka, New South Wales, Woody Head Reef offers a captivating and accessible shore dive, ideally suited for intermediate divers. With shallow depths ranging from 4 to 10 metres, this rocky reef is a macro spotting paradise, famous for its intricate details and the diverse small marine life it harbours. Its easy shore access makes it an ideal spot for relaxed explorations during spring and autumn, revealing a hidden world of fascinating nudibranchs, colourful cowfish, and elusive small rays. Woody Head Reef is a cherished local treasure, a vibrant aquatic microcosm where natural beauty meets abundant and friendly macro life, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: This intermediate dive explores shallow depths from 4 to 10 metres, perfect for extended bottom times and macro photography.
*   Visibility: Typically ranges from 6 to 10 metres. Optimal visibility is generally found during spring and autumn. As a coastal site, visibility can be influenced by swell and coastal runoff. Strong easterly swells can stir up sediment, reducing clarity. Localised plankton blooms can also occur in warmer months. Calm days are generally best for uninhibited views. Moderate coastal runoff from the surrounding natural areas can temporarily reduce clarity after significant rainfall.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 19°C to 25°C, making for pleasant diving conditions throughout the prime seasons.
*   Current/Conditions: Divers can expect gentle to moderate currents, especially on incoming tides. The site is exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive. Shore access makes it relatively easy, but awareness of local conditions is wise.
*   Viz Implications: Swell, particularly strong easterly swells, is the primary factor in reducing visibility by stirring up sediment. Strong currents and localised plankton blooms can also contribute. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Woody Head Reef features a rugged rocky reef terrain with numerous ledges, gutters, and sand patches. The reef structures are adorned with a variety of soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward due to the shallow depths and the close proximity to the shore. Divers can leisurely explore the various formations, following the reef line or drifting over sandy areas. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This macro paradise is teeming with interesting marine life. Divers will frequently encounter a dazzling array of nudibranchs in a kaleidoscope of colours, meticulously crawling across the reef surfaces. Colourful cowfish are often spotted gracefully navigating the reef, while various species of small rays can be seen gliding over the sandy bottom. Keep an eye out for inquisitive octopus, shy cuttlefish, and a variety of small reef fish. The healthy ecosystem supports diverse invertebrate life, making it a macro photographer's delight.

Logistics & Facilities:
Woody Head Reef offers convenient shore access, making it highly accessible for divers. Basic amenities can be found nearby at the Woody Head campground, including toilets and parking. The optimal diving season is during spring and autumn for warmer waters and peak marine activity, coinciding with generally calmer weather. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants, particularly the intricate macro life.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers and macro photographers. Its shallow depths, accessible shore entry, and abundant macro life make it ideal for relaxed explorations, training, and peaceful underwater photography, particularly for spotting unique small creatures. It is also suitable for confident beginners under supervision.

Pro-Tip:
Due to the focus on macro life, move very slowly and deliberately, using a dive light to illuminate crevices and hidden corners. Patience will be rewarded with incredible sightings of nudibranchs, pipefish, and other tiny inhabitants. Consider diving during slack tide to minimise current.

75-word excerpt:
Woody Head Reef, Iluka (4-10m), is an intermediate shore dive macro paradise near a campground. Visibility (6-10m) is best in spring/autumn, influenced by swell and coastal runoff. It hosts nudibranchs, cowfish, and small rays. This accessible, dynamic site demands moderate current handling and good buoyancy, offering rich biodiversity for capable divers and macro photographers. Features shore access and nearby amenities, ideal for engaging macro encounters."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(188, "Latitude Rock", article_text_188)
update_article_in_db_and_combined_file(207, "Mullaway Reef", article_text_207)
update_article_in_db_and_combined_file(210, "Woody Head Reef", article_text_210)
