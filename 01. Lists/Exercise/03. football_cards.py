kicked = input().split()
team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
a = 11
b = 11
for player in kicked:
    if a < 7 or b < 7:
        print(f"Team A - {a}; Team B - {b}")
        print("Game was terminated")
        break
    if player in team_a:
        team_a.remove(player)
        a -= 1
    elif player in team_b:
        team_b.remove(player)
        b -= 1
else:
    print(f"Team A - {a}; Team B - {b}")