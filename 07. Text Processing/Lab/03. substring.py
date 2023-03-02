string_to_remove = input()
sequence_of_strings = input()

while string_to_remove in sequence_of_strings:
    sequence_of_strings = sequence_of_strings.replace(string_to_remove, "")

print(sequence_of_strings)