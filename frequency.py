def count_characters(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

user_input = input("Enter a string: ")

char_frequency = count_characters(user_input)

print("Character frequencies:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
