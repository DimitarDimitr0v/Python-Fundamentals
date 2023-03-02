name_and_number = input()


phone_dictionary = {}

while not name_and_number.isnumeric():
    split = name_and_number.split("-")
    name = split[0]
    number = split[1]

    phone_dictionary[name] = number

    name_and_number = input()

n = int(name_and_number)

for el in range(1, n + 1):
    name_check = input()
    for key, value in phone_dictionary.items():
        if key in name_check:
            print(f"{name_check} -> {value}")
            break

    else:
        print(f"Contact {name_check} does not exist.")