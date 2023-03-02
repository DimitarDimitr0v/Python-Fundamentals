command = input()
resources_quantities = []
resource_dictionary = {}

while not command == "stop":
    resources_quantities.append(command)
    command = input()

for el in range(0, len(resources_quantities), 2):
    resource_key = resources_quantities[el]
    quantity_value = int(resources_quantities[el + 1])


    if resource_key not in resource_dictionary:
        resource_dictionary[resource_key] = quantity_value
    else:
        resource_dictionary[resource_key] += quantity_value

for key, value in resource_dictionary.items():
    print(f"{key} -> {value}")