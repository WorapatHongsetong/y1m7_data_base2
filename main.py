import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/maydata.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS rent_log (id INTEGER PRIMARY KEY, renter TEXT NOT NULL, renter_id INTEGER NOT NULL, title TEXT NOT NULL, book_id INTEGER NOT NULL)")

members_data = [
    ("Josh", "josh@email.com"),
    ("Sean", "sean@email.com"),
    ("Luke", "luke@email.com")
]

books_data = [
    ("Fun Novel", "Funny Man"),
    ("Mathematic", "Smart Man"),
    ("Brew Tea", "How to Easy"),
    ("Love chips", "Intel Person")
]

cursor.executemany("INSERT INTO members (username, email) VALUES (?, ?)", members_data)
cursor.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books_data)

con.commit()
con.close()
