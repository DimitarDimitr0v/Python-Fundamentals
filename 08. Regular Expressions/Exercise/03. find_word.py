import re

count = 0
text = input().lower()
pattern = rf"\b{input().lower()}\b"

for el in re.finditer(pattern, text):
    count += 1

print(count)