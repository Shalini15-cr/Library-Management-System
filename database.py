import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

# Students Table
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    name TEXT,
    dept TEXT
)
""")

# Books Table
cur.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    status TEXT
)
""")

# Transactions Table
cur.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    book_name TEXT,
    issue_date TEXT
)
""")

# Insert Books
books = [
("Operating Systems: Internals and Design Principles", "William Stallings", "Available"),

("This is Marketing", "Seth Godin", "Available"),

("The Psychology Of Money", "Morgan Housel", "Available"),

("Atomic Habits", "James Clear", "Available"),

("The Power of Positive Thinking", "Norman Vincent Peale", "Available")
]

cur.executemany("""
INSERT INTO books(title, author, status)
VALUES (?, ?, ?)
""", books)

conn.commit()

print("Database Created Successfully")