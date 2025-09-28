# Python Function Programs

# 1. Simple function to print "MySirG"
def print_mysirg():
    print("MySirG")

# 2. Function with two arguments
def print_two(a, b):
    print("First:", a, "Second:", b)

# 3. Function with unknown number of arguments (*args)
def print_args(*args):
    print("Arguments:", args)

# 4. Function with keyword arguments (**kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# 5. Function with list as argument
def list_function(lst):
    print("List items:", lst)

# 6. Function to find max of four numbers
def max_of_four(a, b, c, d):
    return max(a, b, c, d)

# 7. Sum all numbers in a list
def sum_list(lst):
    return sum(lst)

# 8. Multiply all numbers in a list
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# 9. Check if number falls in range
def in_range(num, start, end):
    return start <= num <= end

# 10. Check if number is even or odd
def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # 1
    print_mysirg()
    # 2
    print_two("Hello", "World")
    # 3
    print_args(1, 2, 3, 4, 5)
    # 4
    print_kwargs(name="Alice", age=25, country="India")
    # 5
    list_function([10, 20, 30, 40])
    # 6
    print("Max of four:", max_of_four(10, 25, 5, 18))
    # 7
    print("Sum of list:", sum_list([1, 2, 3, 4, 5]))
    # 8
    print("Product of list:", multiply_list([1, 2, 3, 4, 5]))
    # 9
    print("Is 15 in range 10-20?:", in_range(15, 10, 20))
    # 10
    print("7 is:", even_or_odd(7))
    print("10 is:", even_or_odd(10))
