def adding(collection: list, card: str):
    if card not in collection:
        collection.append(card)
        print(f"Card successfully added")
        return collection
    else:
        print(f"Card is already in the deck")
        return collection


def removing_by_card(collection: list, card: str):
    if card not in collection:
        print(f"Card not found")
        return collection
    else:
        collection.remove(card)
        print(f"Card successfully removed")
        return collection


def removing_by_index(collection: list, index: int):
    if 0 <= index <= len(collection):
        collection.pop(index)
        print(f"Card successfully removed")
        return collection
    else:
        print(f"Index out of range")
        return collection


def inserting(collection: list, index: int, card: str):
    if 0 <= index <= len(collection):
        if card in collection:
            print(f"Card is already added")
            return collection
        else:
            collection.insert(index, card)
            print(f"Card successfully added")
            return collection
    else:
        print(f"Index out of range")
        return collection


card_list = input().split(", ")
n = int(input())


for rotations in range(n):
    command = input().split(", ")
    order = command[0]

    if order == "Add":
        card_name = command[1]
        card_list = adding(card_list, card_name)

    elif order == "Remove":
        card_name = command[1]
        card_list = removing_by_card(card_list, card_name)

    elif order == "Remove At":
        current_index = int(command[1])
        card_list = removing_by_index(card_list, current_index)

    elif order == "Insert":
        current_index = int(command[1])
        card_name = command[2]
        card_list = inserting(card_list, current_index, card_name)

print(", ".join(card_list))