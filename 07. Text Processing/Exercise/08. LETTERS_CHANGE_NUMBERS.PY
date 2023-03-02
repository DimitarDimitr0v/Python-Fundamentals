import string
sequence = input().split()

number = ""
first_letter = ""
last_letter = ""
total_sum = 0


for el in sequence:
    number = ""
    for ch in el:

        first_letter = el[0]
        last_letter = el[-1]

        if ch.isnumeric():
            number += ch

    number = int(number)
    if first_letter.isupper():
        first_position = string.ascii_uppercase.index(first_letter) + 1
        total_sum += (number / int(first_position))
    else:
        first_position = string.ascii_lowercase.index(first_letter) + 1
        total_sum += number * int(first_position)


    if last_letter.isupper():
        second_position = string.ascii_uppercase.index(last_letter) + 1
        total_sum -= int(second_position)
    else:
        second_position = string.ascii_lowercase.index(last_letter) + 1
        total_sum += int(second_position)

print(f"{total_sum:.2f}")