# ==============================
# Task 1: Single-line comment & print
# ==============================
print("Task 1:")
# This is a single line comment
print("Learning Python")
print("\n")

# ==============================
# Task 2: Multi-line comments & print 4 variables
# ==============================
print("Task 2:")
"""
This is a multi-line comment.
We declare four variables and print each on a new line.
"""
a = 10
b = 20
c = "Python"
d = 3.14

print(a)
print(b)
print(c)
print(d)
print("\n")

# ==============================
# Task 3: Print types of variables
# ==============================
print("Task 3:")
x = 35       # Integer
y = True     # Boolean
z = "MySirG" # String
w = 5.46     # Float
v = 3 + 4j   # Complex

print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(v))
print("\n")

# ==============================
# Task 4: Print id of two variables with same integer
# ==============================
print("Task 4:")
m = 100
n = 100

print("ID of m:", id(m))
print("ID of n:", id(n))
print("\n")

# ==============================
# Task 5: Print value, type, and id of 4 variables
# ==============================
print("Task 5:")
var1 = 10          # Integer
var2 = 3.14        # Float
var3 = "Python"    # String
var4 = True        # Boolean

variables = [var1, var2, var3, var4]

for var in variables:
    print("Value:", var, "Type:", type(var), "ID:", id(var))
print("\n")

# ==============================
# Task 6: Print all Python keywords
# ==============================
print("Task 6:")
import keyword
print(keyword.kwlist)
print("\n")

# ==============================
# Task 7: Using help() to display keywords
# ==============================
print("Task 7: (Display in Python shell)")
# Uncomment the line below when running in Python shell
# help("keywords")
print("Run help('keywords') in Python shell to see the list of keywords.\n")

# ==============================
# Task 8: Import variable from A1.py
# ==============================
print("Task 8:")
# Make sure you have A1.py in same folder with: my_variable = "Hello from A1"
try:
    import A1
    print(A1.my_variable)
except ModuleNotFoundError:
    print("A1.py not found. Create A1.py with variable my_variable first.")
print("\n")

# ==============================
# Task 9: Keywords used as data
# ==============================
print("Task 9:")
print("Some keywords used as data: True, False, None")
print("Other keywords cannot be used as variable names.\n")

# ==============================
# Task 10: Display current date and time
# ==============================
print("Task 10:")
from datetime import datetime

current_date = datetime.now().date()
current_time = datetime.now().time()

print("Date:", current_date.strftime("%d-%m-%Y"))
print("Time:", current_time.strftime("%I:%M %p"))
