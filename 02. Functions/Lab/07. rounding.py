import math


def rounding(nums):
    new = []
    for el in nums:
        new.append(round(el))
    return new


numbers = [float(x) for x in input().split(" ")]

print(rounding(numbers))
