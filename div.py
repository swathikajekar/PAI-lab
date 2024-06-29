def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    while True:
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '4':
            print("Exiting the program.")
            break
        
        if choice in ['1', '2', '3']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == '3':
                result = divide(num1, num2)
                if result == "Error: Division by zero is not allowed.":
                    print(result)
                else:
                    print(f"The result of division is: {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
