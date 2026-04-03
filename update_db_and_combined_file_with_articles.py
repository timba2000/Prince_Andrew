
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

# Article for Shark Cave (ID 36)
article_text_36 = """# Shark Cave, Rottnest Island: Western Australia's Thrilling Shark Encounters for Advanced Divers

Off the pristine shores of Rottnest Island, Western Australia, lies Shark Cave—a truly exhilarating and renowned dive site perfectly suited for advanced divers. Descending to depths between 18 and 30 metres, this site is a captivating cave system, famously popular for consistent observations of impressive grey nurse sharks. Accessible exclusively by boat, Shark Cave offers a thrilling and demanding dive experience, promising unforgettable encounters with these majestic predators, along with various crayfish and schooling sweep. It’s a bucket-list destination for experienced divers seeking unique geological formations and close-up marine interactions in Western Australia's temperate waters, particularly during the prime season of November to April.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 18 to 30 metres, involving an overhead environment.
*   Visibility: Generally excellent, often exceeding 20 metres on calm days. Optimal visibility is typically found between November and April. As an oceanic cave system, it benefits from minimal coastal runoff. Visibility is largely influenced by strong oceanic currents and offshore weather systems. While consistently good year-round, it can be reduced by surge and localized plankton blooms during warmer months. Strong currents outside the cave can affect overall clarity. Internal navigation within the cave system relies on guidelines, not direct visual cues from the surface.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 19°C to 24°C, ensuring pleasant diving conditions throughout the prime season.
*   Current/Conditions: Divers can expect moderate to strong currents, particularly near the cave entrance and outside the sheltered sections. Surge can also be significant, especially during larger ocean swells. This is a boat-only dive, requiring careful planning and execution for an overhead environment.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary factors in reducing visibility outside the cave. Within the cave, diver-induced silt can reduce visibility, making good buoyancy control essential. Planning dives during calm weather and periods of lighter currents will ensure the best experience.

Terrain & Navigation:
Shark Cave features a dramatic cave system carved into the rocky reef, with imposing entrances and intriguing passages. Navigation within the cave demands meticulous planning, excellent buoyancy control, and appropriate training for overhead environments. Divers will follow guidelines and rely on their training to explore the various sections. Outside the cave, rocky reefs and kelp forests add to the diversity. The clear water, when present, aids significantly in orientation, but reliance on a dive guide experienced with the caves is paramount. Compass readings are unreliable near the cave.

Marine Life Highlights:
This site is world-renowned for its aggregations of **grey nurse sharks**, which are often found resting within the cave system, providing incredible photographic opportunities. Divers will also encounter various crayfish tucked into rocky crevices and large schools of sweep patrolling the entrance. Keep an eye out for inquisitive wobbegong sharks, colourful nudibranchs, and a variety of smaller reef fish. The cave system itself provides shelter for unique species adapted to low light. Encounters with larger pelagics in the surrounding waters are also possible.

Logistics & Facilities:
Access to Shark Cave is exclusively by boat, typically arranged through dive charter operators from Fremantle or Hillarys Boat Harbour. There are no on-site facilities directly at the dive site. The optimal diving season is from November to April for warmer waters and peak grey nurse shark activity. Conservation is paramount; divers are expected to adhere to strict guidelines for cave diving, avoiding disturbance to the delicate cave ecosystems and marine life, and adhering to safe penetration practices (if qualified and equipped).

Who Is It For?:
This is an **Advanced** dive site, suitable only for highly experienced divers with specialised training in cave or cavern diving. Excellent physical fitness, advanced diving certifications, and comfort with overhead environments are essential. It's an ultimate destination for adventure seekers and serious underwater photographers.

Pro-Tip:
Due to the overhead environment and the presence of sharks, always dive Shark Cave with a buddy who is equally experienced, and ensure all your gear is in excellent working order. Carry at least two independent light sources and be proficient in line-following techniques. Plan your dive to minimise silt disturbance within the cave.

75-word excerpt:
Shark Cave, Rottnest Island (18-30m), is an advanced boat dive cave system famed for grey nurse sharks, crayfish, and schooling sweep. Visibility (over 20m on calm days) is best November-April, influenced by oceanic currents and surge. This bucket-list site demands specialised cave diving training, excellent buoyancy, and careful planning for its overhead environment and thrilling marine encounters in Western Australia's clear temperate waters."""

# Article for Wreck of the Alert (ID 22)
article_text_22 = """# Wreck of the Alert: Phillip Island's Historic Clipper Wreck for Advanced Divers

Off the rugged coastline of Phillip Island, Victoria, lies the historic Wreck of the Alert—a captivating and challenging dive site perfectly suited for advanced divers. Resting at depths between 18 and 33 metres, this decommissioned clipper wreck is a testament to maritime history, now transformed into a vibrant artificial reef heavily adorned with soft corals. Its vast structure provides an intricate exploration of a bygone era, teeming with diverse species. Accessible exclusively by boat, the Wreck of the Alert promises an exhilarating journey into an underwater museum, blending maritime heritage with a thriving marine ecosystem, making it a premier wreck dive in Victoria's cooler temperate waters, particularly during the prime season of December to March.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 18 to 33 metres, making it suitable for divers comfortable with deeper profiles and decompression procedures.
*   Visibility: Variable, but can be remarkable when conditions are right. Typically ranges from 10 to 25 metres. Optimal visibility is generally found between December and March. As a coastal wreck site, visibility is largely influenced by coastal conditions, strong currents, and tidal movements. Strong southerly swells and heavy rainfall can reduce clarity considerably. The visibility can also be impacted by localized plankton blooms during warmer months. Reliable near the wreck due to magnetic interference is not applicable for recreational diving; underwater navigation relies heavily on natural wreck features. Planning dives around slack tide will offer the best clarity.
*   Water Temperature: Water temperatures range from a cool 13°C in winter to a more moderate 20°C in summer. A good wetsuit (7mm+) or drysuit is recommended due to the cooler water.
*   Current/Conditions: Divers can expect moderate to strong currents, especially on tidal movements around the wreck. Surge can also be significant, particularly during larger ocean swells. This is a boat-only dive, requiring careful planning and execution.
*   Viz Implications: Strong southerly swells, coastal runoff after heavy rain, and strong currents are the primary factors in reducing visibility. Planning dives for calm, dry weather around slack tide will provide the best chance for remarkable visibility.

Terrain & Navigation:
The Wreck of the Alert is a substantial and intricate structure, sitting on the seabed, now heavily encrusted with a diverse array of soft corals, sponges, and anemones. Navigation involves exploring its various sections, including masts, rigging (now collapsed), and hull. Due to the depth and potential for currents, meticulous planning, excellent buoyancy control, and appropriate wreck diving training are crucial. Divers will need to rely on the wreck's features for underwater navigation, as compass readings can be unreliable near large metal structures. The wreck provides abundant hiding spots and intricate swim-throughs for those with excellent buoyancy control and experience in more challenging environments.

Marine Life Highlights:
This artificial reef is a vibrant hub of marine activity. Divers frequently encounter various species of colourful reef fish, including wrasse, leatherjackets, and morwongs, gracefully swimming through the structure. A dazzling array of nudibranchs in a kaleidoscope of colours can be found meticulously crawling across the wreck surfaces. Keep an eye out for inquisitive octopus, cuttlefish, and various species of larger fish that patrol the wreck. The healthy growth on the wreck supports diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to the Wreck of the Alert is exclusively by boat, typically arranged through dive charter operators from Phillip Island or nearby coastal towns. There are no on-site facilities directly at the dive site. The optimal diving season is from December to March for warmer waters and generally calmer conditions. Conservation is paramount; divers are expected to practice responsible wreck diving, avoiding disturbance to the wreck structure or marine life, and adhering to safe penetration practices (if qualified and equipped).

Who Is It For?:
This is an **Advanced** dive site, suitable for experienced divers comfortable with deep profiles, managing potential currents, and exploring complex wreck structures. Advanced diving certifications, including wreck specialist, are highly recommended. Excellent buoyancy control is essential to avoid disturbing sediment within the wreck.

Pro-Tip:
Due to the historical significance and the wreck's delicate state, always dive with a "look but don't touch" policy. Carry a good dive light to illuminate the darker sections and reveal the true colours of the soft corals and hidden marine life.

75-word excerpt:
Wreck of the Alert, Phillip Island (18-33m), is an advanced boat dive on a historic clipper, now a vibrant artificial reef. Visibility is variable (10-25m, remarkable when right), best December-March, impacted by coastal conditions and surge. It hosts reef fish, nudibranchs, and cuttlefish. This challenging wreck demands advanced skills, proper training, and careful planning, offering a thrilling blend of maritime history and marine biodiversity in Victoria's temperate waters."""

# Article for Stack Island (ID 29)
article_text_29 = """# Stack Island: Shellharbour's Offshore Gem with Caves and Pelagics for Advanced Divers

Off the rugged coastline of Shellharbour, New South Wales, Stack Island stands as a captivating and challenging offshore dive site, ideally suited for advanced divers. Descending to depths between 10 to 25 metres, this small island reef is renowned for its intriguing caves, exhilarating swim-throughs, and the impressive pelagic species that frequent its deeper sections. Accessible exclusively by boat, Stack Island offers a dynamic underwater landscape, showcasing a rich diversity of temperate and tropical marine species. It’s a jewel in a protected marine area, promising engaging encounters with kingfish, various turtles, and other pelagics against a backdrop of unique geological formations, particularly during the prime season of October to April.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 10 to 25 metres, offering extensive reef exploration and cave entry options.
*   Visibility: Generally excellent, typically ranging from 15 to 25 metres (consistent with "typical for Jervis Bay"). Optimal visibility is found between October and April. As an offshore island, it benefits from minimal coastal runoff. Visibility is largely influenced by strong oceanic currents and offshore weather systems. While consistently good year-round, it can experience seasonal thermoclines and plankton events in warmer months. Divers should anticipate that strong currents can bring in plankton or stir up sediment, temporarily affecting clarity. Calm conditions are generally best for uninhibited views.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 17°C in cooler months to a pleasant 23°C in summer.
*   Current/Conditions: Divers can expect moderate to strong oceanic currents, particularly on incoming tides or around prominent reef features. Surge can also be significant, especially during larger ocean swells. This is a boat-only dive, requiring careful planning and execution. Awareness of boat traffic is also important.
*   Viz Implications: Strong oceanic currents and offshore weather systems are the primary factors in reducing visibility. Occasional surge can also contribute to turbid conditions. Planning dives during calm, dry periods will ensure the best possible clarity and an enjoyable experience.

Terrain & Navigation:
Stack Island features a rugged rocky reef terrain with numerous ledges, gutters, impressive caves, and fascinating swim-throughs. The reef structures are heavily adorned with a variety of hard and soft corals, sponges, and anemones, providing ample shelter for marine life. Navigation is relatively straightforward, following the reef contours and exploring the various passages. Divers will find numerous crevices and overhangs to explore, offering hiding spots for smaller creatures. The clear water, when present, allows for easy orientation, but paying attention to current direction is vital for a relaxed dive. Boat-based GPS navigation to the site is standard; underwater navigation relies on natural features and depth.

Marine Life Highlights:
This vibrant offshore gem is home to an incredible array of marine life, particularly larger species. Divers can expect frequent encounters with schooling kingfish, often seen patrolling the deeper sections and around the bommies. Various species of green and loggerhead turtles are often spotted cruising along the reef. Keep an eye out for inquisitive wobbegong sharks tucked away under ledges, and a dazzling array of pelagic fish, including trevally and barracuda, in the surrounding blue water. The healthy coral ecosystems support diverse invertebrate life, adding intricate detail to the dive experience.

Logistics & Facilities:
Access to Stack Island is exclusively by boat, typically arranged through dive charter operators in Shellharbour or nearby coastal towns. There are no on-site facilities directly at the dive site. The optimal diving season is from October to April for warmer waters and peak marine activity. Conservation is paramount; divers are expected to practice responsible diving, observing marine life without touching or disturbing the delicate reef ecosystem and its inhabitants, and adhering to safe exploration practices within the caves and swim-throughs.

Who Is It For?:
This is an **Advanced** dive site, suitable for experienced divers comfortable with deep profiles, managing moderate to strong currents and surge, and adept at navigating complex reef systems with overhead environments. Excellent physical fitness and advanced diving certifications are highly recommended. It's an ultimate destination for adventure seekers and serious underwater photographers.

Pro-Tip:
Due to the potential for strong currents and the exposed nature of the site, always dive Stack Island with a buddy who is equally experienced. Consider using a surface marker buoy (SMB) for safety stops and to ensure easy surface detection by your dive boat. Plan your dive to make the most of the slack tide when currents are minimal.

75-word excerpt:
Stack Island, Shellharbour (10-25m), is an advanced boat dive offshore gem with caves, swim-throughs, and pelagic species like kingfish and turtles. Visibility (15-25m, excellent) is best October-April, influenced by oceanic currents and surge. This dynamic site demands advanced skills for complex geological exploration and big-animal encounters, ideal for experienced divers seeking thrilling adventures in a protected marine area."""

# Execute the updates for the IDs
update_article_in_db_and_combined_file(36, "Shark Cave", article_text_36)
update_article_in_db_and_combined_file(22, "Wreck of the Alert", article_text_22)
update_article_in_db_and_combined_file(29, "Stack Island", article_text_29)
