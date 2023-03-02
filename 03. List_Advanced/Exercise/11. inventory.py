def collect(item: str, collection: list):
    if not exist_validation(item, collection):
        collection.append(item)

        return collection
    else:
        return collection


def drop(item: str, collection: list):
    if exist_validation(item, collection):
        collection.remove(item)

        return collection
    else:
        return collection


def combine_items(new_item: str, old_item: str, collection: list):
    if exist_validation(old_item, collection):
        for i in range(len(collection)):
            if collection[i] == old_item:
                collection.insert(i + 1, new_item)
                return collection
    else:
        return collection


def renew(item: str, collection: list):
    if exist_validation(item, collection):
        collection.remove(item)
        collection.append(item)

        return collection
    else:
        return collection


def exist_validation(item: str, collection: list):
    for el in collection:
        if item == el:
            # in the list
            return True
        # not in the list
    return False


items = input().split(", ")
command = input()

while not command == "Craft!":
    cmd_args = command.split(" - ")
    order = cmd_args[0]
    current_item = cmd_args[1]

    if order == "Collect":
        items = collect(current_item, items)
    elif order == "Drop":
        items = drop(current_item, items)
    elif order == "Combine Items":
        combine_items_args = cmd_args[1].split(":")
        cmd_old_item = combine_items_args[0]
        cmd_new_item = combine_items_args[1]
        items = combine_items(cmd_new_item, cmd_old_item, items)
    elif order == "Renew":
        items = renew(current_item, items)

    command = input()

print(", ".join(items))