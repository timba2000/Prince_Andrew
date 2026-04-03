
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

# Article for Wigton Reef (ID 163)
article_text_163 = """# Wigton Reef: Outer GBR's Pristine Hard Coral Wonderland for Advanced Divers

Far out in the magnificent Outer Great Barrier Reef, Queensland, Wigton Reef stands as a testament to pristine marine environments, offering a spectacular and challenging dive experience for advanced divers. Descending to depths between 12 and 28 metres, this reef is celebrated for its exquisite hard coral formations, vibrant ecosystems, and the moderate currents that bring abundant pelagic life. Accessible primarily as a liveaboard dive site, Wigton Reef promises thrilling encounters with trevally, various sharks, and a kaleidoscope of butterflyfish in consistently clear waters. It’s a bucket-list destination for experienced divers seeking untouched beauty and dynamic marine interactions in a remote, world-class setting.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 12 to 28 metres, offering extensive reef exploration.
*   Visibility: Consistently excellent, typically ranging from 15 to 20 metres. As a remote Outer GBR site, it benefits from minimal coastal runoff. Visibility is largely influenced by strong oceanic currents, localized plankton blooms, and offshore weather systems. While consistently good year-round, it can experience seasonal thermoclines and plankton events in warmer months. Optimal conditions are generally found between April and October.
*   Water Temperature: Water temperatures are consistently warm, ranging from 24°C to 28°C, ensuring comfortable diving throughout the prime season.
*   Current/Conditions: Divers should expect moderate to strong oceanic currents, requiring good finning technique and careful dive planning. The reef is exposed to open ocean conditions, so while generally calm during the prime season, offshore weather systems can influence conditions. Underwater navigation relies on the natural reef contours and depth.
*   Viz Implications: Strong oceanic currents can occasionally introduce nutrient-rich waters that may foster plankton blooms, temporarily affecting clarity. Offshore weather systems are the main external influence, but overall, excellent visibility is a hallmark.

Terrain & Navigation:
Wigton Reef features a diverse terrain dominated by extensive hard coral gardens, sloping reef walls, and sandy channels. The reef structures are adorned with a vibrant array of corals, sponges, and anemones. Navigation is generally intuitive, following the reef contours, but dive guides are highly recommended for new visitors to explore the best features. The dynamic environment, with moderate currents, adds an element of drift diving to the experience. Good buoyancy control is essential to avoid contact with the delicate coral ecosystems.

Marine Life Highlights:
This pristine reef is a vibrant hub of marine activity. Divers frequently encounter large schools of trevally and various species of sharks, including reef sharks and the occasional grey reef shark, patrolling the reef edge. A dazzling array of butterflyfish, surgeonfish, and parrotfish populate the coral gardens. Keep an eye out for inquisitive blue gropers, various species of rays, and a variety of smaller invertebrates clinging to the coral structures. The healthy ecosystem supports diverse macro life, making it a macro photographer's delight.

Logistics & Facilities:
Access to Wigton Reef is primarily via liveaboard dive vessels, typically departing from Cairns or Port Douglas, or from Mackay for shorter trips. Due to its remote location in the Outer GBR, it is not accessible for day trips. Liveaboards provide all necessary facilities, including dive gear, accommodation, and meals. The optimal diving season is from April to October for generally calmer weather and peak marine activity. Conservation is paramount; Wigton Reef is a highly protected area, and divers are expected to adhere to strict marine park regulations, including no-touch policies and responsible interaction with marine life.

Who Is It For?:
This is an **Advanced** dive site, suitable for experienced divers comfortable with deep profiles, drift diving, and encounters with pelagic marine life. Strong finning skills and excellent buoyancy control are essential. It's an ultimate destination for adventure seekers and serious underwater photographers who appreciate untouched coral ecosystems.

Pro-Tip:
Due to the remote location and liveaboard access, ensure all your gear is in excellent working order before departure. Consider bringing a reef hook for safety stops in strong currents, allowing you to observe the reef without exerting yourself.

75-word excerpt:
Wigton Reef, Outer GBR (12-28m), is an advanced liveaboard dive with pristine hard coral and moderate currents. Visibility (15-20m) is influenced by oceanic currents and plankton. It boasts trevally, sharks, and butterflyfish in a remote, world-class setting. Requires excellent buoyancy and current management for thrilling pelagic encounters and untouched beauty, ideal for experienced divers and photographers seeking dynamic marine interactions."""

# Article for Round Top Island (ID 164)
article_text_164 = """# Round Top Island: Mackay Coast's Sheltered Gem for Beginner Divers

Just off the picturesque Mackay Coast, Queensland, Round Top Island offers a delightfully sheltered and accessible dive site, perfectly suited for beginner divers and snorkelers. Descending to shallow depths between 3 to 10 metres, this site is a charming mosaic of seagrass beds and scattered coral bommies, creating a tranquil and visually engaging underwater environment. Its close-to-shore location and accessible shore/boat entry make it an ideal spot for relaxed explorations from May to October, revealing a hidden world of fascinating marine life. Round Top Island is a local treasure, a vibrant aquatic classroom where natural beauty meets abundant and friendly marine life, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An inviting depth range for beginners, from a shallow 3 metres down to 10 metres, perfect for leisurely observation.
*   Visibility: Typically ranges from 5 to 8 metres. While generally good during the prime season, it can be influenced by tidal flow and coastal runoff. Optimal visibility is generally found between May and October, particularly during calm, dry periods. Moderate coastal runoff from the mainland can temporarily reduce clarity after significant rainfall. Strong tidal flows can also stir up sediment, reducing visibility. Calm conditions with minimal tidal movement are ideal.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 23°C to 27°C, ensuring pleasant diving throughout the prime season.
*   Current/Conditions: Divers can expect some gentle tidal flow, particularly around the island. The site is generally sheltered close to shore, making it very safe for beginners. However, strong tidal flows on larger tides can create moderate currents, so awareness of local conditions is wise.
*   Viz Implications: Coastal runoff after rain and strong tidal flows are the primary factors leading to reduced visibility. Choosing a dive day with calm seas and a period of dry weather will ensure the best experience.

Terrain & Navigation:
Round Top Island features a diverse underwater terrain, transitioning from rocky reefs to expansive seagrass beds and scattered coral bommies. The reef sections provide numerous crevices and overhangs, while the seagrass offers a different habitat for unique marine life. Navigation is straightforward due to the shallow depths and the close proximity to the shore. Divers can leisurely explore the various formations, following the reef line or drifting over the seagrass. The clear water, when present, aids significantly in orientation.

Marine Life Highlights:
This gentle site is teeming with interesting marine life. Divers will frequently encounter delicate seahorses expertly camouflaged amongst the seagrass and sponge growth. Various species of rays can often be spotted gliding gracefully over the sandy patches. Keep an eye out for curious pipefish, small reef fish, and an array of colourful nudibranchs. The seagrass is also a nursery for juvenile fish, making it a fantastic site for macro photography. Encounters with octopus and cuttlefish are also common.

Logistics & Facilities:
Round Top Island offers convenient shore access and is also accessible by small boat, making it highly flexible for divers. While there are no dedicated dive facilities directly at the site, basic amenities can be found nearby in Mackay. The site is diveable from May to October for warmer waters and generally calmer conditions. Conservation is paramount here; divers are encouraged to practice responsible diving, avoiding disturbance to the delicate ecosystem and its inhabitants, particularly within the seagrass beds and coral bommies.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting unique small creatures.

Pro-Tip:
Due to the prevalence of seahorses and pipefish, move slowly and deliberately through the seagrass beds and around the coral bommies. These creatures are masters of camouflage and are easily overlooked. A keen eye and patience will be richly rewarded.

75-word excerpt:
Round Top Island, Mackay Coast (3-10m), is a beginner-friendly shore/boat dive with seagrass and coral bommies. Visibility (5-8m) is best May-October, influenced by tidal flow and coastal runoff. It hosts seahorses, rays, and pipefish. Its sheltered nature and easy access make it ideal for relaxed macro photography and new divers seeking unique small marine life in a tranquil setting, adhering to marine conservation principles."""

# Article for Green Island – South West Rocks (ID 186)
article_text_186 = """# Green Island – South West Rocks: A Soft Coral Garden for Intermediate Divers

Just off South West Rocks, New South Wales, Green Island presents a captivating and vibrant boat dive site, ideally suited for intermediate divers. Ranging in depth from 8 to 16 metres, this small island reef is celebrated for its spectacular soft coral gardens, bustling fish life, and frequent encounters with marine megafauna. Accessible exclusively by boat, Green Island offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species. It’s a jewel within a protected marine area, promising engaging dives with impressive biodiversity and healthy ecosystems for those seeking a memorable exploration off the Mid North Coast.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 8 to 16 metres, offering a good vertical range along the reef.
*   Visibility: Consistently excellent, typically ranging from 10 to 15 metres. As an oceanic site, it benefits from minimal coastal runoff. Visibility is largely influenced by strong oceanic currents and offshore weather systems. While consistently good year-round, it can experience seasonal thermoclines and plankton events in warmer months. However, strong easterly swells can create significant surge, impacting clarity. Optimal conditions are generally found between October and March. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 18°C to 24°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers can expect moderate to strong oceanic currents and significant surge, particularly on incoming tides or during larger ocean swells. This is an exposed site that demands excellent finning skills and vigilant situational awareness. Boat traffic in the area also requires caution.
*   Viz Implications: Strong oceanic currents and easterly swells are the primary factors in reducing visibility and creating challenging conditions. Heavy rainfall, though minimal from the natural coastline, can also contribute. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Green Island features a rugged rocky reef terrain with numerous ledges, gutters, and sand patches. The reef structures are heavily adorned with spectacular soft coral gardens, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef's contours around the island. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant reef is home to an incredible array of marine life. Divers can expect frequent encounters with curious octopus, graceful green and loggerhead turtles cruising along the reef, and various species of colourful wrasse. Large schools of reef fish, including snapper and morwong, patrol the coral formations. Keep an eye out for inquisitive blue gropers, wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the soft corals. The healthy soft coral ecosystems support diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Green Island is exclusively by boat, typically arranged through dive charter operators in South West Rocks. There are no on-site facilities, so divers must be self-sufficient. The optimal diving season is from October to March for warmer waters and peak marine activity. As part of a protected marine area, strict conservation guidelines apply; divers are expected to observe marine life responsibly without touching or disturbing the delicate soft coral ecosystems and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate to strong currents and surge, and adept at navigating reef systems. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Green Island is renowned for its soft corals. Take your time to gently drift over the reef, observing the intricate polyps and the small creatures that make their homes amongst them. Good buoyancy is essential to avoid damaging these delicate structures.

75-word excerpt:
Green Island – South West Rocks (8-16m) is an intermediate boat dive showcasing spectacular soft coral gardens and abundant fish life. Visibility (10-15m) is influenced by oceanic currents and easterly swells, best in calm conditions (October-March). It hosts octopus, turtles, and wrasse, offering a dynamic exploration for capable divers within a protected marine area, demanding current management and appreciation for vibrant ecosystems."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(163, "Wigton Reef", article_text_163)
update_article_in_db_and_combined_file(164, "Round Top Island", article_text_164)
update_article_in_db_and_combined_file(186, "Green Island – South West Rocks", article_text_186)
