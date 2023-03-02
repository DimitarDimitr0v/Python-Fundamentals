command = input()

company_dictionary = {}

while not command == "End":
    split = command.split(" -> ")
    name = split[0]
    id = split[1]

    if name not in company_dictionary:
        company_dictionary[name] = [id]
    else:
        if id not in company_dictionary[name]:
            company_dictionary[name].append(id)

    command = input()


for key, value in company_dictionary.items():
    print(f"{key}")
    for el in value:
        print(f"-- {el}")