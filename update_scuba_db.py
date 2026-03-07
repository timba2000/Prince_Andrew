
import pandas as pd
import sqlite3
import numpy as np

csv_file = 'scubadownunder.csv'
db_file = 'scubadownunder.db'
table_name = 'dive_sites'

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row # Allows access to columns by name
    return conn

def add_validation_status_column(cursor):
    """Adds a 'validation_status' column to the dive_sites table if it doesn't exist."""
    try:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN validation_status TEXT DEFAULT 'unverified';")
        print(f"Added 'validation_status' column to {table_name}.")
    except sqlite3.OperationalError as e:
        if "duplicate column name: validation_status" in str(e):
            print("'validation_status' column already exists.")
        else:
            raise

def update_or_insert_dive_site(conn, row):
    """
    Updates an existing dive site or inserts a new one based on ID or Name/Region.
    Also performs basic validation and sets validation_status.
    """
    cursor = conn.cursor()
    
    # Clean column names from CSV to match DB
    row_data = row.to_dict()
    cleaned_row_data = {k.replace(' ', '_').replace('[^A-Za-z0-9_]+', ''): v for k, v in row_data.items()}
    
    site_id = cleaned_row_data.get('ID')
    site_name = cleaned_row_data.get('Name')
    latitude = cleaned_row_data.get('Latitude')
    longitude = cleaned_row_data.get('Longitude')
    region = cleaned_row_data.get('Region')

    validation_status = 'unverified'
    update_fields = {}

    # Basic Validation Checks
    if not site_name or pd.isna(site_name):
        validation_status = 'needs_name'
    elif pd.isna(latitude) or pd.isna(longitude) or not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        validation_status = 'missing_or_invalid_coords'
    else:
        # Default to needs web corroboration for now
        validation_status = 'needs_web_corroboration'
        # Add other specific flags here based on content of other fields if needed
        if 'SS Yongala Wreck' in str(site_name): # Example: special flag for known sites
            validation_status = 'high_priority_review'
            
    update_fields['validation_status'] = validation_status

    # Prepare data for UPSERT
    columns = []
    values = []
    for key, value in cleaned_row_data.items():
        # Exclude 'ID' if it's None or NaN, as DB might auto-increment
        if key == 'ID' and (pd.isna(value) or value is None):
            continue
        columns.append(f'"{key}"')
        values.append(value if not pd.isna(value) else None)
        
    # Add/Update validation_status in columns and values
    if 'validation_status' not in cleaned_row_data:
        columns.append('"validation_status"')
        values.append(validation_status)
    else: # If validation_status somehow exists in CSV, ensure it's updated
        # This part assumes we want to override CSV's validation_status with our logic
        idx = columns.index('"validation_status"')
        values[idx] = validation_status
        
    placeholders = ', '.join(['?' for _ in values])
    column_names = ', '.join(columns)

    if site_id and not pd.isna(site_id):
        # Try to update by ID
        update_set_parts = [f'"{col.strip('"')}" = ?' for col in columns if col != '"ID"']
        update_values = [v for k, v in zip(columns, values) if k != '"ID"']
        
        try:
            cursor.execute(f"UPDATE {table_name} SET {', '.join(update_set_parts)} WHERE ID = ?", update_values + [site_id])
            if cursor.rowcount > 0:
                return 'updated'
        except Exception as e:
            print(f"Error updating by ID {site_id}: {e}")
            
    # Fallback to Name and Region for identification or for new inserts
    # For simplicity, we'll try to find by Name and Region first for update
    # If not found or if ID was problematic, then insert
    
    # Check if a record with the same name and region already exists
    # This part should be more robust for duplicates if we want to flag them specifically
    existing_id = None
    if site_name and region:
        cursor.execute(f"SELECT ID FROM {table_name} WHERE Name = ? AND Region = ?", (site_name, region))
        result = cursor.fetchone()
        if result:
            existing_id = result['ID']
            
    if existing_id:
        # Update existing record identified by Name/Region
        update_set_parts = [f'"{col.strip('"')}" = ?' for col in columns if col not in ['"ID"', '"Name"', '"Region"']]
        update_values = [v for k, v in zip(columns, values) if k not in ['"ID"', '"Name"', '"Region"']]
        
        try:
            cursor.execute(f"UPDATE {table_name} SET {', '.join(update_set_parts)} WHERE ID = ?", update_values + [existing_id])
            if cursor.rowcount > 0:
                return 'updated'
        except Exception as e:
            print(f"Error updating by Name/Region for {site_name}: {e}")
            
    # If no update occurred, insert a new record
    try:
        cursor.execute(f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})", values)
        return 'inserted'
    except Exception as e:
        print(f"Error inserting {site_name}: {e}")
        return 'error'

def main():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        add_validation_status_column(cursor)
        
        # Read the CSV with the 'python' engine for better error handling
        df = pd.read_csv(csv_file, engine='python', on_bad_lines='skip')

        # Clean column names in DataFrame to match DB
        df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('[^A-Za-z0-9_]+', '', regex=True)

        inserted_count = 0
        updated_count = 0
        error_count = 0

        for index, row in df.iterrows():
            result = update_or_insert_dive_site(conn, row)
            if result == 'inserted':
                inserted_count += 1
            elif result == 'updated':
                updated_count += 1
            else:
                error_count += 1

        conn.commit()
        print(f"Database update complete.")
        print(f"New records inserted: {inserted_count}")
        print(f"Existing records updated: {updated_count}")
        print(f"Records with errors: {error_count}")

    except Exception as e:
        print(f"An error occurred in main: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
