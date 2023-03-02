import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

valid_matches = re.findall(pattern, text)
print(" ".join(valid_matches))