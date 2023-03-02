prices_without_tax = input()

list_of_all_prices = []
total_money = 0

while not prices_without_tax == "special":
    if prices_without_tax == "regular":
        break
    if float(prices_without_tax) > 0:
        list_of_all_prices.append(float(prices_without_tax))
        total_money += float(prices_without_tax)
    else:
        print(f"Invalid price!")

    prices_without_tax = input()

taxes = total_money * (20 / 100)
price = total_money
total_money = total_money + taxes

if prices_without_tax == "special":
    discount = total_money * (10 / 100)
    total_money -= discount


if total_money <= 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_money:.2f}$")