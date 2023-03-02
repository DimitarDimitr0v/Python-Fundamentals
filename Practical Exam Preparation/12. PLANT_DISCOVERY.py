n = int(input())
current_plant = input()

plants_info = {}

# extract plant's data
for current_rotation in range(1, n + 1):
    current_plant = current_plant.split("<->")
    plant = current_plant[0]
    rarity = int(current_plant[1])

    plants_info[plant] = [rarity, []]

    if current_rotation == n:
        break

    current_plant = input()

# Commands
command = input()

# index[0] - rarity
# index[1] - rating
# index[2] - count

while not command == "Exhibition":
    args = ' '.join(command.split(" - ")).split()
    args = ' '.join(args).split()
    command_cmd = args[0]
    plant_name = args[1]

    if plant_name not in plants_info:
        print(f"error")
        break

    if command_cmd == "Rate:":
        rating = int(args[2])
        plants_info[plant_name][1].append(rating)

    elif command_cmd == "Update:":
        new_rarity = int(args[2])
        plants_info[plant_name][0] = new_rarity

    elif command_cmd == "Reset:":
        plants_info[plant_name][1] = []

    command = input()



print(f"Plants for the exhibition:")

for el in plants_info.items():
    if not el[1][1]:
        # means if el[1][1] is empty list
        average = 0
    else:
        average = sum(el[1][1]) / len(el[1][1])

    print(f"- {el[0]}; Rarity: {el[1][0]}; Rating: {average:.2f}")
