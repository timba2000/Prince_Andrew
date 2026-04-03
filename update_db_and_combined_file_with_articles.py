
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

# Article for Shark Point (ID 48)
article_text_48 = """# Shark Point, Clovelly: An Advanced Deep Reef Adventure

For the experienced and adventurous diver, Shark Point in Clovelly, New South Wales, offers a captivating journey into a deep reef system. Resting at depths between 10 to 25 metres, this site is celebrated for its impressive large boulders, dramatic drop-offs, and exceptional marine life diversity, including the occasional shark sighting that gives the point its evocative name. Its challenging conditions, including surge and strong currents, make it strictly an advanced dive. Primarily accessible via a shore entry that demands careful planning, Shark Point promises an exhilarating exploration into Sydney's deeper, more untamed underwater landscapes, providing a stark contrast to its calmer neighbours.

The Essentials:
*   Depth Range: An advanced dive with depths ranging from 10 to 25 metres, suitable for divers comfortable with deeper profiles.
*   Visibility: Variable, but can be very good, especially with low swell (<1.2m). Optimal visibility is generally found between September and April, though it is significantly impacted by rain events and high swells. Strong easterly swells and heavy rainfall can reduce clarity considerably. Calm conditions, particularly with light offshore winds, are crucial for the best experience. Navigational guidance advises against going below 270 degrees to avoid Gordons Bay and warns against heading too far north into False Bay.
*   Water Temperature: Water temperatures range from 17°C in cooler months to a pleasant 22°C in summer.
*   Current/Conditions: Divers must be prepared for strong currents and significant surge, particularly on incoming tides and during larger ocean swells. This is an exposed site that demands excellent finning skills and vigilant situational awareness.
*   Viz Implications: Heavy rainfall and high easterly swells are the primary factors in reducing visibility. Strong currents also play a role by keeping sediment in suspension. Planning dives during periods of calm, dry weather is essential.

Terrain & Navigation:
Shark Point is characterized by a rugged and dramatic underwater topography. It features imposing large boulders, steep drop-offs, and deep gutters that create a complex yet fascinating environment. Navigation requires careful planning due to the potential for strong currents and variable visibility. Divers will need to follow distinct reef contours and be mindful of their depth and ascent rates. The deep reef structure provides abundant hiding spots and intricate swim-throughs for those with excellent buoyancy control and experience in more challenging environments.

Marine Life Highlights:
As its name implies, Shark Point offers a chance to encounter various shark species, including the occasional wobbegong or Port Jackson shark, often found resting under ledges. Large, curious blue gropers are common, and divers will also find an exceptional diversity of nudibranchs in a kaleidoscope of colours. Schools of reef fish, including trevally and kingfish, patrol the deeper sections. The site's unique topography and nutrient-rich waters attract a wide array of invertebrates, making it a macro photographer's delight.

Logistics & Facilities:
Access to Shark Point is via a shore entry from Clovelly, which can be challenging due to the rocky entry and potential for surge. Parking is limited, particularly on weekends. The optimal diving season is from September to April for warmer waters and generally better conditions, though success hinges on weather and swell. There are no on-site dive facilities, so divers must be self-sufficient and well-prepared. Conservation is paramount; divers are encouraged to practice responsible diving, avoiding disturbance to the fragile deep reef ecosystem and its inhabitants.

Who Is It For?:
This is an **Advanced** dive site, suitable only for highly experienced divers who are comfortable with deep profiles, strong currents, significant surge, and navigating complex reef structures in potentially variable visibility. Excellent physical fitness and advanced diving certifications are highly recommended.

Pro-Tip:
Due to the demanding conditions, always dive Shark Point with a buddy who is equally experienced, and consider using a robust surface marker buoy (SMB) to ensure easy surface detection by your shore support or boat crew. Plan your dive to coincide with periods of lower swell and incoming tide for potentially better visibility.

75-word excerpt:
Shark Point, Clovelly (10-25m), is an advanced shore dive with large boulders, drop-offs, and diverse marine life, including sharks and blue gropers. Visibility is variable (best in low swell, impacted by rain/high swell) with strong currents. Optimal September-April, it requires careful planning and experience due to demanding conditions. A thrilling Sydney deep reef adventure for proficient divers seeking challenging exploration and rich biodiversity."""

# Article for Muttonbird Island (ID 177)
article_text_177 = """# Muttonbird Island: A Gentle Shore Dive for Beginners in Coffs Harbour

Just off the coast of Coffs Harbour, New South Wales, Muttonbird Island presents a charming and accessible shore dive, perfectly suited for beginner divers. With shallow depths ranging from 3 to 10 metres, this site offers a delightful exploration of vibrant reef and expansive seagrass beds, all within a protected and gentle environment. Accessible via a straightforward shore entry, Muttonbird Island is a tranquil escape, promising intimate encounters with a variety of fascinating marine life. It's an ideal spot for those new to diving, or for seasoned divers seeking a relaxed and richly rewarding experience, especially during calm conditions when its underwater beauty truly shines.

The Essentials:
*   Depth Range: A beginner-friendly depth range from 3 metres down to 10 metres, making it perfect for leisurely dives and extended bottom times.
*   Visibility: Variable, typically ranging from 4 to 8 metres, but can extend to 20 metres on exceptionally clear days. Optimal visibility is found only in calm conditions and during dry periods. It is significantly impacted by moderate coastal runoff from Coffs Harbour, heavy rainfall, strong currents, and disturbance from boat traffic. Prevailing winds from the east and south-east can stir up sediment, reducing clarity. Calm, dry periods with light offshore winds are ideal for the best experience.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 19°C to 25°C, making for pleasant diving throughout much of the year.
*   Current/Conditions: The site is generally calm in protected areas, but divers should be aware of potential swell, especially on less calm days. It is strongly recommended to dive here only during calm conditions to ensure optimal enjoyment and safety.
*   Viz Implications: Heavy rainfall and moderate coastal runoff are primary factors reducing visibility. Strong currents, if present, and boat traffic can also contribute to turbid conditions. Planning dives during calm, dry weather with minimal swell is crucial.

Terrain & Navigation:
Muttonbird Island features a diverse underwater terrain, transitioning from rocky reefs to expansive seagrass beds. The reef sections provide numerous crevices and overhangs, while the seagrass offers a different habitat for unique marine life. Navigation is straightforward due to the shallow depths and the proximity to the shore. Divers can leisurely explore the various formations, following the reef line or drifting over the seagrass. The clear water, when present, aids significantly in orientation.

Marine Life Highlights:
This gentle site is teeming with interesting marine life. Divers will frequently encounter various species of crabs scuttling across the bottom and camouflaged octopus peeking from rocky hideaways. Smaller rays can often be spotted gliding gracefully over the sandy patches and within the seagrass beds. The seagrass is also a nursery for juvenile fish, and a variety of colourful reef fish add vibrancy to the rocky sections. Macro enthusiasts will delight in the many nudibranchs and smaller invertebrates.

Logistics & Facilities:
Muttonbird Island offers convenient shore access, making it highly accessible for divers. There are no dedicated dive facilities directly at the site, but basic amenities can be found nearby in Coffs Harbour. The best time to dive is when conditions are calm, which can be year-round, though warmer waters are typically found in spring and summer. Conservation is paramount here; divers are encouraged to practice responsible diving, avoiding disturbance to the delicate ecosystem and its inhabitants, particularly within the seagrass beds.

Who Is It For?:
This is an ideal site for **Beginner** divers and snorkelers. Its shallow, protected waters, coupled with rich marine life and easy access, make it perfect for introductory dives, training, and peaceful underwater observation. It's a superb site for building confidence and enjoying a relaxed marine experience.

Pro-Tip:
When diving Muttonbird Island, take your time to explore the seagrass beds. Many unique macro creatures, including pipefish and seahorses, are experts at camouflage and can be easily missed if you're rushing through the site.

75-word excerpt:
Muttonbird Island, Coffs Harbour (3-10m), is a beginner-friendly shore dive with reefs and seagrass beds, perfect for calm conditions. Visibility (4-8m, up to 20m) is best on calm, dry days but impacted by coastal runoff, rainfall, and currents. It hosts crabs, octopus, and small rays, offering a tranquil exploration for new divers seeking diverse marine life and protected underwater environments."""

# Execute the updates for both IDs
update_article_in_db_and_combined_file(48, "Shark Point", article_text_48)
update_article_in_db_and_combined_file(177, "Muttonbird Island", article_text_177)
