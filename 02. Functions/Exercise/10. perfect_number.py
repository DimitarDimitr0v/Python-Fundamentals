def perfect_number(number: int):
    total = 0
    for el in range(1, number):
        if number % el == 0:
            total += el

    if total == number:
        return print(f"We have a perfect number!")

    return print(f"It's not so perfect.")


num = int(input())

perfect_number(num)



