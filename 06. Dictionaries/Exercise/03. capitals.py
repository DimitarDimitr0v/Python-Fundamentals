countries = input().split(", ")
capitals = input().split(", ")

for el in range(len(countries)):
    print(" ".join(f"{key} -> {value}"
    for key, value in dict(zip([countries[el]], [capitals[el]])).items()))