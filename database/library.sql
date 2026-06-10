CREATE DATABASE IF NOT EXISTS library_db;

USE library_db;

CREATE TABLE books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    quantity INT
);

CREATE TABLE issued_books(
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    student_name VARCHAR(100),
    issue_date DATE,
    FOREIGN KEY(book_id) REFERENCES books(id)
);