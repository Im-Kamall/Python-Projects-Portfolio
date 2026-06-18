print("Personal AI Assistant")

while True:
    command = input("Enter command: ").lower()

    if command == "exit":
        print("Assistant stopped.")
        break
    elif "hello" in command:
        print("Hello Kamal!")
    elif "study" in command:
        print("Focus on Python, Data Science, Machine Learning, and AI.")
    elif "motivate" in command:
        print("Keep building projects. Your portfolio will grow stronger.")
    else:
        print("Command not recognized.")