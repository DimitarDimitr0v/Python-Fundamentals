current_version = input().split(".")

n1 = int(current_version[0])
n2 = int(current_version[1])
n3 = int(current_version[2])


def last(n_1, n_2, n_3):
    already_added = False
    new_version = [0] * 3

    if n_3 == 9:
        pass
    else:
        if not already_added:
            already_added = True
            new_version[2] += (n_3 + 1)

    if not already_added:
        if n_2 == 9:
            pass
        else:
            already_added = True
            new_version[1] += (n_2 + 1)
    else:
        new_version[1] = current_version[1]

    if not already_added:
        if n_1 == 9:
            pass
        else:
            already_added = True
            new_version[0] += (n_1 + 1)
    else:
        new_version[0] = current_version[0]

    return print(".".join([str(x) for x in new_version]))


last(n1, n2, n3)

# METHOD 2 IS TO CONCATENATE ALL VALUES AS INTEGERS AND WITHOUT DOTS TEHN
# ADD 1 TO THEM AND PRINT THEM WITH JOINED "."
