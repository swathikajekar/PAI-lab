def generate_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j} = {i * j}")
        print()

range_limit = int(input("Enter the range for the multiplication table: "))

generate_multiplication_table(range_limit)
