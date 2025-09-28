# Python String Operations

# 1. Create a String in 3 different possible ways
def create_strings():
    s1 = "Hello"         # Using double quotes
    s2 = 'World'         # Using single quotes
    s3 = """Python"""    # Using triple quotes
    return s1, s2, s3

# 2. Get characters from start to position 5
def slice_start_to_5():
    text = "iNeuron"
    return text[:5]  # from start to index 4

# 3. Get characters from position 2 to position 5
def slice_2_to_5():
    text = "Hello Learners"
    return text[2:6]  # characters at index 2,3,4,5

# 4. String Concatenation with space
def concat_strings():
    a = "Learning"
    b = "Python"
    return a + " " + b

# 5. Count total characters
def count_characters():
    a = "iNeuron"
    return len(a)

# 6. Reverse a String
def reverse_string():
    text = "iNeuron"
    return text[::-1]

# 7. Check if string contains a specific substring
def contains_substring(text, sub):
    return sub in text

# 8. Check if string contains only numbers
def is_numeric(text):
    return text.isdigit()

# 9. Check if string contains only alphabet characters
def is_alpha(text):
    return text.isalpha()

# 10. Convert integer to string
def int_to_string(num):
    return str(num)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("1. Create strings:", create_strings())
    print("2. Slice start to 5:", slice_start_to_5())
    print("3. Slice 2 to 5:", slice_2_to_5())
    print("4. Concatenation:", concat_strings())
    print("5. Character count:", count_characters())
    print("6. Reverse string:", reverse_string())
    print("7. Contains 'Neuron':", contains_substring("iNeuron", "Neuron"))
    print("8. Is '12345' numeric?:", is_numeric("12345"))
    print("9. Is 'Python' alphabetic?:", is_alpha("Python"))
    print("10. Convert int 100 to string:", int_to_string(100))
