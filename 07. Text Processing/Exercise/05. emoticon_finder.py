text = input()
for i in range(len(text)):
    if text[i] == ':':
        print(f":{text[i + 1]}")

# [print(f":{text[i + 1]}") for i in range(len(text)) if text[i] == ':']