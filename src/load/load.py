import sqlite3

def load_to_sqlite(df, table_name, db_path="energy.db"):
    """
    Load a DataFrame into SQLite.
    If table exists, replaces it.
    """
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
