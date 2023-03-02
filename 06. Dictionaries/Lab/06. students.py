data = input()
students_info = {}

while not data == data.lower():
    split = data.split(":")
    student_name = split[0]
    student_id = split[1]
    student_course = split[2]
    if student_course not in students_info:
        students_info[student_course] = {student_name: student_id}
    else:
        students_info[student_course][student_name] = student_id

    data = input()

course = " ".join(data.split("_"))

for key, value in students_info.items():
    if key == course:
        for name, id in value.items():
            print(f"{name} - {id}")