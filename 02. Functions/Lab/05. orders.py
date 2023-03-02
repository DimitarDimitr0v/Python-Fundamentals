def orders(stock, amount):
    if stock == "coffee":
        print(f"{1.5 * amount:.2f}")
    elif stock == "water":
        print(f"{1 * amount:.2f}")
    elif stock == "coke":
        print(f"{1.4 * amount:.2f}")
    elif stock == "snacks":
        print(f"{2 * amount:.2f}")


stock_ = input()
amount_ = int(input())

orders(stock_, amount_)
