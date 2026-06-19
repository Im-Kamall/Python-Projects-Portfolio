expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append([name, amount])
        print("Expense added.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(expense[0], ":", expense[1])

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[1]
        print("Total Expense:", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")