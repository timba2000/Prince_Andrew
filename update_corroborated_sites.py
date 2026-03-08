
import sqlite3
import json

db_file = 'dive_sites.db'
table_name = 'dive_sites'
sites_to_update = ["Terrigal HMAS Adelaide (Currently Closed)", "Bare Island Deep Wall"]

try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for site_name in sites_to_update:
        update_query = f"""
            UPDATE {table_name}
            SET validation_status = 'corroborated_ai_review'
            WHERE Name = ?;
        """
        cursor.execute(update_query, (site_name,))
    conn.commit()
    print(json.dumps({"status": "updated_corroboration", "sites": sites_to_update}))

except Exception as e:
    print(json.dumps({"status": "error", "message": str(e)}))
finally:
    if 'conn' in locals() and conn:
        conn.close()
