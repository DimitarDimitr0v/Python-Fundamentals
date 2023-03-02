command = input()

product_dictionary = {}

while not command == "buy":
    split = command.split(" ")
    product = split[0]
    price = float(split[1])
    quantity = int(split[2])

    if product not in product_dictionary:
        product_dictionary[product] = [price, quantity]
    else:
        product_dictionary[product][0] = price
        product_dictionary[product][1] += quantity

    command = input()

for key, value in product_dictionary.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")