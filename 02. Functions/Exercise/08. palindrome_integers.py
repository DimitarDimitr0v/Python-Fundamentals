def only_palindromes(sequence: list):
    for el in sequence:
        if el == el[::-1]:
            print('True')
        else:
            print('False')


numbers = input().split(", ")

only_palindromes(numbers)
