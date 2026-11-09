import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "fm4songs.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Creates tables if non-existent
cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE,
        description TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER,
        song_title TEXT UNIQUE
    )
""")
# 2. Inserting categories
cursor.execute("INSERT OR IGNORE INTO categories (title, description) VALUES ('New Songs', 'Songs new to Arrow Dance Mayhem Funny Mix 4.')")
cursor.execute("INSERT OR IGNORE INTO categories (title, description) VALUES ('Returning Songs', 'Songs from previous Arrow Dance Mayhem games.')")
cursor.execute("INSERT OR IGNORE INTO categories (title, description) VALUES ('Unlockable Songs', 'New and old songs that need to be unlocked through gameplay.')")
cursor.execute("INSERT OR IGNORE INTO categories (title, description) VALUES ('Boss Songs', 'Hardest songs in the game, with Level 10 Master charts.')")

# 3. Assigning songs to each category
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (1, 'Open Your Eyes')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (1, 'Its What You Do')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (1, 'Developers')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (2, 'Exercise with Link')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (2, 'Together Forever')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (3, 'A Certain Gooey Thing')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (3, 'Jumper')")
cursor.execute("INSERT OR IGNORE INTO songs (category_id, song_title) VALUES (4, 'POT')")

# 4. Save and exit
conn.commit()
conn.close()

print("Song categories actioned.")