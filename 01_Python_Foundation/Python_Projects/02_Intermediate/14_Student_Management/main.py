students = {}

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        students[roll_no] = {
            "name": name,
            "marks": marks
        }

        print("Student added.")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for roll_no, details in students.items():
                print("Roll No:", roll_no)
                print("Name:", details["name"])
                print("Marks:", details["marks"])
                print("----------------")

    elif choice == "3":
        roll_no = input("Enter roll number to search: ")
        if roll_no in students:
            print("Name:", students[roll_no]["name"])
            print("Marks:", students[roll_no]["marks"])
        else:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")