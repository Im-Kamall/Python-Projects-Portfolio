website = input("Enter website name: ")
username = input("Enter username: ")
password = input("Enter password: ")

with open("passwords.txt", "a") as file:
    file.write(f"Website: {website}, Username: {username}, Password: {password}\n")

print("Password saved successfully.")