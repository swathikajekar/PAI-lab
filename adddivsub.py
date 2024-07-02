def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations and print results
print(f"The result of addition is: {add(num1, num2)}")
print(f"The result of subtraction is: {subtract(num1, num2)}")
print(f"The result of division is: {divide(num1, num2)}")
