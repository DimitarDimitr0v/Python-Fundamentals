import math
biscuits_worker_produce_daily = int(input())
workers = int(input())
competing_factory = int(input())

total_biscuits = 0



for working_days in range(1, 30 + 1):
    total_biscuit_per_worker = biscuits_worker_produce_daily * workers

    if working_days % 3 == 0:
        total_biscuit_per_worker *= (75 / 100)
        total_biscuits += math.floor(total_biscuit_per_worker)
    else:
        total_biscuits += total_biscuit_per_worker

print(f"You have produced {math.floor(total_biscuits)} biscuits for the past month.")

if total_biscuits > competing_factory:
    percent_diff = (total_biscuits - competing_factory) / competing_factory * 100
    print(f"You produce {percent_diff:.2f} percent more biscuits.")
elif total_biscuits < competing_factory:
    percent_diff = (competing_factory - total_biscuits) / competing_factory * 100
    print(f"You produce {percent_diff:.2f} percent less biscuits.")