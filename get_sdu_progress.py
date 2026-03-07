
import sqlite3
import json

db_file = 'dive_sites.db'

try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get total number of sites
    cursor.execute(f"SELECT COUNT(*) FROM dive_sites;")
    total_sites = cursor.fetchone()[0]

    # Get number of corroborated sites
    cursor.execute(f"SELECT COUNT(*) FROM dive_sites WHERE validation_status LIKE 'corroborated_%';")
    corroborated_sites = cursor.fetchone()[0]

    percentage_complete = 0.0
    if total_sites > 0:
        percentage_complete = (corroborated_sites / total_sites) * 100

    # Get names of currently in-progress sites
    cursor.execute(f"SELECT Name FROM dive_sites WHERE validation_status = 'corroboration_in_progress';")
    in_progress_sites = [row[0] for row in cursor.fetchall()]

    print(json.dumps({
        "status": "success",
        "total_sites": total_sites,
        "corroborated_sites": corroborated_sites,
        "percentage_complete": round(percentage_complete, 2),
        "in_progress_sites": in_progress_sites
    }))

except Exception as e:
    print(json.dumps({"status": "error", "message": str(e)}))
finally:
    if 'conn' in locals() and conn:
        conn.close()
