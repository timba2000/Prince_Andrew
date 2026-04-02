
import csv
import sys

completed_articles_for_update = [
    "Glenelg Dredge Wreck",
    "Noarlunga Tyre Reef",
    "North Haven Wall",
    "Port Noarlunga Reef",
    "North West Solitary Island",
    "Spot X Reef",
    "Mount Hypipamee Crater",
    "North Ballina Wall",
    "North Bondi Rocks",
    "Kings Beach – Broken Head",
    "Julian Rocks",
    "Julian Rocks Marine Sanctuary",
    "Julian Rocks – Cod Hole",
    "Julian Rocks – Hugo's Trench",
    "Julian Rocks – The Nursery",
    "Clovelly Pool",
    "Shark Point"
]

input_csv_path = "updated_divesites.csv"

updated_rows = []
with open(input_csv_path, 'r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    updated_rows.append(header)
    
    site_name_index = header.index("Site Name")
    has_article_index = header.index("Has Article")

    for row in reader:
        site_name = row[site_name_index]
        if site_name in completed_articles_for_update:
            row[has_article_index] = "Yes"
        updated_rows.append(row)

with open(input_csv_path, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(updated_rows)

print(f"Updated CSV written to {input_csv_path}")
