import re

pattern = r"\b\_(?P<variable>[A-Za-z0-9]+)\b"
valid_variables = []
text = input()

matches = re.finditer(pattern, text)

for match in matches:
    valid_variables.append(match.group('variable'))

print(','.join(valid_variables))