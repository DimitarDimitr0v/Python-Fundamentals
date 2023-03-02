z = ([x for x in input().split(" ") if len(x) % 2 == 0])
for i in range(len(z)):
    print("".join([str(x) for x in z[i]]))
