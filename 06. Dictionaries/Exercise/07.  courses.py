command = input()

registered_students = {}

while not command == "end":
    split = command.split(" : ")
    course = split[0]
    name = split[1]

    if course not in registered_students:
        registered_students[course] = [name]
    else:
        registered_students[course].append(name)

    command = input()

for key, value in registered_students.items():
    print(f"{key}: {len(value)}")
    for el in value:
        print(f"-- {el}")