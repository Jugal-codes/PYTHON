'''
Recursion is a programming technique where a function calls itself to solve a problem.

Instead of solving the whole problem at once, recursion 
    Breaks the problem into smaller sub-problems,
    Solves the smallest problem first,
    Builds the solution step by step while returning back

Every recursive solution has two mandatory parts:
    1. Base Case (Stopping Condition) :
        The condition where the function stops calling itself
        Prevents infinite recursion

    2. Recursive Case :
        The part where the function calls itself
        Moves the problem closer to the base case
'''



# Problem : Find factorial of a number
def factorial(n):
    if n == 1 or n == 0:        # Base case
        return 1
    return n * factorial(n - 1)   # Recursive call

print(factorial(3))



# Problem : Sum of Numbers (1 to n) :
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(4))



# Problem : Fibonacci Tree (Very Important) :
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(4))

