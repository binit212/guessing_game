import sqlite3
conn = sqlite3.connect("leaderboard.db")
cursor = conn.cursor()
cursor.execute("SELECT *FROM scores")
print(cursor.fetchall())
conn.close()
