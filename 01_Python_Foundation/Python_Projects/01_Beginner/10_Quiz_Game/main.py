score = 0

print("Welcome to Python Quiz Game!")

answer = input("1. What is the keyword used to define a function in Python? ")
if answer.lower() == "def":
    score += 1

answer = input("2. Which symbol is used for comments in Python? ")
if answer == "#":
    score += 1

answer = input("3. Which data type stores True or False values? ")
if answer.lower() == "boolean":
    score += 1

print("Your score is:", score, "/ 3")