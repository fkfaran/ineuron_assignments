import math

# 1. Reverse a number
num = int(input("Enter a number to reverse: "))
rev = 0
temp = abs(num)
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
rev = rev if num >= 0 else -rev
print(f"Reversed number: {rev}")

# 2. Check whether a number is prime
num_prime = int(input("Enter a number to check if it's prime: "))
is_prime = True
if num_prime <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num_prime)) + 1):
        if num_prime % i == 0:
            is_prime = False
            break
print(f"{num_prime} is {'a prime' if is_prime else 'not a prime'} number")

# 3. Print all prime numbers under 100
print("Prime numbers under 100:")
for n in range(2, 100):
    prime_flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_flag = False
            break
    if prime_flag:
        print(n, end=" ")
print()

# 4. Print all prime numbers between two given numbers
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
print(f"Prime numbers between {low} and {high}:")
for n in range(low, high + 1):
    if n <= 1:
        continue
    prime_flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_flag = False
            break
    if prime_flag:
        print(n, end=" ")
print()

# 5. Find next prime number of a given number
num_next = int(input("Enter a number to find its next prime: "))
candidate = num_next + 1
while True:
    is_prime = True
    for i in range(2, int(math.sqrt(candidate)) + 1):
        if candidate % i == 0:
            is_prime = False
            break
    if is_prime:
        break
    candidate += 1
print(f"Next prime after {num_next} is {candidate}")

# 6. Print first N prime numbers
N_primes = int(input("Enter N to print first N prime numbers: "))
count = 0
num_check = 2
print(f"First {N_primes} prime numbers:")
while count < N_primes:
    prime_flag = True
    for i in range(2, int(math.sqrt(num_check)) + 1):
        if num_check % i == 0:
            prime_flag = False
            break
    if prime_flag:
        print(num_check, end=" ")
        count += 1
    num_check += 1
print()

# 7. Check whether two numbers are co-prime
a = int(input("Enter first number to check co-prime: "))
b = int(input("Enter second number to check co-prime: "))
gcd_val = math.gcd(a, b)
print(f"{a} and {b} are {'co-prime' if gcd_val == 1 else 'not co-prime'}")

# 8. Print first N terms of Fibonacci series
N_fibo = int(input("Enter N to print first N Fibonacci terms: "))
a, b = 0, 1
print(f"First {N_fibo} Fibonacci terms:")
for _ in range(N_fibo):
    print(a, end=" ")
    a, b = b, a + b
print()

# 9. Calculate LCM of two numbers
x = int(input("Enter first number to find LCM: "))
y = int(input("Enter second number to find LCM: "))
lcm = x * y // math.gcd(x, y)
print(f"LCM of {x} and {y} is {lcm}")

# 10. Calculate HCF of two numbers
m = int(input("Enter first number to find HCF: "))
n = int(input("Enter second number to find HCF: "))
hcf = math.gcd(m, n)
print(f"HCF of {m} and {n} is {hcf}")
