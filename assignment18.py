# Python Dictionary Operations

# 1. Create and print a dictionary with personal information
def create_info_dict():
    return {"name": "John", "age": 25, "gender": "Male", "country": "India"}

# 2. Access items of a dictionary by key
def access_by_key():
    info = create_info_dict()
    return info["name"], info["age"]

# 3. Get list of values from dictionary
def get_values():
    info = create_info_dict()
    return list(info.values())

# 4. Change value by referring to key
def change_value():
    info = create_info_dict()
    info["age"] = 30
    return info

# 5. Print all keys one by one
def get_keys():
    info = create_info_dict()
    return [key for key in info]

# 6. Create a dictionary with three nested dictionaries
def nested_dict():
    return {
        "child1": {"name": "Mike", "age": 15},
        "child2": {"name": "Anna", "age": 12},
        "child3": {"name": "Tom", "age": 18}
    }

# 7. Create three dicts and combine them into one
def combine_dicts():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"e": 5, "f": 6}
    return {"dict1": dict1, "dict2": dict2, "dict3": dict3}

# 8. Convert two lists into dictionary
def lists_to_dict():
    list1 = ["name", "age", "gender"]
    list2 = ["Alice", 22, "Female"]
    return dict(zip(list1, list2))

# 9. Merge two dictionaries
def merge_dicts():
    dict1 = {"a": 10, "b": 20}
    dict2 = {"c": 30, "d": 40}
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# 10. Get key of lowest value
def key_of_lowest_value():
    sample_dict = {"C": 92, "Java": 66, "Python": 85}
    return min(sample_dict, key=sample_dict.get)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("1. Info dictionary:", create_info_dict())
    print("2. Access by key:", access_by_key())
    print("3. Values list:", get_values())
    print("4. Changed value:", change_value())
    print("5. Keys:", get_keys())
    print("6. Nested dictionary:", nested_dict())
    print("7. Combined dictionary:", combine_dicts())
    print("8. Lists to dictionary:", lists_to_dict())
    print("9. Merged dictionary:", merge_dicts())
    print("10. Key with lowest value:", key_of_lowest_value())
