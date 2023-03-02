def increase_reduce(last_problem: int, collection: list, shot: list):
    for elements in range(len(targets)):
        if targets[elements] not in shot_values:
            if targets[elements] > last_target:
                targets[elements] -= last_target
            else:
                targets[elements] += last_target

    return collection


targets = [int(el) for el in input().split(" ")]
index = input()
shot_indexes = []
shot_values = []
count = 0

while not index == "End":
    for i in range(len(targets)):
        if i == int(index):
            last_target = targets[i]
            if i not in shot_indexes:
                targets[i] = -1
                count += 1
                shot_indexes.append(i)
                shot_values.append(targets[i])

            targets = increase_reduce(last_target, targets, shot_values)

    index = input()

targets = [str(el) for el in targets]

print(f"Shot targets: {count} ->", end=" ")
print(" ".join(targets))
