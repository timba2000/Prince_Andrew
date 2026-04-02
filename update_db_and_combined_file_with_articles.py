
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

# Article for North Bondi Rocks (ID 24)
article_text_24 = """# North Bondi Rocks: A Sheltered Wonderland for Beginner Divers

Nestled in the iconic Bondi Beach, North Bondi Rocks offers a surprisingly sheltered and vibrant dive site, perfectly suited for beginner divers and snorkelers. Located near the famous Bondi Icebergs Club and rock pool, this site plunges to depths of 2 to 12 metres, revealing a rich tapestry of rocky outcrops teeming with diverse marine life. Its accessibility from the shore, coupled with the convenient beach amenities, makes it an ideal spot for an easy and rewarding underwater exploration. North Bondi Rocks is a true hidden gem, providing a tranquil escape from the bustling beach above, inviting all to discover its underwater charm.

The Essentials:
*   Depth Range: An inviting depth range for beginners, from a shallow 2 metres down to 12 metres.
*   Visibility: Visibility typically ranges from 5 to 10 metres. The best conditions for clarity are generally from October to April, with autumn often providing the clearest water (10-15m). However, visibility can be significantly impacted by several factors. Northerly swells churn up sand, while strong easterly swells can drastically reduce visibility to under 3 metres. Rain events, especially heavy ones, can reduce visibility by 50-60% for 2-3 days due to runoff from the large urban catchment of Bondi, Bellevue Hill, and surrounds, exacerbated by the Bondi Beach stormwater drain approximately 600m north. Calm, dry periods with minimal swell are ideal.
*   Water Temperature: Water temperatures are comfortable, ranging from 17°C in cooler months to a pleasant 23°C in summer.
*   Current/Conditions: The site is generally sheltered, but divers should be mindful of some swell and surge, particularly on larger ocean days. Proximity to the beach means awareness of swimmers is also necessary.
*   Viz Implications: Urban runoff after rain and strong swells (especially northerly and easterly) are the primary factors leading to reduced visibility. Choosing a dive day with calm seas and a period of dry weather will yield the best experience.

Terrain & Navigation:
North Bondi Rocks features a varied terrain of rocky outcrops, gutters, and sandy patches. Navigation is straightforward, with divers often following the rock formations. There are numerous small caves and overhangs to explore, providing shelter for various creatures. The site is relatively open, but divers should be aware of the contours to avoid being caught in any surge. The presence of the rock pool provides a clear reference point for entry and exit.

Marine Life Highlights:
This site is surprisingly rich in marine biodiversity. Divers frequently encounter curious leatherjackets and graceful octopus camouflaged amongst the rocks. Various species of rays, including stingrays, can be spotted gliding over the sandy bottom. The site is particularly famous for its resident blue groper, affectionately nicknamed "Lizzo," who is known to be quite friendly with divers. Keep an eye out for colourful nudibranchs and a variety of small reef fish in the cracks and crevices.

Logistics & Facilities:
North Bondi Rocks offers easy shore access directly from Bondi Beach. Ample beach amenities, including toilets and parking (though parking can be challenging on busy days), make it a convenient dive location. The best time to dive is between October and April for warmer waters and generally calmer conditions. Conservation efforts focus on protecting this accessible marine habitat, and divers are encouraged to observe marine life without touching or disturbing the environment.

Who Is It For?:
This is an excellent site for **Beginner** divers and snorkelers. Its sheltered nature, relatively shallow depths, and abundant marine life make it perfect for introductory dives, training, and leisurely explorations. Those looking to spot Lizzo will particularly enjoy this site!

Pro-Tip:
For the best chance to spot "Lizzo" the blue groper, approach slowly and calmly. She is often seen around the rock pools and the main reef structure. A bit of patience can lead to a wonderful encounter with this local celebrity.

75-word excerpt:
North Bondi Rocks, a beginner-friendly shore dive off Bondi Beach (2-12m), boasts rocky outcrops and abundant marine life, including the famous blue groper, Lizzo. Visibility (5-10m) is best October-April, but is impacted by northerly/easterly swells and urban runoff after rain. Its sheltered location and easy access make it ideal for new divers seeking vibrant underwater encounters near Sydney's iconic coastline."""

# Article for Kings Beach – Broken Head (ID 198)
article_text_198 = """# Kings Beach – Broken Head: A Protected Coastal Gem for Beginner Divers

Located within the tranquil embrace of Broken Head, New South Wales, Kings Beach offers a wonderfully protected shore dive, making it an ideal spot for beginner divers and snorkelers. Resting in shallow depths of 3 to 8 metres, this site is a charming mosaic of bommies and rock walls that teem with fascinating marine life. Its natural shelter provides calm conditions, perfect for those new to the underwater world, or for relaxed explorations on "calm days only." Kings Beach is a pristine example of a coastal sanctuary, inviting divers to discover its gentle beauty and the diverse creatures that call its sheltered waters home, just a stone's throw from the Broken Head Nature Reserve.

The Essentials:
*   Depth Range: A very accessible depth range for beginners, from 3 to 8 metres.
*   Visibility: Visibility typically ranges from 6 to 10 metres. While generally good on calm days, it is variable and influenced by heavy rainfall, strong easterly swells, and onshore winds. Optimal conditions are experienced in calmer, drier periods, ideally with offshore winds (westerly) to keep the water clear. Moderate coastal runoff from the Broken Head Nature Reserve can also temporarily reduce clarity after significant rain.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 25°C, making for pleasant diving throughout much of the year.
*   Current/Conditions: The site is generally protected, but divers should be aware that swells can still affect the area, especially on less calm days. It is strongly recommended to dive here only during calm conditions to ensure optimal enjoyment and safety.
*   Viz Implications: Heavy rainfall and strong easterly swells are the main culprits for reduced visibility, bringing in sediment and creating turbid conditions. Onshore winds can also contribute to stirred-up particles. Choosing a dive day with minimal swell and dry weather is key for the best experience.

Terrain & Navigation:
Kings Beach features a delightful terrain of scattered bommies (small, isolated reef outcrops) and natural rock walls. These structures provide excellent shelter and habitat for marine life. Navigation is straightforward due to the shallow depths and the protected nature of the site, allowing divers to leisurely explore the various formations. The sandy channels between the bommies offer contrasting scenery and opportunities to spot camouflaged creatures. The clear, calm water on good days makes for easy orientation and relaxed exploration.

Marine Life Highlights:
This protected site is a vibrant hub of marine activity. Divers will frequently encounter various species of eels, often peeking out from rocky crevices. Graceful rays can be spotted gliding over the sandy bottom, while a myriad of wrasse species add splashes of colour to the bommies. Keep an eye out for octopus and cuttlefish, masters of camouflage, as well as a variety of juvenile reef fish. The healthy rock walls and bommies support diverse invertebrate life, providing endless macro opportunities.

Logistics & Facilities:
Kings Beach offers convenient shore entry, making it highly accessible for divers. While there are no dedicated dive facilities directly at the beach, basic amenities can be found nearby in Broken Head. The best time to dive is on calm days, ensuring optimal visibility and enjoyment. As part of a natural reserve area, conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the delicate ecosystem and its inhabitants.

Who Is It For?:
This is an ideal site for **Beginner** divers and snorkelers. Its shallow, protected waters, combined with rich marine life and easy access, make it perfect for introductory dives, training, and peaceful underwater observation. It's a superb site for building confidence.

Pro-Tip:
Due to the variable conditions, it's always a good idea to check local weather and swell forecasts before planning a dive at Kings Beach. Aim for days with minimal easterly swell and light winds for the best possible experience.

75-word excerpt:
Kings Beach – Broken Head, a beginner-friendly shore dive in NSW (3-8m), boasts protected bommies and rock walls teeming with eels, rays, and wrasse. Visibility (6-10m) is influenced by rainfall, easterly swells, and onshore winds; best on calm, dry days. Its natural shelter and rich marine life make it perfect for relaxed exploration and building dive confidence near Broken Head Nature Reserve."""

# Execute the updates
update_article_in_db_and_combined_file(24, "North Bondi Rocks", article_text_24)
update_article_in_db_and_combined_file(198, "Kings Beach – Broken Head", article_text_198)
