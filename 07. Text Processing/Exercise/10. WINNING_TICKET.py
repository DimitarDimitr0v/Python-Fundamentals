import string
tickets = input().split()
x = "".join(tickets)
tickets = x.split(",")
symbols = ["@", "#", "$", "^"]

for el in tickets:
    if "@" or "#" or "$" or "^" in el:

        if len(el) != 20:
            print(f"invalid ticket")
            continue

        else:
            right_half = el[:10]
            left_half = el[10:]

            for index in range(4):

                if symbols[index] * 10 in right_half and symbols[index] * 10 in left_half:
                    print(f'ticket "{el}" - {10}{symbols[index]} Jackpot!')
                    break

                elif symbols[index] * 9 in right_half and symbols[index] * 9 in left_half:
                    print(f'ticket "{el}" - {9}{symbols[index]}')
                    break

                elif symbols[index] * 8 in right_half and symbols[index] * 8 in left_half:
                    print(f'ticket "{el}" - {8}{symbols[index]}')
                    break

                elif symbols[index] * 7 in right_half and symbols[index] * 7 in left_half:
                    print(f'ticket "{el}" - {7}{symbols[index]}')
                    break

                elif symbols[index] * 6 in right_half and symbols[index] * 6 in left_half:
                    print(f'ticket "{el}" - {6}{symbols[index]}')
                    break

            else:
                print(f'ticket "{el}" - no match')
                continue




