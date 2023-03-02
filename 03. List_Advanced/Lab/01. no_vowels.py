vowels = ["a", "o", "e", "u", "i"]
print("".join([str(el) for el in input() if not el.lower() in vowels]))