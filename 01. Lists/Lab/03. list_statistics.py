n = int(input())
list_positive = []
list_negative = []
pos = 0
neg_sum = 0
for each in range(1, n + 1):
    current_number = int(input())
    if current_number > 0:
        pos += 1
        list_positive.append(current_number)
    elif current_number <= 0:
        neg_sum += current_number
        list_negative.append(current_number)

print(list_positive)
print(list_negative)
print(f"Count of positives: {pos}")
print(f"Sum of negatives: {neg_sum}")

