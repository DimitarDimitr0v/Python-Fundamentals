def swap(i1: int, i2: int, collection: list):
    temp = collection[i1]
    collection[i1] = collection[i2]
    collection[i2] = temp

    return collection


def multiply(i1: int, i2: int, collection: list):
    multiplied = collection[i1] * collection[i2]
    collection[i1] = multiplied

    return collection


def decrease(collection: list):
    for i in range(len(collection)):
        collection[i] -= 1

    return collection


numbers = [int(x) for x in input().split(" ")]

command = input()
while not command == "end":
    spit_args = command.split(" ")
    task = spit_args[0]

    if task == "swap":
        index_1 = int(spit_args[1])
        index_2 = int(spit_args[2])
        numbers = swap(index_1, index_2, numbers)
    elif task == "multiply":
        index_1 = int(spit_args[1])
        index_2 = int(spit_args[2])
        numbers = multiply(index_1, index_2, numbers)
    elif task == "decrease":
        numbers = decrease(numbers)

    command = input()


print(", ".join([str(x) for x in numbers]))

