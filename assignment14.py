# Python Script for Multiple List Operations

# 1. Create a list of first N natural numbers
def first_n_natural_numbers(N):
    return [i for i in range(1, N + 1)]

# 2. Create a list of first N odd natural numbers
def first_n_odd_numbers(N):
    return [i for i in range(1, 2*N, 2)]

# 3. Create a list of first N even natural numbers
def first_n_even_numbers(N):
    return [i for i in range(2, 2*N + 1, 2)]

# 4. Find the greatest number in a given list
def find_greatest(lst):
    return max(lst) if lst else None

# 5. Find the smallest number in a given list
def find_smallest(lst):
    return min(lst) if lst else None

# 6. Calculate the sum of elements in a given list
def sum_of_elements(lst):
    return sum(lst)

# 7. Remove all non-int values from a list
def remove_non_int(lst):
    return [i for i in lst if isinstance(i, int)]

# 8. Print distinct elements along with their frequencies
def element_frequencies(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 9. Print indices of all occurrences of a given element
def find_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

# 10. Sort a list
def sort_list(lst):
    return sorted(lst)

# ------------------- Example Usage -------------------
if __name__ == "__main__":
    N = 10
    sample_list = [1, 2, 2, 3, 4, 'a', 5, 2]

    print("First N natural numbers:", first_n_natural_numbers(N))
    print("First N odd numbers:", first_n_odd_numbers(N))
    print("First N even numbers:", first_n_even_numbers(N))
    print("Greatest number:", find_greatest(sample_list))
    print("Smallest number:", find_smallest(sample_list))
    print("Sum of elements:", sum_of_elements(remove_non_int(sample_list)))
    print("List after removing non-int values:", remove_non_int(sample_list))
    print("Element frequencies:", element_frequencies(sample_list))
    print("Indices of element 2:", find_indices(sample_list, 2))
    print("Sorted list:", sort_list(remove_non_int(sample_list)))
