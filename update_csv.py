
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
    "Shark Point",
    "Muttonbird Island",
    "Split Solitary Island",
    "The Looking Glass – South Solitary Island",
    "Gordon's Bay",
    "Wedding Cake Island",
    "Osprey Reef",
    "Dolphin Reef – Crescent Head",
    "Racecourse Reef – Crescent Head",
    "Wedge Island Caves",
    "Hardwicke Bay Jetty",
    "Fairy Bower",
    "Neptune Islands (Shark Cage)",
    "Yena Gap",
    "Wigton Reef",
    "Round Top Island",
    "Green Island – South West Rocks",
    "Latitude Rock",
    "Mullaway Reef",
    "Woody Head Reef",
    "HMAS Swan Wreck",
    "Manta Bommie",
    "Rapid Bay Jetty",
    "Edithburgh Jetty",
    "Shark Cave",
    "Wreck of the Alert",
    "Stack Island",
    "Flinders Pier",
    "Portsea Pier",
    "Five Fathom Reef",
    "Fishery Bay Reef",
    "Point Drummond",
    "Port Lincoln Jetty",
    "Port Neill Jetty",
    "Streaky Bay Jetty"
]

input_csv_path = "updated_divesites.csv"

def update_and_report_csv(csv_path, completed_list):
    total_sites = 0
    completed_articles_count = 0
    updated_rows = []
    try:
        with open(csv_path, 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            updated_rows.append(header)
            
            site_name_index = header.index("Site Name")
            has_article_index = header.index("Has Article")

            for row in reader:
                total_sites += 1
                site_name = row[site_name_index]
                if site_name in completed_list:
                    row[has_article_index] = "Yes"
                    completed_articles_count += 1
                elif row[has_article_index] == "Yes": # Count existing 'Yes' entries
                    completed_articles_count += 1
                updated_rows.append(row)

        with open(csv_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(updated_rows)
        print(f"Updated CSV written to {csv_path}")

        if total_sites == 0:
            print("Percentage of sites with articles: 0.00%")
        else:
            percentage = (completed_articles_count / total_sites) * 100
            print(f"Percentage of sites with articles: {percentage:.2f}%")

    except FileNotFoundError:
        print(f"Error: The file {csv_path} was not found.")
    except ValueError as e:
        print(f"Error processing CSV: {e}")

if __name__ == "__main__":
    update_and_report_csv(input_csv_path, completed_articles_for_update)
