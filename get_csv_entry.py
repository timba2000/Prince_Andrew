
import csv
import json

def get_csv_entry(csv_file, entry_id):
    csv_data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_data.append(row)

    for row in csv_data:
        if row.get('ID') == str(entry_id):
            print(json.dumps(row, indent=2))
            return
    print(f"Entry with ID {entry_id} not found in {csv_file}")

csv_file_path = "scubadownunder.csv"
target_id = 28

get_csv_entry(csv_file_path, target_id)
