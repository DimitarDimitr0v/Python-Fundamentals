import re
total_length = 0
valid_locations = []

text = input()
pattern = r"(\=(?P<location>[A-Z]{1}[A-Za-z]{2,})\=)|(\/(?P<location_2>[A-Z]{1}[A-Za-z]{2,})\/)"


valid_matches = re.finditer(pattern, text)

for match in valid_matches:
    dict_of_matches = match.groupdict()
    for el in dict_of_matches.values():
        if el is not None:
            total_length += len(el)
            valid_locations.append(el)

a = ", ".join(valid_locations)

print(f"Destinations: {a}")
print(f"Travel Points: {total_length}")