# ---------------- Exception Handling in Python ----------------

# 1. Create an ArithmeticError
def create_arithmetic_error():
    raise ArithmeticError("This is an ArithmeticError")

# 2. Create a ValueError
def create_value_error():
    raise ValueError("This is a ValueError")

# 3. Handle ArithmeticError
def handle_arithmetic_error():
    try:
        1 / 0
    except ArithmeticError as e:
        print("Handled ArithmeticError:", e)

# 4. Handle ValueError
def handle_value_error():
    try:
        int("abc")
    except ValueError as e:
        print("Handled ValueError:", e)

# 5. Handle multiple exceptions
def handle_multiple_exceptions():
    try:
        lst = [1, 2, 3]
        x = lst[5]  # IndexError
        y = 1 / 0   # ZeroDivisionError
    except (IndexError, ZeroDivisionError) as e:
        print("Handled multiple exceptions:", e)

# 6. Calculator with exception handling
def calculator(a, b, operation):
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        print("Error occurred:", e)

# 7. Calculator with finally block
def calculator_finally(a, b, operation):
    try:
        result = calculator(a, b, operation)
        return result
    except Exception as e:
        print("Error:", e)
    finally:
        print("Calculation attempt completed.")

# 8. Try, except, else block for division
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Division by zero.")
    else:
        print("Division result:", result)

# 9. Raise ValueError
def raise_value_error():
    raise ValueError("This is a raised ValueError")

# 10. Nested try-except
def nested_try_except():
    try:
        x = int("abc")
        try:
            y = 1 / 0
        except ZeroDivisionError as e:
            print("Inner except:", e)
    except ValueError as e:
        print("Outer except:", e)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    print("3. Handle ArithmeticError:")
    handle_arithmetic_error()

    print("\n4. Handle ValueError:")
    handle_value_error()

    print("\n5. Handle multiple exceptions:")
    handle_multiple_exceptions()

    print("\n6. Calculator examples:")
    print("Add:", calculator(10, 5, "+"))
    print("Divide:", calculator(10, 0, "/"))
    print("Invalid operation:", calculator(10, 5, "^"))

    print("\n7. Calculator with finally block:")
    calculator_finally(10, 5, "+")
    calculator_finally(10, 0, "/")

    print("\n8. Try, except, else for division:")
    divide(10, 2)
