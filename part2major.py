num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nCalculator Menu:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operator = input("\nChoose an operation (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"\nThe result of {num1} + {num2} is {result}")
elif operator == '-':
    result = num1 - num2
    print(f"\nThe result of {num1} - {num2} is {result}")
elif operator == '*':
    result = num1 * num2
    print(f"\nThe result of {num1} * {num2} is {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print(f"\nThe result of {num1} / {num2} is {result}")
else:
    print("Invalid operator. Please choose from +, -, *, /")
