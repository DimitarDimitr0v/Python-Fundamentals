number_wagons = int(input())
train = [0] * number_wagons
command = input()

while not command == "End":
    cmd = command.split(" ")
    order = cmd[0]

    if order == "add":
        index = int(cmd[1])
        train[-1] += index
    elif order == "insert":
        index = int(cmd[1])
        value = int(cmd[2])
        train[index] += value
    elif order == "leave":
        index = int(cmd[1])
        value = int(cmd[2])
        train[index] -= value
    command = input()

print(train)
