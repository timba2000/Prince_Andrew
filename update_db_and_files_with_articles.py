
import sqlite3
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def update_article_in_db_and_file(site_id, site_name, article_text, output_dir="dive_site_articles"):
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

        # Create Markdown file
        file_slug = slugify(site_name)
        file_name = f"{file_slug}.md"
        file_path = os.path.join(output_dir, file_name)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(article_text)
        print(f"Created Markdown file for '{site_name}' at {file_path}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except IOError as e:
        print(f"File I/O error: {e}")
    finally:
        if conn:
            conn.close()

# Article for Mount Hypipamee Crater (ID 46)
article_text_46 = """Mount Hypipamee Crater: A Deep, Emerald Enigma for Advanced Divers

Nestled within the Atherton Tablelands of Queensland, the Mount Hypipamee Crater presents a truly unique and challenging dive experience for the advanced and technically proficient. This ancient volcanic crater lake, plunging to extreme depths of up to 125 metres, is an emerald enigma, its dark, clear waters holding secrets for those brave enough to explore its restricted confines. While not a typical coral reef dive, its geological significance and the sheer scale of the underwater environment offer a compelling adventure for divers seeking something far removed from the ordinary. Access requires a special permit, underscoring its protected and unique nature, making each descent into its cool depths a privilege.

The Essentials:
*   Depth Range: An extreme depth range from 20 metres down to 125 metres, making it suitable only for highly advanced technical divers.
*   Visibility: The crater lake is known for its emerald green waters, which suggest generally high clarity. Visibility is typically good, offering clear views within the unique light conditions of a deep lake. Given its internal navigation relies on visual cues from the crater walls, consistent clarity is paramount. There is no coastal runoff, and visibility is largely unaffected by wind or swell direction. However, deep thermoclines can create distinct visual layers. As a freshwater system, it lacks the plankton blooms and sediment issues of coastal sites.
*   Water Temperature: Temperatures are relatively stable, ranging from 20°C to 22°C, though deeper sections will experience significant thermoclines, with temperatures dropping considerably with depth.
*   Current/Conditions: There are no significant currents within the crater lake, but vertical thermoclines can create interesting pressure changes. The primary challenge comes from the extreme depth and overhead environment.
*   Viz Implications: Visibility is consistently good, with minimal external influences. Any reduction in clarity would likely be due to internal organic matter or diver-induced disturbance.

Terrain & Navigation:
The terrain of Mount Hypipamee Crater is dominated by its sheer, almost vertical walls that plunge into incredible depths. Navigation is primarily visual, following the crater walls downwards. The bottom is likely silty, so impeccable buoyancy control is crucial to avoid stirring up sediment. Divers will encounter submerged rock formations and potentially fallen trees from the rim. The overhead environment demands meticulous planning and execution, suitable for cave or cavern trained divers.

Marine Life Highlights:
While not a coral reef, the crater lake is home to its own fascinating ecosystem. Divers may encounter various species of freshwater eels, often larger than their marine counterparts, lurking in the darker recesses. Freshwater fish species adapted to deep, cool environments can also be observed. The unique light penetration creates an ethereal ambiance, transforming the familiar into the alien. This site offers a different kind of marine encounter, focusing on the resilience of freshwater inhabitants.

Logistics & Facilities:
Access to Mount Hypipamee Crater is strictly controlled and requires a special permit, usually obtained through Queensland Parks and Wildlife Service. This is not a casual dive site. The best time to dive is during the dry season, typically May to September, when surface conditions are stable and temperatures are moderate. Due to the extreme nature of the dive, comprehensive safety protocols, experienced guides, and specialised equipment are essential. There are no dive-specific facilities at the site; it is a wilderness experience.

Who Is It For?:
This is an **Advanced** dive site, exclusively for highly experienced technical divers with appropriate certifications (e.g., cave, cavern, or trimix certifications) due to the extreme depth, overhead environment, and remoteness. It is not suitable for recreational open-water divers.

Pro-Tip:
Due to the extreme depth and unique environment, consider using a rebreather to maximise bottom time and minimise decompression obligations, allowing for a more thorough exploration of this geological marvel.

75-word excerpt:
Mount Hypipamee Crater, an advanced technical dive in Queensland's Atherton Tablelands, plunges to 125m in clear, emerald waters (20-22°C). Visibility is consistently good, unaffected by wind/swell, but deep thermoclines exist. Home to freshwater eels, it requires special permits and meticulous planning due to extreme depth and overhead environment, ideal for experienced cave/cavern divers seeking unique geological exploration."""

# Article for North Ballina Wall (ID 200)
article_text_200 = """North Ballina Wall: A Challenging Coastal Ledge for Advanced Divers

Stretching out from the headland near Ballina, New South Wales, the North Ballina Wall presents an exposed and challenging dive site strictly for advanced divers. This rocky ledge, ranging in depth from 8 to 18 metres, is renowned for its big swell exposure and the dynamic conditions it offers. While its strong currents and surge demand respect, the wall rewards experienced divers with encounters with impressive marine life, including large groper, elusive crayfish, and occasional shark sightings. Its shore access can be difficult, often requiring careful timing, adding to its allure for those seeking a truly adventurous coastal dive.

The Essentials:
*   Depth Range: This advanced dive ranges from 8 to 18 metres, offering a good vertical profile along the wall.
*   Visibility: Visibility here is highly variable, typically ranging from a poor 1-5 metres, extending to 10-15 metres on exceptionally good days. The best conditions are experienced during spring and summer, primarily during long dry periods and around slack high tide. Visibility is significantly impacted by heavy rainfall, river outflow from the Richmond River, strong tidal currents, and continuous boat traffic. Strong easterly and south-easterly swells can also stir up sediment, greatly reducing clarity. Calm, dry periods with light offshore winds (westerly) are essential for any chance of reasonable visibility.
*   Water Temperature: Water temperatures are comfortably warm, ranging from 20°C to 25°C, making for pleasant diving conditions when visibility permits.
*   Current/Conditions: Divers must be prepared for strong currents and significant surge, especially on incoming tides and during larger ocean swells. This is not a site for the faint-hearted or inexperienced.
*   Viz Implications: Heavy rainfall and river outflow from the Richmond River are the primary detractors of visibility, bringing in sediment and reducing clarity to very poor levels. Strong tidal currents further compound this by keeping particles in suspension. Offshore weather systems, especially after storms, will also severely limit visibility.

Terrain & Navigation:
The North Ballina Wall is characterised by a dominant rocky ledge extending from the headland, featuring numerous cracks, crevices, and overhangs. Navigation involves following the contours of the wall, being mindful of the strong currents. The terrain transitions to a sandy bottom at its base. Divers will need to maintain excellent buoyancy control to avoid being pushed into the wall or swept away by the current. Visual cues are key, but reliance on a dive guide is highly recommended due to the challenging conditions.

Marine Life Highlights:
Despite the challenging conditions, the North Ballina Wall is home to a robust array of marine life. Encounters with impressive Queensland groper, often sheltering in the larger crevices, are a highlight. Divers can spot various species of crayfish tucked into rocky hideaways. There are also occasional sightings of small reef sharks patrolling the deeper sections. The rocky surfaces are adorned with colourful sponges and hard corals, attracting schools of smaller reef fish.

Logistics & Facilities:
Access to the North Ballina Wall can be challenging. While shore access is technically possible, it is often difficult and dependent on calm swell conditions and precise timing. Boat access via local dive operators is the more common and safer option. There are no on-site facilities directly at the dive site. The optimal diving season is spring and summer (September to March) for warmer waters, but successful dives are highly dependent on extended periods of dry weather and minimal swell. Divers must be highly self-sufficient and prepared for demanding conditions.

Who Is It For?:
This is an **Advanced** dive site, suitable only for highly experienced divers who are comfortable with strong currents, significant surge, and potentially low visibility. Excellent finning skills, proficient navigation, and comfort in exposed conditions are essential.

Pro-Tip:
Due to the highly variable and often poor visibility, it is highly advisable to dive with an experienced local guide who understands the specific conditions and optimal dive times for the North Ballina Wall. Always carry a safety sausage and a dive computer with appropriate gas planning for dynamic conditions.

75-word excerpt:
North Ballina Wall, an advanced dive off Ballina, NSW (8-18m), is a rocky ledge known for big swell exposure and challenging conditions. Visibility (1-15m) is highly variable, best in dry, calm spring/summer, but impacted by river runoff and strong currents. It hosts groper, crayfish, and occasional sharks. Access is difficult, suitable only for highly experienced divers comfortable with dynamic, exposed environments."""

# Execute the updates
update_article_in_db_and_file(46, "Mount Hypipamee Crater", article_text_46)
update_article_in_db_and_file(200, "North Ballina Wall", article_text_200)
