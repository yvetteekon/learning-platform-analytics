# src/database.py
import sqlite3
import pandas as pd
from pathlib import Path
from config import DB_PATH, DATA_DIR

def get_connection(db_path=DB_PATH):
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_schema(conn):
    """Create database schema from schema.sql file."""
    schema_path = Path("schema.sql")
    if schema_path.exists():
        with open(schema_path, "r") as f:
            conn.executescript(f.read())
        conn.commit()
        print("Schema created or updated successfully.")
    else:
        print("Warning: schema.sql file not found.")

def load_all_data(conn, data_dir=DATA_DIR):
    """Load all CSV files from data directory into the database."""
    data_path = Path(data_dir)
    if not data_path.exists():
        print(f"Warning: Data directory '{data_dir}' not found.")
        return

    csv_files = list(data_path.glob("*.csv"))
    
    for file in csv_files:
        table_name = file.stem
        try:
            df = pd.read_csv(file)
            df.to_sql(table_name, conn, if_exists="append", index=False)
            print(f"Loaded {len(df):,} rows into table: {table_name}")
        except Exception as e:
            print(f"Failed to load {file.name}: {e}")
    
    conn.commit()
    print("Data loading completed.")