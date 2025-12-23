import csv

students = []

with open("name.csv") as file:
    # reader = csv.reader(file)  # reader() returns a list
    reader = csv.DictReader(file)  # DictReader() returns a Dict
    for row in reader:  # this will take "" as one, and separate by comma
        students.append({"name": row["name"], "clan": row["clan"]})  # or simply students.append(row)

# def get_name(student):  # student is a dictionary
#     return student["name"]


for student in sorted(students, key=lambda member: member["name"]):
    # member's each student dictionary,also the name of
    # the parameter passed to the lambda function
    print(student["name"], student["clan"])
