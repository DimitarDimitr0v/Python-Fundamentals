def contains_statement(f_activation_key: str, f_substring: str):
    if f_substring in f_activation_key:
        print(f"{f_activation_key} contains {f_substring}")
    else:
        print(f"Substring not found!")


def flip_statement(f_activation_key: str, f_case: str, f_starting_point: int, f_finishing_point: int):
    if case == "Upper":
        f_activation_key = f_activation_key.replace(f_activation_key[f_starting_point:f_finishing_point],
                                                    f_activation_key[f_starting_point:f_finishing_point].upper())
        print(f_activation_key)
        return f_activation_key

    elif case == "Lower":
        f_activation_key = f_activation_key.replace(f_activation_key[f_starting_point:f_finishing_point],
                                                    f_activation_key[f_starting_point:f_finishing_point].lower())
        print(f_activation_key)
        return f_activation_key

    return f_activation_key


def slice_statement(f_activation_key: str, f_start_index: int, f_end_index: int):
    f_activation_key = f_activation_key.replace(f_activation_key[start_index:end_index], "")
    print(f_activation_key)
    return f_activation_key


raw_activation_key = input()
operations = input()
activation_key = raw_activation_key

while not operations == "Generate":
    operation_args = operations.split(">>>")

    command = operation_args[0]

    if command == "Contains":
        substring = operation_args[1]
        contains_statement(activation_key, substring)

    elif command == "Flip":
        case = operation_args[1]
        starting_point = int(operation_args[2])
        finishing_point = int(operation_args[3])
        activation_key = flip_statement(activation_key, case, starting_point, finishing_point)

    elif command == "Slice":
        start_index = int(operation_args[1])
        end_index = int(operation_args[2])
        activation_key = slice_statement(activation_key, start_index, end_index)

    operations = input()

print(f"Your activation key is: {activation_key}")