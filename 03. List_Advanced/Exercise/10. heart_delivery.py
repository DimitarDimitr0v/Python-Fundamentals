def cupid_jump(collection: list, index: int):

    if collection[index] == 0:
        print(f"Place {index} already had Valentine's day.")

        return collection

    elif index <= len(collection):
        collection[index] -= 2

        if collection[index] == 0:
            print(f"Place {index} has Valentine's day.")

            return collection
        else:
            return collection


houses = [int(el) for el in input().split('@')]
initial_houses = len(houses)
command = input()
latest_index = 0

while not command == 'Love!':
    cmd_args = command.split()
    cmd_type = cmd_args[0]
    cmd_index = int(cmd_args[1]) + latest_index
    if cmd_index >= len(houses):
        cmd_index = 0

    if cmd_type == 'Jump':
        houses = cupid_jump(houses, cmd_index)

    latest_index = cmd_index

    command = input()

print(f"Cupid's last position was {latest_index}.")

if len([el for el in houses if el == 0]) == initial_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([el for el in houses if el != 0])} places.")