
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

# Article for Flinders Pier (ID 6)
article_text_6 = """# Flinders Pier: Mornington Peninsula's Macro Jewel for Beginner Divers

On the scenic Mornington Peninsula, Victoria, Flinders Pier stands as one of Melbourne's most beloved and accessible shore dives, perfectly suited for beginner divers and macro photography enthusiasts. Descending to shallow depths between 2 to 8 metres, this iconic pier structure is a vibrant underwater gallery, attracting a phenomenal array of unique marine life. Famous for its resident weedy sea dragons, seahorses, and a plethora of captivating macro creatures, Flinders Pier offers an enchanting experience year-round, with exceptional opportunities for night diving. Its easy shore access and nearby facilities make it an ideal spot for relaxed explorations into Victoria's cool temperate waters, inviting all to discover its gentle charm and astonishing biodiversity.

The Essentials:
*   Depth Range: An ideal beginner depth range from a shallow 2 metres down to 8 metres, perfect for leisurely observation and macro photography.
*   Visibility: Typically ranges from 2 to 8 metres, with generally good visibility. It can, however, be impacted by moderate runoff from the local town and pier activities, heavy rainfall, and strong tidal currents, which can stir up sediment. Visibility is often better on incoming tides during calm conditions. Strong westerly or southerly winds can reduce clarity. Optimal conditions are often experienced in winter when plankton levels are lower, boosting clarity.
*   Water Temperature: Water temperatures range from a cool 12°C in winter to a more moderate 18°C in summer. A good wetsuit (7mm+) or drysuit is recommended due to the cooler water.
*   Current/Conditions: Divers can expect some gentle tidal currents around the pier pylons. The site is generally sheltered, but awareness of localized currents and the pier structure is wise. Limited visibility can be a factor, especially after rain or with strong currents.
*   Viz Implications: Heavy rainfall and strong tidal currents are the primary factors in reducing visibility. Planning dives around slack tide and during calmer periods will ensure the best clarity and ease of navigation.

Terrain & Navigation:
Flinders Pier features a terrain dominated by its extensive wooden pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom beneath and around the pier is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the pier and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. Compass readings can be unreliable under the metal structure, so navigation relies on visual cues from the pier itself. It is also an excellent site for night diving.

Marine Life Highlights:
This iconic pier is a macro photographer's paradise, particularly famous for the majestic **weedy sea dragons**. Divers are often rewarded with sightings of these master camouflagers amongst the pier pylons and seagrass. Frequent encounters with various species of seahorses, including the common big-belly seahorse, curious octopus, and elegant pipefish are also common. A dazzling array of colourful nudibranchs, various crabs, and schooling fish add vibrancy to the site. The healthy growth on the pylons supports diverse invertebrate life, making it a macro enthusiast's dream.

Logistics & Facilities:
Flinders Pier offers excellent shore access, with easy entry directly from the beach or steps. Public facilities, including toilets and parking, are conveniently located nearby. The site is diveable year-round, though conditions are often better in winter due to improved visibility. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the pier structures, especially the delicate sea dragon habitats. Always adhere to local marine park regulations.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting rare and unusual creatures.

Pro-Tip:
Spend ample time scanning the pier pylons and seagrass patches very slowly. Weedy sea dragons and seahorses are masters of disguise, blending seamlessly with their environment. A patient approach and a good dive light will significantly increase your chances of a magical encounter.

75-word excerpt:
Flinders Pier, Mornington Peninsula (2-8m), is a beginner-friendly shore dive famed for weedy sea dragons, seahorses, and macro life on encrusted pylons. Visibility (2-8m) is best year-round, influenced by runoff and currents. Easy access and nearby facilities make it ideal for relaxed exploration and night diving. Requires careful navigation near the pier and keen observation for camouflaged wonders in Victoria's temperate waters."""

# Article for Portsea Pier (ID 16)
article_text_16 = """# Portsea Pier: Mornington Peninsula's Macro Marvel and Seahorse Haven for Beginner Divers

On the southern tip of the Mornington Peninsula, Victoria, Portsea Pier stands as an iconic and highly accessible dive site, perfectly suited for beginner divers and macro photography enthusiasts. Descending to shallow depths between 3 to 10 metres, this extensive pier structure is a vibrant underwater gallery, attracting a phenomenal array of unique marine life. Famous for its resident seahorses, cuttlefish, and a plethora of captivating nudibranchs, Portsea Pier offers an enchanting experience during the prime season of November to March. Its easy shore access makes it an ideal spot for relaxed explorations into Victoria's cool temperate waters, inviting all to discover its gentle charm and astonishing biodiversity.

The Essentials:
*   Depth Range: An ideal beginner depth range from a shallow 3 metres down to 10 metres, perfect for leisurely observation and macro photography.
*   Visibility: Variable, typically ranging from 5 to 15 metres. Optimal visibility is generally found between November and March, often better on incoming and high tides (when there's sufficient light to see the bottom). As a coastal pier site, visibility is largely influenced by local sediment, coastal runoff, and tidal movements. Strong currents and surge can reduce clarity considerably. The sheltered conditions within the bay behind the pier generally aid visibility, but it can be impacted by local sediment stirred by surge or strong winds.
*   Water Temperature: Water temperatures range from a cool 12°C in winter to a more moderate 20°C in summer. A good wetsuit (7mm+) or drysuit is recommended due to the cooler water.
*   Current/Conditions: Divers can expect some surge, particularly on incoming tides or during periods of stronger oceanic influence. While generally calm, strong southerly swells can create moderate currents around the pier. Shore access makes it relatively easy, but awareness of local conditions is wise.
*   Viz Implications: Strong southerly swells, coastal runoff after rain, and local sediment disturbance are the primary factors in reducing visibility. Planning dives around slack tide and during calmer periods will ensure the best clarity and ease of navigation.

Terrain & Navigation:
Portsea Pier features a terrain dominated by its extensive wooden pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom beneath and around the pier is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the pier and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. Compass readings can be unreliable under the metal structure, so navigation relies on visual cues from the pier itself.

Marine Life Highlights:
This iconic pier is a macro photographer's paradise, particularly famous for its resident **seahorses**, including the common big-belly seahorse and occasionally the elusive weedy sea dragon. Divers frequently encounter curious cuttlefish, often camouflaged amongst the rocks, and elegant pipefish. A dazzling array of colourful nudibranchs, various crabs, and schooling fish add vibrancy to the site. Keep an eye out for inquisitive octopus, various species of wrasse, and a variety of smaller reef fish. The healthy growth on the pylons supports diverse invertebrate life, making it a macro enthusiast's dream.

Logistics & Facilities:
Portsea Pier offers excellent shore access, with easy entry directly from the beach or steps. Public facilities, including toilets and parking, are conveniently located nearby. The optimal diving season is from November to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the pier structures, especially the delicate seahorse habitats. Always adhere to local marine park regulations.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting rare and unusual creatures.

Pro-Tip:
To maximise your chances of spotting seahorses and other camouflaged macro life, move very slowly and deliberately, carefully scanning the pier pylons and seagrass. Diving on an incoming or high tide often brings clearer water and better light conditions under the pier.

75-word excerpt:
Portsea Pier, Mornington Peninsula (3-10m), is a beginner-friendly macro haven famed for seahorses, cuttlefish, and nudibranchs. Visibility is variable (5-15m), best November-March on incoming/high tides, influenced by surge and cold water. Easy access and nearby facilities make it ideal for relaxed photography and new divers. Requires careful navigation near the pier and keen observation for camouflaged wonders in Victoria's temperate waters."""

# Article for Five Fathom Reef (ID 20)
article_text_20 = """# Five Fathom Reef: Rockingham's Vibrant Reef System for Intermediate Divers

Off the stunning coastline of Rockingham, Western Australia, Five Fathom Reef stands as a popular and vibrant reef system, ideally suited for intermediate divers. Descending to depths between 8 to 20 metres, this extensive reef is renowned for its diverse hard coral formations, healthy fish life, and frequent encounters with reef sharks and graceful rays. Accessible exclusively by boat, Five Fathom Reef offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species. It’s an inviting site for those seeking engaging encounters with groupers, stingrays, and a bustling array of reef fish against a backdrop of healthy coral ecosystems during the prime season of September to March.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 8 to 20 metres, offering a good vertical range along the reef.
*   Visibility: Generally good, but can be impacted by swell. Typically ranges from 10 to 20 metres (best in low swell under 1m). Optimal visibility is generally found between September and March. As an oceanic site, visibility is largely influenced by strong oceanic currents and offshore weather systems. While consistently good year-round, it can be reduced by surge and localized plankton blooms during warmer months. Strong currents can reduce clarity by stirring up sediment. GPS is used to locate the site; underwater navigation relies on natural reef features and wreck structures (if present).
*   Water Temperature: Water temperatures are comfortably warm, ranging from 18°C to 24°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. Surge can also be significant, particularly during larger ocean swells. This is a boat-only dive, requiring careful planning and execution. Awareness of boat traffic in the area is also wise.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary factors in reducing visibility. Swell (especially over 1m) and occasional surge can also contribute to turbid conditions. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Five Fathom Reef features a diverse terrain of hard coral formations, rocky outcrops, and sand channels. The reef structures are heavily adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef contours. Divers will find numerous ledges, gutters, and small caves to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive. Compass readings may be unreliable near any wreck structure.

Marine Life Highlights:
This vibrant reef is home to an incredible array of marine life. Divers can expect frequent encounters with various species of reef sharks, often patrolling the reef edge, and graceful stingrays resting on the sandy bottom. Impressive groupers often take shelter in the larger reef structures. Schools of reef fish, including snapper, morwong, and parrotfish, add vibrancy to the coral gardens. Keep an eye out for inquisitive blue gropers, wobbegong sharks tucked away under ledges, and a dazzling array of macro life, including nudibranchs, clinging to the corals.

Logistics & Facilities:
Access to Five Fathom Reef is exclusively by boat, typically arranged through dive charter operators in Rockingham or Fremantle. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is from September to March for warmer waters and peak marine activity, coinciding with generally calmer weather. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate coral ecosystems and its inhabitants.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents and surge, and adept at navigating reef systems with challenging features. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant coral and frequent wildlife encounters.

Pro-Tip:
Due to the presence of sharks and rays, maintain a respectful distance and observe calmly. If the site includes any wreck components, be aware of potential magnetic interference with your compass and rely on visual navigation. Always dive with a buddy and carry a surface marker buoy (SMB).

75-word excerpt:
Five Fathom Reef, Rockingham (8-20m), is an intermediate boat dive with hard corals, reef sharks, and rays. Visibility (10-20m) is best September-March in low swell, influenced by oceanic currents and surge. It hosts groupers and stingrays. This dynamic site demands moderate current/surge handling and good navigation for a rewarding exploration of its vibrant coral ecosystems and frequent wildlife encounters off Western Australia's coast."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(6, "Flinders Pier", article_text_6)
update_article_in_db_and_combined_file(16, "Portsea Pier", article_text_16)
update_article_in_db_and_combined_file(20, "Five Fathom Reef", article_text_20)
