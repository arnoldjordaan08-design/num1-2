num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = float(num1) + float(num2)
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == "-":
    result = float(num1) - float(num2)
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == "*":
    result = float(num1) * float(num2)
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == "/":
    result = float(num1) / float(num2)
    print(f"The result of {num1} / {num2} is: {result}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")