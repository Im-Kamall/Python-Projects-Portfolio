from datetime import date

name = input("Enter student name: ")
status = input("Present or Absent: ")

with open("attendance.txt", "a") as file:
    file.write(f"{date.today()} - {name} - {status}\n")

print("Attendance saved.")