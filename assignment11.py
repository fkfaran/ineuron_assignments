# Python Script for Various Number Operations

# 1. Sum of first N natural numbers
N = int(input("Enter N for sum of first N natural numbers: "))
sum_natural = N * (N + 1) // 2
print(f"Sum of first {N} natural numbers: {sum_natural}")

# 2. Sum of squares of first N natural numbers
sum_squares = N * (N + 1) * (2 * N + 1) // 6
print(f"Sum of squares of first {N} natural numbers: {sum_squares}")

# 3. Sum of cubes of first N natural numbers
sum_cubes = (N * (N + 1) // 2) ** 2
print(f"Sum of cubes of first {N} natural numbers: {sum_cubes}")

# 4. Sum of first N odd natural numbers
sum_odd = N ** 2
print(f"Sum of first {N} odd natural numbers: {sum_odd}")

# 5. Sum of first N even natural numbers
sum_even = N * (N + 1)
print(f"Sum of first {N} even natural numbers: {sum_even}")

# 6. Factorial of a given number
num_fact = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, num_fact + 1):
    factorial *= i
print(f"Factorial of {num_fact} is: {factorial}")

# 7. Count digits in a given number
num_digits = int(input("Enter a number to count its digits: "))
count = 0
temp = abs(num_digits)
if temp == 0:
    count = 1
while temp > 0:
    temp //= 10
    count += 1
print(f"Number of digits in {num_digits}: {count}")

# 8. Sum of digits of a given number
num_sum_digits = int(input("Enter a number to calculate sum of its digits: "))
sum_digits = 0
temp = abs(num_sum_digits)
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print(f"Sum of digits of {num_sum_digits}: {sum_digits}")

# 9. Binary equivalent of a given decimal number (without bin())
num_binary = int(input("Enter a decimal number to convert to binary: "))
if num_binary == 0:
    binary = "0"
else:
    binary = ""
    temp = num_binary
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
print(f"Binary equivalent of {num_binary}: {binary}")

# 10. Octal equivalent of a given decimal number (without oct())
num_octal = int(input("Enter a decimal number to convert to octal: "))
if num_octal == 0:
    octal = "0"
else:
    octal = ""
    temp = num_octal
    while temp > 0:
        octal = str(temp % 8) + octal
        temp //= 8
print(f"Octal equivalent of {num_octal}: {octal}")
