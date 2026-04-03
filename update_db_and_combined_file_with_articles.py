
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

# Article for Gordon's Bay (ID 58)
article_text_58 = """# Gordon's Bay: Sydney's Underwater Nature Trail for Beginners

Nestled between Clovelly and Coogee, Gordon's Bay in New South Wales offers a truly serene and accessible dive experience, making it a perfect sanctuary for beginner divers and snorkelers. This calm bay, with depths ranging from 3 to 12 metres, is famous for its unique underwater nature trail—a rope guided path leading you through fascinating rocky reefs and sandy patches. Its sheltered conditions and easy shore access via steps make it an ideal spot for relaxed explorations year-round. Gordon's Bay is a cherished local treasure, a vibrant aquatic classroom where urban convenience meets abundant marine life, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An inviting depth range for beginners, from a shallow 3 metres down to 12 metres, perfect for relaxed exploration.
*   Visibility: Typically ranges from 5 to 10 metres. While generally good year-round, especially in autumn/winter (10-15m), it can be significantly impacted. Easterly swells over 1m stir up sand, reducing clarity. After rain, visibility drops to 3-5m for 1-2 days due to moderate urban stormwater runoff from Coogee and Randwick, exacerbated by the Coogee Beach stormwater drain approximately 500m north. South-easterly storms can push turbid water across the bay. Calm, dry periods with light offshore winds are ideal. Summer visibility is variable (5-12m), and spring (6-10m) can see plankton blooms.
*   Water Temperature: Water temperatures are comfortable, ranging from 17°C in cooler months to a pleasant 23°C in summer.
*   Current/Conditions: The bay is generally calm and sheltered, making it very safe for beginners. However, divers should be aware of low visibility in swell. While largely protected, very strong easterly swells might still cause some agitation at the entrance.
*   Viz Implications: Urban runoff after rain and easterly swells are the primary factors leading to reduced visibility. South-easterly storms can also bring turbid water. Choosing a dive day with calm seas and a period of dry weather will ensure the best experience.

Terrain & Navigation:
Gordon's Bay is characterized by its unique underwater nature trail, a rope that guides divers through the main points of interest, including rocky reefs, sandy areas, and patches of seagrass. This trail makes navigation incredibly easy and enjoyable. The terrain is a mix of boulders and rocky outcrops adorned with colourful sponges and soft corals, interspersed with sandy channels. The clear water, when present, allows for excellent visual navigation and observation.

Marine Life Highlights:
This protected bay is a vibrant hub of marine activity. Divers frequently encounter curious octopus, often camouflaged amongst the rocks, and elegant cuttlefish displaying their mesmerising colour changes. Schools of bream and various species of wrasse dart amongst the reef structures. Keep an eye out for friendly blue gropers, shy dumpling squid, and a variety of smaller invertebrates. The healthy seagrass beds are also a nursery for juvenile fish, making it a fantastic site for macro photography.

Logistics & Facilities:
Gordon's Bay offers excellent shore access via steps, making it highly accessible for divers. While there are no dedicated dive facilities directly at the bay, basic amenities can be found nearby in Clovelly and Coogee. The site is diveable year-round, with calm conditions making it a reliable choice. Conservation is paramount here; divers are encouraged to practice responsible diving, staying on the nature trail, avoiding disturbance to the marine life, and respecting the delicate ecosystem.

Who Is It For?:
This is an ideal site for **Beginner** divers and snorkelers, as well as families and those seeking a relaxing and safe marine experience. Its calm waters, unique nature trail, and abundant, friendly marine life make it perfect for introductory dives, training, and peaceful underwater photography.

Pro-Tip:
Follow the underwater nature trail ropes to ensure you don't miss any of the key features and to help navigate the bay efficiently. Take your time to observe the smaller creatures that often hide amongst the rocks and seagrass.

75-word excerpt:
Gordon's Bay, Sydney (3-12m), is a beginner-friendly shore dive with an underwater nature trail. Visibility (5-10m) is best in autumn/winter, but impacted by urban runoff and easterly swells. It hosts octopus, cuttlefish, and bream. Its sheltered nature and easy access make it ideal for relaxed exploration, particularly for new divers, offering a vibrant aquatic classroom near Sydney's eastern beaches."""

# Article for Wedding Cake Island (ID 71)
article_text_71 = """# Wedding Cake Island: Coogee's Exposed Reef with Diverse Marine Life for Intermediate Divers

Just off Coogee Beach, New South Wales, Wedding Cake Island stands as a prominent and dynamic dive site, ideally suited for intermediate divers. Ranging in depth from 8 to 16 metres, this rocky reef offers an exciting underwater landscape, characterized by fascinating swim-throughs and a rich diversity of marine life. Accessible primarily by boat, Wedding Cake Island presents a thrilling challenge due to its exposure to ocean swells and varied visibility conditions. It’s a site that constantly offers something new, from schooling fish to larger pelagics, making it a beloved spot for those seeking an adventurous and rewarding experience in Sydney's temperate waters.

The Essentials:
*   Depth Range: An intermediate dive with depths ranging from 8 to 16 metres, suitable for divers comfortable with moderate depths.
*   Visibility: Highly variable, typically ranging from 10 to 15 metres, but it is one of the most unpredictable sites in the area, capable of being 2m or 20m on different days. It is very swell-exposed; any swell over 1m reduces visibility. Southerly storms can drastically drop clarity to 1-2m. Cold upwellings from the south can occasionally bring very clear deep water, boosting visibility to 15m+. The Coogee Beach stormwater drain, approximately 300m north, and urban runoff from Coogee, also impact visibility. Optimal conditions are found between October and April, but careful daily assessment is crucial.
*   Water Temperature: Water temperatures range from 17°C in cooler months to a pleasant 23°C in summer.
*   Current/Conditions: Divers can expect surge and strong currents, particularly on incoming tides and during larger ocean swells. This is an exposed site that demands excellent finning skills and vigilant situational awareness. Boat traffic in the area also requires caution.
*   Viz Implications: High swell exposure, southerly storms, and urban stormwater runoff are the primary factors in reducing visibility. Cold water upwellings can sometimes provide exceptional clarity. Divers must be prepared for rapidly changing conditions.

Terrain & Navigation:
Wedding Cake Island features a rugged rocky reef with numerous gutters, ledges, and fascinating swim-throughs carved into the rock. Navigation involves carefully following the reef contours and exploring the various passages. The terrain transitions to sandy patches at its base, where different marine life can be found. Good buoyancy control is essential to navigate the swim-throughs gracefully and to avoid stirring up sediment from the bottom. Given the potential for variable visibility, familiarity with the site or a local guide is highly recommended.

Marine Life Highlights:
This vibrant reef is home to a diverse array of marine life. Divers frequently encounter curious octopus and large, friendly blue gropers. Various species of morwong and schooling fish, including trevally and kingfish, patrol the reef structure. Keep an eye out for wobbegong sharks tucked under ledges and a variety of colourful nudibranchs. The swim-throughs often provide shelter for smaller reef fish, offering excellent macro opportunities.

Logistics & Facilities:
Access to Wedding Cake Island is exclusively by boat, typically arranged through dive operators in Coogee or nearby areas. There are no on-site facilities, so divers must be self-sufficient. The optimal diving season is from October to April for warmer waters and peak marine activity. However, due to its exposed nature, successful dives are highly dependent on favourable weather and swell conditions. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the delicate reef ecosystem and its inhabitants.

Who Is It For?:
This is an excellent site for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling surge and strong currents, and adept at navigating reef systems with challenging features like swim-throughs. It offers a thrilling and rewarding experience for those seeking diverse marine life and dynamic conditions.

Pro-Tip:
Due to the extreme variability in visibility, it is absolutely essential to check local dive reports and weather forecasts immediately before planning a trip to Wedding Cake Island. Prioritise calm days with minimal swell for the best chance of an exceptional dive.

75-word excerpt:
Wedding Cake Island, Coogee (8-16m), is an intermediate boat dive with rocky reefs, swim-throughs, and diverse marine life including octopus and groper. Visibility (10-15m, highly variable) is impacted by swell, storms, and urban runoff, but can be boosted by cold upwellings. Exposed to surge and currents, it demands skilled diving and careful weather assessment for a rewarding experience near Coogee Beach."""

# Article for Osprey Reef (ID 7)
article_text_7 = """# Osprey Reef: Coral Sea's Pristine Atoll for Advanced Liveaboard Adventurers

Far out in the pristine Coral Sea, Queensland, lies Osprey Reef—a truly world-class atoll offering an unparalleled advanced diving experience. Plunging from the surface to beyond 40 metres, this stunning oceanic reef is celebrated for its dramatic wall diving, colossal pelagic encounters, and impeccably pristine coral ecosystems. Accessible exclusively by liveaboard, Osprey Reef is a remote diver's paradise, promising thrilling shark encounters (grey, silvertip, hammerhead), majestic rays, and an explosion of reef fish in visibility often exceeding 40 metres. It's a bucket-list destination for those seeking the ultimate untouched, big-animal diving adventure.

The Essentials:
*   Depth Range: An advanced dive from the surface down to 40 metres (and beyond for technical diving), offering dramatic wall dives.
*   Visibility: Consistently excellent, often exceeding 40 metres, making it one of the clearest dive sites globally. Minimal coastal runoff, as it's an isolated offshore reef, contributes to its superb clarity. However, strong oceanic currents can sometimes bring in localised plankton blooms, temporarily affecting visibility. Seasonal thermoclines may also be present. Optimal conditions are generally found between June and November, though excellent visibility is experienced year-round.
*   Water Temperature: Water temperatures are consistently warm, ranging from 24°C to 29°C, ensuring comfortable diving throughout the year.
*   Current/Conditions: Divers should be prepared for potentially strong oceanic currents, requiring good finning technique and careful dive planning. The reef is exposed to open ocean conditions, so while generally calm during the prime season, offshore weather systems can influence conditions. Underwater navigation relies on the natural reef walls and depth contours.
*   Viz Implications: While strong oceanic currents can occasionally lead to plankton blooms, the remote nature of the reef minimises external factors, ensuring consistently high visibility. Offshore weather systems are the main external influence.

Terrain & Navigation:
Osprey Reef is a spectacular underwater atoll characterized by dramatic vertical walls that plunge into the abyss. The terrain includes sheer drop-offs, deep canyons, and extensive plateau areas adorned with an incredible diversity of hard and soft corals. Navigation is primarily visual, following the reef walls, often with the assistance of a dive guide. The vastness of the site demands careful dive planning, especially for multi-level and drift dives. The pristine condition of the reef is a visual feast, offering endless photographic opportunities.

Marine Life Highlights:
Osprey Reef is a true big-animal hotspot. It is world-renowned for its thrilling shark encounters, with frequent sightings of grey reef sharks, silvertip sharks, and the majestic scalloped hammerheads. Divers will also marvel at graceful manta rays and eagle rays, various species of reef fish, barracuda, and trevally schooling in the blue. The healthy coral gardens are home to an array of macro life, adding another layer of interest to this vibrant ecosystem. This is a site where every dive holds the promise of an awe-inspiring encounter.

Logistics & Facilities:
Access to Osprey Reef is exclusively via liveaboard dive vessels, typically departing from Cairns or Port Douglas. Due to its remote location in the Coral Sea, it is not accessible for day trips. Liveaboards provide all necessary facilities, including dive gear, accommodation, and meals. The optimal diving season is from June to November for generally calmer weather and peak pelagic activity. Conservation is paramount; Osprey Reef is a highly protected area, and divers are expected to adhere to strict marine park regulations, including no-touch policies and responsible interaction with marine life.

Who Is It For?:
This is an **Advanced** dive site, suitable for experienced divers comfortable with deep profiles, drift diving, and encounters with large marine predators. Strong finning skills and excellent buoyancy control are essential. It's an ultimate destination for adventure seekers and serious underwater photographers.

Pro-Tip:
Consider taking a dedicated underwater camera setup for Osprey Reef – the consistently clear water and abundance of large marine life provide unparalleled photographic opportunities. Participate in organised shark feeds (if offered) for an exhilarating and controlled encounter, but always follow your dive guide's instructions precisely.

75-word excerpt:
Osprey Reef, Coral Sea (0-40m), is an advanced liveaboard destination renowned for dramatic wall diving, big pelagics, and pristine corals. Visibility often exceeds 40m, influenced by oceanic currents. It teems with grey nurse, silvertip, and hammerhead sharks, plus majestic rays and reef fish. Remote and challenging, it's a bucket-list site for experienced divers seeking untouched, big-animal encounters in crystal-clear waters."""

# Article for Dolphin Reef – Crescent Head (ID 219)
article_text_219 = """# Dolphin Reef – Crescent Head: A Scenic Reef for Intermediate Divers

Off the picturesque coastline of Crescent Head, New South Wales, lies Dolphin Reef—a beautiful rocky reef dive site perfectly suited for intermediate divers. Ranging in depth from 8 to 16 metres, this reef is famously named for the frequent sightings of dolphins in its vicinity, adding a magical element to every dive. Accessible primarily by boat, Dolphin Reef offers a vibrant underwater landscape, showcasing a healthy ecosystem with snapper, rays, and turtles. It’s an inviting site for those seeking a tranquil yet rewarding exploration, promising a blend of scenic beauty and delightful marine encounters off a natural headland.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 8 to 16 metres, offering a good vertical range along the reef.
*   Visibility: Variable, typically ranging from 10 to 15 metres. It is influenced by strong easterly swells, strong currents, and high winds. Optimal visibility is often best during calm periods, especially from October to March, with minimal coastal runoff from the natural headland. However, it can be very turbulent and murky with strong swells, dropping to 8m or less. Light offshore winds and flat seas are ideal.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 18°C to 24°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers can expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. The site is exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive. Boat traffic is also a consideration given its accessibility by charter.
*   Viz Implications: Strong easterly swells, strong currents, and high winds are the primary factors in reducing visibility, creating turbulent and murky conditions. Heavy rainfall, though minimal from the natural headland, can also contribute. Planning dives during calm weather is crucial for the best experience.

Terrain & Navigation:
Dolphin Reef features a rugged rocky reef terrain with numerous ledges, gutters, and sand patches. The reef structures are adorned with a variety of soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef's contours. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This site is renowned for its diverse marine life. Divers can expect frequent encounters with schooling snapper and various species of graceful rays, including stingrays and eagle rays. Green and loggerhead turtles are often seen cruising along the reef or resting in sheltered spots. Keep an eye out for inquisitive blue gropers, wobbegong sharks tucked away under ledges, and a dazzling array of colourful reef fish. The healthy ecosystem supports diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Dolphin Reef is exclusively by boat, typically arranged through dive charter operators in Crescent Head. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is from October to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate ecosystem.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents, and adept at navigating reef systems. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with frequent wildlife encounters.

Pro-Tip:
Keep an eye on the surface during your boat ride and safety stops – the frequent dolphin sightings that give the reef its name are a spectacular bonus to any dive trip here!

75-word excerpt:
Dolphin Reef, Crescent Head (8-16m), is an intermediate boat dive on a rocky reef, famous for frequent dolphin sightings, snapper, rays, and turtles. Visibility (10-15m) is variable, best in calm conditions (October-March), but impacted by easterly swells and strong currents. It offers a scenic and vibrant exploration for capable divers, demanding awareness of dynamic ocean conditions and showcasing rich marine life."""

# Article for Racecourse Reef – Crescent Head (ID 214)
article_text_214 = """# Racecourse Reef – Crescent Head: A Fringing Reef Adventure for Intermediate Divers

Also off the picturesque coastline of Crescent Head, New South Wales, Racecourse Reef offers an engaging fringing reef dive, ideally suited for intermediate divers. Ranging in depth from 6 to 14 metres, this site is characterized by its captivating coral bommies and ledges, creating a dynamic and visually stimulating underwater environment. Accessible primarily by boat, Racecourse Reef promises a rewarding exploration into a healthy marine ecosystem, teeming with morwong, stingrays, and gropers. It’s an excellent choice for those seeking vibrant reef life and a scenic dive within the natural beauty of the Hat Head National Park surrounds.

The Essentials:
*   Depth Range: This intermediate dive explores depths from 6 to 14 metres, offering a good vertical range along the reef.
*   Visibility: Variable, typically ranging from 10 to 12 metres, but can extend to 18 metres on exceptionally clear days. Optimal visibility is often best from October to March, particularly during calmer, drier periods. It is influenced by moderate coastal runoff from Hat Head National Park, heavy rainfall, strong easterly swells, and onshore winds. Prevailing easterly winds and swells can stir up sediment, reducing clarity. Calm, dry periods with light offshore winds are ideal.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 18°C to 24°C, making for pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers should expect moderate currents, especially on incoming tides or during periods of stronger oceanic influence. The site is exposed to ocean swells, so calmer conditions are preferable for a more relaxed dive. Boat traffic is also a consideration given its accessibility by charter.
*   Viz Implications: Heavy rainfall, strong easterly swells, and onshore winds are the primary factors in reducing visibility, bringing in sediment and creating turbid conditions. Moderate coastal runoff can also contribute. Planning dives during calm, dry weather is crucial for the best experience.

Terrain & Navigation:
Racecourse Reef features a fringing reef terrain with numerous coral bommies and ledges that provide ample shelter and habitat for marine life. Navigation is relatively straightforward, following the reef contours. Divers will find various crevices and overhangs to explore, offering hiding spots for smaller creatures. The terrain transitions to sandy patches at its base, where different marine life can be found. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive.

Marine Life Highlights:
This vibrant reef is home to a diverse array of marine life. Divers can expect frequent encounters with large schools of morwong and various species of graceful stingrays, often found resting in sandy areas. Impressive gropers often take shelter in the larger reef structures. Keep an eye out for inquisitive blue gropers, wobbegong sharks tucked away under ledges, and a dazzling array of colourful reef fish. The healthy coral ecosystems support diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Racecourse Reef is exclusively by boat, typically arranged through dive charter operators in Crescent Head. There are no on-site facilities directly at the dive site, so divers must be self-sufficient. The optimal diving season is from October to March for warmer waters and peak marine activity. Conservation is paramount; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate ecosystem.

Who Is It For?:
This dive is perfectly suited for **Intermediate** divers who are comfortable with boat entries/exits, capable of handling moderate currents, and adept at navigating reef systems. It's an excellent site for those looking to expand their experience in a scenic and dynamic environment with vibrant reef life.

Pro-Tip:
When diving Racecourse Reef, pay close attention to the smaller crevices and overhangs within the bommies and ledges. These often hide a fascinating array of macro life, including nudibranchs and small crustaceans, that are easily overlooked during a faster swim-through.

75-word excerpt:
Racecourse Reef, Crescent Head (6-14m), is an intermediate boat dive with fringing reef, coral bommies, and ledges. Visibility (10-12m) is variable, best in calm, dry periods (October-March), impacted by coastal runoff, rainfall, and easterly swells. It hosts morwong, stingrays, and gropers, offering a rewarding exploration for capable divers seeking vibrant reef life and a scenic dive within Hat Head National Park surrounds."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(58, "Gordon's Bay", article_text_58)
update_article_in_db_and_combined_file(71, "Wedding Cake Island", article_text_71)
update_article_in_db_and_combined_file(7, "Osprey Reef", article_text_7)
update_article_in_db_and_combined_file(219, "Dolphin Reef – Crescent Head", article_text_219)
update_article_in_db_and_combined_file(214, "Racecourse Reef – Crescent Head", article_text_214)
