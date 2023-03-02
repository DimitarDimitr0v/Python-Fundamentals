def line_up(up_dict: dict, side: str, user: str):
    # passing the command
    for total_users in up_dict.values():
        if user in total_users:
            return up_dict

    # completely new user and side
    if side not in up_dict:
        up_dict[side] = [user]
        return up_dict

    # side exist, user doesn't
    elif side in up_dict and user not in up_dict[side]:
        up_dict[side].append(user)
        return up_dict


def side_pointer(side_dict: dict, side: str, user: str):

    # changing sides
    for total_sides in side_dict.keys():
        if user in side_dict[total_sides]:
            side_dict[total_sides].remove(user)
            side_dict[side].append(user)
            print(f"{user} joins the {side} side!")
            return side_dict

    # completely new user and side
    if side not in side_dict:
        side_dict[side] = [user]

    # side exist, user doesn't
    elif side in side_dict and user not in side_dict[side]:
        side_dict[side].append(user)

    print(f"{user} joins the {side} side!")
    return side_dict


command = input()
side_user_dictionary = {}

while not command == "Lumpawaroo":

    if "|" in command:
        split = command.split(" | ")
        force_side = split[0]
        force_user = split[1]
        side_user_dictionary = line_up(side_user_dictionary, force_side, force_user)

    elif "->" in command:
        split = command.split(" -> ")
        force_side = split[1]
        force_user = split[0]
        side_user_dictionary = side_pointer(side_user_dictionary, force_side, force_user)

    command = input()

for key, value in side_user_dictionary.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for el in value:
            print(f"! {el}")