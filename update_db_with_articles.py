
import sqlite3

def update_article_in_db(site_id, article_text):
    try:
        conn = sqlite3.connect('dive_sites.db')
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE dive_sites SET article_status = ?, article_full_text = ? WHERE ID = ?",
            ('Completed', article_text, site_id)
        )
        conn.commit()
        print(f"Successfully updated article for Site ID {site_id}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

# Article for Port Noarlunga Reef (ID 78)
article_text_78 = """Port Noarlunga Reef: Adelaide's Underwater Wonderland for Beginners

Just a stone's throw from the popular jetty, Port Noarlunga Reef in Adelaide, SA, stands as a premier underwater playground for beginner divers and snorkelers alike. This shallow, protected reef, ranging from 2 to 10 metres in depth, is renowned for its incredible biodiversity and fascinating swim-throughs. Easily accessible from the shore, it offers a welcoming and safe environment for those new to the underwater world, or for experienced divers seeking a relaxed and rich photographic opportunity. The reef is a vibrant tapestry of marine life, making it an ideal spot to witness the beauty of South Australia's temperate waters without venturing far offshore.

The Essentials:
*   Depth Range: An excellent beginner dive, ranging from a very shallow 2 metres to a maximum of 10 metres.
*   Visibility: Visibility typically ranges from 6 to 10 metres. The best conditions for clear water are from October to March. However, similar to nearby coastal areas, visibility can be negatively impacted by moderate runoff from the Onkaparinga River and coastal development, heavy rainfall, river outflow, and strong south-westerly swells. Expect variable visibility (5-15m), often better in late summer and autumn. It can be quite poor after heavy winter rains. Prevailing south-westerly winds and swell can significantly reduce clarity by stirring up sediment.
*   Water Temperature: Water temperatures are comfortable, ranging from 16°C in cooler months to a pleasant 22°C in summer.
*   Current/Conditions: Generally calm and protected, though some mild surge can be present, particularly near the reef's edge or during stronger swells. Divers should also be aware of boat traffic when accessing from shore.
*   Viz Implications: Heavy rainfall and strong south-westerly swells are the primary factors that can lead to reduced visibility due to runoff and sediment. Calm, dry periods are best for optimal conditions.

Terrain & Navigation:
Port Noarlunga Reef is a long, natural limestone reef running parallel to the shore. Its most defining features are the numerous channels and swim-throughs carved into the reef, creating an exciting labyrinth to explore. The reef is carpeted with a variety of algae, sponges, and invertebrate life, providing a rich visual tapestry. Navigation is easy due to the reef's linear nature and the clear presence of the jetty overhead, which serves as an excellent reference point.

Marine Life Highlights:
This reef is a biodiversity hotspot. Divers will frequently encounter schools of bream and various species of wrasse darting amongst the reef structures. Colourful seastars are abundant, clinging to the rock formations. Keep an eye out for octopus, cuttlefish, and shy dumpling squid. The reef is also a nursery for juvenile fish, and occasionally, you might spot larger predatory fish passing by. Macro enthusiasts will delight in the many nudibranchs and smaller invertebrates.

Logistics & Facilities:
Port Noarlunga Reef boasts exceptional accessibility, with entry directly from the shore via the jetty. This makes it a perfect spot for independent divers and groups. Facilities nearby include public toilets and ample parking, adding to its convenience. The best time to dive is between October and March when the water is warmer and conditions are generally more stable. Conservation is paramount here, and divers are encouraged to practice a "look but don't touch" policy to protect this precious ecosystem.

Who Is It For?:
This is an ideal site for Beginner divers and snorkelers. Its shallow depths, protected environment, and easy access make it perfect for introductory dives, training, and leisurely explorations.

Pro-Tip:
Explore the jetty pylons before heading out to the reef; they are often covered in interesting marine growth and provide shelter for unique macro life, offering a fantastic opportunity for photography even before reaching the main reef.

75-word excerpt:
Port Noarlunga Reef, off Adelaide (2-10m), is a beginner-friendly gem with rich biodiversity and swim-throughs. Best visibility (6-10m) is October-March, though runoff and south-westerly swells can reduce clarity. Accessible from shore, it teems with bream, wrasse, and seastars, offering a safe, vibrant underwater experience perfect for new divers and snorkelers."""

# Article for North Haven Wall (ID 91) - already successfully updated in DB, but included for completeness if needed for future script modifications
article_text_91 = """North Haven Wall: Adelaide's Thriving Artificial Reef for Intermediate Divers

Nestled off the coast of Adelaide, the North Haven Wall is a remarkable artificial reef wall, beckoning intermediate divers to explore its depths. Resting between 5 to 14 metres, this submerged structure has blossomed into a bustling ecosystem, teeming with schooling fish and vibrant sponge growth. A testament to successful marine conservation efforts, the wall provides a rich and engaging dive experience, primarily accessible by boat. It's a sanctuary where nature and human ingenuity converge, offering a unique opportunity to witness the dynamic marine life thriving within its carefully constructed contours.

The Essentials:
*   Depth Range: This intermediate dive generally ranges from 5 to 14 metres.
*   Visibility: Visibility is quite variable, typically between 8 and 12 metres. The best conditions for clarity are usually from October to March, particularly during incoming tides and dry periods. However, significant runoff from the nearby marina and urban areas, heavy rainfall, strong northerly winds, and frequent boat traffic can drastically reduce visibility, sometimes to as little as 3-5 metres. Strong northerly winds are particularly detrimental as they can stir up sediment.
*   Water Temperature: Expect water temperatures to fluctuate between a cool 16°C in winter and a more pleasant 22°C in summer.
*   Current/Conditions: Divers should be prepared for moderate currents, especially on tidal movements, requiring good awareness and finning techniques.
*   Viz Implications: Heavy rainfall, strong northerly winds, and boat traffic are key factors in reducing visibility. Planning dives during calm, dry periods and incoming tides will yield the best conditions.

Terrain & Navigation:
The North Haven Wall is a linear artificial structure, now heavily adorned with sponges, soft corals, and other sessile organisms. Its clear, defined shape makes navigation relatively straightforward, with divers often following its length. The wall provides numerous ledges and crevices, offering hiding spots for smaller creatures and an excellent backdrop for marine photography. While generally open, divers should maintain good buoyancy to avoid stirring up sediment from the bottom.

Marine Life Highlights:
The wall is a vibrant habitat, particularly known for its large schools of fish that often envelop divers. Expect to encounter various species of leatherjackets, gracefully navigating the structure. Rays are frequent visitors, gliding silently across the sandy patches adjacent to the wall. Keep an eye out for inquisitive squid, which can often be seen hovering or camouflaging themselves against the reef. The sponge growth itself provides micro-habitats for a plethora of smaller invertebrates.

Logistics & Facilities:
Access to the North Haven Wall is exclusively by boat, typically launched from nearby boat ramps. There are no on-site facilities directly at the dive site. The prime diving season is from October to March, offering warmer waters and generally more favourable conditions. Divers should always be aware of boat traffic in the area and display a dive flag. Conservation efforts focus on protecting this vital artificial reef and its inhabitants, encouraging responsible diving practices.

Who Is It For?:
This dive is perfectly suited for Intermediate divers who are comfortable with boat entries/exits, navigating in potentially variable visibility, and managing moderate currents. It offers an excellent opportunity to progress skills in a stimulating environment.

Pro-Tip:
Consider carrying a slate and pencil to note down the different species of sponges and corals you encounter on the North Haven Wall – it’s a surprisingly diverse and beautiful botanical garden underwater!

75-word excerpt:
The North Haven Wall, an intermediate boat dive off Adelaide, is a vibrant artificial reef bustling with schooling fish and sponges. Visibility (8-12m) is best October-March, especially during incoming tides, but is affected by runoff, heavy rain, and northerly winds. It offers an engaging experience for divers comfortable with currents, exploring its unique marine landscape."""

# Execute the update for Port Noarlunga Reef (ID 78)
update_article_in_db(78, article_text_78)
