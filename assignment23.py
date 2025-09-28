import math

# 1. Use iter and next method to access all elements of a set
def iterate_set(s):
    it = iter(s)
    while True:
        try:
            print(next(it), end=" ")
        except StopIteration:
            break
    print()

# 2. Generator: first n odd numbers
def odd_generator(n):
    for i in range(1, 2*n, 2):
        yield i

# 3. Generator: first n even numbers
def even_generator(n):
    for i in range(2, 2*n+1, 2):
        yield i

# 4. Generator: squares of first n natural numbers
def squares_generator(n):
    for i in range(1, n+1):
        yield i*i

# 5. Generator: first n terms of Fibonacci series
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 6. Generator: first n prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    count, num = 0, 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# 7. Endless generator: Fibonacci series
def endless_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 8. Endless generator: Prime numbers
def endless_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# 9. Decorator: check validity of triangle before perimeter
def valid_triangle(func):
    def wrapper(a, b, c):
        if a+b > c and a+c > b and b+c > a:
            return func(a, b, c)
        else:
            return "Invalid Triangle"
    return wrapper

@valid_triangle
def perimeter(a, b, c):
    return a + b + c

# 10. Decorator: check whether two numbers are co-prime
def check_coprime(func):
    def wrapper(a, b):
        h = func(a, b)
        if h == 1:
            return f"HCF = {h}, Numbers are Co-prime"
        else:
            return f"HCF = {h}, Numbers are NOT Co-prime"
    return wrapper

@check_coprime
def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # 1
    print("1. Iterate set elements:")
    iterate_set({10, 20, 30, 40})

    # 2
    print("2. First 5 odd numbers:", list(odd_generator(5)))

    # 3
    print("3. First 5 even numbers:", list(even_generator(5)))

    # 4
    print("4. Squares of first 5 numbers:", list(squares_generator(5)))

    # 5
    print("5. First 7 Fibonacci terms:", list(fibonacci_generator(7)))

