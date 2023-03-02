route = input().split("||")
fuel = int(input())
ammunition = int(input())


for el in route:
    split = el.split(" ")
    order = split[0]


    if not order == "Titan":
        value = int(split[1])

        if order == "Travel":
            if fuel - value >= 0:
                print(f"The spaceship travelled {value} light-years.")
                fuel -= value
            else:
                print(f"Mission failed.")
                break


        elif order == "Enemy":
            if ammunition - value >= 0:
                print(f"An enemy with {value} armour is defeated.")
                ammunition -= value
            else:
                run_consumed_fuel = value * 2
                if fuel - run_consumed_fuel >= 0:
                    print(f"An enemy with {value} armour is outmaneuvered.")
                    fuel -= run_consumed_fuel
                else:
                    print(f"Mission failed.")
                    break
        elif order == "Repair":
            fuel_added = value
            ammunition_added = value * 2
            fuel += fuel_added
            ammunition += ammunition_added
            print(f"Ammunitions added: {ammunition_added}.")
            print(f"Fuel added: {fuel_added}.")

    else:
        print(f"You have reached Titan, all passengers are safe.")
        break