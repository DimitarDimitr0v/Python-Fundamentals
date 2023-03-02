import re
n = int(input())
pattern = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1'

for _ in range(n):
    text = input()
    match = re.match(pattern, text)
    if match is None:
        print('Try another password!')
    else:
        one = match.group(2)
        two = match.group(3)
        three = match.group(4)
        four = match.group(5)
        print('Password:', end=' ')
        print(one + two + three + four)
