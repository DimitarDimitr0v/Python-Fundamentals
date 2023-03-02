initial_energy = int(input())
distance_command = input()
out_of_energy = False
count_wins = 0

while distance_command != "End of battle":
    if initial_energy - int(distance_command) >= 0:
        count_wins += 1
        initial_energy -= int(distance_command)
    else:
        out_of_energy = True
        break

    if count_wins % 3 == 0:
        initial_energy += count_wins

    distance_command = input()

if out_of_energy:
    print(f"Not enough energy! Game ends with {count_wins} won battles and {initial_energy} energy")
elif not out_of_energy:
    print(f"Won battles: {count_wins}. Energy left: {initial_energy}")
