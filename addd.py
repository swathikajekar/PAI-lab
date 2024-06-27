def add_two_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def main():
    # Read input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Add the two numbers
    result = add_two_numbers(num1, num2)
    
    # Print the result
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
