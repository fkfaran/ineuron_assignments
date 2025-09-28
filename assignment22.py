# Recursive Python Calculation Programs

# 1. Sum of first N natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

# 2. Sum of first N odd natural numbers
def sum_odd(n):
    if n == 0:
        return 0
    return (2*n - 1) + sum_odd(n - 1)

# 3. Sum of first N even natural numbers
def sum_even(n):
    if n == 0:
        return 0
    return (2*n) + sum_even(n - 1)

# 4. Sum of squares of first N natural numbers
def sum_squares(n):
    if n == 0:
        return 0
    return n*n + sum_squares(n - 1)

# 5. Sum of cubes of first N natural numbers
def sum_cubes(n):
    if n == 0:
        return 0
    return n**3 + sum_cubes(n - 1)

# 6. Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 7. Sum of digits of a number
def sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)

# 8. Print binary of a decimal number
def print_binary(num):
    if num > 1:
        print_binary(num // 2)
    print(num % 2, end="")

# 9. Print octal of a decimal number
def print_octal(num):
    if num > 7:
        print_octal(num // 8)
    print(num % 8, end="")

# 10. Find Nth term of Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    N = 5
    print("1. Sum of first N natural numbers:", sum_natural(N))
    print("2. Sum of first N odd numbers:", sum_odd(N))
    print("3. Sum of first N even numbers:", sum_even(N))
    print("4. Sum of squares:", sum_squares(N))
    print("5. Sum of cubes:", sum_cubes(N))
    print("6. Factorial of 5:", factorial(5))
    print("7. Sum of digits (12345):", sum_digits(12345))
    print("8. Binary of 10:", end=" ")
    print_binary(10)
    print("\n9. Octal of 25:", end=" ")
    print_octal(25)
    print("\n10. 7th Fibonacci term:", fibonacci(7))
