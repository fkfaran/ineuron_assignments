# ==============================
# Take input N from user
# ==============================
N = int(input("Enter the value of N: "))

# ==============================
# Task 1: Print "MySirG" N times
# ==============================
print("Task 1:")
for _ in range(N):
    print("MySirG")
print("\n")

# ==============================
# Task 2: Print first N natural numbers
# ==============================
print("Task 2:")
for i in range(1, N + 1):
    print(i, end=" ")
print("\n\n")

# ==============================
# Task 3: Print first N natural numbers in reverse order
# ==============================
print("Task 3:")
for i in range(N, 0, -1):
    print(i, end=" ")
print("\n\n")

# ==============================
# Task 4: Print first N odd natural numbers
# ==============================
print("Task 4:")
for i in range(1, 2 * N, 2):
    print(i, end=" ")
print("\n\n")

# ==============================
# Task 5: Print first N odd natural numbers in reverse order
# ==============================
print("Task 5:")
for i in range(2 * N - 1, 0, -2):
    print(i, end=" ")
print("\n\n")

# ==============================
# Task 6: Print first N even natural numbers
# ==============================
print("Task 6:")
for i in range(2, 2 * N + 1, 2):
    print(i, end=" ")
print("\n\n")

# ==============================
# Task 7: Print first N even natural numbers in reverse order
# ==============================
print("Task 7:")
for i in range(2 * N, 1, -2):
    print(i, end=" ")
print("\n\n")

# ==============================
# Task 8: Print squares of first N natural numbers
# ==============================
print("Task 8:")
for i in range(1, N + 1):
    print(f"{i}^2 = {i**2}")
print("\n")

# ==============================
# Task 9: Print cubes of first N natural numbers
# ==============================
print("Task 9:")
for i in range(1, N + 1):
    print(f"{i}^3 = {i**3}")
print("\n")

# ==============================
# Task 10: Print first 10 multiples of N
# ==============================
print("Task 10:")
for i in range(1, 11):
    print(N * i, end=" ")
print("\n")
