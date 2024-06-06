def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

fib_sequence = fibonacci(num_terms)

print(f"The first {num_terms} terms of the Fibonacci sequence are: {fib_sequence}")
