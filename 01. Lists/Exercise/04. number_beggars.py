numbers = [int(num) for num in input().split(", ")]
beggars = int(input())
count = 0
beggars_list = [0] * beggars

for current_number in numbers:
    beggars_list[count] += current_number
    count += 1
    if count >= beggars:
        count = 0
print(beggars_list)