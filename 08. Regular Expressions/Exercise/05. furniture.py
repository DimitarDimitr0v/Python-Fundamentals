import re

text = input()
total_money = 0
pattern = r"\>>(?P<furniture_name>[A-Za-z]+)\<<(?P<price>[0-9][0-9\.]+)\!(?P<quantity>\d+)"

print(f"Bought furniture:")

while text != "Purchase":
    matches = re.finditer(pattern, text)
    for match in matches:
        current_name = match.group('furniture_name')
        current_price = float(match.group('price'))
        current_quantity = int(match.group('quantity'))
        total_money += (current_quantity * current_price)
        print(current_name)
    text = input()

print(f"Total money spend: {total_money:.2f}")