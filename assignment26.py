# Required modules
import threading
import time
import random

# ---------------- OOP: Method and Operator Overloading ----------------

# 1. Method overloading in Python (using default args)
class Multiply:
    def multiply(self, a, b, c=None, d=None):
        result = a * b
        if c is not None:
            result *= c
        if d is not None:
            result *= d
        return result

# 2. UserAccount class with operator overloading for addition
class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    # 3. Operator overloading for printing object
    def __str__(self):
        return f"UserID: {self.userid}, Balance: {self.balance}"

# ---------------- Multithreading ----------------

# 4. Thread to print Even numbers and Odd numbers till 100
def print_even():
    for i in range(2, 101, 2):
        print("Even:", i, end=" ")
    print()

def print_odd():
    for i in range(1, 101, 2):
        print("Odd:", i, end=" ")
    print()

# 5. Threads to sum values from 1 to 100
sum_even_val = 0
sum_odd_val = 0
lock = threading.Lock()

def sum_even_numbers():
    global sum_even_val
    sum_even_val = sum(i for i in range(2, 101, 2))

def sum_odd_numbers():
    global sum_odd_val
    sum_odd_val = sum(i for i in range(1, 101, 2))

# 6. Threads to fill list with random numbers
random_list = []

def fill_random_numbers():
    for _ in range(20):
        num = random.randint(1, 100)
        with lock:
            random_list.append(num)

# 7. Clock threads
def print_time():
    while True:
        print("Current Time:", time.strftime("%H:%M:%S"))
        time.sleep(1)

def minute_completed():
    while True:
        time.sleep(60)
        print("1 Minute Completed")

# 8. Change thread name
def named_thread_example():
    print(f"Thread Name: {threading.current_thread().name}")

# 10. Check prime or Armstrong in threads
def check_prime(num):
    if num < 2:
        print(f"{num} is not prime")
        return
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(f"{num} is not prime")
            return
    print(f"{num} is prime")

def check_armstrong(num):
    total = sum(int(d)**3 for d in str(num))
    if total == num:
        print(f"{num} is Armstrong")
    else:
        print(f"{num} is not Armstrong")


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("\n1. Multiply numbers:")
    m = Multiply()
    print(m.multiply(2,3))
    print(m.multiply(2,3,4))
    print(m.multiply(2,3,4,5))

    print("\n2 & 3. UserAccount objects and addition:")
    u1 = UserAccount(101, 1000)
    u2 = UserAccount(102, 1500)
    u3 = UserAccount(103, 2000)
    print(u1, u2, u3)
    print("Total Balance:", u1 + u2 + u3)

    print("\n4. Threads for Even and Odd numbers:")
    t_even = threading.Thread(target=print_even)
    t_odd = threading.Thread(target=print_odd)
    t_even.start()
    t_odd.start()
    t_even.join()
    t_odd.join()

    print("\n5. Threads to sum numbers 1 to 100:")
    t_sum_even = threading.Thread(target=sum_even_numbers)
    t_sum_odd = threading.Thread(target=sum_odd_numbers)
    t_sum_even.start()
    t_sum_odd.start()
    t_sum_even.join()
    t_sum_odd.join()
    print("Sum of even:", sum_even_val)
    print("Sum of odd:", sum_odd_val)

    print("\n6. Threads to fill list with random numbers:")
    threads = [threading.Thread(target=fill_random_numbers) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Random List:", random_list)

    # 7. Clock threads (commented out to prevent infinite loop during run)
    # threading.Thread(target=print_time, daemon=True).start()
    # threading.Thread(target=minute_completed, daemon=True).start()

    print("\n8. Thread name example:")
    t_name = threading.Thread(target=named_thread_example, name="CustomThread")
    t_name.start()
    t_name.join()

    print("\n10. Check prime and Armstrong numbers using threads:")
    num1, num2 = 153, 29
    t_prime = threading.Thread(target=check_prime, args=(num2,))
    t_arm = threading.Thread(target=check_armstrong, args=(num1,))
    t_prime.start()
    t_arm.start()
    t_prime.join()
    t_arm.join()
