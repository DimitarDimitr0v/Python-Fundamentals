import re

names = []
ages = []

pattern = r"(\@(?P<name>[A-Za-z]+)\|)|\#(?P<age>[0-9]+)\*"
n = int(input())

for el in range(n):
    text = input()
    valid_matches = re.finditer(pattern, text)

    for match in valid_matches:
        if match.group('name'):
            names.append(match.group('name'))
        elif match.group('age'):
            ages.append(match.group('age'))

for x in range(len(names)):
    print(f"{names[x]} is {ages[x]} years old.")