# ==============================
# Task 1: Remove the last digit from a number
# ==============================``

print("Task 1:")
num = int(input("Enter a number: "))
removed_last = num // 10
print("Number after removing last digit:", removed_last)
print("\n")

# ==============================
# Task 2: Get the last digit from a number
# ==============================
print("Task 2:")
num = int(input("Enter a number: "))
last_digit = num % 10
print("Last digit of the number:", last_digit)
print("\n")

# ==============================
# Task 3: Swap data of two variables
# ==============================
print("Task 3:")
a = input("Enter first value: ")
b = input("Enter second value: ")
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)
print("\n")

# ==============================
# Task 4: Find x power y
# ==============================
print("Task 4:")
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
power = x ** y
print(f"{x} raised to the power {y} is: {power}")
print("\n")

# ==============================
# Task 5: Display first digit of a three-digit number
# ==============================
print("Task 5:")
num = int(input("Enter a three-digit number: "))
first_digit = num // 100
print("First digit:", first_digit)
print("\n")

# ==============================
# Task 6: Display middle digit of a three-digit number
# ==============================
print("Task 6:")
num = int(input("Enter a three-digit number: "))
middle_digit = (num // 10) % 10
print("Middle digit:", middle_digit)
print("\n")

# ==============================
# Task 7: Display last digit of a three-digit number
# ==============================
print("Task 7:")
num = int(input("Enter a three-digit number: "))
last_digit = num % 10
print("Last digit:", last_digit)
print("\n")

# ==============================
# Task 8: Use IN operator to display data present in list
# ==============================
print("Task 8:")
my_list = [10, 20, 30, 40, 50]
item = int(input("Enter a number to check in the list: "))
if item in my_list:
    print(item, "is present in the list")
else:
    print(item, "is not present in the list")
print("\n")

# ==============================
# Task 9: Use NOT IN operator to display data not present in list
# ==============================
print("Task 9:")
item = int(input("Enter a number to check not in the list: "))
if item not in my_list:
    print(item, "is NOT present in the list")
else:
    print(item, "is present in the list")
print("\n")

# ==============================
# Task 10: Use IS operator to check if two variables are same object
# ==============================
print("Task 10:")
var1 = input("Enter first value: ")
var2 = input("Enter second value: ")
if var1 is var2:
    print("Both variables are the same object")
else:
    print("Variables are not the same object")
