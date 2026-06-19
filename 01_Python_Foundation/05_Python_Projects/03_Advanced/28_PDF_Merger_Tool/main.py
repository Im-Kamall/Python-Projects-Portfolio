files = []

while True:
    file_name = input("Enter PDF file name or type done: ")

    if file_name.lower() == "done":
        break

    files.append(file_name)

print("Files to merge:")
for file in files:
    print(file)

print("PDF merge simulation completed.")