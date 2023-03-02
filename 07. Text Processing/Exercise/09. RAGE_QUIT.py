text = input()

temp_text = ""
result = ""
number = ""
count_of_symbols = 0

for i in range(len(text)):
    if not text[i].isnumeric():
        temp_text += text[i].upper()

        if text[i].upper() in result:
            pass
        else:
            count_of_symbols += 1
    else:
        x = i
        while text[x].isnumeric():
            number += text[x]
            if 0 <= x + 1 < len(text):
                x += 1
            else:
                break


        result += temp_text * int(number)
        number = ""

        temp_text = ""
print(f"Unique symbols used: {count_of_symbols}")
print(result)
