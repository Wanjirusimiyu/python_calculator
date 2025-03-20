num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    result = num_1 + num_2
    print(result)
elif operation == '-':
    result = num_1 - num_2
    print(result)
elif operation == '*':
    result = num_1 * num_2
    print(result)
elif operation == '/':
    result = num_1 / num_2
    print(result)
else:
    print("Invalid operation")