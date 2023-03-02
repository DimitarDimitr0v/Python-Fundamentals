def loading_bar_max_90(number: int):
    print(f"{number}%", end=" ")
    total_places = 10
    fill = number // 10
    print(f"[", end="")
    for el in range(1, fill + 1):
        print(f"%", end="")
        total_places -= 1
    for dots in range(1, total_places + 1):
        print(".", end="")
    print("]")

    print(f"Still loading...")


def loading_bar_max_100(number: int):
    print(f"100% Complete!")
    print("[%%%%%%%%%%]")


num = int(input())

if not num > 90:
    loading_bar_max_90(num)
elif num == 100:
    loading_bar_max_100(num)
