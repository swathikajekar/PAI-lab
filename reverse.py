def reverse_string(s):
    return s[::-1]

user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(user_input)

print(f"The reversed string is: {reversed_string}")
