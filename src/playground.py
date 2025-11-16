import sqlite3

conn = sqlite3.connect("energy.db")
cursor = conn.execute("PRAGMA table_info(elexon_weather);")
columns = cursor.fetchall()
conn.close()

print(columns)