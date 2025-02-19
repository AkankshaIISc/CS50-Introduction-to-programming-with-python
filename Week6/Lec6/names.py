# name = input("What's your name? ")

# file = open("text.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("text.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("text.txt", "r") as file:
#      lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())


# with open("text.txt", "r") as file:
#      for line in file:
#           print("hello,", line.rstrip())

# names = []
# with open("text.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}")

# with open("text.txt") as file:
#     for line in sorted(file, reverse = True):
#         print(f"Hello, {line.rstrip()}")

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
#import csv

# students = []

# # with open("students.csv") as file:
# #     for line in file:
# #         name, house = line.rstrip().split(",")
# #         student = {"name": name, "house": house}
# #         students.append(student)

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# #def get_name(students):
#  #   return students["name"]

# #for student in sorted(students, key = get_name):
#  #   print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key = lambda student: students["name"]):
#     print(f"{student['name']} is in {student['home']}")
# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("Students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

names = []

with open('./names.txt') as file: # in general open always read file till the time you assign it to write the file
    for line in sorted(file, reverse=True):
        print(f'hello, {line.rstrip()}')
