def jump(jump_length: int, collection: list):

    if collection[jump_length] == 0:
        print(f"Place {jump_length} already had Valentine's day.")

        return collection

    elif jump_length <= len(collection):
        collection[jump_length] -= 2

        if collection[jump_length] <= 0:
            print(f"Place {jump_length} has Valentine's day.")

            return collection
        else:
            return collection


houses = [int(x) for x in input().split("@")]
command = input()
previous_length = 0

while not command == "Love!":
    cmd_args = command.split(" ")

    order = cmd_args[0]
    length = int(cmd_args[1]) + previous_length

    if length > len(houses) - 1:
        length = 0

    if order == "Jump":
        houses = jump(length, houses)

    previous_length = length

    command = input()


failed = 0
for el in houses:
    if el != 0:
        failed += 1

print(f"Cupid's last position was {previous_length}.")
if failed > 0:
    print(f"Cupid has failed {failed} places.")
else:
    print(f"Mission was successful")
