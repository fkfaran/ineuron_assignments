# ==============================
# Task 1: Display number of days in a month
# ==============================
print("Task 1:")
month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))
if month in [1,3,5,7,8,10,12]:
    days = 31
elif month in [4,6,9,11]:
    days = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
else:
    days = None

if days:
    print(f"Number of days in month {month}:", days)
else:
    print("Invalid month number")
print("\n")

# ==============================
# Task 2: Menu driven calculator
# ==============================
print("Task 2:")
print("Menu: 1.Addition 2.Subtraction 3.Multiplication 4.Division")
choice = int(input("Enter your choice: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")
print("\n")

# ==============================
# Task 3: Triangle check menu
# ==============================
print("Task 3:")
while True:
    print("Menu:\na. Isosceles\nb. Right angled\nc. Equilateral\nd. Exit")
    option = input("Enter your choice: ").lower()
    if option == 'd':
        break
    x = float(input("Enter side 1: "))
    y = float(input("Enter side 2: "))
    z = float(input("Enter side 3: "))
    if option == 'a':
        if x == y or y == z or x == z:
            print("It is an isosceles triangle")
        else:
            print("Not an isosceles triangle")
    elif option == 'b':
        sides = sorted([x, y, z])
        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6:
            print("It is a right angled triangle")
        else:
            print("Not a right angled triangle")
    elif option == 'c':
        if x == y == z:
            print("It is an equilateral triangle")
        else:
            print("Not an equilateral triangle")
    else:
        print("Invalid option")
print("\n")

# ==============================
# Task 4: Categorize person by age
# ==============================
print("Task 4:")
age = int(input("Enter your age: "))
if age < 10:
    print("Kid")
elif age < 20:
    print("Teen")
elif age < 40:
    print("Young")
elif age < 60:
    print("Experienced")
else:
    print("Senior Citizen")
print("\n")

# ==============================
# Task 5: Print name based on number
# ==============================
print("Task 5:")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Saurabh Shukla")
elif num % 2 != 0 and num < 0:
    print("Prateek Jain")
else:
    print("Aditya Choudhary")
print("\n")

# ==============================
# Task 6: Check multiword string using match-case
# ==============================
print("Task 6:")
text = input("Enter a string: ")
words = text.strip().split()
match len(words):
    case 1:
        print("Single word string")
    case _:
        print("Multiword string")
print("\n")

# ==============================
# Task 7: Check positive, negative or zero using match-case
# ==============================
print("Task 7:")
num = float(input("Enter a number: "))
match num:
    case _ if num > 0:
        print("Positive")
    case _ if num < 0:
        print("Negative")
    case 0:
        print("Zero")
print("\n")

# ==============================
# Task 8: Compare two strings using match-case
# ==============================
print("Task 8:")
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
match str1 == str2, str1 < str2:
    case True, _:
        print("Strings are identical")
    case False, True:
        print("First string comes before second")
    case False, False:
        print("First string comes after second")
print("\n")

# ==============================
# Task 9: Check year type
# ==============================
print("Task 9:")
year = int(input("Enter a year: "))
match (year % 4 == 0, year % 100 == 0, year % 400 == 0):
    case True, False, _:
        print("Non-century leap year")
    case True, True, True:
        print("Century leap year")
    case False, _, _:
        print("Non-century non-leap year")
    case True, True, False:
        print("Century non-leap year")
print("\n")

# ==============================
# Task 10: Day based on favorite colour
# ==============================
print("Task 10:")
sentence = input("Enter your favourite colour in a sentence (lowercase): ")
colour = ""
for word in sentence.split():
    if word in ["yellow","blue","orange","white","black","red"]:
        colour = word
        break

match colour:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case _:
        print("Sunday")
