food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
pig_weight = float(input()) * 1000
not_enough = False
days = 30

for current_day in range(1, days + 1):

    if food_quantity - 300 <= 0:
        not_enough = True
        break
    else:
        food_quantity -= 300

    if current_day % 2 == 0:
        percent_value = (food_quantity / 20)
        if hay_quantity - percent_value <= 0:
            not_enough = True
            break
        else:
            hay_quantity -= percent_value

    if current_day % 3 == 0:
        one_third_value = pig_weight / 3
        if cover_quantity - one_third_value <= 0:
            not_enough = True
            break
        else:
            cover_quantity -= one_third_value

if not_enough:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity / 1000:.2f}," 
          f" Hay: {hay_quantity / 1000:.2f}, Cover: {cover_quantity / 1000:.2f}.")