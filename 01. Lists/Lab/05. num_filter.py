n = int(input())
total = []
positive = []
negative = []
even = []
odd = []
is_even = False
is_odd = False
is_positive = False
is_negative = False
for positions in range(1, n + 1):
    current_number = int(input())
    total.append(current_number)
type = input()
for element in total:
    if type == "even":
        if element % 2 == 0 or element == 0:
            even.append(element)
            is_even = True
    elif type == "odd":
        if not element % 2 == 0:
            odd.append(element)
            is_odd = True
    elif type == "negative":
        if element < 0:
            negative.append(element)
            is_negative = True
    elif type == "positive":
        if element >= 0:
            positive.append(element)
            is_positive = True
if is_even:
    print(even)
elif is_odd:
    print(odd)
elif is_positive:
    print(positive)
else:
    print(negative)