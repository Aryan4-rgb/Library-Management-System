📚 Library Management System

A console-based Library Management System developed using Python and MySQL for efficient management of library records. The system allows librarians to manage books, track issued books, and maintain inventory through a simple menu-driven interface.

---

🚀 Features

- Add new books to the library
- View all available books
- Search books by title
- Issue books to students
- Return issued books
- Delete books from inventory
- Automatic quantity updates
- MySQL database integration

---

🛠️ Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Git
- GitHub

---

📂 Project Structure

Library-Management-System/

├── main.py

├── library.sql

├── requirements.txt

└── README.md

---

🗄️ Database Schema

Books Table

Column| Type
id| INT
title| VARCHAR(200)
author| VARCHAR(100)
quantity| INT

Issued Books Table

Column| Type
issue_id| INT
book_id| INT
student_name| VARCHAR(100)
issue_date| DATE

---

⚙️ Installation & Setup

1. Clone Repository

git clone https://github.com/yourusername/Library-Management-System.git
cd Library-Management-System

2. Install Dependencies

pip install -r requirements.txt

3. Create Database

Run the SQL script:

source library.sql;

4. Configure Database Credentials

Open "main.py" and update:

host="localhost"
user="root"
password="YOUR_PASSWORD"
database="library_db"

5. Run the Project

python main.py

---

📸 Sample Menu

===== LIBRARY MANAGEMENT SYSTEM =====

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

---

🎯 Learning Outcomes

- Database Design using MySQL
- CRUD Operations
- SQL Queries
- Python Database Connectivity
- Data Management and Validation
- Version Control with Git & GitHub

---

🔮 Future Improvements

- User Authentication
- Fine Calculation System
- GUI using Tkinter
- Book Reservation Feature
- Dashboard and Analytics
- Export Reports to CSV/PDF

---

👨‍💻 Author

Aryan

Developed as a portfolio project to demonstrate Python programming, SQL database management, and software development fundamentals.

