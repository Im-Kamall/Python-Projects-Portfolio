from src.tracker import ExpenseTracker
from src.utils import get_valid_amount, get_valid_date


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Monthly Summary")
        print("5. Category-wise Spending")
        print("6. Export Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = get_valid_date()
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = get_valid_amount()

            tracker.add_expense(date, category, description, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            keyword = input("Enter keyword/category/date to search: ")
            tracker.search_expenses(keyword)

        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            tracker.monthly_summary(month)

        elif choice == "5":
            tracker.category_summary()

        elif choice == "6":
            tracker.export_report()

        elif choice == "7":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()