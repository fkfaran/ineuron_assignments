# Recursive Python Programs

# 1. Print first N natural numbers
def print_natural(n):
    if n > 0:
        print_natural(n - 1)
        print(n, end=" ")

# 2. Print first N natural numbers in reverse
def print_natural_reverse(n):
    if n > 0:
        print(n, end=" ")
        print_natural_reverse(n - 1)

# 3. Print first N odd natural numbers
def print_odd(n):
    if n > 0:
        print_odd(n - 1)
        print(2*n - 1, end=" ")

# 4. Print first N odd natural numbers in reverse
def print_odd_reverse(n):
    if n > 0:
        print(2*n - 1, end=" ")
        print_odd_reverse(n - 1)

# 5. Print first N even natural numbers
def print_even(n):
    if n > 0:
        print_even(n - 1)
        print(2*n, end=" ")

# 6. Print first N even natural numbers in reverse
def print_even_reverse(n):
    if n > 0:
        print(2*n, end=" ")
        print_even_reverse(n - 1)

# 7. Print squares of first N natural numbers
def print_squares(n):
    if n > 0:
        print_squares(n - 1)
        print(n*n, end=" ")

# 8. Print cubes of first N natural numbers
def print_cubes(n):
    if n > 0:
        print_cubes(n - 1)
        print(n**3, end=" ")

# 9. Print first N multiples of a given number
def print_multiples(num, n):
    if n > 0:
        print_multiples(num, n - 1)
        print(num * n, end=" ")

# 10. Print a number in reverse order (digits)
def print_reverse_number(num):
    if num > 0:
        print(num % 10, end="")
        print_reverse_number(num // 10)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    N = 5
    print("1. First N natural numbers:")
    print_natural(N)
    print("\n2. First N natural numbers in reverse:")
    print_natural_reverse(N)
    print("\n3. First N odd numbers:")
    print_odd(N)
    print("\n4. First N odd numbers in reverse:")
    print_odd_reverse(N)
    print("\n5. First N even numbers:")
    print_even(N)
    print("\n6. First N even numbers in reverse:")
    print_even_reverse(N)
    print("\n7. Squares of first N natural numbers:")
    print_squares(N)
    print("\n8. Cubes of first N natural numbers:")
    print_cubes(N)
    print("\n9. First N multiples of 3:")
    print_multiples(3, N)
    print("\n10. Reverse of number 12345:")
    print_reverse_number(12345)
    print()
