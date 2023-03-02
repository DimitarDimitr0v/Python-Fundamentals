gifts = input().split()
command = input()

while command != "No Money":
    split_command = command.split(" ")
    command_itself = split_command[0]
    gift_itself = split_command[1]
    gifts_length = len(gifts)

    if "OutOfStock" in command:
        for i in range(len(gifts)):
            if gifts[i] in gift_itself:
                gifts[i] = "None"

    elif "JustInCase" in command:
        for index in range(len(gifts) + 1):
            if index == gifts_length:
                gifts[index - 1] = gift_itself

    else:
        split_command = command.split(" ")
        command_required = split_command[0]
        gift_required = split_command[1]
        index_required = split_command[2]
        for required_index in range(len(gifts)):
            if required_index == int(index_required):
                gifts[required_index] = gift_required

    command = input()

gifts_without_None = []

for current_gift in gifts:
    if current_gift != "None":
        gifts_without_None.append(current_gift)

print(" ".join([str(x) for x in gifts_without_None]))