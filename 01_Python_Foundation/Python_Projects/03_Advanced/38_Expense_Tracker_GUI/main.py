print("Expense Tracker GUI Simulation")

expenses = []

expense_name = input("Enter expense name: ")
amount = float(input("Enter amount: "))

expenses.append([expense_name, amount])

print("Expense added successfully.")
print("Expenses:", expenses)