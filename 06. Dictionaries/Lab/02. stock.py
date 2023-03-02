elements = input().split(" ")
search_for_elements = input().split(" ")

for current_meal in search_for_elements:
    for i in range(0, len(elements), 2):
        key = elements[i]
        value = int(elements[i + 1])
        if key == current_meal:
            print(f"We have {value} of {key} left")
            break
    else:
        print(f"Sorry, we don't have {current_meal}")