employees = {}

while True:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")

        employees[emp_id] = name

    elif choice == "2":
        for emp_id, name in employees.items():
            print(emp_id, "-", name)

    elif choice == "3":
        break