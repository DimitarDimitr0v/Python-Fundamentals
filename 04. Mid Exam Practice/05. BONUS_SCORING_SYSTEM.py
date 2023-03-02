import math
number_students = int(input())
lectures = int(input())
additional_bonus = int(input())
attendance_list = []
lecture_list = []


for el in range(number_students):
    current_attendances = int(input())
    total_bonus = (current_attendances / lectures) * (5 + additional_bonus)
    attendance_list.append(total_bonus)
    lecture_list.append(current_attendances)


    print(f"Max Bonus: {math.ceil(max(attendance_list))}.")
    print(f"The student has attended {max(lecture_list)} lectures.")