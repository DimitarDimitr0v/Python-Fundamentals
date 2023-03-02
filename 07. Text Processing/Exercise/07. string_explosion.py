text = input()

result_text = ''

i = 0
bomb_power = 0

while i < len(text):

    curr_ch = text[i]
    if curr_ch == ">":

        result_text += ">"
        bomb_power += int(text[i + 1])

    else:
        if bomb_power > 0:
            bomb_power -= 1

        else:
            result_text += curr_ch

    i += 1
print(result_text)