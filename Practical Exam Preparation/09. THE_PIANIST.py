def add_case(f_favorite_pieces: dict, f_piece_name: str, f_composer: str, f_key: str):

    if f_piece_name not in f_favorite_pieces:
        f_favorite_pieces[f_piece_name] = [f_composer, f_key]
        print(f"{f_piece_name} by {f_composer} in {f_key} added to the collection!")
        return f_favorite_pieces

    print(f"{f_piece_name} is already in the collection!")
    return f_favorite_pieces


def remove_case(f_favorite_pieces: dict, f_piece_to_remove):

    if f_piece_to_remove in f_favorite_pieces:
        print(f"Successfully removed {f_piece_to_remove}!")
        f_favorite_pieces.pop(f_piece_to_remove)
        return f_favorite_pieces

    print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    return f_favorite_pieces


def change_case(f_favorite_pieces: dict, f_piece_name: str, f_key_to_change: str):

    if f_piece_name in f_favorite_pieces:
        f_favorite_pieces[f_piece_name][1] = f_key_to_change
        print(f"Changed the key of {f_piece_name} to {key_to_change}!")
        return f_favorite_pieces

    print(f"Invalid operation! {f_piece_name} does not exist in the collection.")
    return f_favorite_pieces


number_of_pieces = int(input())

pieces_info = {}

for pieces in range(number_of_pieces):
    current_piece = input().split("|")
    piece_name = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]

    pieces_info[piece_name] = [composer, key]

command = input()

while not command == "Stop":
    command_args = command.split("|")
    order = command_args[0]

    if order == "Add":
        cmd_piece_name = command_args[1]
        cmd_composer = command_args[2]
        cmd_key = command_args[3]
        add_case(pieces_info, cmd_piece_name, cmd_composer, cmd_key)

    elif order == "Remove":
        piece_to_remove = command_args[1]
        remove_case(pieces_info, piece_to_remove)

    elif order == "ChangeKey":
        c_piece_name = command_args[1]
        key_to_change = command_args[2]
        change_case(pieces_info, c_piece_name, key_to_change)

    command = input()

for elements in pieces_info.items():
    print(f"{elements[0]} -> Composer: {elements[1][0]}, Key: {elements[1][1]}")