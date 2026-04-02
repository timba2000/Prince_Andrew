
import csv

input_csv_path = "updated_divesites.csv"

def calculate_completion_percentage(csv_path):
    total_sites = 0
    completed_articles = 0
    try:
        with open(csv_path, 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Skip header
            has_article_index = header.index("Has Article")

            for row in reader:
                total_sites += 1
                if row[has_article_index] == "Yes":
                    completed_articles += 1

        if total_sites == 0:
            return 0.0
        return (completed_articles / total_sites) * 100
    except FileNotFoundError:
        print(f"Error: The file {csv_path} was not found.")
        return 0.0
    except ValueError as e:
        print(f"Error processing CSV: {e}")
        return 0.0

if __name__ == "__main__":
    percentage = calculate_completion_percentage(input_csv_path)
    print(f"Percentage of sites with articles: {percentage:.2f}%")
