
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

# Article for Manta Bommie (ID 228)
article_text_228 = """# Manta Bommie: North Stradbroke Island's Pelagic Paradise for All Levels

Off the stunning coastline of North Stradbroke Island, Queensland, Manta Bommie stands as a world-renowned dive site, perfectly suited for divers of all levels. Descending to depths between 3 to 15 metres, this site is a captivating collection of rocky outcrops surrounded by a rugged rocky reef, famously known for its consistent encounters with majestic manta rays. Accessible exclusively by boat, Manta Bommie offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species, including leopard sharks, stingrays, and an array of macro life. It’s a bucket-list destination for those seeking exhilarating pelagic encounters and vibrant reef life during the prime season of November to May.

The Essentials:
*   Depth Range: Suitable for all levels, depths range from a shallow 3 metres to a maximum of 15 metres, perfect for extended bottom times.
*   Visibility: Consistently excellent, typically ranging from 10 to 30 metres. Optimal visibility is generally found between November and May. As an oceanic site, visibility is largely influenced by strong oceanic currents and offshore weather systems. While consistently good year-round, it can experience occasional surge. There is no specific coastal runoff information, implying oceanic influences are paramount. Divers should anticipate that strong currents can bring in plankton or stir up sediment, temporarily affecting clarity. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 22°C to 26°C, ensuring pleasant diving throughout the prime season.
*   Current/Conditions: Divers can expect occasional surge, particularly on incoming tides or during periods of stronger oceanic influence. The site is exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive. Boat traffic in the area also requires caution.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary factors in reducing visibility. Occasional surge can also contribute to turbid conditions. Planning dives during calm, dry periods will ensure the best possible clarity and an enjoyable experience.

Terrain & Navigation:
Manta Bommie features a collection of rocky outcrops and a rugged rocky reef terrain with numerous ledges, gutters, and sand patches. The reef structures are heavily adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef contours. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This pelagic paradise is home to an incredible array of marine life, with manta rays being the star attraction. Divers can expect frequent encounters with these majestic creatures, often seen gliding gracefully through the water. Leopard sharks and shovel nose sharks are also common, resting on the sandy bottom. Various species of stingrays and bull rays can be spotted cruising over the reef. Keep an eye out for inquisitive octopus, various species of colourful wrasse, and a dazzling array of macro life, including nudibranchs, clinging to the reef structures. The healthy coral ecosystems support diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Manta Bommie is exclusively by boat, typically arranged through dive charter operators in North Stradbroke Island or Brisbane. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is from November to May for warmer waters and peak manta ray activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **All Levels** of divers. Beginners can enjoy the shallower, more protected areas teeming with life, while intermediate and advanced divers can explore deeper sections, navigate stronger currents, and seek out specific large marine encounters. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the consistent manta ray encounters, consider taking a wide-angle lens for your underwater camera. Approach mantas slowly and calmly, allowing them to approach you, for the best possible interaction and photographic opportunities.

75-word excerpt:
Manta Bommie, North Stradbroke Island (3-15m), is an all-level boat dive with rocky outcrops, famous for manta rays, leopard sharks, and diverse macro life. Visibility (10-30m) is best November-May, influenced by oceanic currents and occasional surge. This pelagic paradise offers thrilling encounters and vibrant reef life for all divers in a world-class setting, demanding respect for its delicate ecosystem."""

# Article for Rapid Bay Jetty (ID 12)
article_text_12 = """# Rapid Bay Jetty: Fleurieu Peninsula's Leafy Sea Dragon Haven for Beginner Divers

Off the stunning coastline of the Fleurieu Peninsula, South Australia, Rapid Bay Jetty stands as an iconic and accessible shore dive, perfectly suited for beginner divers. Descending to depths between 3 to 10 metres, this site is famously known as a haven for the elusive leafy sea dragons, making it a bucket-list destination for marine enthusiasts and underwater photographers alike. Its encrusted jetty pylons, teeming with diverse marine life, provide an intricate exploration. Accessible via an easy shore entry, Rapid Bay Jetty offers a tranquil yet rewarding dive experience, promising intimate encounters with octopus, cuttlefish, and a vibrant array of macro life. It’s a cherished local treasure, a dynamic aquatic classroom where natural beauty meets astonishing biodiversity, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An ideal depth range for beginners, from a shallow 3 metres down to 10 metres, perfect for leisurely observation and photography.
*   Visibility: Typically ranges from 5 to 15 metres. Optimal visibility is generally found between October and May. As a coastal jetty site, visibility is largely influenced by local sediment, coastal runoff, and strong currents. Strong southerly swells can reduce clarity considerably. Cold water upwellings can occur, sometimes bringing very clear water. The sheltered conditions within the bay behind the jetty generally aid visibility, but it can be impacted by local sediment stirred by surge or strong winds. Planning dives around slack tide will offer the best clarity.
*   Water Temperature: Water temperatures range from a cool 11°C in winter to a more moderate 20°C in summer. A good wetsuit (5-7mm) or drysuit is recommended.
*   Current/Conditions: Divers can expect some surge, particularly on incoming tides or during periods of stronger oceanic influence. While generally calm, strong southerly swells can create moderate currents around the jetty. Shore access makes it relatively easy, but awareness of local conditions is wise.
*   Viz Implications: Strong southerly swells, coastal runoff after rain, and local sediment disturbance are the primary factors in reducing visibility. Cold water upwellings can sometimes provide exceptional clarity. Planning dives during calm, dry periods will ensure the best experience.

Terrain & Navigation:
Rapid Bay Jetty features a terrain dominated by its old and new jetty pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom around the jetty is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the jetty and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. The clear water, when present, allows for excellent visual navigation and observation.

Marine Life Highlights:
This iconic jetty is a macro photographer's paradise, particularly famous for the elusive **leafy sea dragons**. Divers are often rewarded with sightings of these master camouflagers amongst the jetty pylons and seagrass. Frequent encounters with curious octopus, often camouflaged amongst the rocks, and elegant cuttlefish displaying their mesmerizing colour changes are also common. Various species of wrasse, bream, and other colourful reef fish add vibrancy to the site. Keep an eye out for a dazzling array of nudibranchs and smaller invertebrates clinging to the jetty structures. The healthy seagrass beds are also a nursery for juvenile fish.

Logistics & Facilities:
Rapid Bay Jetty offers excellent shore access, with easy entry directly from the beach. While there are no dedicated dive facilities directly at the jetty, basic amenities can be found nearby in the town. The site is diveable from October to May for warmer waters and generally calmer conditions. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the jetty structures, especially the delicate leafy sea dragon habitats. Always adhere to local marine park regulations.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting rare and unusual creatures.

Pro-Tip:
Move slowly and deliberately, especially when searching for leafy sea dragons. Their camouflage is extraordinary. A keen eye, patience, and perhaps a local guide will greatly increase your chances of a successful sighting. Maintain good buoyancy to avoid disturbing the sandy/silty bottom.

75-word excerpt:
Rapid Bay Jetty, Fleurieu Peninsula (3-10m), is a beginner-friendly shore dive famed for leafy sea dragons, octopus, and cuttlefish amidst encrusted pylons. Visibility (5-15m) is best October-May, but impacted by swell, cold water, and local sediment. Its easy access and abundant macro life make it ideal for relaxed photography and new divers. Requires careful search for camouflaged wonders and adherence to marine conservation."""

# Article for Edithburgh Jetty (ID 17)
article_text_17 = """# Edithburgh Jetty: Yorke Peninsula's Macro Haven and Leafy Sea Dragon Hotspot for All Levels

On the eastern tip of the Yorke Peninsula, South Australia, Edithburgh Jetty stands as a globally renowned macro photography haven and a prime location for encountering the elusive leafy sea dragon. Descending to depths between 3 to 10 metres, this quiet jetty dive offers an intricate exploration of encrusted pylons teeming with an astonishing array of nudibranchs, curious cuttlefish, and various macro life. Accessible via an easy jetty access, Edithburgh Jetty is an ideal spot for relaxed explorations from October to April, revealing a hidden world of fascinating marine life for divers of all levels. It’s a cherished local treasure, a vibrant aquatic microcosm where natural beauty meets astonishing biodiversity, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An ideal depth range for all levels, from a shallow 3 metres down to 10 metres, perfect for leisurely observation and macro photography.
*   Visibility: Variable, typically ranging from 5 to 15 metres. Optimal visibility is generally found between October and April. As a coastal jetty site, visibility is largely influenced by local sediment, coastal runoff, and tidal movements. Strong currents can reduce clarity considerably. The sheltered conditions within the bay behind the jetty generally aid visibility, but it can be impacted by local sediment stirred by surge or strong winds. While not consistently documented, local experience suggests it can be excellent on calm days.
*   Water Temperature: Water temperatures are comfortable, ranging from 15°C in cooler months to a pleasant 21°C in summer. A good wetsuit (5-7mm) is recommended.
*   Current/Conditions: Divers can expect some surge, particularly on incoming tides or during periods of stronger oceanic influence. While generally calm, strong southerly swells can create moderate currents around the jetty. Jetty access makes it relatively easy, but awareness of boat traffic and local conditions is wise.
*   Viz Implications: Strong southerly swells, coastal runoff after rain, and local sediment disturbance are the primary factors in reducing visibility. Planning dives around slack tide will offer the best clarity and ease of navigation around the jetty structures.

Terrain & Navigation:
Edithburgh Jetty features a terrain dominated by its extensive network of pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom around the jetty is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the jetty and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. The clear water, when present, allows for excellent visual navigation and observation.

Marine Life Highlights:
This iconic jetty is a macro photographer's paradise, particularly famous for the elusive **leafy sea dragons**. Divers are often rewarded with sightings of these master camouflagers amongst the jetty pylons and seagrass. Frequent encounters with a dazzling array of nudibranchs in a kaleidoscope of colours, curious cuttlefish displaying their mesmerizing colour changes, and graceful octopus camouflaged amongst the rocks are also common. Various species of wrasse, bream, and other colourful reef fish add vibrancy to the site. The healthy seagrass beds are also a nursery for juvenile fish.

Logistics & Facilities:
Edithburgh Jetty offers excellent shore access, with easy entry directly from the jetty. Public parking and nearby amenities are available, adding to its convenience. The site is diveable from October to April for warmer waters and generally calmer conditions. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the jetty structures, especially the delicate leafy sea dragon habitats. Always adhere to local marine park regulations.

Who Is It For?:
This is an ideal site for **All Levels** of divers and macro photographers. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting rare and unusual creatures. It's a superb site for building confidence and enjoying a relaxed marine experience.

Pro-Tip:
To truly appreciate the macro wonders of Edithburgh Jetty, move slowly and deliberately, using a dive light to illuminate crevices and hidden corners. Leafy sea dragons are masters of camouflage and require a keen eye and patience to spot. Diving at slack tide minimises current and maximises observation time.

75-word excerpt:
Edithburgh Jetty, Yorke Peninsula (3-10m), is a world-renowned macro haven for all levels, famous for leafy sea dragons, nudibranchs, and cuttlefish. Visibility (5-15m) is best October-April, influenced by sediment and currents. Easy jetty access, with amenities nearby. Its abundant, unique macro life and calm waters are ideal for relaxed photography, promising extraordinary encounters with master camouflagers and vibrant ecosystems."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(228, "Manta Bommie", article_text_228)
update_article_in_db_and_combined_file(12, "Rapid Bay Jetty", article_text_12)
update_article_in_db_and_combined_file(17, "Edithburgh Jetty", article_text_17)
