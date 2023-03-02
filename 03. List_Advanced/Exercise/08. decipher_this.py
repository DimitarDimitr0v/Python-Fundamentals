text = input().split(" ")
result = []
for element in text:
    split_list = []
    remove = []
    result_number_to_ascii = []
    for i in range(len(element)):
        split_list.append(element[i])

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
    for elements in split_list:
        if elements in nums:
            result_number_to_ascii.append(elements)
            remove.append(elements)

    for e3 in remove:
        if e3 in split_list:
            split_list.remove(e3)

    a = "".join(result_number_to_ascii)

    letter = chr(int(a))
    split_list.insert(0, letter)

    temp = split_list[1]
    last = len(split_list) - 1

    split_list[1] = split_list[last]
    split_list[last] = temp

    cleared = "".join([str(x) for x in split_list])
    result.append(cleared)

print(" ".join(result))
