
import sqlite3
import json

db_file = 'dive_sites.db'
table_name = 'dive_sites'
batch_size = 10

try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Select uncorroborated sites
    select_query = f"""
        SELECT ID, Name
        FROM {table_name}
        WHERE validation_status NOT LIKE 'corroborated_%' OR validation_status IS NULL
        LIMIT {batch_size};
    """
    cursor.execute(select_query)
    sites_to_process = cursor.fetchall()

    if not sites_to_process:
        print(json.dumps({"status": "no_new_sites"}))
    else:
        site_ids = [site[0] for site in sites_to_process]
        site_names = [site[1] for site in sites_to_process]

        # Update their status to 'corroboration_in_progress'
        update_query = f"""
            UPDATE {table_name}
            SET validation_status = 'corroboration_in_progress'
            WHERE id IN ({','.join(map(str, site_ids))});
        """
        cursor.execute(update_query)
        conn.commit()

        print(json.dumps({"status": "processing_batch", "sites": site_names}))

except Exception as e:
    print(json.dumps({"status": "error", "message": str(e)}))
finally:
    if 'conn' in locals() and conn:
        conn.close()
