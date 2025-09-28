# 1. Store multiple items in a single variable using list
mylist1 = ["Java", "Python", "SQL", "C"]
print(f"List of items: {mylist1}")

# 2. Get the data type of a list
print(f"Data type of the list: {type(mylist1)}")

# 3. Get the last item of a list
mylist2 = ["Java", "C", "Python"]
print(f"Last item of the list: {mylist2[-1]}")

# 4. Change values in a list
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# Replacing "SQL" with "NoSQL" and "Reactnative" with "Flutter"
thislist[thislist.index("SQL")] = "NoSQL"
thislist[thislist.index("Reactnative")] = "Flutter"
print(f"Updated list: {thislist}")

# 5. Add an item to the end of the list
mylist3 = ["Java", "SQL", "C", "Reactnative"]
mylist3.append("Python")
print(f"List after adding 'Python': {mylist3}")

# 6. Append elements from another list
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
firstlist.extend(secondlist)
print(f"Combined list: {firstlist}")

# 7. Print all items by index
thislist2 = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print("Items in the list by index:")
for i in range(len(thislist2)):
    print(f"Index {i}: {thislist2[i]}")

# 8. Sort the list alphanumerically
thislist3 = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist3.sort()
print(f"Sorted list: {thislist3}")

# 9. Create a list of city names taken from user
n = int(input("Enter the number of cities you want to add: "))
cities = []
for i in range(n):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)
print(f"List of cities: {cities}")

# 10. Create a list where each element is a digit of a given number
num = input("Enter a number: ")
digit_list = [int(d) for d in num]
print(f"List of digits: {digit_list}")
