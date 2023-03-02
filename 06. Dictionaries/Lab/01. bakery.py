elements = input().split(" ")
bakery = {}

for i in range(0, len(elements), 2):
    keys = elements[i]
    values = int(elements[i + 1])
    bakery[keys] = int(values)

print(bakery)