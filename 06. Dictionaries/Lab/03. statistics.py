command = input()
bakery = {}

while not command == "statistics":
    spited = command.split(" ")
    kay = (spited[0])
    value = int((spited[1]))

    if kay in bakery:
        bakery[kay] += value
    else:
        bakery[kay] = value
    command = input()

print(f"Products in stock:")
# Dictionary comprehension: (25, 26 LINE)
# [print(f"- {key}: {value}") for (key, value) in bakery]
for kay, value in bakery.items():
    print(f"- {kay} {value}")

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")