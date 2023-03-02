numbers = [int(el) for el in input().split(" ")]


def min_max_sum(n):
    print(f"The minimum number is {min(n)}")
    print(f"The maximum number is {max(n)}")
    print(f"The sum number is: {sum(n)}")


min_max_sum(numbers)