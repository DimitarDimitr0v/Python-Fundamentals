def index_validation(f_stops: str, f_index: int):
    if f_index in range(len(f_stops)):
        return True

    return False


def add_stop_case(f_stops: str, f_index: int, f_string: str):
    if index_validation(f_stops, f_index):
        return f_stops[:f_index] + f_string + f_stops[f_index:]

    return f_stops


def remove_case(f_stops: str, f_start_index: int, f_end_index: int):
    if index_validation(f_stops, start_index) and index_validation(f_stops, end_index):
        return f_stops[:f_start_index] + f_stops[f_end_index + 1:]

    return f_stops


def switch_case(f_stops: str, f_old_string: str, f_new_string: str):
    return f_stops.replace(old_string, new_string)



stops = input()
command = input()

while not command == "Travel":
    command_args = command.split(":")
    order = command_args[0]

    if order == "Add Stop":
        index = int(command_args[1])
        string = command_args[2]
        stops = add_stop_case(stops, index, string)

    elif order == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        stops = remove_case(stops, start_index, end_index)

    elif order == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]
        stops = switch_case(stops, old_string, new_string)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")