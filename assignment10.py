# ==============================
# Task 1: First 10 multiples of 5
# ==============================
print("Task 1:")
for i in range(1, 11):
    print(5 * i, end=" ")
print("\n\n")

# ==============================
# Task 2: First 10 multiples of N
# ==============================
print("Task 2:")
N = int(input("Enter N: "))
for i in range(1, 11):
    print(N * i, end=" ")
print("\n\n")

# ==============================
# Task 3: First M multiples of N
# ==============================
print("Task 3:")
N = int(input("Enter N: "))
M = int(input("Enter M: "))
for i in range(1, M + 1):
    print(N * i, end=" ")
print("\n\n")

# ==============================
# Task 4: First 10 multiples of N in reverse order
# ==============================
print("Task 4:")
N = int(input("Enter N: "))
for i in range(10, 0, -1):
    print(N * i, end=" ")
print("\n\n")

# ==============================
# Task 5: Table of user's choice
# ==============================
print("Task 5:")
num = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print("\n")

# ==============================
# Task 6: First N even natural numbers
# ==============================
print("Task 6:")
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print(2 * i, end=" ")
print("\n\n")

# ==============================
# Task 7: First N odd natural numbers
# ==============================
print("Task 7:")
N = int(input("Enter N: "))
for i in range(N):
    print(2 * i + 1, end=" ")
print("\n\n")

# ==============================
# Task 8: Squares of first N natural numbers
# ==============================
print("Task 8:")
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print(f"{i}^2 = {i**2}")
print("\n")

# ==============================
# Task 9: Cubes of first N natural numbers
# ==============================
print("Task 9:")
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print(f"{i}^3 = {i**3}")
print("\n")

# ==============================
# Task 10: Display all prime numbers within a range
# ==============================
print("Task 10:")
start = 15
end = 45

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print("\n")
