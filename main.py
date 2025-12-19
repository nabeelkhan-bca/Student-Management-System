from database import connect_db

def add_student():
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    attendance = input("Enter Attendance: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students VALUES (NULL, ?, ?, ?)",
        (name, marks, attendance)
    )
    conn.commit()
    conn.close()
    print("Student Added Successfully")

def view_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
