# Python Tuple Operations

# 1. Store multiple items in a tuple
def create_tuple():
    return ("Java", "Python", "SQL", "C")

# 2. Store only one item using tuple
def single_item_tuple():
    return ("Python",)   # must include comma

# 3. Reverse the tuple
def reverse_tuple(t):
    return t[::-1]

# 4. Swap two tuples
def swap_tuples(t1, t2):
    t1, t2 = t2, t1
    return t1, t2

# 5. Check if all items in tuple are the same
def all_items_same(t):
    return all(x == t[0] for x in t)

# 6. Divide tuple into four variables
def unpack_tuple():
    tuple1 = (100, 200, 300, 400)
    a, b, c, d = tuple1
    return a, b, c, d

# 7. Copy elements 4 and 5 into new tuple
def copy_elements():
    tuple1 = (1, 2, 3, 4, 5, 6)
    return tuple1[3:5]

# 8. Sort tuple of tuples by second item
def sort_tuple_by_second():
    tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
    return tuple(sorted(tuple1, key=lambda x: x[1]))

# 9. Print value 20 from nested tuple
def get_nested_value():
    tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
    return tuple1[1][1]

# 10. Change first item (22) of list within tuple to 222
def modify_nested_list():
    tuple1 = (11, [22, 33], 44, 55)
    tuple1[1][0] = 222
    return tuple1


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("1. Multiple items tuple:", create_tuple())
    print("2. Single item tuple:", single_item_tuple())
    print("3. Reverse tuple:", reverse_tuple((1, 2, 3, 4, 5)))
    print("4. Swap tuples:", swap_tuples((1, 2), (3, 4)))
    print("5. All items same?:", all_items_same((5, 5, 5, 5)))
    print("6. Unpack tuple:", unpack_tuple())
    print("7. Copy elements 4 & 5:", copy_elements())
    print("8. Sort tuple by second:", sort_tuple_by_second())
    print("9. Nested value 20:", get_nested_value())
    print("10. Modified tuple:", modify_nested_list())
