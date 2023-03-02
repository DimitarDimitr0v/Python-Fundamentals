factor = int(input())
count = int(input())
numbers = []
for index in range(1, count + 1):
    x = index * factor
    numbers.append(x)
print(numbers)