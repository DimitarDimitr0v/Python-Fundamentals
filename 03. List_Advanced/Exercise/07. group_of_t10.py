sequence = input().split(", ")
temp = []
last_max = 0
current_max = 10
x = True
count = len(sequence)
for_remove = []

while x:
    if count == 0:
        x = False
        break
    for elements in sequence:
        if last_max <= int(elements) <= current_max:
            temp.append(elements)
            for_remove.append(elements)
            count -= 1
    for e in for_remove:
        if e in sequence:
            sequence.remove(e)
    print(f"Group of {current_max}'s: {[int(x) for x in temp]}")
    last_max += 10
    current_max += 10
    temp = []