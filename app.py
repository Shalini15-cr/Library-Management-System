from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database connection
def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Student Login
@app.route('/student', methods=['GET', 'POST'])
def student():

    if request.method == 'POST':

        student_id = request.form['student_id']
        name = request.form['name']
        dept = request.form['dept']

        conn = connect_db()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO students(student_id, name, dept)
        VALUES (?, ?, ?)
        """, (student_id, name, dept))

        conn.commit()

        books = cur.execute("SELECT * FROM books").fetchall()

        return render_template(
            'student_dashboard.html',
            books=books
        )

    return render_template('student_login.html')

# Search Book
@app.route('/search', methods=['POST'])
def search():

    book_name = request.form['book_name']

    conn = connect_db()
    cur = conn.cursor()

    book = cur.execute("""
    SELECT * FROM books
    WHERE title LIKE ?
    """, ('%' + book_name + '%',)).fetchone()

    if book:
        return f"Book Available: {book[1]}"
    else:
        return "Book is not available in library"

# Admin Login
@app.route('/admin')
def admin():

    conn = connect_db()
    cur = conn.cursor()

    students = cur.execute("SELECT * FROM students").fetchall()
    transactions = cur.execute("SELECT * FROM transactions").fetchall()

    return render_template(
        'admin_dashboard.html',
        students=students,
        transactions=transactions
    )

if __name__ == '__main__':
    app.run(debug=True)