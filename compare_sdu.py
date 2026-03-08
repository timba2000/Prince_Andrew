
import csv
import sqlite3
import re

def normalize_csv_header(header):
    if header is None:
        return None # Or a suitable placeholder if None keys are expected to be mapped
    # Convert "Space separated" to "snake_case" and handle specific renames
    header = header.replace(' ', '_').strip()
    # Specific renames from previous runs or common discrepancies
    if header == 'Image_URL':
        return 'Image_URL'
    if header == 'Created_At':
        return 'Created_At'
    if header == 'Viz_Seasonal':
        return 'Viz_Seasonal'
    if header == 'Viz_Slug':
        return 'Viz_Slug'
    if header == 'Best_Time':
        return 'Best_Time'
    if header == 'Skill_Level':
        return 'Skill_Level'
    if header == 'Depth_Range':
        return 'Depth_Range'
    if header == 'Marine_Life':
        return 'Marine_Life'
    if header == 'Water_Temperature':
        return 'Water_Temperature'
    if header == 'Compass_Bearing':
        return 'Compass_Bearing'
    if header == 'Nearby_Runoff':
        return 'Nearby_Runoff'
    if header == 'Viz_Triggers':
        return 'Viz_Triggers'
    if header == 'Visibility':
        return 'Visibility'
    if header == 'Hazards':
        return 'Hazards'
    if header == 'Facilities':
        return 'Facilities'
    if header == 'Featured':
        return 'Featured'
    return header

def process_csv_row(row):
    processed_row = {}
    for key, value in row.items():
        normalized_key = normalize_csv_header(key)
        if normalized_key is None:
            continue # Skip if the key itself is None after normalization attempt

        # Convert empty strings to None to match SQLite NULLs
        processed_value = value.strip() if isinstance(value, str) else value
        if processed_value == '':
            processed_value = None

        # Convert 'Featured' boolean strings to 1/0
        if normalized_key == 'Featured':
            if processed_value is not None:
                processed_value = 1 if str(processed_value).lower() == 'true' else 0
            else:
                processed_value = 0 # Assume false if not specified
        
        # Convert numerical fields to appropriate types for comparison
        if normalized_key in ['ID', 'Latitude', 'Longitude', 'Compass_Bearing']:
            if processed_value is not None:
                try:
                    if normalized_key == 'ID':
                        processed_value = int(processed_value)
                    elif normalized_key == 'Compass_Bearing':
                        processed_value = float(processed_value)
                    else: # Latitude, Longitude
                        processed_value = float(processed_value)
                except ValueError:
                    # If conversion fails, keep as string for discrepancy reporting
                    pass
        
        processed_row[normalized_key] = processed_value
    return processed_row

def compare_data(csv_file, db_file):
    csv_raw_data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_raw_data.append(row)

    csv_data = [process_csv_row(row) for row in csv_raw_data]

    db_data = []
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dive_sites")
    
    db_column_names = [description[0] for description in cursor.description]
    
    for row in cursor.fetchall():
        db_entry = dict(zip(db_column_names, row))
        # Ensure 'Featured' is 0/1 for consistent comparison
        if 'Featured' in db_entry and db_entry['Featured'] is not None:
            db_entry['Featured'] = 1 if db_entry['Featured'] == 1 else 0
        db_data.append(db_entry)
    
    conn.close()

    discrepancies = []
    
    db_data_dict = {str(row.get('ID')): row for row in db_data if row.get('ID') is not None}
    csv_data_dict = {str(row.get('ID')): row for row in csv_data if row.get('ID') is not None}

    # Check for entries in CSV but not in DB (deleted)
    for csv_id, csv_row in csv_data_dict.items():
        if csv_id not in db_data_dict:
            discrepancies.append(f"Entry with ID {csv_id} (Name: {csv_row.get('Name', 'N/A')}) found in CSV but not in DB (possibly deleted).")

    # Check for entries in DB but not in CSV (new)
    for db_id, db_row in db_data_dict.items():
        if db_id not in csv_data_dict:
            discrepancies.append(f"Entry with ID {db_id} (Name: {db_row.get('Name', 'N/A')}) found in DB but not in CSV (possibly new entry).")
            
    # Compare common entries for actual value changes
    # Only compare fields that are in the original CSV (after normalization)
    original_csv_fields = set()
    if csv_data: # Get fields from the first row as a representative set
        # Use keys from the *processed* first row to get normalized names
        original_csv_fields = set(csv_data[0].keys())

    # Exclude internal DB fields from content comparison
    internal_db_fields = ['validation_status', 'corroboration_sources']
    
    fields_to_compare = original_csv_fields.intersection(set(db_column_names))
    fields_to_compare = fields_to_compare.difference(set(internal_db_fields))

    for common_id in set(csv_data_dict.keys()) & set(db_data_dict.keys()):
        csv_row = csv_data_dict[common_id]
        db_row = db_data_dict[common_id]
        
        row_discrepancies = []
        
        for key in fields_to_compare:
            csv_value = csv_row.get(key)
            db_value = db_row.get(key)

            # Handle None vs empty string consistently
            if csv_value == '': csv_value = None
            if db_value == '': db_value = None

            # Special handling for numerical values due to potential precision issues
            if key in ['Latitude', 'Longitude', 'Compass_Bearing']:
                if csv_value is not None and db_value is not None:
                    try:
                        if abs(float(csv_value) - float(db_value)) > 0.000001: # Small tolerance
                            row_discrepancies.append(f"  Field '{key}': CSV='{csv_value}', DB='{db_value}'")
                    except (ValueError, TypeError): # If not convertable to float, treat as string
                        if str(csv_value) != str(db_value):
                            row_discrepancies.append(f"  Field '{key}': CSV='{csv_value}', DB='{db_value}'")
                elif csv_value is not None or db_value is not None: # One is None, the other is not
                    if str(csv_value) != str(db_value): # Compare as strings if one is None
                        row_discrepancies.append(f"  Field '{key}': CSV='{csv_value}', DB='{db_value}'")
            elif str(csv_value) != str(db_value): # General string comparison for non-numerical fields
                row_discrepancies.append(f"  Field '{key}': CSV='{csv_value}', DB='{db_value}'")

        if row_discrepancies:
            discrepancies.append(f"Discrepancies for ID {common_id} (Name: {csv_row.get('Name', 'N/A')}):")
            discrepancies.extend(row_discrepancies)

    return discrepancies

csv_file_path = "scubadownunder.csv"
db_file_path = "dive_sites.db"

results = compare_data(csv_file_path, db_file_path)

if results:
    print("Found actual content discrepancies (excluding structural/internal field changes):")
    for result in results:
        print(result)
    print(f"Total actual content discrepancies found: {len(results)}")
else:
    print("No actual content discrepancies found between the CSV and the database (excluding structural/internal field changes).")
