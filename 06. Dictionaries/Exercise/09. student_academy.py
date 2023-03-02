rows = int(input())
count = 1
students_dictionary = {}

for _ in range(1, rows + 1):
    name = input()
    grade = float(input())

    if name not in students_dictionary:
        students_dictionary[name] = [grade, count]
    else:
        students_dictionary[name][0] += grade
        students_dictionary[name][1] += count

for key, value in students_dictionary.items():
    if value[0] / value[1] >= 4.50:
        print(f"{key} -> {value[0] / value[1]:.2f}")