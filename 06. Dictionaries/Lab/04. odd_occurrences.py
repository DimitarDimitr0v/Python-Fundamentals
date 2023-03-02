elements = [x.lower() for x in input().split(" ")]
element_dict = {}
value = 0

for el in elements:
    key = el
    if el not in element_dict:
        element_dict[key] = value
        element_dict[key] += 1
    else:
        element_dict[key] += 1

print(" ".join([keys for keys, values in element_dict.items() if not values % 2 == 0]))
