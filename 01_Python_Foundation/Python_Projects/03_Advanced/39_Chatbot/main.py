print("Chatbot: Hello! I am your Python chatbot.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user:
        print("Chatbot: Hello Kamal!")
    elif "python" in user:
        print("Chatbot: Python is a great programming language.")
    elif "name" in user:
        print("Chatbot: My name is PyBot.")
    else:
        print("Chatbot: Sorry, I don't understand.")