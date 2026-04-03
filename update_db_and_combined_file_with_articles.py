
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

# Article for Wedge Island Caves (ID 121)
article_text_121 = """# Wedge Island Caves: Spencer Gulf's Dramatic Cave System for Advanced Divers

Off the rugged coast of Spencer Gulf, South Australia, lies Wedge Island, home to an exhilarating cave system perfectly suited for advanced divers: the Wedge Island Caves. Descending to depths between 12 and 25 metres, this site is renowned for its dramatic walls, intricate cave passages, and the impressive pelagic species that patrol its surroundings. Accessible exclusively by boat, Wedge Island Caves offers a thrilling and demanding dive experience, promising encounters with snapper, various sharks, and colourful nudibranchs within a dynamic and often calm bay. It’s a bucket-list destination for experienced divers seeking unique geological formations and abundant marine life in South Australia’s temperate waters.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 12 to 25 metres, suitable for divers comfortable with overhead environments.
*   Visibility: Generally good, especially in the sheltered bay behind the island where conditions are often calm. Visibility is best during summer months. Strong oceanic currents outside the bay can influence overall clarity, and localised plankton blooms may occur. The calm water conditions within the bay behind Wedge Island typically lead to very good visibility, but conditions outside can be more variable. Strong swells from the Southern Ocean, while less impactful inside the bay, can still affect clarity in exposed areas.
*   Water Temperature: Water temperatures range from a cool 14°C in winter to a more comfortable 19°C in summer.
*   Current/Conditions: Divers can expect some currents, especially near the entrances to the caves and outside the sheltered bay. Navigation within the cave system requires excellent buoyancy control and awareness of the overhead environment. This is a boat-only dive, requiring careful planning and execution.
*   Viz Implications: While the sheltered bay usually ensures good visibility, any strong oceanic currents or significant swells outside the bay can introduce turbid water. Divers should plan their dives for calm weather to maximise visibility and safety within the caves.

Terrain & Navigation:
Wedge Island Caves features a dramatic underwater terrain of impressive cave entrances and tunnels. Navigation within the cave system demands meticulous planning, excellent buoyancy control, and appropriate training for overhead environments. The walls are adorned with unique invertebrate life, while the sandy bottom areas host a variety of benthic creatures. Outside the caves, rocky reefs and kelp forests add to the diversity. The site's clear water, when present, aids significantly in navigation, but reliance on a dive guide experienced with the caves is paramount.

Marine Life Highlights:
This site is teeming with interesting marine life, both inside and outside the caves. Divers frequently encounter schools of snapper and various species of sharks, including wobbegongs and, occasionally, larger pelagic species patrolling the entrance. Colourful nudibranchs can be found meticulously crawling across the cave walls and reef surfaces. Keep an eye out for curious blue devils, various reef fish, and shy cuttlefish. The cave system itself provides shelter for unique species adapted to low light.

Logistics & Facilities:
Access to Wedge Island Caves is exclusively by boat, typically arranged through dive charter operators from nearby ports on the Eyre Peninsula. There are no on-site facilities directly at the dive site. The optimal diving season is during summer (December to February) for warmer waters and calmer conditions. Conservation is paramount; divers are expected to adhere to strict guidelines for cave diving, avoiding disturbance to the delicate cave ecosystems and marine life.

Who Is It For?:
This is an **Advanced** dive site, suitable only for highly experienced divers with specialised training in cave or cavern diving. Excellent physical fitness, advanced diving certifications, and comfort with overhead environments are essential. It's an ultimate destination for adventure seekers and serious cave explorers.

Pro-Tip:
Due to the overhead environment, always carry at least two independent light sources and ensure your buddy is also properly equipped. Practise your buoyancy control before entering the caves to minimise silt disturbance and maximise visibility for yourself and others.

75-word excerpt:
Wedge Island Caves, Spencer Gulf (12-25m), is an advanced boat dive into a dramatic cave system. Visibility is generally good in the sheltered bay (best in summer), with snapper, sharks, and nudibranchs. Requires cave/cavern training and excellent buoyancy due to overhead environment and potential currents. A thrilling geological and wildlife experience for proficient divers seeking unique exploration in South Australia's temperate waters."""

# Article for Hardwicke Bay Jetty (ID 122)
article_text_122 = """# Hardwicke Bay Jetty: Yorke Peninsula's Quiet Macro Haven for Beginners

On the tranquil shores of the Yorke Peninsula, South Australia, Hardwicke Bay Jetty offers a wonderfully quiet and accessible dive experience, perfectly suited for beginner divers and macro enthusiasts. Descending to shallow depths between 3 to 7 metres, this site is a charming underwater garden, famous for its abundant sponge growth and the sheltered, calm conditions it provides. Its easy jetty access makes it an ideal spot for relaxed explorations from October to April, revealing a hidden world of fascinating marine life. Hardwicke Bay Jetty is a cherished local treasure, a vibrant aquatic microcosm where urban convenience meets astonishing biodiversity, inviting all to discover its gentle charm and diverse ecosystems.

The Essentials:
*   Depth Range: An ideal depth range for beginners, from a shallow 3 metres down to 7 metres, perfect for leisurely observation.
*   Visibility: Typically ranges from 5 to 7 metres. While generally good during the prime season, it can be influenced by local sediment and disturbance. Optimal visibility is generally found between October and April, particularly during calm, dry periods. The sheltered conditions within the bay help maintain clarity, but strong winds or local disturbances can reduce it. Heavy rainfall, though minimal impact due to the wide bay, could temporarily affect clarity. Expect some variability due to the sandy/silty bottom.
*   Water Temperature: Water temperatures are comfortable, ranging from 15°C in cooler months to a pleasant 22°C in summer.
*   Current/Conditions: The jetty area is exceptionally calm and sheltered, making it very safe for beginners. There is minimal current or surge, making it a truly relaxing experience. Low visibility in swell can occur, but generally, the bay offers protected conditions.
*   Viz Implications: Low visibility can occur in strong swells or after heavy rain due to stirred-up sediment, though the shallow, sheltered nature helps mitigate this. Calm conditions are paramount for the best experience.

Terrain & Navigation:
Hardwicke Bay Jetty features a terrain dominated by the jetty pylons, which are heavily encrusted with a diverse array of sponges, ascidians, and algae. The sandy bottom around the jetty is home to various benthic creatures and patches of seagrass. Navigation is incredibly easy due to the linear structure of the jetty and its shallow depths. Divers can leisurely explore the pylons, observing the macro life, or venture out to the surrounding seagrass beds. The clear water, when present, allows for excellent visual navigation and observation.

Marine Life Highlights:
This quiet jetty is a macro photographer's dream. Divers frequently encounter curious squid, often seen hovering around the pylons, and delicate seahorses expertly camouflaged amongst the sponge growth or seagrass. Various species of rays can be spotted gliding gracefully over the sandy bottom. Keep an eye out for octopus, cuttlefish, and an array of smaller invertebrates clinging to the jetty structures. The sheltered conditions make it an ideal environment for observing juvenile fish and various colourful nudibranchs.

Logistics & Facilities:
Hardwicke Bay Jetty offers convenient jetty access, making it highly accessible for divers. While there are no dedicated dive facilities directly at the jetty, basic amenities can be found nearby in the town. The site is diveable from October to April for warmer waters and generally calmer conditions. Conservation is paramount here; divers are encouraged to practice responsible diving, avoiding disturbance to the marine life or the jetty structures, especially the delicate sponges and seahorse habitats.

Who Is It For?:
This is an ideal site for **Beginner** divers and macro photographers, as well as those seeking a relaxing and safe marine experience. Its shallow, calm waters and abundant macro life make it perfect for introductory dives, training, and peaceful underwater photography, particularly for spotting unique small creatures.

Pro-Tip:
Move slowly and deliberately around the jetty pylons, carefully scanning the sponge growth and seagrass. Seahorses are masters of camouflage and require a keen eye and patience to spot. Bringing a macro lens will truly enhance your photographic opportunities.

75-word excerpt:
Hardwicke Bay Jetty, Yorke Peninsula (3-7m), is a beginner-friendly shore dive with abundant sponge growth and calm conditions. Visibility (5-7m) is best October-April, influenced by local sediment. It hosts squid, seahorses, and rays. Its sheltered nature and easy access make it ideal for relaxed macro photography and new divers seeking unique small marine life in a tranquil setting."""

# Article for Fairy Bower (ID 50)
article_text_50 = """# Fairy Bower: Manly's Enchanting Aquatic Reserve for All Levels

Nestled between Manly Beach and Shelly Beach, Fairy Bower in Manly, New South Wales, offers an enchanting and highly accessible dive site suitable for all levels of divers and snorkelers. With gentle slopes descending to depths of 5 to 12 metres, this site is renowned for its vibrant reef ledges, captivating swim-throughs, and excellent visibility. As part of the Cabbage Tree Bay Aquatic Reserve, Fairy Bower is a protected marine sanctuary, offering year-round access and a high chance of encountering resident wobbegongs, graceful stingrays, and elusive cuttlefish. It’s a cherished local jewel, a lively aquatic playground where stunning natural beauty meets abundant and friendly marine life.

The Essentials:
*   Depth Range: Suitable for all levels, depths range from a shallow 5 metres to a maximum of 12 metres, perfect for relaxed and extended dives.
*   Visibility: Generally good, ranging from 10 to 15 metres. Optimal visibility is usually from October to March. While less swell-exposed than Shelly Beach, it is still influenced by oceanic conditions. Moderate northerly or easterly swells can reduce visibility to 4-6m. Rain events affect visibility within 24-48 hours due to some Manly urban stormwater runoff from the peninsula, though it experiences less direct runoff than Shelly Beach. Overall, summer averages 10m, winter 7m, and spring (6-10m) can see plankton blooms. Calm days are best.
*   Water Temperature: Water temperatures are comfortable, ranging from 17°C in cooler months to a pleasant 23°C in summer.
*   Current/Conditions: The site generally features a gentle slope with minimal currents, making it very safe for all levels. However, occasional swell can be present, particularly during larger ocean days. It is a well-protected bay, but being mindful of local conditions is always wise.
*   Viz Implications: Urban stormwater runoff after rain and moderate northerly/easterly swells are the primary factors leading to reduced visibility. Plankton blooms in spring can also affect clarity. Diving during calm, dry periods will ensure the best experience.

Terrain & Navigation:
Fairy Bower features a gentle sloping reef terrain characterized by distinct ledges, rocky outcrops, and fascinating swim-throughs. The reef structures are heavily adorned with a rich variety of sponges, soft corals, and anemones. Navigation is incredibly easy due to the natural contours of the reef and its shallow depths. Divers can leisurely explore the various formations, follow the ledges, or venture through the swim-throughs. The clear water, when present, allows for excellent visual navigation and observation.

Marine Life Highlights:
This enchanting sanctuary is teeming with marine life. Divers frequently encounter majestic wobbegong sharks, often resting camouflaged under ledges. Graceful stingrays can be spotted gliding over the sandy bottom, while elusive cuttlefish display their mesmerizing colour changes. Schools of bream, wrasse, and other colourful reef fish add vibrancy to the coral gardens. Keep an eye out for friendly blue gropers (though less common than at Clovelly), octopus, and an array of macro life such as nudibranchs.

Logistics & Facilities:
Fairy Bower offers excellent shore access, with steps leading directly to the water. Convenient amenities are available, including showers and easy access to Manly's facilities. The site is diveable year-round, with consistently good conditions making it a reliable choice. As part of a protected aquatic reserve, strict conservation guidelines apply; divers are encouraged to practice responsible diving, observing marine life without touching or disturbing the delicate ecosystem.

Who Is It For?:
This is an ideal site for **All Levels** of divers and snorkelers. Its gentle conditions, accessible depths, and abundant, friendly marine life make it perfect for introductory dives, training, refresher courses, and peaceful underwater photography. It's a superb site for enjoying Sydney's vibrant marine ecosystems.

Pro-Tip:
Due to the popularity of the site, especially on weekends, consider diving early in the morning or on weekdays for a more tranquil experience. Pay close attention to the smaller crevices and ledges for hidden macro gems and camouflaged creatures.

75-word excerpt:
Fairy Bower, Manly (5-12m), is an enchanting all-level shore dive with reef ledges and swim-throughs, part of Cabbage Tree Bay Aquatic Reserve. Visibility (10-15m) is best October-March, influenced by swell and urban runoff. It hosts wobbegongs, stingrays, and cuttlefish, offering year-round access and abundant marine life for relaxed exploration. Features showers and easy access near Manly Beach."""

# Article for Neptune Islands (Shark Cage) (ID 142)
article_text_142 = """# Neptune Islands (Shark Cage): Eyre Peninsula's Ultimate Great White Encounter for Advanced Divers

Off the rugged coast of the Eyre Peninsula, South Australia, the Neptune Islands stand as a globally renowned and utterly thrilling destination for advanced divers seeking the ultimate adrenaline rush: Great White Shark cage diving. Descending to depths between 10 to 30 metres (within the safety of the cage), this remote pelagic zone is famous for its consistent encounters with one of the ocean's most formidable predators. Accessible exclusively by specially equipped charter boat, the Neptune Islands promise an unparalleled, year-round experience for advanced divers and thrill-seekers. It’s a bucket-list adventure, offering a rare and awe-inspiring glimpse into the world of great white sharks and the powerful pelagic ecosystem.

The Essentials:
*   Depth Range: An advanced dive with cage depths ranging from 10 to 30 metres, focusing on controlled observation of great white sharks.
*   Visibility: Typically ranges from 15 to 30 metres, often excellent. Visibility is generally influenced by strong oceanic currents and offshore weather systems. While consistently good year-round, it can be reduced by localised plankton blooms, especially during warmer months. The remote offshore location ensures minimal coastal runoff impact. Divers should anticipate that the presence of bait for shark attraction can sometimes reduce immediate visibility around the cage, but overall water clarity is high.
*   Water Temperature: Water temperatures range from a cool 14°C in winter to a more moderate 20°C in summer. Thick wetsuits (7mm+) or drysuits are recommended.
*   Current/Conditions: Divers should be prepared for strong oceanic currents. The site is in an exposed pelagic zone, so conditions can vary significantly with weather and swell. Cage diving ensures safety, but physical comfort can be impacted by rough seas. This is a charter boat access-only experience.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary influences on natural visibility. The use of chum and bait around the cage can temporarily reduce immediate visibility for close-up views. Divers must be prepared for dynamic open-ocean conditions.

Terrain & Navigation:
The terrain around Neptune Islands is characterized by rocky reefs and vast open ocean. For cage diving, the focus is on the pelagic zone surrounding the islands. Navigation within the cage is, of course, restricted, but observing the underwater environment outside the cage involves scanning the open blue water and the deep reef formations below. The remoteness and exposed nature mean no fixed underwater trails or structures for navigation beyond the cage itself. Safety protocols are paramount, guided by the experienced crew.

Marine Life Highlights:
Undoubtedly, the star attraction is the **Great White Shark**. Divers are virtually guaranteed encounters with these magnificent predators. Beyond the sharks, the pelagic zone around the islands is rich with other marine life, including various species of tuna, large schools of trevally, and occasionally other shark species like bronze whalers. Graceful seals often interact with the surface activities. This is an unparalleled opportunity for big-animal encounters and witnessing apex predators in their natural habitat.

Logistics & Facilities:
Access to Neptune Islands is exclusively by specially equipped liveaboard or day-charter boats that depart from Port Lincoln. Due to the remote location, participants must book with a reputable and licensed shark cage diving operator. All necessary equipment and facilities are typically provided on board. The optimal time for great white shark encounters is year-round, though specific seasons might offer different levels of activity. Conservation is paramount; operators adhere to strict regulations to ensure the safety of both divers and sharks, promoting ethical interactions.

Who Is It For?:
This is an **Advanced** dive experience, suitable for thrill-seeking divers who are comfortable in open ocean environments and understand the inherent risks of interacting with large predators. While cage diving minimises direct danger, a basic level of diving fitness and comfort in the water is essential. It's a life-changing adventure for those seeking unparalleled wildlife encounters.

Pro-Tip:
Listen meticulously to your dive masters' briefings and follow all safety instructions without deviation. Be prepared for potentially rough boat rides to and from the islands. While in the cage, stay calm, breathe steadily, and keep your camera ready – these moments are fleeting and truly extraordinary!

75-word excerpt:
Neptune Islands (Shark Cage), Eyre Peninsula (10-30m), is an advanced, year-round liveaboard destination for thrilling Great White Shark encounters. Visibility (15-30m) is influenced by oceanic currents and bait. It teems with great whites and tuna in a remote pelagic zone. This ultimate bucket-list adventure requires cage diving, charter access, and a preparedness for strong currents and dynamic open-ocean conditions for an awe-inspiring wildlife experience."""

# Article for Yena Gap (ID 55)
article_text_55 = """# Yena Gap: Kamay Botany Bay NP's Remote Deep Dive for Advanced Explorers

Within the historical confines of Kamay Botany Bay National Park, New South Wales, Yena Gap presents a challenging and remote dive site strictly for advanced divers. Descending to depths between 10 to 26 metres, this dramatic site is characterized by impressive drop-offs and intriguing cave formations, offering a truly adventurous exploration. Accessible by a long walk or boat, Yena Gap rewards proficient divers with encounters with majestic bull rays and vast schools of fish against a backdrop of rugged underwater topography. It’s a site that demands respect and meticulous planning, promising a unique journey into Sydney's wilder, less-frequented marine landscapes.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 10 to 26 metres, featuring dramatic drop-offs.
*   Visibility: Moderate, typically ranging from 5 to 10 metres year-round. It is best after extended dry periods in summer; winter can be clearer in settled conditions. Visibility is significantly impacted by Botany Bay industrial and stormwater runoff from Port Botany, as it receives catchment from the Cooks River and surrounding industrial areas. Post-rain turbidity from Port Botany and Cooks River can last 3-5 days. North winds push murky port water towards the site. The best visibility is experienced after a week of dry weather, ideally with light offshore winds.
*   Water Temperature: Water temperatures range from a cool 16°C in winter to a pleasant 21°C in summer.
*   Current/Conditions: Divers can expect surge and potentially strong currents, particularly around the drop-offs and cave entrances. This is a remote site with no facilities, demanding self-sufficiency and excellent physical fitness, especially for the long walk-in option. Strong currents and surge are significant considerations.
*   Viz Implications: Urban and industrial runoff after rain and north winds are the primary factors in reducing visibility. Planning dives for extended dry periods with minimal northern wind influence is crucial for the best experience.

Terrain & Navigation:
Yena Gap features a dramatic and rugged underwater terrain of steep drop-offs, deep gutters, and intriguing cave formations. Navigation requires careful planning due to its remote nature, potential for strong currents, and variable visibility. Divers will need to follow distinct reef contours and be mindful of their depth and ascent rates, especially near the overhead environments of the caves. The deep reef structure provides abundant hiding spots and intricate swim-throughs for those with excellent buoyancy control and experience in more challenging environments. Reliance on a dive guide familiar with the site is highly recommended.

Marine Life Highlights:
Despite its challenging access, Yena Gap is home to impressive marine life. Divers frequently encounter majestic bull rays, often cruising along the drop-offs or resting on sandy patches. Large schools of various fish species, including trevally and kingfish, patrol the deeper sections. Keep an eye out for wobbegong sharks tucked under ledges, curious blue devilfish, and the possibility of spotting sea dragons amongst the kelp and sponge gardens. The caves themselves may offer shelter to unique invertebrates.

Logistics & Facilities:
Access to Yena Gap is remote and can be challenging. It can be reached either by a long walk through Kamay Botany Bay National Park or by boat. There are no on-site facilities, so divers must be completely self-sufficient and prepared for a wilderness dive. The optimal diving season is from spring to summer (September to March) for warmer waters and potentially better visibility, but success hinges on recent weather patterns. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the fragile deep reef ecosystem and its inhabitants, and respecting the national park environment.

Who Is It For?:
This is an **Advanced** dive site, suitable only for highly experienced divers who are comfortable with deep profiles, strong currents, significant surge, and navigating complex reef structures with overhead environments. Excellent physical fitness, advanced diving certifications, and self-sufficiency are essential due to its remote and demanding nature.

Pro-Tip:
Due to the remote location and challenging entry/exit (if walking), it is highly advisable to dive Yena Gap with an experienced local guide. Always carry a robust surface marker buoy (SMB) and ensure your dive plan accounts for potential low visibility and strong currents. Pack light for the walk-in, but don't compromise on essential safety gear.

75-word excerpt:
Yena Gap, Kamay Botany Bay NP (10-26m), is an advanced, remote dive with dramatic drop-offs and caves. Visibility (5-10m) is best after dry periods, impacted by urban/industrial runoff and north winds. It hosts bull rays and large fish schools. Requiring a long walk or boat access, it demands advanced skills, self-sufficiency, and meticulous planning for challenging conditions within Sydney's wilder marine landscapes."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(121, "Wedge Island Caves", article_text_121)
update_article_in_db_and_combined_file(122, "Hardwicke Bay Jetty", article_text_122)
update_article_in_db_and_combined_file(50, "Fairy Bower", article_text_50)
update_article_in_db_and_combined_file(142, "Neptune Islands (Shark Cage)", article_text_142)
update_article_in_db_and_combined_file(55, "Yena Gap", article_text_55)
