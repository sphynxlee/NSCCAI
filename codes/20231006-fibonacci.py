import time
import sys

# sys.set_int_max_str_digits(100000)
sys.setrecursionlimit(1000000)

"""
def fibonacci () :
    lists = [1, 1]
    total = int(input("Enter the number of Fibonacci terms to generate: "))

    for num in range(2, total):
        lists.append(lists[num-1] + lists[num-2])

    print(f'The Fibonacci sequence is {lists}')
# fibonacci()


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
# number = int(input("Enter the number of terms: "))
# print("Fibonacci sequence:", fib_recursive(number))
"""
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)
# number = int(input("Enter the number of terms: "))
r_start = time.time()
factorial_recursive(100000)
# print("Factorial:", factorial_recursive())
r_end = time.time()
print(f'Recursion time taken: {r_end - r_start}')


def factorial_function(num):
    # num = int(input("Enter the number of terms: "))
    res = 1
    for i in range(1, num + 1):
        # print(f'{res} * {i} = {res * i}')
        res = res * i
    return res
i_start = time.time()
factorial_function(100000)
# print(factorial_function())
i_end = time.time()
print(f'Iteration time taken: {i_end - i_start}')