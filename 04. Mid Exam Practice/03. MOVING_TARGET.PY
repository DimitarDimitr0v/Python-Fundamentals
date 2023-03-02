def shoot(position, power, collection):
    if index_validation(index, targets):
        collection[position] -= power
        if collection[position] <= 0:
            collection.remove(collection[position])

    return collection


def add(position, value, collection):
    if index_validation(index, targets):
        collection.insert(position, value)
        return collection
    else:
        print(f"Invalid placement!")
        return collection


def strike(position, radius, collection):
    left_side = position - radius
    right_side = position + radius
    if index_validation(right_side, collection) and \
            index_validation(left_side, collection) and \
            index_validation(position, collection):

        for remove in range(left_side, right_side + 1):
            collection.pop(left_side)
        return collection
    else:
        print(f"Strike missed!")
        return collection


def index_validation(position: int, collection: list):
    if 0 <= position < len(collection):
        return True

    return False


targets = [int(el) for el in input().split(" ")]
command = input()

while not command == "End":
    split = command.split(" ")

    order = split[0]
    index = int(split[1])
    value_radius = int(split[2])

    if order == "Shoot":
        targets = shoot(index, value_radius, targets)
    elif order == "Add":
        targets = add(index, value_radius, targets)
    elif order == "Strike":
        targets = strike(index, value_radius, targets)

    command = input()

targets = [str(x) for x in targets]
print("|".join(targets))
