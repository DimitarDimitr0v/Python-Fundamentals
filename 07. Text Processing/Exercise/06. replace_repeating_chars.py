txt = input()
last_el = ""

for current_el in txt:
    if not current_el == last_el:
        print(current_el, end="")
        last_el = current_el