import sqlite3

conn = sqlite3.connect('databases/converter_database.db')

c = conn.cursor()


c.execute('''
CREATE TABLE IF NOT EXISTS workout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    round INTEGER,
    rep INTEGER,
    weight INTEGER
)
''')

conn.commit()


conn.close()

