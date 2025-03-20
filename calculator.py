# Create a calculator that asks a uset to input two numbers and an operation and perform an operation on the number
# then print the result

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /): ")

#if-elif statement to perform the operations based on user inputs.
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