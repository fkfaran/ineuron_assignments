# ==============================
# Task 1: Check whether a number is positive or non-positive
# ==============================
print("Task 1:")
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is non-positive")
print("\n")

# ==============================
# Task 2: Check whether a number is divisible by 5
# ==============================
print("Task 2:")
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 5")
print("\n")

# ==============================
# Task 3: Check whether a number is even or odd
# ==============================
print("Task 3:")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
print("\n")

# ==============================
# Task 4: Print greater between two numbers
# ==============================
print("Task 4:")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print(a)  # Both are same, print once
print("\n")

# ==============================
# Task 5: Print two words in dictionary order
# ==============================
print("Task 5:")
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
if word1 < word2:
    print(word1, word2)
else:
    print(word2, word1)
print("\n")

# ==============================
# Task 6: Check whether a number is three-digit
# ==============================
print("Task 6:")
num = int(input("Enter a number: "))
if 100 <= abs(num) <= 999:
    print(num, "is a three-digit number")
else:
    print(num, "is not a three-digit number")
print("\n")

# ==============================
# Task 7: Check whether a number is positive, negative or zero
# ==============================
print("Task 7:")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
print("\n")

# ==============================
# Task 8: Check roots of a quadratic equation
# ==============================
print("Task 8:")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    print("Two real and distinct roots")
elif discriminant == 0:
    print("Two real and equal roots")
else:
    print("Imaginary roots")
print("\n")

# ==============================
# Task 9: Check leap year
# ==============================
print("Task 9:")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
print("\n")

# ==============================
# Task 10: Print greater among three numbers
# ==============================
print("Task 10:")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
greater = max(x, y, z)
print("Greater number:", greater)
print("\n")

# ==============================
# Task 11: Display number of days in a month
# ==============================
print("Task 11:")
month = int(input("Enter month number (1-12): "))
if month in [1,3,5,7,8,10,12]:
    days = 31
elif month in [4,6,9,11]:
    days = 30
elif month == 2:
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
else:
    days = None

if days:
    print(f"Number of days in month {month}:", days)
else:
    print("Invalid month number")
print("\n")

# ==============================
# Task 12: Compare real and imaginary part of a complex number
# ==============================
print("Task 12:")
num = complex(input("Enter a complex number (a+bj): "))
real_part = num.real
imag_part = num.imag
if real_part > imag_part:
    print("Greater part is Real:", real_part)
elif imag_part > real_part:
    print("Greater part is Imaginary:", imag_part)
else:
    print("Real and Imaginary parts are equal:", real_part)
