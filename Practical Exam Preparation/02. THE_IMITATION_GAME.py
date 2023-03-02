def move_case(collection: list, number_of_letters: int):
    for moves in range(1, number_of_letters + 1):
        current_letter = collection[0]
        collection.remove(current_letter)
        collection.append(current_letter)

    return collection


def insert_case(collection: list, f_index: int, f_value: str):
    if 0 <= f_index <= len(collection):
        # collection.insert(f_index, f_value)
        for c in f_value:
            collection.insert(f_index, c)
            f_index += 1

    return collection


def change_all_case(collection: list, f_substring: str, f_replacement: str):
    for position in range(len(collection)):
        current_letter = collection[position]

        if current_letter == f_substring:
            collection[position] = f_replacement

    return collection


encrypted_message = input()
current_command = input()
encrypted_message_list = []

for el in encrypted_message:
    encrypted_message_list.append(el)

while current_command != "Decode":
    string_args = current_command.split("|")
    command = string_args[0]

    if command == "Move":
        number = int(string_args[1])
        move_case(encrypted_message_list, number)

    elif command == "Insert":
        index = int(string_args[1])
        value = string_args[2]
        insert_case(encrypted_message_list, index, value)

    elif command == "ChangeAll":
        substring = string_args[1]
        replacement = string_args[2]
        change_all_case(encrypted_message_list, substring, replacement)

    current_command = input()

decrypted_message = "".join(encrypted_message_list)
print(f"The decrypted message is: {decrypted_message}")