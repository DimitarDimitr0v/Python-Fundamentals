targets = [int(x) for x in input().split()]
remove = []


def is_valid(position: int, collection: list):
    if 0 <= position < len(collection):
        return True
    return False


def shoot(position: int, value: int, collection: list):
    if is_valid(position, collection):
        collection[position] -= value

        if collection[position] <= 0:
            collection.pop(position)

    return collection


def add(position: int, value: int, collection: list):
    if is_valid(position, collection):
        collection.insert(index, value)
    else:
        print(f"Invalid placement!")

    return collection


def strike(position: int, radius: int, collection: list):
    left_side = position - radius
    right_side = position + radius

    if is_valid(left_side, collection) and \
            is_valid(right_side, collection) and \
            is_valid(position, collection):

        for i in range(left_side, right_side + 1):
            collection.pop(left_side)
    else:
        print(f"Strike missed!")

    return collection


not_end = True
result_list = []
while not_end:
    order = input().split(" ")
    if order[0] == "End":
        not_end = False
        break
    else:
        command = order[0]
        index = int(order[1])
        value_radius = int(order[2])

        if command == "Shoot":
            result_list = shoot(index, value_radius, targets)
        elif command == "Add":
            result_list = add(index, value_radius, targets)
        elif command == "Strike":
            result_list = strike(index, value_radius, targets)

print("|".join(str(x) for x in result_list))
