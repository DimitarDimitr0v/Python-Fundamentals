import re

pattern = r"(^|(?<=\s))\-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_numbers = re.finditer(pattern, text)
for match in valid_numbers:
    print(match.group(), end=" ")