import math


def coordinates(x1, y1, x2, y2):
    result = math.floor(abs(x1)) + math.floor(abs(y1))
    result_2 = math.floor(abs(x2)) + math.floor(abs(y2))
    if result < result_2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

coordinates(x_1, y_1, x_2, y_2)
