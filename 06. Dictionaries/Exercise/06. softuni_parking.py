cars_to_register = int(input())

registered_users = {}

for _ in range(1, cars_to_register + 1):
    command = input()
    split = command.split(" ")
    order = split[0]
    name = split[1]

    if order == "register":
        plate = split[2]
        if name not in registered_users:
            registered_users[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")

    elif order == "unregister":
        if name in registered_users:
            registered_users.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key, value in registered_users.items():
    print(f"{key} => {value}")