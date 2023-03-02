import re
valid_links = []
text = input()
pattern = r"(?P<link>(?P<sub_domain>\www)\.(?P<domain_name>[A-Za-z0-9\-\.]+)\.(?P<domain_extension>[a-z]+))"


while True:
    if text == "":
        break
    else:
        matches = re.finditer(pattern, text)
        for match in matches:
            valid_links.append(match.group('link'))
    text = input()

for el in valid_links:
    print(el)
