import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/maydata.db")
cursor = con.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL)")
# cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)")
# cursor.execute("CREATE TABLE IF NOT EXISTS rent_log (id INTEGER PRIMARY KEY, renter TEXT NOT NULL, renter_id INTEGER NOT NULL, title TEXT NOT NULL, book_id INTEGER NOT NULL)")

# members_data = [
#     ("Josh", "josh@email.com"),
#     ("Sean", "sean@email.com"),
#     ("Luke", "luke@email.com")
# ]

# books_data = [
#     ("Fun Novel", "Funny Man"),
#     ("Mathematic", "Smart Man"),
#     ("Brew Tea", "How to Easy"),
#     ("Love chips", "Intel Person")
# ]

# cursor.executemany("INSERT INTO members (username, email) VALUES (?, ?)", members_data)
# cursor.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books_data)

# cursor.execute("DROP TABLE IF EXISTS rent_log")

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS rent_log (
#         id INTEGER PRIMARY KEY,
#         renter_id INTEGER NOT NULL,
#         book_id INTEGER NOT NULL,
#         FOREIGN KEY(renter_id) REFERENCES members(id) ON DELETE CASCADE,
#         FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
#     )
# """)

# rent_log_data = [
#     (1, 1),  # Josh,Fun Novel
#     (2, 2),  # Sean,Mathematic
#     (3, 3),  # Luke,Brew Tea
# ]

# cursor.executemany("INSERT INTO rent_log (renter_id, book_id) VALUES (?, ?)", rent_log_data)

cursor = con.execute("SELECT username FROM members WHERE username LIKE '%a%'")
print("Members whose username contains the letter 'a':")
for row in cursor:
    print(row)

cursor = con.execute("""
    SELECT m.username, b.title 
    FROM rent_log r
    JOIN members m ON r.renter_id = m.id
    JOIN books b ON r.book_id = b.id
    WHERE b.title = 'Fun Novel'
""")
print("\nMembers who rented 'Fun Novel':")
for row in cursor:
    print(row)

con.commit()
con.close()
