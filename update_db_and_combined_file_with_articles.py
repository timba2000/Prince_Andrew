
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

# Article for The Apartments (ID 60)
article_text_60 = """# The Apartments: Freshwater's Unique Underwater Cityscape for Intermediate Divers

Off the picturesque coastline of Freshwater, New South Wales, lies "The Apartments"—a truly unique and captivating offshore dive site, ideally suited for intermediate divers. Descending to depths between 6 to 15 metres, this site is renowned for its remarkable underwater rock formations that strikingly resemble building blocks, complete with intriguing tunnels and exhilarating swim-throughs. Accessible exclusively by boat, The Apartments offers a dynamic and visually stunning underwater cityscape, showcasing a rich diversity of temperate marine species. It’s an inviting site for those seeking engaging encounters with moray eels, schooling kingfish, and graceful rays against a backdrop of unique geological features, particularly during the prime season of October to April.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 6 to 15 metres, offering a good vertical range along the reef.
*   Visibility: Consistently good, typically ranging from 8 to 12 metres, but can extend to 30 metres on exceptionally clear days. Optimal visibility is usually from October to April. As an offshore reef, it benefits from minimal coastal runoff. Visibility is largely influenced by strong oceanic currents, localized plankton blooms, and offshore weather systems. While consistently good year-round, it can be impacted by large swells or plankton. Strong oceanic currents and offshore weather systems are the main external influences. Calm days are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 17°C in cooler months to a pleasant 23°C in summer.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. Surge can also be significant, particularly during larger ocean swells. This is a boat-only dive, requiring careful planning and execution. Awareness of boat traffic in the area is also important.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary factors in reducing visibility. Large swells and occasional plankton blooms can also contribute to turbid conditions. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
The Apartments features a rugged rocky reef terrain dominated by its unique rock formations, resembling stacked building blocks. These formations create numerous tunnels, swim-throughs, ledges, and gutters, providing ample shelter and exploration opportunities for marine life. Navigation is relatively straightforward, following the contours of these "buildings." Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant reef is home to an incredible array of marine life. Divers can expect frequent encounters with inquisitive moray eels peering from rocky crevices and large schools of kingfish, often patrolling the reef edge. Graceful rays, including stingrays and eagle rays, are often spotted cruising over the sandy bottom. Various species of morwong and colourful wrasse add vibrancy to the site. Keep an eye out for inquisitive blue gropers, wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the soft corals. The healthy ecosystem supports diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to The Apartments is exclusively by boat, typically arranged through dive charter operators from Manly or other nearby northern beaches. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is from October to April for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate coral ecosystems and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents and surge, and adept at navigating reef systems with challenging features like swim-throughs. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with unique geological formations and vibrant marine life.

Pro-Tip:
Due to the captivating tunnels and swim-throughs, consider carrying a good dive light, even during the day, to illuminate the darker sections and reveal hidden creatures. Always check your gauge and remaining air pressure before entering confined spaces.

75-word excerpt:
"The Apartments", Freshwater (6-15m), is an intermediate boat dive featuring unique rock formations resembling an underwater cityscape with tunnels and swim-throughs. Visibility (8-12m) is best October-April, influenced by oceanic currents and large swells. It hosts moray eels, kingfish, and rays. This dynamic site demands moderate current/surge handling for an exhilarating exploration of its unique geology and rich marine life off Sydney's northern beaches."""

# Article for Gold Coast Seaway (ID 232)
article_text_232 = """# Gold Coast Seaway: Queensland's Dynamic Urban Dive for All Levels

At the bustling heart of the Gold Coast, Queensland, the Gold Coast Seaway offers a truly dynamic and accessible dive site, suitable for divers of all levels. Descending to depths between 5 to 25 metres, this popular urban shore dive is a vibrant hub of marine life, boasting over 400 species, including delicate seahorses, curious pufferfish, and impressive Queensland groupers. Its convenient shore access makes it an ideal spot for varied explorations, particularly around high tide, revealing a hidden world where urban convenience meets astonishing biodiversity. The Gold Coast Seaway is a cherished local treasure, a lively aquatic microcosm inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: Suitable for all levels, depths range from a shallow 5 metres to a maximum of 25 metres, offering extensive exploration.
*   Visibility: Highly variable, typically ranging from 2 to 10 metres. Optimal visibility is generally found around high tide during dry periods. However, it is significantly impacted by significant runoff from the Nerang River and Gold Coast Broadwater, heavy rainfall, river outflow, strong tidal currents, and continuous boat traffic. Heavy rainfall and river outflow can reduce clarity to very poor levels (2-5m). Calm, dry periods with light offshore winds are ideal. Planning dives for incoming high tide is crucial for the best clarity.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 24°C, ensuring pleasant diving throughout the year.
*   Current/Conditions: Divers must be prepared for strong currents, particularly on incoming and outgoing tides. The site is exposed to significant boat traffic, necessitating extreme caution and a prominent dive flag. While primarily a shore dive, the strong currents mean it is often experienced as a drift dive.
*   Viz Implications: Heavy rainfall, river outflow, strong tidal currents, and boat traffic are the primary factors in reducing visibility, bringing in sediment and creating turbid conditions. Diving around slack high tide is essential for optimal conditions.

Terrain & Navigation:
The Gold Coast Seaway features a diverse underwater terrain, including rocky walls, sand flats, and scattered artificial structures. The walls are heavily encrusted with a variety of sponges, soft corals, and algae, providing ample shelter for marine life. Navigation is relatively straightforward, following the main channel or exploring the various rock walls. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. Due to the strong currents and variable visibility, familiarity with the site or a local guide is highly recommended. Underwater navigation relies on natural features and careful current awareness.

Marine Life Highlights:
This vibrant urban dive is a macro photographer's paradise, boasting over 400 species. Divers frequently encounter delicate seahorses expertly camouflaged amongst the sponge growth and seagrass. Curious pufferfish are common, as are impressive Queensland groupers taking shelter in the larger rock formations. Keep an eye out for octopus, cuttlefish, and a dazzling array of colourful nudibranchs clinging to the walls. Various species of wrasse, bream, and other reef fish add vibrancy to the site. Encounters with larger pelagics like kingfish and trevally are also possible.

Logistics & Facilities:
Gold Coast Seaway offers excellent shore access, with entry directly from the adjacent beach. Public facilities, including toilets and parking, are conveniently located nearby. The site is diveable year-round, though conditions are highly dependent on tidal movements and recent weather. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the structures, and adhering to strict safety protocols due to boat traffic and strong currents. Always use a dive flag.

Who Is It For?:
This is an excellent site for **All Levels** of divers, particularly those comfortable with strong currents and urban dive environments. Beginners should ideally dive with an experienced guide or during minimal current periods. It's an ultimate destination for macro photography and big-animal encounters within an urban setting.

Pro-Tip:
Due to the incredibly strong currents, plan your dive to coincide precisely with slack high tide. This will provide the calmest conditions and best visibility, allowing for a more relaxed and extended exploration of this dynamic site. Always use a large, visible dive flag and be aware of boat traffic.

75-word excerpt:
Gold Coast Seaway, Queensland (5-25m), is an all-level urban shore dive with 400+ species, including seahorses and groper. Visibility (2-10m) is highly variable, best at high tide, impacted by river runoff, currents, and boat traffic. This dynamic site demands strong current management and diligent safety, offering rich biodiversity for macro photography and big-animal encounters within an accessible urban setting."""

# Article for Kirra Reef (ID 234)
article_text_234 = """# Kirra Reef: Gold Coast's Accessible Inshore Haven for All Levels

Just off the iconic Kirra Beach on the Gold Coast, Queensland, Kirra Reef offers a wonderfully accessible and vibrant inshore dive site, suitable for divers of all levels. Descending to shallow depths between 5 to 10 metres, this site is characterized by its large rock formations and a rich tapestry of diverse marine life, creating a tranquil and visually stimulating underwater environment. Accessible via a convenient shore entry, Kirra Reef promises rewarding explorations into a healthy marine ecosystem, teeming with curious octopus, graceful cuttlefish, and various nudibranchs. It’s an excellent choice for those seeking vibrant reef life and a scenic dive within the natural beauty of the Gold Coast surrounds, particularly year-round during calm conditions.

The Essentials:
*   Depth Range: Suitable for all levels, depths range from a shallow 5 metres to a maximum of 10 metres, perfect for leisurely dives and extended bottom times.
*   Visibility: Variable, typically ranging from 5 to 10 metres, but can extend to 15 metres on exceptionally clear days. Optimal visibility is generally found year-round during calm conditions. However, it is influenced by moderate coastal runoff from residential areas and small creeks, heavy rainfall, strong easterly swells, and onshore winds. Prevailing easterly swells and onshore winds can stir up sediment, reducing clarity. Calm, dry periods with light offshore winds are ideal.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 24°C, ensuring pleasant diving throughout the year.
*   Current/Conditions: Divers can expect gentle to moderate currents, especially on incoming tides. The site is exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive. Shore access makes it relatively easy, but awareness of local conditions is wise.
*   Viz Implications: Heavy rainfall, strong easterly swells, and onshore winds are the primary factors in reducing visibility, bringing in sediment and creating turbid conditions. Moderate coastal runoff can also contribute. Planning dives during calm, dry weather is crucial for the best experience.

Terrain & Navigation:
Kirra Reef features a terrain dominated by large rock formations, creating numerous ledges, gutters, and sand patches. These structures are heavily adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward due to the shallow depths and the close proximity to the shore. Divers can leisurely explore the various formations, following the reef line or drifting over sandy areas. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant inshore reef is home to an incredible array of marine life. Divers can expect frequent encounters with curious octopus, graceful cuttlefish, and a dazzling array of colourful nudibranchs, flatworms, and other invertebrates clinging to the rocks. Various species of stingrays and eagle rays are often spotted gliding over the sandy bottom. Keep an eye out for wobbegong sharks tucked away under ledges and various blind sharks in darker crevices. Schools of reef fish, including wrasse, bream, and parrotfish, add vibrancy to the coral gardens.

Logistics & Facilities:
Kirra Reef offers excellent shore access directly from Kirra Beach. Public facilities, including toilets, showers, and parking, are conveniently located nearby. The site is diveable year-round, though conditions are highly dependent on swell and recent rainfall. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants.

Who Is It For?:
This is an ideal site for **All Levels** of divers and snorkelers, as well as macro photographers. Its shallow, calm waters and abundant, unique marine life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting fascinating small creatures and unique shark species.

Pro-Tip:
Due to the excellent macro opportunities, move very slowly and deliberately, using a dive light to illuminate crevices and hidden corners. Patience will be rewarded with incredible sightings of nudibranchs, flatworms, and camouflaged invertebrates. Always check local weather and swell forecasts before heading out.

75-word excerpt:
Kirra Reef, Gold Coast (5-10m), is an all-level shore dive with large rocks and diverse marine life, including octopus, cuttlefish, and nudibranchs. Visibility (5-10m) is variable, best year-round in calm conditions, impacted by runoff, easterly swells, and onshore winds. Easy access and nearby amenities make it ideal for relaxed photography and new divers seeking vibrant reef life and unique macro encounters."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(60, "The Apartments", article_text_60)
update_article_in_db_and_combined_file(232, "Gold Coast Seaway", article_text_232)
update_article_in_db_and_combined_file(234, "Kirra Reef", article_text_234)
