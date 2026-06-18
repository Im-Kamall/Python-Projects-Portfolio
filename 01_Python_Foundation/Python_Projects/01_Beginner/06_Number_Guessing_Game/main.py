import random

secret = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret:
    print("You Win!")
else:
    print("You Lose!")
    print("Number was:", secret)