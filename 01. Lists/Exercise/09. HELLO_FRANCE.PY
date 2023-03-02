import math
items = input().split("|")
budget = float(input())
money_from_sales = 0
bought_items_prices = []
new_prices = []
profit = 0
total = 0

for i in range(len(items)):
    split = items[i].split("->")

    current_item = split[0]
    item_price = float(split[1])

    if current_item == "Clothes":
        if budget >= item_price:
            if item_price > 50.00:
                continue
            else:
                budget -= item_price
                bought_items_prices.append(item_price)

    elif current_item == "Shoes":
        if budget >= item_price:
            if item_price > 35.00:
                continue
            else:
                budget -= item_price
                bought_items_prices.append(item_price)

    elif current_item == "Accessories":
        if budget >= item_price:
            if item_price > 20.50:
                continue
            else:
                budget -= item_price
                bought_items_prices.append(item_price)

for current_price in bought_items_prices:
    new_price = current_price + (current_price * (40 / 100))
    total += new_price
    profit += (new_price - current_price)
    new_prices.append(new_price)



for e in new_prices:
    print(f"{e:.2f}",end=" ")
print()

if (total + budget) - 150 >= 0:
    print(f"Profit: {profit:.2f}")
    print(f"Hello, France!")
else:
    print(f"Profit: {profit:.2f}")
    print(f"Not enough money.")