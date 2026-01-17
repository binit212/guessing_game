import sqlite3
conn = sqlite3.connect("leaderboard.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        score INTEGER,
        time REAL
    )
    """)
conn.commit()
conn.close
print("DataBase created successfully!")
