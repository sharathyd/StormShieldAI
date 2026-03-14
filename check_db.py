import sqlite3
import os
db_path = r'c:\sharath\hackathon\rajesh\StormShieldAI\stormshield\data\stormshield.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM flood_zones;")
    count = cursor.fetchone()[0]
    print(f"Total flood zones in DB: {count}")
    conn.close()
else:
    print("Database not found")
