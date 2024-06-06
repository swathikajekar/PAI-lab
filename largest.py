def find_largest(numbers):
    return max(numbers)

user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(float, user_input.split()))
largest_number = find_largest(numbers)

print(f"The largest number is: {largest_number}")
