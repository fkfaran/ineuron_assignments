# 1. Profile class with 3 attributes
class Profile:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

# 2. Profile class with encapsulation
class ProfileEncap:
    def __init__(self, name, email, age):
        self.name = name
        self.__email = email
        self.__age = age

    # getters
    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    # setters
    def set_email(self, email):
        self.__email = email

    def set_age(self, age):
        self.__age = age

# 4. Adding class variable and classmethod
class ProfileClassVar(ProfileEncap):
    platform = "PythonApp"

    @classmethod
    def get_platform(cls):
        return cls.platform

# 5. Calculator class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# 6. Calculator 2.0 with multiplication & division (inherits Calculator)
class Calculator2(Calculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Division by zero error"

# 7. Phone class with features
class Phone:
    def call(self, number):
        print(f"Calling {number}...")

    def sms(self, number, message):
        print(f"Sending SMS to {number}: {message}")

# 8. SmartPhone class inheriting Calculator2 and Phone
class SmartPhone(Calculator2, Phone):
    pass

# 9. Truecaller class
class Truecaller:
    def __init__(self):
        self.contacts = {}

    def fetch_name(self, number):
        return self.contacts.get(number, "Unknown Number")

    def add_contact(self, number, name):
        self.contacts[number] = name

# 10. SmartPhone method to use Truecaller
def add_truecaller_method_to_smartphone():
    def use_truecaller(self, truecaller_obj, number):
        name = truecaller_obj.fetch_name(number)
        print(f"Number {number} belongs to {name}")
    setattr(SmartPhone, "use_truecaller", use_truecaller)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # 1
    profile1 = Profile("Alice", "alice@mail.com", 22)
    print("1. Profile:", vars(profile1))

    # 2 & 3
    p_encap = ProfileEncap("Bob", "bob@mail.com", 28)
    print("2 & 3. Email:", p_encap.get_email(), "Age:", p_encap.get_age())
    p_encap.set_email("bob_new@mail.com")
    p_encap.set_age(29)
    print("Updated Email & Age:", p_encap.get_email(), p_encap.get_age())

    # 4. Class variable & classmethod
    print("4. Platform:", ProfileClassVar.get_platform())

    # 5 & 6. Calculator 2.0
    calc = Calculator2()
    print("5. Add:", calc.add(10, 5))
    print("Subtract:", calc.subtract(10, 5))
    print("6. Multiply:", calc.multiply(10, 5))
    print("Divide:", calc.divide(10, 5))

    # 7 & 8. Phone & SmartPhone
    phone = Phone()
    phone.call("1234567890")
    phone.sms("1234567890", "Hello!")
    sp = SmartPhone()
    sp.call("9876543210")
    sp.sms("9876543210", "Hi there!")
    print("SmartPhone Multiply 2 numbers:", sp.multiply(4, 5))

    # 9. Truecaller
    tc = Truecaller()
    tc.add_contact("1111111111", "Alice")
    tc.add_contact("2222222222", "Bob")
    print("9. Fetch number 1111111111:", tc.fetch_name("1111111111"))

    # 10. SmartPhone use Truecaller
    add_truecaller_method_to_smartphone()
    sp.use_truecaller(tc, "1111111111")
    sp.use_truecaller(tc, "3333333333")  # unknown number
