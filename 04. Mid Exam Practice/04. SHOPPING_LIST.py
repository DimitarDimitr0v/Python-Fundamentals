def exist_validation(current_item: str, collection: list):
    for el in collection:
        if el == item:
            return True

    return False


def urgent(current_item: str, collection: list):
    if not exist_validation(current_item, collection):
        collection.insert(0, current_item)

        return collection
    else:
        return collection


def unnecessary(current_item: str, collection: list):
    if exist_validation(current_item, collection):
        collection.remove(current_item)

        return collection
    else:
        return collection


def correct(old: str, new: str, collection: list):
    if exist_validation(old, collection):
        for i in range(len(collection)):
            if collection[i] == old:
                collection.insert(i, new_item)
                collection.remove(old)
                return collection
    else:
        return collection


def rearrange(current_item: str, collection: list):
    if exist_validation(current_item, collection):
        collection.remove(current_item)
        collection.append(current_item)

        return collection
    else:
        return collection


items = input().split("!")
command = input()

while not command == "Go Shopping!":
    cmd_args = command.split(" ")
    order = cmd_args[0]
    item = cmd_args[1]

    if order == "Urgent":
        items = urgent(item, items)
    elif order == "Unnecessary":
        items = unnecessary(item, items)
    elif order == "Correct":
        new_item = cmd_args[2]
        items = correct(item, new_item, items)
    elif order == "Rearrange":
        items = rearrange(item, items)

    command = input()

print(", ".join(items))
