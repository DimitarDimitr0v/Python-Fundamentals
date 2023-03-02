def plunder_case(f_destination_info: dict, f_target_city: str, f_population_killed: int, f_gold_stolen: int):
    print(f"{f_target_city} plundered! {gold_stolen} gold stolen, {f_population_killed} citizens killed.")
    f_destination_info[f_target_city][0] -= f_population_killed
    f_destination_info[f_target_city][1] -= f_gold_stolen

    if f_destination_info[f_target_city][0] <= 0:
        print(f"{f_target_city} has been wiped off the map!")
        f_destination_info.pop(f_target_city)
    elif f_destination_info[target_city][1] <= 0:
        print(f"{f_target_city} has been wiped off the map!")
        f_destination_info.pop(f_target_city)


    return f_destination_info


def prosper_case(f_destination_info: dict, f_target_city: str, f_gold_added: int):
    if f_gold_added >= 0:
        f_destination_info[f_target_city][1] += f_gold_added
        total_gold = f_destination_info[f_target_city][1]
        print(f"{f_gold_added} gold added to the city treasury. {f_target_city} now has {total_gold} gold.")
        return f_destination_info

    print(f"Gold added cannot be a negative number!")
    return f_destination_info


command = input()
destination_info = {}

while not command == "Sail":
    command_args = command.split("||")
    city = command_args[0]
    population = int(command_args[1])
    gold = int(command_args[2])

    if city not in destination_info:
        destination_info[city] = [population, gold]
    else:
        destination_info[city][0] += population
        destination_info[city][1] += gold

    command = input()


events = input()

while not events == "End":
    event_args = events.split("=>")
    order = event_args[0]


    if order == "Plunder":
        target_city = event_args[1]
        population_killed = int(event_args[2])
        gold_stolen = int(event_args[3])
        plunder_case(destination_info, target_city, population_killed, gold_stolen)

    elif order == "Prosper":
        target_city = event_args[1]
        gold_added = int(event_args[2])
        prosper_case(destination_info, target_city, gold_added)

    events = input()

if len(destination_info) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(destination_info)} wealthy settlements to go to:")


for info in destination_info.items():
    print(f"{info[0]} -> Population: {info[1][0]} citizens, Gold: {info[1][1]} kg")