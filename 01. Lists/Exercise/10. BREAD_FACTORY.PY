events = input().split("|")

initial_energy = 100
initial_coins = 100
bankrupted = False

for i in range(len(events)):
    split = events[i].split("-")

    event_name = split[0]
    value = int(split[1])

    # rest
    if event_name == "rest":
        gained_energy = value
        if gained_energy + initial_energy > 100:
            gained_energy = 100 - initial_energy

        initial_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    # order
    elif event_name == "order":
        coins_earned = value
        if initial_energy - 30 >= 0:
            initial_energy -= 30
            initial_coins += coins_earned
            print(f"You earned {coins_earned} coins.")
        else:
            print(f"You had to rest!")
            initial_energy += 50
            continue

    # ingredient
    else:
        coins_spent = value
        if initial_coins - coins_spent > 0:
            initial_coins -= coins_spent
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            bankrupted = True
            break

if not bankrupted:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
