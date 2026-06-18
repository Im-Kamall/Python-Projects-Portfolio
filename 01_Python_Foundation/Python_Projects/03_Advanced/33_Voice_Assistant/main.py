command = input("Enter your command: ").lower()

if "hello" in command:
    print("Assistant: Hello Kamal!")
elif "time" in command:
    print("Assistant: I can tell time in the advanced version.")
elif "open" in command:
    print("Assistant: Opening app simulation.")
else:
    print("Assistant: Sorry, I did not understand.")