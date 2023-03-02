def data(kind, value):
    if kind == 'int':
        return print(int(value) * 2)
    elif kind == 'real':
        return print(f"{float(value) * 1.5:.2f}")
    elif kind == "string":
        return print(f"${value}$")


type_var = input()
amount = input()

data(type_var, amount)
