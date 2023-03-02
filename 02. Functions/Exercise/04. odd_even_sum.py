def even_odd(number: str):
    even = 0
    odd = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)

    return print(f"Odd sum = {odd}, Even sum = {even}")

num = input()

even_odd(num)