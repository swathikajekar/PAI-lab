def divide_numbers(num1, num2):
    """Divides num1 by num2 and returns the result."""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

def main():
    # Read input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Divide the two numbers
    result = divide_numbers(num1, num2)
    
    # Print the result
    print(f"The result of dividing {num1} by {num2} is: {result}")

if __name__ == "__main__":
    main()
