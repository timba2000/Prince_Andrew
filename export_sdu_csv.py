
import csv
import sqlite3

def export_db_to_csv(db_file, table_name, csv_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
        writer.writerows(rows)

    conn.close()
    print(f"Successfully exported data from {table_name} to {csv_file}")

db_file_path = "dive_sites.db"
table = "dive_sites"
csv_output_file = "scubadownunder_latest_export.csv"

export_db_to_csv(db_file_path, table, csv_output_file)
