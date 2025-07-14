# database/db_handler.py
import sqlite3
DB_NAME = "poultry_records.db"
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tab_name TEXT,
            input_data TEXT,
            prediction TEXT,
            treatment TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
def insert_record(tab_name, input_data, prediction, treatment=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO records (tab_name, input_data, prediction, treatment)
        VALUES (?, ?, ?, ?)
    """, (tab_name, input_data, prediction, treatment))
    conn.commit()
    conn.close()