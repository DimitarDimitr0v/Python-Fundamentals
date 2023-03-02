def absolute_value(collection):
    new = []
    for el in collection:
        new.append(abs(el))

    return new


sequence = [float(x) for x in input().split(" ")]

print(absolute_value(sequence))
