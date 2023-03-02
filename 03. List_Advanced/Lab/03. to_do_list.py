result = ['0'] * 10

while True:
    command = input()
    if command == "End":
        break
    split = command.split("-")

    position = int(split[0]) - 1
    task = split[1]
    result.pop(position)
    result.insert(position, task)

print([el for el in result if '0' not in el])
