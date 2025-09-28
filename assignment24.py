# 1 & 2. User class with properties and greet method
class User:
    def __init__(self, name=None, age=None, email=None):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        print(f"Hello {self.name}, welcome!")

# 3. Create 2 objects with different values
user1 = User("Alice", 22, "alice@mail.com")
user2 = User("Bob", 28, "bob@mail.com")

# 4. Init with default values
default_user = User()

# 5. Delete the age property
delattr(user1, "age")

# 6. Create 3 user objects and find youngest
u1 = User("Mike", 30, "mike@mail.com")
u2 = User("Sara", 20, "sara@mail.com")
u3 = User("Tom", 25, "tom@mail.com")
youngest = min([u1, u2, u3], key=lambda u: u.age if u.age else float("inf"))

# 7. Laptop class
class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}GB, CPU: {self.cpu}, HDD: {self.hdd}GB")

# 8. Create 3 Laptop objects and sort by RAM
l1 = Laptop("Dell", 8, "i5", 512)
l2 = Laptop("HP", 16, "i7", 1024)
l3 = Laptop("Lenovo", 4, "i3", 256)
sorted_laptops = sorted([l1, l2, l3], key=lambda l: l.ram)

# 9. School class
class School:
    school_name = "MySchool"   # class variable

    def __init__(self, name, students, teachers):
        self.name = name
        self.students = students
        self.teachers = teachers

# 10. Employee class
class Employee:
    def __init__(self, empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary

    def input_details(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.empid}, Name: {self.name}, Salary: {self.salary}")


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("2. Greeting user2:")
    user2.greet()

    print("\n3. User1 & User2 objects:")
    print(vars(user1))
    print(vars(user2))

    print("\n4. Default user object:")
    print(vars(default_user))

    print("\n6. Youngest user is:", youngest.name, youngest.age)

    print("\n7. Laptop configurations:")
    l1.showConfig()
    l2.showConfig()
    l3.showConfig()

    print("\n8. Sorted laptops by RAM:")
    for laptop in sorted_laptops:
        laptop.showConfig()

    print("\n9. School object:")
    s = School("Green Valley", 500, 40)
    print(vars(s), "Class variable:", s.school_name)

    print("\n10. Employee object:")
    e = Employee()
    e.input_details(101, "John", 50000)
    e.display_details()
