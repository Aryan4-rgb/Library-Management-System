import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryan@4444",
    database="library_db"
)

cursor = conn.cursor()

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    sql = "INSERT INTO books(title,author,quantity) VALUES(%s,%s,%s)"
    values = (title, author, quantity)

    cursor.execute(sql, values)
    conn.commit()

    print("Book Added Successfully")

def view_books():
    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    print("\nBOOK LIST")

    for book in books:
        print(book)

def search_book():
    name = input("Enter Book Name: ")

    sql = "SELECT * FROM books WHERE title LIKE %s"

    cursor.execute(sql, ('%' + name + '%',))

    books = cursor.fetchall()

    if books:
        for book in books:
            print(book)
    else:
        print("Book Not Found")

def issue_book():
    book_id = int(input("Enter Book ID: "))
    student = input("Enter Student Name: ")

    cursor.execute(
        "SELECT quantity FROM books WHERE id=%s",
        (book_id,)
    )

    result = cursor.fetchone()

    if result and result[0] > 0:

        cursor.execute(
            """
            INSERT INTO issued_books
            (book_id,student_name,issue_date)
            VALUES(%s,%s,%s)
            """,
            (book_id, student, date.today())
        )

        cursor.execute(
            """
            UPDATE books
            SET quantity=quantity-1
            WHERE id=%s
            """,
            (book_id,)
        )

        conn.commit()

        print("Book Issued Successfully")

    else:
        print("Book Not Available")

def return_book():
    issue_id = int(input("Enter Issue ID: "))

    cursor.execute(
        "SELECT book_id FROM issued_books WHERE issue_id=%s",
        (issue_id,)
    )

    result = cursor.fetchone()

    if result:

        book_id = result[0]

        cursor.execute(
            "UPDATE books SET quantity=quantity+1 WHERE id=%s",
            (book_id,)
        )

        cursor.execute(
            "DELETE FROM issued_books WHERE issue_id=%s",
            (issue_id,)
        )

        conn.commit()

        print("Book Returned Successfully")

    else:
        print("Issue ID Not Found")

def delete_book():
    book_id = int(input("Enter Book ID: "))

    cursor.execute(
        "DELETE FROM books WHERE id=%s",
        (book_id,)
    )

    conn.commit()

    print("Book Deleted Successfully")

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")