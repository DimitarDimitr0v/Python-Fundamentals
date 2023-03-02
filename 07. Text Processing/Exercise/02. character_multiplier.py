strings = input().split(" ")

shortest_length_in_list = (min(strings, key=len))
longest_length_in_list = (max(strings, key=len))

total_sum = 0

name_1 = strings[0]
name_2 = strings[1]

length_1 = len(name_1)
length_2 = len(name_2)

difference = 0

new_1 = []
new_2 = []

if length_1 > length_2:
    difference = length_1 - length_2
else:
    difference = length_2 - length_1


for el_1 in name_1:
    new_1.append(el_1)

for el_2 in name_2:
    new_2.append(el_2)


for x in range(len(longest_length_in_list) - difference):
    current_sum = ord(name_1[x]) * ord(name_2[x])
    total_sum += current_sum
    new_1.remove(name_1[x])
    new_2.remove(name_2[x])


for left_letters_1 in new_1:
    total_sum += ord(left_letters_1)

for left_letters_2 in new_2:
    total_sum += ord(left_letters_2)

print(total_sum)