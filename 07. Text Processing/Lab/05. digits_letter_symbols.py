current_string = input()

alphanumeric = ''
digits = ''
symbols = ''

for el in current_string:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        alphanumeric += el
    else:
        symbols += el

print(digits)
print(alphanumeric)
print(symbols)