rooms = int(input())
chairs_left = 0
chairs_are_enough = True
for room in range(1, rooms + 1):

    current_room = input().split(" ")
    chairs_available = 0

    chairs = current_room[0]
    for i in range(len(chairs)):
        chairs_available += 1

    visitors = int(current_room[1])

    if chairs_available >= visitors:
        chairs_left += (chairs_available - visitors)
    else:
        needed_chairs = visitors - chairs_available
        chairs_are_enough = False
        print(f"{needed_chairs} more chairs needed in room {room}")

if chairs_are_enough:
    print(f"Game On, {chairs_left} free chairs left")
