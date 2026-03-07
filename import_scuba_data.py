
import pandas as pd
import sqlite3

csv_file = 'scubadownunder.csv'
db_file = 'dive_sites.db'
table_name = 'dive_sites'

try:
    # Read the CSV with the 'python' engine for better error handling
    # and try to infer delimiters and handle quoting more flexibly.
    # Using on_bad_lines='skip' to ignore rows with too many/few fields
    quote_char = '"'
    df = pd.read_csv(csv_file, engine='python', sep=',', quotechar=quote_char, on_bad_lines='skip')

    # Clean column names (remove leading/trailing spaces, special characters if necessary)
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('[^A-Za-z0-9_]+', '', regex=True)

    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Drop the existing table if it exists, to ensure a clean import
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    conn.commit()

    # Write the DataFrame to the SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    print(f"Successfully imported {len(df)} rows from {csv_file} to {table_name} in {db_file}")

    # Verify the import
    count_query = f"SELECT COUNT(*) FROM {table_name};"
    count_result = pd.read_sql_query(count_query, conn)
    print(f"Total rows in {table_name} after import: {count_result.iloc[0, 0]}")

except Exception as e:
    print(f"An error occurred during CSV import: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()
