import re
valid_strings = []

total_pairs = []
valid_mirror_pairs = []

text = input()
pattern = r"((\#([A-Za-z]{3,})\#)|(\#[A-Za-z]{3,})\#){2}|((\@([A-Za-z]{3,})\@)|(\@[A-Za-z]{3,})\@){2}"

valid_matches = re.finditer(pattern, text)

for match in valid_matches:
    total_pairs.append(match.group())

pattern = r"(((\#([A-Za-z]{3,})\#)|(\#[A-Za-z]{3,})\#)|((\@([A-Za-z]{3,})\@)|(\@[A-Za-z]{3,})\@))"

valid_matches = re.finditer(pattern, text)
for m in valid_matches:
    valid_strings.append(m.group())





# mirror pair check
for i in range(len(valid_strings)):
    if 0 <= i + 1 <= len(valid_strings):
        if valid_strings[i - 1] == valid_strings[i][::-1]:

            x = [valid_strings[i - 1], " <=> ", valid_strings[i]]
            valid_mirror_pairs.append(x)


for lists in valid_mirror_pairs:
    for element in lists:
        if element in valid_strings:
            valid_strings.remove(element)


if len(total_pairs) <= 0:
    print(f"No word pairs found!")
else:

    print(f"{len(total_pairs)} word pairs found!")

if len(valid_mirror_pairs) <= 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")

clean_mirror_pairs = []

for el in valid_mirror_pairs:
    for i in range(len(el)):
        current_element = el[i]
        el.pop(i)
        ch = current_element[1:-1]
        el.insert(i, ch)

counter = 0

clear_list = []

for lists in valid_mirror_pairs:
    pair_as_string = " ".join(lists)
    clear_list.append(pair_as_string)

print(", ".join(clear_list), end="")