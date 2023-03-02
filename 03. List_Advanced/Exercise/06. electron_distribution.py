electrons = int(input())
filled_shells = []
for shell in range(1, 101):
    shell_fits = 2 * (shell ** 2)
    if electrons >= shell_fits:
        filled_shells.append(shell_fits)
        electrons -= shell_fits
    else:
        if not electrons == 0:
            filled_shells.append(electrons)
        break

print(filled_shells)
