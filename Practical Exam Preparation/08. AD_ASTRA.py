import re
info_dict = {}
calories = []

total_calories = 0
days = 0

pattern = r"(?P<separator>\#|\|)(?P<item_name>[A-Za-z\s]+)(?P=separator)(?P<exp_date>\d{2}\/\d{2}\/\d{2})(?P=separator)(?P<calories>\d+)(?P=separator)"
text = input()

valid_matches = re.finditer(pattern, text)

i = 0
for match in valid_matches:
    info_dict[i] = match.groupdict()
    calories.append(match.group('calories'))
    i += 1


for cal in calories:
    total_calories += int(cal)

while total_calories - 2000 >= 0:
    total_calories -= 2000
    days += 1

print(f"You have food to last you for: {days} days!")

for el in range(len(info_dict)):
    print(f"Item: {info_dict[el]['item_name']}, Best before: {info_dict[el]['exp_date']}, Nutrition: {info_dict[el]['calories']}")
