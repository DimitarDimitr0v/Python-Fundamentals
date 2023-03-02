fires_and_cells = input().split("#")
water_available = int(input())
total_fire = 0
total_effort = 0
print("Cells:")

for _ in fires_and_cells:
    split = _.split(" =")

    burn_level = split[0]
    cell_number = int(split[1])

    if not water_available - cell_number >= 0:
        continue
    else:
        if burn_level == "High":
            if 81 <= cell_number <= 125:
                total_fire += cell_number
                water_available -= cell_number
                print(f"- {cell_number}")
            else:
                continue
        elif burn_level == "Medium":
            if 51 <= cell_number <= 80:
                total_fire += cell_number
                water_available -= cell_number
                print(f"- {cell_number}")
            else:
                continue
        elif burn_level == "Low":
            if 1 <= cell_number <= 50:
                total_fire += cell_number
                water_available -= cell_number
                print(f"- {cell_number}")
            else:
                continue

        effort = cell_number * (25 / 100)
        total_effort += effort

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
