
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

# Article for Port Lincoln Jetty (ID 99)
article_text_99 = """# Port Lincoln Jetty: Eyre Peninsula's Urban Macro Haven for Beginner Divers

On the vibrant shores of the Eyre Peninsula, South Australia, Port Lincoln Jetty offers an accessible and surprisingly rich shore dive, perfectly suited for beginner divers and macro enthusiasts. Descending to shallow depths between 2 to 7 metres, this urban jetty is a bustling underwater gallery, famous for its mix of macro life and sponge-covered pylons. Its easy jetty access and nearby facilities make it an ideal spot for relaxed explorations from October to March, revealing a hidden world of fascinating squid, small rays, and colourful leatherjackets. Port Lincoln Jetty is a cherished local treasure, a dynamic aquatic microcosm where urban convenience meets abundant marine biodiversity, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An ideal beginner depth range from a shallow 2 metres down to 7 metres, perfect for leisurely observation and macro photography.
*   Visibility: Variable, typically ranging from 5 to 7 metres, but can extend to 10 metres on exceptionally clear days. Optimal visibility is generally found between October and March, often better on incoming tides during calmer conditions. However, it is significantly impacted by moderate runoff from the Port Lincoln town and harbour, heavy rainfall, strong tidal currents within the harbour, and boat traffic. Strong southerly winds can also reduce clarity. Planning dives around slack tide and during calmer, drier periods will ensure the best clarity and ease of navigation.
*   Water Temperature: Water temperatures range from a cool 14°C in winter to a more moderate 20°C in summer. A good wetsuit (5-7mm) is recommended.
*   Current/Conditions: Divers can expect some gentle to moderate tidal currents around the jetty pylons, especially within the harbour. The site is generally sheltered, but awareness of localized currents and boat traffic is wise. Low visibility can be a factor, especially after rain or with strong currents.
*   Viz Implications: Heavy rainfall, strong tidal currents, and moderate urban runoff are the primary factors in reducing visibility. Boat activity can also stir up sediment. Planning dives around slack tide and during calmer, drier periods will ensure the best experience.

Terrain & Navigation:
Port Lincoln Jetty features a terrain dominated by its extensive wooden pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom beneath and around the jetty is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the jetty and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. Compass readings can be unreliable under the metal structure, so navigation relies on visual cues from the jetty itself.

Marine Life Highlights:
This vibrant urban jetty is a macro photographer's paradise. Divers frequently encounter curious squid, often seen hovering around the pylons, and graceful small rays resting on the sandy bottom. Various species of colourful leatherjackets add vibrancy to the site. Keep an eye out for octopus, cuttlefish, and a dazzling array of colourful nudibranchs clinging to the pylons. The healthy growth on the pylons supports diverse invertebrate life, making it a macro enthusiast's dream. Juvenile fish often shelter amongst the structures.

Logistics & Facilities:
Port Lincoln Jetty offers excellent shore access, with easy entry directly from the jetty. Public facilities, including toilets, parking, and cafes, are conveniently located nearby. The site is diveable from October to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the jetty structures, especially the delicate sponge and macro habitats. Always adhere to local marine park regulations.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting fascinating small creatures.

Pro-Tip:
Due to the consistent macro life, move slowly and deliberately around the jetty pylons, carefully scanning the sponge growth. A good dive light, even during the day, will illuminate hidden creatures and bring out the true colours of the encrusting life. Consider a night dive for different encounters.

75-word excerpt:
Port Lincoln Jetty, Eyre Peninsula (2-7m), is a beginner-friendly shore dive with urban access, famed for macro life and sponge-covered pylons. Visibility (5-7m) is best October-March on incoming tides, influenced by runoff, currents, and boat traffic. It hosts squid, small rays, and leatherjackets. Ideal for relaxed macro photography and new divers, it offers a vibrant microcosm of marine biodiversity near town amenities."""

# Article for Port Neill Jetty (ID 117)
article_text_117 = """# Port Neill Jetty: Eyre Peninsula's Quiet Macro Retreat for Beginner Divers

On the serene eastern coastline of the Eyre Peninsula, South Australia, Port Neill Jetty offers a wonderfully quiet and accessible shore dive, perfectly suited for beginner divers and macro enthusiasts. Descending to shallow depths between 2 to 7 metres, this easy-access jetty is a charming underwater garden, famous for its prolific sponge growth and the sheltered, calm conditions it provides. Its easy shore access and nearby parking make it an ideal spot for relaxed explorations from October to March, revealing a hidden world of fascinating squid, graceful rays, and schooling juvenile fish. Port Neill Jetty is a cherished local treasure, a vibrant aquatic microcosm where natural beauty meets abundant and friendly marine life, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An ideal beginner depth range from a shallow 2 metres down to 7 metres, perfect for leisurely observation and macro photography.
*   Visibility: Variable, typically ranging from 5 to 7 metres, but can extend to 10 metres on exceptionally clear days. Optimal visibility is generally found between October and March, often better on incoming tides during calmer conditions. However, it is influenced by minimal coastal runoff from the small town, strong southerly winds, and tidal currents, which can stir up sediment. Disturbance from human activity can also impact clarity. Calm, dry periods with light offshore winds are ideal.
*   Water Temperature: Water temperatures are comfortable, ranging from 15°C in cooler months to a pleasant 21°C in summer. A good wetsuit (5-7mm) is recommended.
*   Current/Conditions: Divers can expect some gentle tidal currents around the jetty pylons. The site is generally sheltered, but awareness of strong southerly winds and tidal currents is wise. Low visibility can be a factor, especially after rain or with strong currents.
*   Viz Implications: Strong southerly winds and tidal currents are the primary factors in reducing visibility by stirring up sediment. Minimal coastal runoff after rain also plays a role. Planning dives around slack tide and during calmer, drier periods will ensure the best experience.

Terrain & Navigation:
Port Neill Jetty features a terrain dominated by its extensive wooden pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom beneath and around the jetty is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the jetty and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. Compass readings can be unreliable under the metal structure, so navigation relies on visual cues from the jetty itself.

Marine Life Highlights:
This quiet jetty is a macro photographer's dream. Divers frequently encounter curious squid, often seen hovering around the pylons, and graceful small rays resting on the sandy bottom. Various species of colourful wrasse, bream, and other juvenile fish add vibrancy to the site. Keep an eye out for octopus, cuttlefish, and a dazzling array of colourful nudibranchs clinging to the pylons. The healthy growth on the pylons supports diverse invertebrate life, making it a macro enthusiast's dream. Juvenile fish often shelter amongst the structures.

Logistics & Facilities:
Port Neill Jetty offers excellent shore access, with easy entry directly from the jetty. Public parking and basic amenities are conveniently located nearby. The site is diveable from October to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the jetty structures, especially the delicate sponge and macro habitats. Always adhere to local marine park regulations.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting fascinating small creatures.

Pro-Tip:
Move slowly and deliberately around the jetty pylons, carefully scanning the sponge growth and crevices. Many macro creatures are masters of disguise and require a keen eye and patience to spot. Consider a night dive for a completely different set of encounters and behaviours.

75-word excerpt:
Port Neill Jetty, Eyre Peninsula (2-7m), is a beginner-friendly shore dive with calm conditions, famed for sponge growth and macro life. Visibility (5-7m) is best October-March, influenced by southerly winds and tidal currents. It hosts squid, rays, and juvenile fish. Easy access and nearby amenities make it ideal for relaxed macro photography and new divers seeking unique small marine life in a tranquil setting."""

# Article for Streaky Bay Jetty (ID 106)
article_text_106 = """# Streaky Bay Jetty: Eyre Peninsula's West Coast Gem for Beginner Divers

On the rugged yet tranquil west coast of the Eyre Peninsula, South Australia, Streaky Bay Jetty offers a wonderfully calm and accessible shore dive, perfectly suited for beginner divers. Descending to shallow depths between 2 to 6 metres, this easy-access jetty is a charming underwater garden, famous for its calm conditions and regular sightings of graceful stingrays. Its easy jetty access and nearby amenities make it an ideal spot for relaxed explorations from November to March, revealing a hidden world of fascinating crabs, curious octopus, and abundant macro life. Streaky Bay Jetty is a cherished local treasure, a vibrant aquatic microcosm where natural beauty meets abundant and friendly marine life, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An ideal beginner depth range from a shallow 2 metres down to 6 metres, perfect for leisurely observation and macro photography.
*   Visibility: Variable, typically ranging from 5 to 6 metres, but can extend to 10 metres on exceptionally clear days. Optimal visibility is generally found between November and March, often better on incoming tides during calmer conditions. However, it is influenced by minimal runoff from Streaky Bay town, strong southerly winds, and tidal currents, which can stir up sediment. Disturbance from human activity and fishing debris can also impact clarity. Calm, dry periods with light offshore winds are ideal.
*   Water Temperature: Water temperatures range from a cool 14°C in winter to a more moderate 20°C in summer. A good wetsuit (5-7mm) is recommended.
*   Current/Conditions: Divers can expect some gentle tidal currents around the jetty pylons. The site is generally calm and sheltered, but awareness of strong southerly winds and tidal currents is wise. Low visibility can be a factor, especially after rain or with strong winds/currents.
*   Viz Implications: Strong southerly winds and tidal currents are the primary factors in reducing visibility by stirring up sediment. Minimal coastal runoff after rain also plays a role. Planning dives around slack tide and during calmer, drier periods will ensure the best experience.

Terrain & Navigation:
Streaky Bay Jetty features a terrain dominated by its extensive wooden pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom beneath and around the jetty is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the jetty and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. Compass readings can be unreliable under the metal structure, so navigation relies on visual cues from the jetty itself. Divers should be mindful of fishing debris.

Marine Life Highlights:
This quiet jetty is a macro photographer's dream. Divers frequently encounter graceful **stingrays**, often resting on the sandy bottom or cruising around the pylons. Various species of crabs scuttle across the bottom, and curious octopus can be seen camouflaged amongst the rocks and sponges. Keep an eye out for a dazzling array of colourful nudibranchs clinging to the pylons, as well as various species of wrasse and juvenile fish. The healthy growth on the pylons supports diverse invertebrate life, making it a macro enthusiast's dream.

Logistics & Facilities:
Streaky Bay Jetty offers excellent shore access, with easy entry directly from the jetty. Public parking and basic amenities are conveniently located nearby. The site is diveable from November to March for warmer waters and generally calmer conditions. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the jetty structures, especially the delicate sponge and macro habitats. Always adhere to local marine park regulations and be mindful of fishing activities.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant, unique macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting fascinating small creatures.

Pro-Tip:
Due to the regular presence of stingrays, maintain a respectful distance and observe them calmly without disturbance. Move slowly and deliberately around the jetty pylons, carefully scanning the sponge growth and crevices for hidden macro gems. Consider a night dive for a completely different set of encounters and behaviours.

75-word excerpt:
Streaky Bay Jetty, Eyre Peninsula (2-6m), is a beginner-friendly shore dive famed for calm conditions and regular stingray sightings. Visibility (5-6m) is best November-March on incoming tides, influenced by southerly winds and tidal currents. It hosts crabs, octopus, and abundant macro life. Easy access and nearby amenities make it ideal for relaxed photography and new divers seeking unique small marine life on South Australia's west coast."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(99, "Port Lincoln Jetty", article_text_99)
update_article_in_db_and_combined_file(117, "Port Neill Jetty", article_text_117)
update_article_in_db_and_combined_file(106, "Streaky Bay Jetty", article_text_106)
