def calculations(operation, num_1, num_2):
    if operation == "multiply":
        return num_1 * num_2
    elif operation == "divide":
        return num_1 // num_2
    elif operation == "add":
        return num_1 + num_2
    elif operation == "subtract":
        return num_1 - num_2


current_operation = input()
n1 = int(input())
n2 = int(input())

print(calculations(current_operation, n1, n2))