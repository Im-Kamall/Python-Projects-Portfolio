books = []

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added.")

    elif choice == "2":
        if len(books) == 0:
            print("No books found.")
        else:
            for index, book in enumerate(books, start=1):
                print(index, book)

    elif choice == "3":
        book = input("Enter book name to search: ")
        if book in books:
            print("Book found:", book)
        else:
            print("Book not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")