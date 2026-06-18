import os

path = input("Enter folder path: ")

files = os.listdir(path)

for file in files:
    print(file)