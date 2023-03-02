numbers = [int(x) for x in input().split(" ")]
total_value = 0
count = 0
greater_numbers = []
last = []
mark = True

for el in numbers:
    total_value += el
    count += 1
average = total_value / count

for x in numbers:
    if x > average:
        greater_numbers.append(x)

if len(greater_numbers) > 5:
    while mark:
        current_max = max(greater_numbers)
        if len(last) < 5:
            last.append(current_max)
            greater_numbers.remove(current_max)
        else:
            mark = False
else:
    last = greater_numbers

if len(last) == 0:
    print(f"No")

last.sort(reverse=True)
print(" ".join([str(x) for x in last]))