def biggest_index_value(collection: list, biggest_num: int, index_with_highest_value_: int):
    for biggest_ in range(len(population)):
        if population[biggest_] > biggest_num:
            index_with_highest_value_ = biggest_
            biggest_num = population[biggest_]
            value = population[index_with_highest_value_]

    return index_with_highest_value_


import sys
population = [int(el) for el in input().split(", ")]
minimum_wealth = int(input())
biggest = 0
braked = False
index_with_highest_value = 0


for i in range(len(population)):
    largest = -sys.maxsize
    index_with_highest_value = biggest_index_value(population, largest, index_with_highest_value)

    if population[i] < minimum_wealth:
        if population[index_with_highest_value] - (minimum_wealth - population[i]) >= minimum_wealth:
            population[index_with_highest_value] -= (minimum_wealth - population[i])
            population[i] += (minimum_wealth - population[i])
        else:
            continue

braked = [x for x in population if x < minimum_wealth]

if braked:
    print(f"No equal distribution possible")
else:
    print(population)
