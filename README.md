# 📚 Library Management System

A modern and user-friendly **Library Management System** built using **Python Flask**, **MongoDB**, **HTML**, **CSS**, and **JavaScript**. This application streamlines library operations by enabling students to search and request books while allowing librarians to manage books, approve requests, and maintain transaction records.

---

## 🚀 Features

### 👨‍🎓 Student Module
- Secure Student Login
- View Available Books
- Search Books by Title
- View Book Details & Reviews
- Request Books
- View Request Status
- Logout

### 👩‍💼 Librarian Module
- Secure Admin Login
- View Student Details
- Add, Update, and Delete Books
- Approve or Reject Book Requests
- Issue & Return Books
- Manage Book Availability
- View Transaction History

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python Flask |
| Database | MongoDB |
| Database Driver | PyMongo |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
Library-Management-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   └── db.py
│
├── models/
│   ├── student.py
│   ├── admin.py
│   ├── book.py
│   └── transaction.py
│
├── templates/
│   ├── index.html
│   ├── student_login.html
│   ├── student_dashboard.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   └── search_result.html
│
└── static/
    ├── style.css
    ├── script.js
    └── images/
```

---

## 📖 Book Collection

The system includes a preloaded collection of books, including:

- **Operating Systems: Internals and Design Principles** – William Stallings
- **This is Marketing** – Seth Godin
- **The Psychology of Money** – Morgan Housel
- **Atomic Habits** – James Clear
- **The Power of Positive Thinking** – Norman Vincent Peale

---

## 🔄 Workflow

```text
Home
   │
   ├── Student Login
   │       │
   │       ├── View Books
   │       ├── Search Books
   │       ├── View Reviews
   │       └── Request Book
   │
   └── Librarian Login
           │
           ├── Manage Books
           ├── View Requests
           ├── Issue Book
           ├── Return Book
           └── Transaction History
```

---

## 💾 Database Collections

- Students
- Admins
- Books
- Requests
- Transactions

---

## ⚡ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Library-Management-System.git
cd Library-Management-System
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure MongoDB

Create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
```

### 6️⃣ Run the Application

Open your browser:

```
https://library-management-system-823498055923.asia-southeast1.run.app 
```

---

## 📸 Screenshots

> Add screenshots here after completing the project.

- Home Page  
- Student Dashboard
- Admin Dashboard
- Book Search
- Transaction History

---

## 🎯 Future Enhancements

- Barcode / QR Code Integration
- Email Notifications
- Due Date Reminders
- Fine Management
- Book Reservation
- Analytics Dashboard
- AI-Based Book Recommendations
- User Profile Management

---

## 🎓 Learning Outcomes

This project helped in understanding:

- Python Flask Web Development
- RESTful Routing
- MongoDB Database Integration
- CRUD Operations
- Role-Based Authentication
- Responsive Web Design
- Git & GitHub Version Control

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Author

**Shalini C. R**

B.Tech – Computer Science and Business Systems

Passionate about Python, Full-Stack Development, Business Analytics, and AI-powered applications.

---

Focus on Learning 
