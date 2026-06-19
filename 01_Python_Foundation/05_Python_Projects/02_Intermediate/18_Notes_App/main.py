note = input("Write a note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note Saved!")