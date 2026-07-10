students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")
        department = input("Enter Department: ")

        student = {
            "Name": name,
            "Roll No": roll_no,
            "Department": department
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Records Found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")
        found = False

        for student in students:
            if student["Roll No"] == roll_no:
                print("Student Found:")
                print(student)
                found = True
                break

        if not found:
            print("Student Not Found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")

        for student in students:
            if student["Roll No"] == roll_no:
                students.remove(student)
                print("Student Deleted Successfully!")
                break
        else:
            print("Student Not Found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice. Please Try Again.")
