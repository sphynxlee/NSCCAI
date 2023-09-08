#!/usr/bin/env python3
def fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number
        sequence.append(next_number)  # Add the next number to the sequence
    return sequence

# Test the function
n_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fib_sequence = fibonacci(n_terms)
print(fib_sequence)
