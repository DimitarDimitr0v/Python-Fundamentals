n = int(input())
word = input()
total = []
special = []
for next_lines in range(1, n + 1):
    strings = input()
    total.append(strings)
    last = [strings]
    if word in " ".join(last):
        special.append(strings)
print(total)
print(special)