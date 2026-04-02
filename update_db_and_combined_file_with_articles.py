
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

# Execute the update for ID 48
update_article_in_db_and_combined_file(48, "Shark Point", article_text_48)
