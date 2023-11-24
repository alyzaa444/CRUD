import sqlite3


# SQLite Database Initialization
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
       CREATE TABLE submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    suggest TEXT NOT NULL,
    rating INTEGER,
    coming INTEGER
    )
    ''')
    cursor.execute('''INSERT INTO submissions (id,fullname,suggest,rating,coming) VALUES (1,"Budi","Great",4,5)''')
    conn.commit()
    conn.close()


init_db()