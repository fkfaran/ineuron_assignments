# Python Set Operations

# 1. Store programming languages using a set
def languages_set():
    return {"Python", "Java", "C", "C++", "SQL", "JavaScript"}

# 2. Store personal information using a set
def personal_info():
    return {"Name: John", "Age: 25", "Gender: Male", "Country: India"}

# 3. Get data type of a set
def get_set_type():
    s = {"Python", "Java"}
    return type(s)

# 4. Check if "Python" is present in set
def check_python():
    thisset = {"Java", "Python", "Django"}
    return "Python" in thisset

# 5. Add items from another set
def add_from_another_set():
    thisset = {"Java", "Python", "SQL"}
    secondset = {"C", "Cpp", "NoSQL"}
    thisset.update(secondset)
    return thisset

# 6. Add elements of list to set
def add_list_to_set():
    thisset = {"Python", "Django", "JavaScript"}
    mylist = ["Java", "C"]
    thisset.update(mylist)
    return thisset

# 7. Remove last item of set
def remove_last_item():
    thisset = {"Python", "Django", "JavaScript", "SQL"}
    thisset.pop()  # removes an arbitrary item (sets are unordered)
    return thisset

# 8. Delete set completely
def delete_set():
    thisset = {"Python", "Django", "JavaScript", "SQL"}
    del thisset
    return "Set deleted"

# 9. Loop through set and print values
def loop_set():
    thisset = {"Python", "Django", "JavaScript", "SQL"}
    return [item for item in thisset]

# 10. Find maximum and minimum value in set
def max_min_in_set():
    numbers = {5, 15, 25, 35, 45}
    return max(numbers), min(numbers)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("1. Languages set:", languages_set())
    print("2. Personal info:", personal_info())
    print("3. Type of set:", get_set_type())
    print("4. Is 'Python' present?:", check_python())
    print("5. Add from another set:", add_from_another_set())
    print("6. Add list to set:", add_list_to_set())
    print("7. Remove last item:", remove_last_item())
    print("8. Delete set:", delete_set())
    print("9. Loop through set:", loop_set())
    print("10. Max & Min in set:", max_min_in_set())
