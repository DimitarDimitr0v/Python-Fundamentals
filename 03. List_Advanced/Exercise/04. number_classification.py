x = [int(x) for x in input().split(", ")]

positives = (", ".join([str(el) for el in x if el >= 0]))
negatives = (", ".join([str(el) for el in x if el < 0]))
even = (", ".join([str(el) for el in x if el % 2 == 0]))
odd = (", ".join([str(el) for el in x if not el % 2 == 0]))

print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {even}")
print(f"Odd: {odd}")
