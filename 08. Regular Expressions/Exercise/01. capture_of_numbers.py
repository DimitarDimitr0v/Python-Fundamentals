import re

pattern = r"\d+"
text = input()


while True:
    if not text == "":
        result = re.findall(pattern, text)
        if len(result) == 0:
            pass
        else:
            print(" ".join(result), end=" ")
        text = input()
    else:
        break


