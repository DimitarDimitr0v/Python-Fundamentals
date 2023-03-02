import re
valid = []
text = input()
pattern = r"(?P<email>((?P<user>(^|(?<=[A-Za-z0-9\s]))\b[A-Za-z0-9][A-Za-z0-9\.\-\_]+[A-Za-z0-9])\@(?P<host>[A-Za-z0-9][A-Za-z0-9\-\.]+\.[A-Za-z0-9\.]+\b)))"

match = re.finditer(pattern, text)

for match in match:
    valid.append(match.group('email'))
