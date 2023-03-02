def sum_numbers(num_1: int, num_2: int):
    total = num_1 + num_2

    return total


def subtract(sum_nums: int, num_3: int):
    total = sum_nums - num_3

    return total


def add_and_subtract(num_1: int, num_2: int, num_3: int):
    summed = sum_numbers(num_1, num_2)
    subtracted = subtract(summed, num_3)

    return subtracted


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))


