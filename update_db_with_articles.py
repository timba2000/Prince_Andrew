
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

# Article for North West Solitary Island (ID 182)
article_text_182 = """North West Solitary Island: A Vibrant Fringing Reef for Intermediate Explorers

Just off the coast of Arrawarra, New South Wales, lies the North West Solitary Island, a magnificent fringing reef that beckons intermediate divers. Resting at depths between 8 and 18 metres, this island boasts a thriving underwater ecosystem, characterised by dense fish schools and abundant soft corals. As part of the Solitary Islands Marine Park, it's a testament to pristine marine environments, offering a serene yet dynamic dive experience for those seeking encounters with large marine life and vibrant reef systems. Accessible primarily by boat, it promises an immersive journey into one of Australia’s most biologically diverse temperate-tropical transition zones.

The Essentials:
*   Depth Range: This intermediate dive spans depths from 8 to 18 metres, catering to a good range of exploration.
*   Visibility: Consistently excellent year-round, typically ranging from 20 to 40 metres. However, divers may encounter seasonal thermoclines and plankton blooms during warmer months, which can slightly reduce clarity. Given its minimal coastal runoff from the natural island environment, visibility is largely influenced by strong oceanic currents, localised plankton blooms, and offshore weather systems. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 26°C, making for pleasant diving conditions.
*   Current/Conditions: Divers should anticipate moderate to strong oceanic currents, requiring good finning technique and careful dive planning. The site is generally exposed to ocean swells.
*   Viz Implications: While generally superb, strong oceanic currents can bring in nutrient-rich waters that, at times, may foster plankton blooms, temporarily affecting visibility. Offshore weather systems, particularly during significant swells, can also introduce suspended particles.

Terrain & Navigation:
The terrain around North West Solitary Island primarily consists of a fringing reef, where rocky outcrops give way to vibrant coral gardens and sandy channels. Navigation is relatively straightforward, following the reef's edge. Divers will find numerous gutters, ledges, and small caves to explore, providing ample hiding spots for marine life. The clear water typically allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This site is a haven for an incredible variety of marine life. Divers can expect frequent encounters with graceful green and loggerhead turtles, often seen cruising along the reef. Large schools of vibrant reef fish, including dazzling blue groupers, patrol the coral formations. Various species of rays, from eagle rays to stingrays, can be spotted gliding over sandy patches. The soft corals themselves host an array of smaller invertebrates, adding intricate detail to the dive experience. Keep an eye out for wobbegong sharks tucked away under ledges.

Logistics & Facilities:
Access to North West Solitary Island is exclusively by boat, typically arranged through dive operators in nearby Coffs Harbour or Arrawarra. There are no on-site facilities, so divers must be self-sufficient. The ideal time to dive is during spring and summer (September to March) when water temperatures are at their warmest and marine activity is at its peak. As part of a protected marine park, strict conservation guidelines apply; divers are expected to observe marine life responsibly without touching or disturbing the delicate ecosystem.

Who Is It For?:
This dive is perfectly suited for Intermediate divers who are comfortable with boat entries/exits, capable of handling moderate to strong currents, and adept at navigating reef systems. It's an excellent site for those looking to expand their experience in a pristine and dynamic environment.

Pro-Tip:
Due to the potential for stronger currents, always carry a safety sausage (DSMB) to ensure easy surface detection by your dive boat, especially if drifting away from the main dive group.

75-word excerpt:
North West Solitary Island, off Arrawarra, NSW, is an intermediate boat dive (8-18m) featuring a vibrant fringing reef with dense fish schools and soft corals. Expect excellent visibility (20-40m) year-round, influenced by oceanic currents and plankton blooms. It's a haven for turtles, blue groupers, and rays, offering a pristine and dynamic experience within the Solitary Islands Marine Park for capable divers."""

# Article for Spot X Reef (ID 189)
article_text_189 = """Spot X Reef: Arrawarra's Hidden Gem of Sand and Coral

Hidden just off the natural coastline near Arrawarra, New South Wales, lies Spot X Reef, a captivating patch reef that offers an enticing dive for intermediate divers. Ranging in depth from 5 to 15 metres, this site is a mosaic of sandy gullies intertwined with healthy coral cover, creating a dynamic and visually engaging underwater landscape. Accessible by both boat and shore, it provides a versatile diving experience, revealing a rich tapestry of marine life against a backdrop of unique geological formations. Spot X Reef is a local favourite, known for its tranquil beauty and consistent encounters with fascinating temperate and tropical species.

The Essentials:
*   Depth Range: This intermediate dive is relatively shallow, ranging from 5 to 15 metres, making it accessible for extended bottom times.
*   Visibility: Visibility is variable, typically ranging from 15 to 30 metres. It is influenced by seasonal currents and localised plankton blooms. Optimal visibility often occurs during calmer weather conditions and periods of stable oceanic currents. Being located near a natural coastline with minimal runoff helps maintain generally good clarity. Strong oceanic currents and offshore weather systems are the primary factors that can lead to fluctuations.
*   Water Temperature: Water temperatures are pleasant, ranging from 19°C to 25°C, ensuring comfortable diving throughout much of the year, particularly during spring and summer.
*   Current/Conditions: Divers should be prepared for moderate currents, especially on stronger tidal movements. The site is somewhat exposed to ocean swells, so calmer days are preferable for a more relaxed dive.
*   Viz Implications: While strong oceanic currents can sometimes introduce plankton-rich waters, the minimal coastal runoff generally ensures good clarity. Offshore weather systems, particularly after heavy storms, can briefly reduce visibility.

Terrain & Navigation:
Spot X Reef's terrain is characterised by undulating patch reefs interspersed with wide, sandy gullies. The coral cover varies from extensive hard and soft corals on the reef patches to barren sand in the channels. Navigation is generally easy, following the reef edges or using the sandy channels as pathways. There are plenty of small bommies and overhangs to explore, providing excellent opportunities for finding hidden marine life. The clear water typically allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
Spot X Reef is a delightful site for marine life enthusiasts. Divers frequently encounter graceful stingrays, often found resting in the sandy gullies or cruising slowly over the reef. Various species of wrasse add splashes of colour to the coral gardens, while macro photographers will revel in the diversity of nudibranchs meticulously crawling across the reef. Keep an eye out for schooling fish that can be seen moving between the reef patches, and inquisitive octopus camouflaged within the cracks and crevices.

Logistics & Facilities:
Spot X Reef offers the convenience of both boat and shore access, making it a flexible choice for divers. Shore access is typically via a sandy beach, while boat access can be arranged through local operators. There are no on-site facilities, so divers should be prepared. The best time to dive is during spring and summer (September to March) when the water is warmest and marine activity is often at its peak. Conservation is important here; divers are reminded to respect the delicate coral ecosystems and avoid touching marine life.

Who Is It For?:
This dive is suitable for Intermediate divers comfortable with both shore and boat entries, capable of managing moderate currents, and keen to explore a diverse reef environment. It's a fantastic site for photography and those who enjoy a relaxed yet rewarding dive.

Pro-Tip:
When exploring the sandy gullies at Spot X Reef, move slowly and keep an eye on the sand itself – you might spot camouflaged flatheads, rays, or even unique pipefish nestled amongst the seagrass beds.

75-word excerpt:
Spot X Reef, near Arrawarra, NSW, is an intermediate patch reef dive (5-15m) featuring sandy gullies and coral. Visibility (15-30m) is variable, influenced by seasonal currents and plankton. Accessible by boat or shore, it's home to stingrays, wrasse, and nudibranchs, offering a captivating and versatile dive for those exploring a unique temperate-tropical ecosystem."""

# Execute the updates
update_article_in_db(182, article_text_182)
update_article_in_db(189, article_text_189)
