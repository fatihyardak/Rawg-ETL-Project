import sqlite3
import json
import os

def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        slug TEXT PRIMARY KEY,
        name TEXT,
        playtime INTEGER,
        rating REAL,
        released TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game_platforms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT,
        platform TEXT,
        FOREIGN KEY(slug) REFERENCES games(slug)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game_stores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT,
        store TEXT,
        FOREIGN KEY(slug) REFERENCES games(slug)
    )
    """)

def load_data_to_table(cursor, table_name, data):
    if table_name == "games":
        cursor.executemany("""
        INSERT OR REPLACE INTO games (slug, name, playtime, rating, released)
        VALUES (?, ?, ?, ?, ?)
        """, [(item['slug'], item['name'], item['playtime'], item['rating'], item['released']) for item in data])
    elif table_name == "game_platforms":
        cursor.executemany("""
        INSERT OR REPLACE INTO game_platforms (slug, platform)
        VALUES (?, ?)
        """, [(item['slug'], item['platform']) for item in data])
    elif table_name == "game_stores":
        cursor.executemany("""
        INSERT OR REPLACE INTO game_stores (slug, store)
        VALUES (?, ?)
        """, [(item['slug'], item['store']) for item in data])
    else:
        print(f"Unknown table: {table_name}")

def main():
    db_path = "data/processed/games.db"
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    create_tables(cursor)

    # Load JSON data
    with open("data/processed/games.json", "r") as f:
        games_data = json.load(f)

    with open("data/processed/game_platforms.json", "r") as f:
        platforms_data = json.load(f)

    with open("data/processed/game_stores.json", "r") as f:
        stores_data = json.load(f)

    # Load data into tables
    load_data_to_table(cursor, "games", games_data)
    print("Games data loaded successfully.")

    load_data_to_table(cursor, "game_platforms", platforms_data)
    print("Game platforms data loaded successfully.")

    load_data_to_table(cursor, "game_stores", stores_data)
    print("Game stores data loaded successfully.")

    conn.commit()
    conn.close()
    print("All data loaded into the database!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Process completed.")
