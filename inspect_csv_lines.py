
import csv

csv_file = 'scubadownunder.csv'
start_line = 60 # Check a few lines before and after line 65
end_line = 70

print(f"Inspecting lines {start_line} to {end_line} of {csv_file}:")

try:
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if start_line <= i + 1 <= end_line: # i is 0-indexed, so i+1 is line number
                print(f"Line {i+1} (columns: {len(row)}): {row}")
except Exception as e:
    print(f"Error reading CSV: {e}")
