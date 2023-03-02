def asckii_between_characters(char_1: str, char_2: str):
    for elements in range(ord(char_1) + 1, ord(char_2)):
        print(chr(elements), end=" ")


first = input()
last = input()

asckii_between_characters(first, last)
