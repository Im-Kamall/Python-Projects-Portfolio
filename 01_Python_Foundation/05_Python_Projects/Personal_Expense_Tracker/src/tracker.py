import csv
import os
from src.expense import Expense


class ExpenseTracker:
    def __init__(self, file_path="data/expenses.csv"):
        self.file_path = file_path
        self.headers = ["Date", "Category", "Description", "Amount"]
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        os.makedirs("data", exist_ok=True)
        os.makedirs("reports", exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)

    def add_expense(self, date, category, description, amount):
        try:
            expense = Expense(date, category, description, amount)

            with open(self.file_path, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(expense.to_list())

            print("Expense added successfully!")

        except Exception as e:
            print(f"Error adding expense: {e}")

    def read_expenses(self):
        expenses = []

        try:
            with open(self.file_path, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    expenses.append(row)

        except FileNotFoundError:
            print("Expense file not found.")

        except Exception as e:
            print(f"Error reading expenses: {e}")

        return expenses

    def view_expenses(self):
        expenses = self.read_expenses()

        if not expenses:
            print("No expenses found.")
            return

        print("\n===== All Expenses =====")
        for expense in expenses:
            print(
                f"{expense['Date']} | {expense['Category']} | "
                f"{expense['Description']} | ₹{float(expense['Amount']):.2f}"
            )

    def search_expenses(self, keyword):
        expenses = self.read_expenses()
        keyword = keyword.lower()

        results = [
            expense for expense in expenses
            if keyword in expense["Date"].lower()
            or keyword in expense["Category"].lower()
            or keyword in expense["Description"].lower()
        ]

        if not results:
            print("No matching expenses found.")
            return

        print("\n===== Search Results =====")
        for expense in results:
            print(
                f"{expense['Date']} | {expense['Category']} | "
                f"{expense['Description']} | ₹{float(expense['Amount']):.2f}"
            )

    def monthly_summary(self, month):
        expenses = self.read_expenses()
        total = 0

        for expense in expenses:
            if expense["Date"].startswith(month):
                total += float(expense["Amount"])

        print(f"\nTotal spending for {month}: ₹{total:.2f}")

    def category_summary(self):
        expenses = self.read_expenses()
        summary = {}

        for expense in expenses:
            category = expense["Category"]
            amount = float(expense["Amount"])

            summary[category] = summary.get(category, 0) + amount

        if not summary:
            print("No expenses available.")
            return

        print("\n===== Category-wise Spending =====")
        for category, total in summary.items():
            print(f"{category}: ₹{total:.2f}")

    def export_report(self):
        expenses = self.read_expenses()

        if not expenses:
            print("No expenses to export.")
            return

        report_path = "reports/expense_report.csv"

        try:
            with open(report_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(expenses)

            print(f"Report exported successfully: {report_path}")

        except Exception as e:
            print(f"Error exporting report: {e}")