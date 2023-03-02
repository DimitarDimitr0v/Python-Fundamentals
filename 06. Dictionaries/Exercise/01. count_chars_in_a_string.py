words = input().split(" ")
letter_dictionary = {}

for each_word in words:
    for each_letter in each_word:
        if each_letter not in letter_dictionary:
            letter_dictionary[each_letter] = 1
        else:
            letter_dictionary[each_letter] += 1

for key, value in letter_dictionary.items():
    print(f"{key} -> {value}")