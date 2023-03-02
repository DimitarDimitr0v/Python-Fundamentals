first_list = input().split(", ")
second_list = input().split(", ")
new = []

for each_word in first_list:
    for ew in second_list:
        if each_word in ew:
            if each_word not in new:
                new.append(each_word)
print(new)
