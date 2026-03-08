
import sqlite3

def insert_dive_site(db_file, data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Define the fields and their values
    fields = list(data.keys())
    values = [data[field] for field in fields]

    # Add validation_status and corroboration_sources
    fields.append('validation_status')
    values.append('corroborated_ai_review')
    fields.append('corroboration_sources')
    values.append('AI_review')

    # Create placeholders for the SQL query
    placeholders = ', '.join(['?' for _ in values])
    columns = ', '.join([f'"{field}"' for field in fields]) # Quote column names

    sql = f"INSERT INTO dive_sites ({columns}) VALUES ({placeholders});"

    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"Successfully inserted The Gutter (ID: {data['ID']}).")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        conn.close()

db_file_path = "dive_sites.db"
gutter_data = {
    "ID": 28,
    "Name": "The Gutter",
    "Latitude": -34.55020000,
    "Longitude": 150.91520000,
    "Water_Temperature": "17–23°C",
    "Skill_Level": "Beginner",
    "Depth_Range": "3–18m",
    "Description": "Narrow entry channel leading to reef and kelp beds, ideal for beginners when calm.",
    "Visibility": "5–12m",
    "Best_Time": "October–April",
    "Region": "Shellharbour, NSW",
    "Marine_Life": "Morwong, rays, soft corals",
    "Hazards": "Surge, low visibility",
    "Facilities": "Shore access",
    "Image_URL": "https://static.wixstatic.com/media/72b162_bf1b1430efca431daf486ac1ed237311~mv2.jpg/v1/fill/w_280",
    "Featured": 0, # Corrected boolean to 0
    "Created_At": None, # Set to None as it was malformed
    "Viz_Slug": None,
    "Compass_Bearing": None,
    "Nearby_Runoff": None,
    "Viz_Triggers": None,
    "Viz_Seasonal": None
}

insert_dive_site(db_file_path, gutter_data)
