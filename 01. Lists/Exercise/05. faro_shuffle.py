cards = input().split()
shuffles = int(input())

# split the deck in half
half_size = (len(cards)) // 2

# a loop that shuffles the deck requested times
for rotations in range(shuffles):

    # the values split into two parts
    first_half = cards[:half_size]
    second_half = cards[half_size:]

    # the result of shuffling
    faro_shuffle = []

    # for each index adding the value of it for both parts
    for i in range(len(first_half)):
        faro_shuffle.append(first_half[i])
        faro_shuffle.append((second_half[i]))

    # replacing the value of cards with faro_shuffle to continue the rotations
    cards = faro_shuffle

print(cards)

##################################################################################

 # My Solution

cards = input().split()
shuffles = int(input())
first_half = []
second_half = []
new = []


cards_size = (len(cards)) // 2

for rotation in range(1, shuffles + 1):
    first_half.clear()
    second_half.clear()

    for index in range(len(cards)):
        if cards_size > index:
            first_half.append(cards[index])
            index += 1
        else:
            second_half.append(cards[index])

    new.clear()
    for i in range(len(first_half)):
        new.append(first_half[i])
        new.append(second_half[i])
        cards = new

print(cards)




