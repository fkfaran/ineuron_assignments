# ==============================
# Task 1: Convert a number into str type
# ==============================
print("Task 1:")
num = 123
num_str = str(num)
print("Original:", num, "Type:", type(num))
print("Converted to string:", num_str, "Type:", type(num_str))
print("\n")

# ==============================
# Task 2: Print Unicode of the character 'm'
# ==============================
print("Task 2:")
char = 'm'
unicode_val = ord(char)
print(f"Unicode of '{char}':", unicode_val)
print("\n")

# ==============================
# Task 3: Print character representation of unicode 100
# ==============================
print("Task 3:")
unicode_num = 100
char_from_unicode = chr(unicode_num)
print(f"Character representation of Unicode {unicode_num}:", char_from_unicode)
print("\n")

# ==============================
# Task 4: Print a number and its binary equivalent
# ==============================
print("Task 4:")
num = 25
print("Number:", num)
print("Binary equivalent:", bin(num))
print("\n")

# ==============================
# Task 5: Print a number and its octal equivalent
# ==============================
print("Task 5:")
num = 25
print("Number:", num)
print("Octal equivalent:", oct(num))
print("\n")

# ==============================
# Task 6: Print a number and its hexadecimal equivalent
# ==============================
print("Task 6:")
num = 25
print("Number:", num)
print("Hexadecimal equivalent:", hex(num))
print("\n")

# ==============================
# Task 7: Store binary number 1100101 and print in decimal
# ==============================
print("Task 7:")
binary_num = 0b1100101
print("Binary number 1100101 in decimal:", binary_num)
print("\n")

# ==============================
# Task 8: Store hexadecimal 2F and print in octal
# ==============================
print("Task 8:")
hex_num = 0x2F
print("Hexadecimal 2F in octal:", oct(hex_num))
print("\n")

# ==============================
# Task 9: Store octal 125 and print in binary
# ==============================
print("Task 9:")
oct_num = 0o125
print("Octal 125 in binary:", bin(oct_num))
print("\n")

# ==============================
# Task 10: Add 25 (octal) + 39 (hex) and display result in binary
# ==============================
print("Task 10:")
num1 = 0o25   # Octal 25 = decimal 21
num2 = 0x39   # Hex 39 = decimal 57
sum_result = num1 + num2
print("25 (octal) + 39 (hex) =", sum_result)
print("Sum in binary:", bin(sum_result))
