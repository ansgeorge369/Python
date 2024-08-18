import math

operation = input("Enter the operation need to be performed (+, -, *, /, root, mod): ")

if operation not in ["+", "-", "*", "/", "root", "mod"]:
    print(f"{operation} is not valid. Enter a valid operation for action.")

if operation == "root":
    a = int(input("Enter a value: "))
    res = math.sqrt(a)
    print(f"The root value of {a} is {res}")

if operation == "mod":
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    if b != 0:
        c = a % b
        print(f"The result is {c}")
    else:
        print("Cannot divide by zero.")

else:
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))

if operation == "+":
    c = a + b
    print(f"The sum of two numbers is {c}")
elif operation == "-":
    c = a - b
    print(f"The difference between the two numbers is {c}")
elif operation == "*":
    c = a * b
    print(f"The product of two numbers is {c}")
elif operation == "/":
    if b != 0:
        c = a / b
        print(f"The result is {c}")
    else:
        print("Cannot divide by zero.")
