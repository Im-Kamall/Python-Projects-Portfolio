inventory = {}

while True:
    print("1. Add Item")
    print("2. View Items")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        item = input("Item Name: ")
        qty = int(input("Quantity: "))

        inventory[item] = qty

    elif choice == "2":
        for item, qty in inventory.items():
            print(item, "-", qty)

    elif choice == "3":
        break