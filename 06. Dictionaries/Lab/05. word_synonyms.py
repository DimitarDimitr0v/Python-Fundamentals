words = int(input())
dictionary = {}

for el in range(1, words + 1):
    current_word = input()
    synonym = input()

    if current_word not in dictionary:
        dictionary[current_word] = [synonym]
    else:
        dictionary[current_word].append(synonym)

for key, value in dictionary.items():
    string_value = ", ".join(value)
    print(f"{key} - {string_value}")