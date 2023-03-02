def factorial(num_1, num_2):
    factorial_1 = 1
    for x in range(1, num_1 + 1):
        factorial_1 *= x

    factorial_2 = 1
    for x in range(1, num_2 + 1):
        factorial_2 *= x

    return factorial_1 / factorial_2


n1 = int(input())
n2 = int(input())

print(f"{factorial(n1, n2):.2f}")
