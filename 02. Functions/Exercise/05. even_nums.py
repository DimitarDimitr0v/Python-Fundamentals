def even_num(nums):
    even_list = []
    for e in nums:
        if int(e) % 2 != 0:
            continue
        else:
            even_list.append(e)
    return even_list


numbers = [int(x) for x in input().split(" ")]

print(even_num(numbers))