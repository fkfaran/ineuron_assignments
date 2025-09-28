import string

# 1. Function to return unique elements of a list
def unique_list(lst):
    return list(set(lst))

# 2. Function to check if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 3. Function to print even numbers from list
def print_even(lst):
    return [x for x in lst if x % 2 == 0]

# 4. Function to check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 5. Function to find minimum of three numbers
def min_of_three(a, b, c):
    return min(a, b, c)

# 6. Function to return squares of numbers 1-30
def squares_1_to_30():
    return [i**2 for i in range(1, 31)]

# 7. Function accessing another function
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x)

# 8. Function to count uppercase and lowercase
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"UPPERCASE": upper, "LOWERCASE": lower}

# 9. Function to check if string is pangram
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

# 10. Function to check if strings are anagrams
def is_anagram(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("1. Unique elements:", unique_list([1, 2, 2, 3, 4, 4, 5]))
    print("2. Is 17 prime?:", is_prime(17))
    print("3. Even numbers:", print_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("4. Is 'Racecar' palindrome?:", is_palindrome("Racecar"))
    print("5. Min of three (10, 4, 8):", min_of_three(10, 4, 8))
    print("6. Squares 1-30:", squares_1_to_30())
    print("7. Outer/Inner function (5 squared):", outer_function(5))
    print("8. Case count in 'Hello World':", count_case("Hello World"))
    print("9. Is pangram?:", is_pangram("The quick brown fox jumps over the lazy dog"))
    print("10. Are 'listen' and 'silent' anagrams?:", is_anagram("listen", "silent"))
