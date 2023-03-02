sequence = input()
for el in sequence.split(" "):
    print(el * len(el), end="")