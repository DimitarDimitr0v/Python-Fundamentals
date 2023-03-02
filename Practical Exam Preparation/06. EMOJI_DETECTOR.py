import re
from functools import reduce
text = input()

# Calculating the required threshold
number_pattern = r"\d"
numbers = re.findall(number_pattern, text)
numbers = [int(x) for x in numbers]
required_threshold = reduce((lambda x, y: x * y), numbers)

# Extracting the emojis
unpacked_emoji = []
valid_emojis = []
length = 0

pattern = r"(?P<whole_emoji>(?P<separator>(\::|\*\*))?(?P<emoji>[A-Z]{1}[a-z]{2,})(?P=separator))"
valid_matches = re.finditer(pattern, text)


for match in valid_matches:
    current_threshold = 0
    emoji_dict = match.groupdict('emoji')
    current_emoji = emoji_dict['emoji']
    current_unpacked = emoji_dict['whole_emoji']

    for char in current_emoji:
        current_threshold += ord(char)

    if current_threshold >= required_threshold:
        valid_emojis.append(current_emoji)
        unpacked_emoji.append(current_unpacked)

    length += 1


print(f"Cool threshold: {required_threshold}")
print(f"{length} emojis found in the text. The cool ones are:")
for emoji in unpacked_emoji:
    print(emoji)
