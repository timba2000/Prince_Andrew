
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

# Article for Nuyts Archipelago Drop-off (ID 139)
article_text_139 = """# Nuyts Archipelago Drop-off: Far West SA's Deep Water Wall Dive for Advanced Explorers

Far off the remote coast of Far West South Australia, within the pristine Nuyts Archipelago, lies a truly spectacular and challenging dive site: the Nuyts Archipelago Drop-off. Plunging to depths between 18 and 35 metres, this deep-water wall dive is renowned for its dramatic scenery, exceptional visibility, and the impressive pelagic species that patrol its depths. Accessible exclusively by boat, this site promises thrilling encounters with various sharks, schooling tuna, and diverse wrasse against a backdrop of unique geological formations, particularly during the prime summer season. It’s a bucket-list destination for advanced divers seeking untouched beauty and dynamic marine interactions in a remote, world-class setting.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 18 to 35 metres, offering dramatic wall exploration into deeper waters.
*   Visibility: Consistently excellent, typically ranging from 20 to 30 metres. Optimal visibility is generally found during summer months. As a remote oceanic site, it benefits from minimal coastal runoff from the remote islands. Visibility is largely influenced by strong oceanic currents, deep-water upwellings, and offshore weather systems. While consistently good year-round, it can experience seasonal thermoclines and plankton events in warmer months. Strong currents can bring in plankton or stir up sediment, temporarily affecting clarity. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures range from a cool 14°C in winter to a more moderate 19°C in summer. A good wetsuit (5-7mm) or drysuit is recommended due to the cooler water.
*   Current/Conditions: Divers should expect strong oceanic currents, particularly along the wall. Good finning technique and careful dive planning are essential. The site is exposed to open ocean conditions, so while generally calm during the prime season, offshore weather systems can influence conditions. This is a boat-only dive, requiring careful planning and execution.
*   Viz Implications: Strong oceanic currents, deep-water upwellings, and offshore weather systems are the primary factors influencing visibility. Planning dives for calm, dry periods will ensure the best possible clarity and an enjoyable experience.

Terrain & Navigation:
Nuyts Archipelago Drop-off features a dramatic underwater terrain of steep vertical walls that plunge into significant depths, interspersed with ledges and small crevices. The reef structures are adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef walls, but dive guides are highly recommended for new visitors to explore the best features. The dynamic environment, with strong currents, adds an element of drift diving to the experience. Good buoyancy control is essential to avoid contact with the delicate coral ecosystems.

Marine Life Highlights:
This pristine reef is a vibrant hub of marine activity, particularly known for its larger pelagic species. Divers frequently encounter various species of sharks, including wobbegongs and, occasionally, larger reef sharks, patrolling the wall. Large schools of tuna and various species of wrasse add vibrancy to the coral gardens. Keep an eye out for inquisitive blue gropers, various species of rays, and a variety of smaller invertebrates clinging to the coral structures. The healthy ecosystem supports diverse macro life, making it a macro photographer's delight.

Logistics & Facilities:
Access to Nuyts Archipelago Drop-off is exclusively by boat, typically arranged through dive charter operators from Ceduna or other ports on the Eyre Peninsula. Due to its remote location, it is not accessible for casual day trips and may require multi-day expeditions. There are no on-site facilities directly at the dive site, so divers must be completely self-sufficient. The optimal diving season is during summer (December to February) for warmer waters and peak marine activity. Conservation is paramount; divers are expected to adhere to strict marine park regulations, observing marine life responsibly and without touching or disturbing the delicate ecosystems.

Who Is It For?:
This is an **Advanced** dive site, suitable for experienced divers comfortable with deep profiles, strong oceanic currents, and encounters with pelagic marine life. Strong finning skills and excellent buoyancy control are essential. It's an ultimate destination for adventure seekers and serious underwater photographers who appreciate untouched coral ecosystems.

Pro-Tip:
Due to the remote location and strong currents, ensure all your gear is in excellent working order before departure. Consider bringing a reef hook for safety stops in strong currents, allowing you to observe the reef without exerting yourself. Always dive with an experienced buddy and stay close to your guide.

75-word excerpt:
Nuyts Archipelago Drop-off, Far West SA (18-35m), is an advanced deep wall dive with dramatic scenery and excellent visibility (20-30m) in summer. Influenced by strong oceanic currents and upwellings, it hosts sharks, tuna, and wrasse. This remote, boat-only site demands advanced skills, offering thrilling pelagic encounters and untouched beauty for experienced divers and photographers seeking dynamic marine interactions."""

# Article for Fingal Head Reef (ID 195)
article_text_195 = """# Fingal Head Reef: Fingal Head's Basalt Boulder Oasis for Intermediate Divers

Off the picturesque coastline of Fingal Head, New South Wales, Fingal Head Reef offers a captivating and dynamic inshore dive site, ideally suited for intermediate divers. Ranging in depth from 4 to 10 metres, this extensive reef is characterized by its unique basalt boulders and expansive seagrass beds, creating a vibrant and visually stimulating underwater environment. Accessible primarily by boat or kayak, Fingal Head Reef promises a rewarding exploration into a healthy marine ecosystem, teeming with wobbegongs, curious cuttlefish, and various octopus. It’s an excellent choice for those seeking vibrant reef life and a scenic dive within the natural beauty of the Fingal Head surrounds, particularly during the spring and summer seasons.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 4 to 10 metres, offering a good vertical range along the reef.
*   Visibility: Variable, typically ranging from 8 to 12 metres, but can extend to 15 metres on exceptionally clear days. Optimal visibility is often best during spring and summer, particularly during calm conditions. It is influenced by moderate coastal runoff from the Tweed River and surrounding areas, heavy rainfall, river outflow, strong northerly swells, and onshore winds. Prevailing northerly swells and onshore winds can stir up sediment, reducing clarity. Calm, dry periods with light offshore winds are ideal.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 25°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. The site is exposed to boat traffic, so caution is advised. While generally good, strong northerly swells and onshore winds can create significant surge, reducing visibility.
*   Viz Implications: Heavy rainfall, river outflow, strong northerly swells, and onshore winds are the primary factors in reducing visibility, bringing in sediment and creating turbid conditions. Planning dives during calm, dry weather is crucial for the best experience.

Terrain & Navigation:
Fingal Head Reef features a rugged rocky reef terrain with numerous basalt boulders, ledges, and extensive seagrass beds. The reef structures are heavily adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef contours. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant reef is home to an incredible array of marine life. Divers can expect frequent encounters with curious wobbegong sharks, often resting camouflaged under ledges or within the basalt formations. Elegant cuttlefish display their mesmerizing colour changes, and inquisitive octopus can be seen peeking from rocky hideaways. Various species of wrasse, bream, and other colourful reef fish add vibrancy to the coral gardens. The healthy seagrass beds are also a nursery for juvenile fish, making it a fantastic site for macro photography. Keep an eye out for a dazzling array of macro life, including nudibranchs, clinging to the corals.

Logistics & Facilities:
Access to Fingal Head Reef is primarily by boat or kayak, typically launched from nearby access points in Fingal Head or the Tweed River. There are no dedicated dive facilities directly at the site, so divers must be self-sufficient. The optimal diving season is from spring to summer (September to March) for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat/kayak entries, capable of handling moderate currents, and adept at navigating reef systems with challenging features. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the unique basalt boulders and seagrass beds, take your time to explore these contrasting habitats. The transition zones often hold interesting macro life. Always check local weather and swell forecasts before heading out, especially for kayak entry.

75-word excerpt:
Fingal Head Reef, Fingal Head (4-10m), is an intermediate inshore dive with basalt boulders and seagrass beds. Visibility (8-12m) is best spring/summer during calm conditions, but impacted by runoff, rainfall, and northerly swells. It hosts wobbegongs, cuttlefish, and octopus. This dynamic site demands moderate current handling and offers rich biodiversity for capable divers. Access is by boat/kayak, ideal for vibrant reef life and scenic exploration."""

# Article for Second Valley (ID 82)
article_text_82 = """# Second Valley: Fleurieu Peninsula's Diverse Reef and Wall Dive for Intermediate Explorers

Off the stunning coastline of the Fleurieu Peninsula, South Australia, Second Valley presents a captivating and diverse dive site, ideally suited for intermediate divers. Descending to depths between 4 to 18 metres, this site is renowned for its intricate rocky reef, impressive wall dive sections, and intriguing caves and ledges, all teeming with a rich array of marine life. Accessible via a convenient jetty access, Second Valley offers a dynamic underwater landscape, showcasing vibrant blue devils, elusive old wives, and curious cuttlefish. It’s an inviting site for those seeking engaging encounters and geological exploration against a backdrop of healthy ecosystems, particularly during the prime season of October to March.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 4 to 18 metres, offering a good vertical range along the reef and wall sections.
*   Visibility: Generally good, typically ranging from 8 to 12 metres, but can extend to 18 metres on exceptionally clear days. Optimal visibility is generally found between October and March during calm conditions. As a coastal site, visibility is influenced by strong southerly winds, tidal currents, and surge. Minimal coastal runoff contributes to overall clarity. Strong southerly winds and surge can reduce clarity. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortable, ranging from 15°C in cooler months to a pleasant 21°C in summer. A good wetsuit (5-7mm) is recommended.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. Surge can also be significant, particularly during larger ocean swells. Jetty access makes it relatively easy, but awareness of boat traffic and local conditions is wise.
*   Viz Implications: Strong southerly winds, tidal currents, and surge are the primary factors in reducing visibility. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Second Valley features a diverse underwater terrain, transitioning from rocky reefs to dramatic wall sections and intriguing caves and ledges. The reef structures are heavily adorned with a variety of colourful sponges, soft corals, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef contours and exploring the various passages. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive. The jetty also provides a good reference point.

Marine Life Highlights:
This vibrant site is home to an incredible array of marine life. Divers can expect frequent encounters with electric-blue blue devils, often darting in and out of rocky crevices. Elusive old wives, with their distinctive elongated fins, are also common. Curious cuttlefish display their mesmerizing colour changes, and various species of wrasse, bream, and other colourful reef fish add vibrancy to the coral gardens. Keep an eye out for inquisitive octopus, wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the sponges. The healthy ecosystem supports diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Second Valley offers excellent jetty access, with easy entry directly from the jetty. Public parking and basic amenities are conveniently located nearby. The site is diveable from October to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants. Always adhere to local marine park regulations and be mindful of fishing activities around the jetty.

Who Is It For?:
This is an excellent site for **Intermediate** divers who are comfortable with jetty entries/exits, capable of handling moderate currents and surge, and adept at navigating diverse reef systems with challenging features. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the diversity of terrain, consider a leisurely swim along the wall and then explore the shallower reef and jetty pylons for macro life. A good dive light will illuminate the colours and hidden creatures within the caves and ledges.

75-word excerpt:
Second Valley, Fleurieu Peninsula (4-18m), is an intermediate jetty dive with rocky reefs, walls, caves, and ledges. Visibility (8-12m) is best October-March during calm conditions, but impacted by southerly winds and surge. It hosts blue devils, old wives, and cuttlefish. This dynamic site demands moderate current/surge handling for a rewarding exploration of its unique geological formations and rich marine life off South Australia's coast."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(139, "Nuyts Archipelago Drop-off", article_text_139)
update_article_in_db_and_combined_file(195, "Fingal Head Reef", article_text_195)
update_article_in_db_and_combined_file(82, "Second Valley", article_text_82)
