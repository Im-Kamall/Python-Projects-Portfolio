tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, task)

    elif choice == "3":
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print("Deleted:", removed_task)
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")