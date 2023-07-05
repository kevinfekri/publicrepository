import csv
from cs50 import SQL

db = SQL("sqlite:///roster.db")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        student = row[1]
        house = row[2]
        head = row[3]
        db.execute("INSERT INTO students (student) VALUES (?)", student)
        db.execute("INSERT INTO houses (house, head) VALUES (?, ?)", house, head)
        db.execute("INSERT INTO assignements (student_id, house_id) VALUES (?, ?)", )
