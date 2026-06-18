rooms = {
    "101": "Available",
    "102": "Available",
    "103": "Available"
}

while True:
    print("\nHotel Management System")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for room, status in rooms.items():
            print(room, "-", status)

    elif choice == "2":
        room_no = input("Enter room number: ")

        if room_no in rooms and rooms[room_no] == "Available":
            rooms[room_no] = "Booked"
            print("Room booked successfully.")
        else:
            print("Room not available.")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")